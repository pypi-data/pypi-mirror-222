import click

from simpeval.utils.helpers import read_lines
from simpeval.utils.constants import (
    VALID_TEST_SETS,
    VALID_METRICS,
    DEFAULT_METRICS,
)
from simpeval.utils.resources import get_orig_sents, get_refs_sents


def get_sys_sents(test_set, sys_sents_path=None):
    # Get system sentences to be evaluated
    if sys_sents_path is not None:
        return read_lines(sys_sents_path)
    else:
        # read the system output
        with click.get_text_stream("stdin", encoding="utf-8") as system_output_file:
            return system_output_file.read().splitlines()


def get_orig_and_refs_sents(test_set, orig_sents_path=None, refs_sents_paths=None):
    # Get original and reference sentences
    if test_set == "custom":
        assert orig_sents_path is not None
        assert refs_sents_paths is not None
        if type(refs_sents_paths) == str:
            refs_sents_paths = refs_sents_paths.split(",")
        orig_sents = read_lines(orig_sents_path)
        refs_sents = [read_lines(ref_sents_path) for ref_sents_path in refs_sents_paths]
    else:
        orig_sents = get_orig_sents(test_set)
        refs_sents = get_refs_sents(test_set)
    # Final checks
    assert all(
        [len(orig_sents) == len(ref_sents) for ref_sents in refs_sents]
    ), f"Not same number of lines for test_set={test_set}, orig_sents_path={orig_sents_path}, refs_sents_paths={refs_sents_paths}"  # noqa: E501
    return orig_sents, refs_sents


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option()
def cli():
    pass


def common_options(function):
    function = click.option(
        "--test_set",
        "-t",
        type=click.Choice(VALID_TEST_SETS),
        required=True,
        help="Test set to use.",
    )(function)
    function = click.option(
        "--orig_sents_path",
        type=click.Path(),
        default=None,
        help='Path to the source sentences. Only used when test_set == "custom".',
    )(function)
    function = click.option(
        "--refs_sents_paths",
        type=str,
        default=None,
        help='Comma-separated list of path(s) to the references(s). Only used when test_set == "custom".',
    )(function)
    function = click.option(
        "--lowercase/--no-lowercase",
        "-lc/--no-lc",
        default=True,
        help="Compute case-insensitive scores for all metrics. ",
    )(function)
    function = click.option(
        "--tokenizer",
        "-tok",
        type=click.Choice(["13a", "intl", "moses", "penn", "none"]),
        default="13a",
        help="Tokenization method to use.",
    )(function)
    function = click.option(
        "--metrics",
        "-m",
        type=str,
        default=",".join(DEFAULT_METRICS),
        help=(
            f'Comma-separated list of metrics to compute. Valid: {",".join(VALID_METRICS)}'
            " (SAMSA is disabled by default for the sake of speed)."
        ),
    )(function)
    return function


@cli.command("evaluate")
@common_options
@click.option(
    "--sys_sents_path",
    "-i",
    type=click.Path(),
    default=None,
    help="Path to the system predictions input file that is to be evaluated.",
)
@click.option(
    "--use-bert",
    "-uB",
    is_flag=True,
    default=False,
    help="Use bert to annotate with TUPA.",
)
def _evaluate_system_output(*args, **kwargs):
    kwargs["metrics"] = kwargs.pop("metrics").split(",")
    kwargs["use_bert"] = kwargs.pop("use_bert")
    metrics_scores = evaluate_system_output(*args, **kwargs)

    def recursive_round(obj):
        def is_castable_to_float(obj):
            try:
                float(obj)
            except (ValueError, TypeError):
                return False
            return True

        if is_castable_to_float(obj):
            return round(obj, 3)
        if type(obj) is dict:
            return {key: recursive_round(value) for key, value in obj.items()}
        return obj

    print(recursive_round(metrics_scores))


def evaluate_system_output(
    test_set,
    sys_sents_path=None,
    orig_sents_path=None,
    refs_sents_paths=None,
    tokenizer="13a",
    lowercase=True,
    metrics=DEFAULT_METRICS,
    use_bert=False,
):
    """
    Evaluate a system output with automatic metrics.
    """
    for metric in metrics:
        assert (
            metric in VALID_METRICS
        ), f'"{metric}" is not a valid metric. Choose among: {VALID_METRICS}'
    sys_sents = get_sys_sents(test_set, sys_sents_path)
    orig_sents, refs_sents = get_orig_and_refs_sents(
        test_set, orig_sents_path, refs_sents_paths
    )

    # compute each metric
    metrics_scores = {}

    if "samsa" in metrics:
        from simpeval.samsa import corpus_samsa

        metrics_scores["samsa"] = corpus_samsa(
            orig_sents,
            sys_sents,
            tokenizer=tokenizer,
            lowercase=lowercase,
            verbose=True,
            use_bert=use_bert,
        )

    return metrics_scores
