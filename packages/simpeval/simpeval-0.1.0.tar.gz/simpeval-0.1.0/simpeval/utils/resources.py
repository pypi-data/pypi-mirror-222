import json
import os
import sys
import tarfile
import time
from urllib.request import urlretrieve
import warnings
import zipfile
import stanza
import importlib


from simpeval.utils.constants import (
    STANFORD_CORENLP_DIR,
    UCCA_DIR,
    TOOLS_DIR,
    UCCA_PARSER_PATH,
    UCCA_BERT_PARSER_PATH,
    UCCA_BERT_DIR,
    TEST_SETS_PATHS,
    SYSTEM_OUTPUTS_DIRS_MAP,
)
from simpeval.utils.helpers import get_temp_filepath, read_lines, safe_divide


def reporthook(count, block_size, total_size):
    # Download progress bar
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size_mb = count * block_size / (1024 * 1024)
    speed = safe_divide(progress_size_mb, duration)
    percent = int(count * block_size * 100 / total_size)
    msg = f"\r... {percent}% - {int(progress_size_mb)} MB - {speed:.2f} MB/s - {int(duration)}s"
    sys.stdout.write(msg)


def download(url, destination_path):
    print(f"Downloading {url}...")
    try:
        urlretrieve(url, destination_path, reporthook)
        sys.stdout.write("\n")
    except (Exception, KeyboardInterrupt, SystemExit):
        print("Rolling back: remove partially downloaded file")
        os.remove(destination_path)
        raise


def unzip(compressed_path, output_dir):
    with zipfile.ZipFile(compressed_path, "r") as f:
        f.extractall(output_dir)


def untar(compressed_path, output_dir):
    with tarfile.open(compressed_path) as f:
        f.extractall(output_dir)


def download_stanford_corenlp():
    """Function using stanza to dowload corenlp models"""
    STANFORD_CORENLP_DIR.mkdir(parents=True, exist_ok=True)
    corenlp_dir = str(STANFORD_CORENLP_DIR)
    os.environ["CORENLP_HOME"] = corenlp_dir
    stanza.install_corenlp(dir=corenlp_dir)
    stanza.download_corenlp_models(model="french", version="4.5.4", dir=corenlp_dir)


def update_ucca_path(use_bert=False):
    # HACK: Change vocab_path from relative to absolute path
    if use_bert:
        url = "https://github.com/jessy3ric/git_memoire/blob/main/utils/vocab.zip?raw=true"
        temp_filepath = get_temp_filepath(create=True)
        download_zip_file(url, temp_filepath)
        unzip(temp_filepath, UCCA_BERT_DIR)

    json_path = (
        str(UCCA_PARSER_PATH) + ".nlp.json"
        if not use_bert
        else str(UCCA_BERT_PARSER_PATH) + ".nlp.json"
    )
    with open(json_path, "r") as f:
        config_json = json.load(f)
    config_json["vocab"] = (
        str(UCCA_DIR / "vocab/fr_core_news_md.csv")
        if not use_bert
        else str(UCCA_BERT_DIR / "vocab/fr_core_news_md.csv")
    )
    with open(json_path, "w") as f:
        json.dump(config_json, f)


def dowload_ucca_model(use_bert=False):
    url = "https://github.com/huji-nlp/tupa/releases/download/v1.3.10/ucca-bilstm-1.3.10-fr.tar.gz"
    if use_bert:
        url = "https://github.com/huji-nlp/tupa/releases/download/v1.4.0/bert_multilingual_layers_4_layers_pooling_weighted_align_sum.tar.gz"
    temp_filepath = get_temp_filepath(create=True)
    download(url, temp_filepath)
    UCCA_DIR.mkdir(
        parents=True, exist_ok=True
    ) if not use_bert else UCCA_BERT_DIR.mkdir(parents=True, exist_ok=True)
    untar(temp_filepath, UCCA_DIR) if not use_bert else untar(
        temp_filepath, UCCA_BERT_DIR
    )
    update_ucca_path(use_bert=use_bert)


def maybe_map_deprecated_test_set_to_new_test_set(test_set):
    """Map deprecated test sets to new test sets"""
    deprecated_test_sets_map = {
        "turk": "turkcorpus_test",
        "turk_valid": "turkcorpus_valid",
    }
    if test_set in deprecated_test_sets_map:
        deprecated_test_set = test_set
        test_set = deprecated_test_sets_map[deprecated_test_set]
        warnings.warn(
            f'"{deprecated_test_set}" test set is deprecated. Please use "{test_set}" instead.'
        )
    return test_set


def get_orig_sents(test_set):
    test_set = maybe_map_deprecated_test_set_to_new_test_set(test_set)
    return read_lines(TEST_SETS_PATHS[(test_set, "orig")])


def get_refs_sents(test_set):
    test_set = maybe_map_deprecated_test_set_to_new_test_set(test_set)
    return [
        read_lines(ref_sents_path)
        for ref_sents_path in TEST_SETS_PATHS[(test_set, "refs")]
    ]


def get_system_outputs_dir(test_set):
    return SYSTEM_OUTPUTS_DIRS_MAP[test_set]


def download_zip_file(url, output_file):
    """Downloads a zip file from the specified URL and saves it to the specified output file.

    Args:
      url: The URL of the zip file to download.
      output_file: The path to the output file to save the zip file to.

    Raises:
      ValueError: If the zip file could not be downloaded.
    """
    import requests

    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
    else:
        raise ValueError(f"Failed to download zip file: {response.status_code}")
