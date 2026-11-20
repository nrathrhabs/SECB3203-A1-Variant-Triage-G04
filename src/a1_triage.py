"""Assignment 1 - clinical variant triage service (synthetic teaching data only).

Reads variant calls, applies ordered triage rules with named thresholds, records a
reason for every decision and produces summaries, a ranked top-k list, a CSV text
and a short text report. Nothing here is clinical advice.
"""
import csv
import json
import sys
from pathlib import Path

DECISIONS = ("prioritize", "review", "exclude")
IMPACT_ORDER = ("high", "moderate", "low", "modifier")
PRIORITY_IMPACTS = frozenset({"high", "moderate"})
CSV_COLUMNS = [
    "variant", "gene", "chrom", "pos", "depth", "quality", "impact", "decision", "reason",
]
CLI_ARGUMENTS = 3


def load_variants(path) -> list[dict]:
    """Read variants.csv into a list of dicts. Every value stays text (Week 6 explains how)."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_params(path) -> dict:
    """Read the group parameters (data/params.json) into a dict."""
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def classify_variant(row: dict, params: dict) -> tuple[str, str]:
    """Return (decision, reason) for one variant row.

    Rules run in this order and the first rule that fires decides:
      1. depth < params["min_depth"]                      -> exclude (low depth)
      2. quality < params["min_quality"]                  -> exclude (low quality)
      3. priority gene and impact high or moderate        -> prioritize
      4. priority gene and impact low or modifier         -> review
      5. other gene and impact high or moderate           -> review
      6. other gene and impact low or modifier            -> exclude
    Gene symbols and impact labels are compared after strip() and case folding.
    depth, quality and pos may arrive as text.
    """
    raise NotImplementedError("TODO: implement classify_variant")


def triage(rows: list[dict], params: dict) -> list[dict]:
    """Classify every row. Returns NEW dicts (row fields plus decision and reason), same order.

    The input rows and params are never modified.
    """
    raise NotImplementedError("TODO: implement triage")


def decision_counts(results: list[dict]) -> dict[str, int]:
    """Number of results per decision; keys are always prioritize, review, exclude (in order)."""
    raise NotImplementedError("TODO: implement decision_counts")


def impact_counts(results: list[dict]) -> dict[str, int]:
    """Impact counts over variants that were NOT excluded.

    Keys are always high, moderate, low, modifier (in that order), zeros included.
    """
    raise NotImplementedError("TODO: implement impact_counts")


def gene_summary(results: list[dict]) -> dict[str, dict]:
    """Per-gene summary, genes in alphabetical order.

    Each value is {"total": n, "prioritize": a, "review": b, "exclude": c, "mean_depth": d}
    where mean_depth is the mean depth of ALL the gene's variants, rounded to 1 decimal.
    """
    raise NotImplementedError("TODO: implement gene_summary")


def rank_variants(results: list[dict], k: int) -> list[dict]:
    """Top k variants that were not excluded, best first.

    Sort by: prioritize before review, then impact (high first), then higher quality,
    then higher depth, then smaller pos. Fewer than k are returned if fewer qualify.

    Raises:
        ValueError: if k is negative.
    """
    raise NotImplementedError("TODO: implement rank_variants")


def results_to_csv(results: list[dict]) -> str:
    """CSV text: a header line (CSV_COLUMNS) and one line per result in the given order.

    Every line ends with a newline. Reason text contains no commas, so no quoting is needed.
    """
    raise NotImplementedError("TODO: implement results_to_csv")


def build_report(results: list[dict], params: dict) -> str:
    """Short text report; the line formats are fixed so the report can be checked.

    Lines: title, 'Thresholds: min_depth=D min_quality=Q', 'Priority genes: A, B, ...',
    'Variants: N', one 'decision: count' line per decision, a blank line,
    'Top K variants' and then 'rank. variant | gene | impact | decision' lines.
    """
    raise NotImplementedError("TODO: implement build_report")


def main(argv: list[str] | None = None) -> int:
    """Command line: python src/a1_triage.py VARIANTS_CSV PARAMS_JSON OUT_DIR."""
    args = sys.argv[1:] if argv is None else argv
    if len(args) != CLI_ARGUMENTS:
        print("usage: python src/a1_triage.py data/variants.csv data/params.json results")
        return 2
    variants_path, params_path, out_dir = args
    rows = load_variants(variants_path)
    params = load_params(params_path)
    results = triage(rows, params)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "triage.csv").write_text(results_to_csv(results), encoding="utf-8")
    report = build_report(results, params)
    (out / "report.txt").write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
