from contextlib import contextmanager
from functools import lru_cache
import sys
from typing import List

from tupa.parse import Parser

from ucca.core import Passage
import ucca.convert

from simpeval.utils.constants import UCCA_PARSER_PATH, UCCA_BERT_PARSER_PATH
from simpeval.utils.resources import dowload_ucca_model, update_ucca_path


@contextmanager
def mock_sys_argv(argv):
    original_sys_argv = sys.argv
    sys.argv = argv
    yield
    sys.argv = original_sys_argv


@lru_cache(maxsize=1)
def get_parser(use_bert=False):
    if not UCCA_PARSER_PATH.parent.exists() and use_bert is False:
        dowload_ucca_model()
    elif not UCCA_BERT_PARSER_PATH.parent.exists() and use_bert is True:
        dowload_ucca_model(use_bert=use_bert)
    update_ucca_path()
    with mock_sys_argv([""]):
        # Need to mock sysargs otherwise the parser will use try to use them and throw an exception
        return (
            Parser(str(UCCA_PARSER_PATH))
            if use_bert is False
            else Parser(str(UCCA_BERT_PARSER_PATH))
        )


def ucca_parse_texts(texts: List[str], use_bert=False):
    passages = []
    for text in texts:
        passages += list(ucca.convert.from_text(text.split(), tokenized=True))
    parser = get_parser(use_bert=use_bert)
    parsed_passages = [
        passage for (passage, *_) in parser.parse(passages, display=False)
    ]
    return parsed_passages


def get_scenes_ucca(ucca_passage: Passage):
    return [x for x in ucca_passage.layer("1").all if x.tag == "FN" and x.is_scene()]


def get_scenes_text(ucca_passage: Passage):
    """Return all the ucca scenes in the given text"""
    scenes_ucca = get_scenes_ucca(ucca_passage)
    scenes_text = [flatten_unit(scene) for scene in scenes_ucca]
    return scenes_text


def flatten_unit(unit_node):
    words = []
    previous_word = ""
    for terminal in unit_node.get_terminals(False, True):
        word = terminal.text
        if word == previous_word:
            # TODO: Iterating this way on the scene sometimes yields duplicates.
            continue
        words.append(word)
        previous_word = word
    return words
