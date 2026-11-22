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
    depth = int(row["depth"])
    quality = int(row["quality"])
    min_depth = int(params["min_depth"])
    min_quality = int(params["min_quality"])

    if depth < min_depth:
        return "exclude", f"rule 1: depth QC: depth={depth} below min_depth={min_depth}"

    if quality < min_quality:
        return "exclude", f"rule 2: quality QC: quality={quality} below " f"min_quality={min_quality}"

    gene = str(row["gene"]).strip()
    gene_key = gene.casefold()
    impact = str(row["impact"]).strip().casefold()

    priority_genes = {str(priority_gene).strip().casefold() for priority_gene in params["priority_genes"]}
    is_priority_gene = gene_key in priority_genes

    if impact not in {"high", "moderate", "low", "modifier"}:
        raise ValueError(f"Unsupported impact value: {row['impact']}")

    if is_priority_gene and impact in {"high", "moderate"}:
        return "prioritize", f"rule 3: priority gene {gene} with {impact} impact"

    if is_priority_gene and impact in {"low", "modifier"}:
        return "review", f"rule 4: priority gene {gene} with {impact} impact"

    if not is_priority_gene and impact in {"high", "moderate"}:
        return "review", f"rule 5: non-priority gene {gene} with {impact} impact"

    return "exclude", f"rule 6: non-priority gene {gene} with {impact} impact"


def triage(rows: list[dict], params: dict) -> list[dict]:
    """Classify every row. Returns NEW dicts (row fields plus decision and reason), same order.

    The input rows and params are never modified.
    """
    results = []

    for row in rows:
        decision, reason = classify_variant(row, params)
        result = dict(row)
        result["decision"] = decision
        result["reason"] = reason
        results.append(result)

    return results


def decision_counts(results: list[dict]) -> dict[str, int]:
    """Number of results per decision; keys are always prioritize, review, exclude (in order)."""
    counts = {
        decision: 0
        for decision in DECISIONS
    }

    for result in results:
        decision = result["decision"]
        counts[decision] += 1

    return counts

def impact_counts(results: list[dict]) -> dict[str, int]:
    """Impact counts over variants that were NOT excluded.

    Keys are always high, moderate, low, modifier (in that order), zeros included.
    """
    counts = {
        impact: 0
        for impact in IMPACT_ORDER
    }

    for result in results:
        if result["decision"] == "exclude":
            continue

        impact = result["impact"].strip().casefold()
        counts[impact] += 1

    return counts

def gene_summary(results: list[dict]) -> dict[str, dict]:
    """Per-gene summary, genes in alphabetical order.

    Each value is {"total": n, "prioritize": a, "review": b, "exclude": c, "mean_depth": d}
    where mean_depth is the mean depth of ALL the gene's variants, rounded to 1 decimal.
    """
    summary = {}
    depth_totals = {}

    for result in results:
        gene = result["gene"].strip()
        decision = result["decision"]
        depth = int(result["depth"])

        if gene not in summary:
            summary[gene] = {
                "total": 0,
                "prioritize": 0,
                "review": 0,
                "exclude": 0,
                "mean_depth": 0.0,
            }
            depth_totals[gene] = 0

        summary[gene]["total"] += 1
        summary[gene][decision] += 1
        depth_totals[gene] += depth

    for gene in summary:
        total = summary[gene]["total"]
        mean_depth = depth_totals[gene] / total
        summary[gene]["mean_depth"] = round(mean_depth, 1)

    return dict(sorted(summary.items()))

def rank_variants(results: list[dict], k: int) -> list[dict]:
    """Top k variants that were not excluded, best first.

    Sort by: prioritize before review, then impact (high first), then higher quality,
    then higher depth, then smaller pos. Fewer than k are returned if fewer qualify.

    Raises:
        ValueError: if k is negative.
    """
    if k < 0:
        raise ValueError("k must be non-negative")

    candidates = [r for r in results if r["decision"] != "exclude"]

    def _rank_key(r: dict) -> tuple:
        impact_clean = r["impact"].strip().lower()
        return(
            DECISIONS.index(r["decision"]),
            IMPACT_ORDER.index(impact_clean),
            -int(r["quality"]),
            -int(r["depth"]),
            int(r["pos"]),
        )

    ranked = sorted(candidates, key=_rank_key)
    return ranked[:k]



def results_to_csv(results: list[dict]) -> str:
    """CSV text: a header line (CSV_COLUMNS) and one line per result in the given order.

    Every line ends with a newline. Reason text contains no commas, so no quoting is needed.
    """
    lines = [",".join(CSV_COLUMNS)]

    for r in results:
        row_text = ",".join(str(r[col]) for col in CSV_COLUMNS)
        lines.append(row_text)

    return "\n".join(lines) + "\n"



def build_report(results: list[dict], params: dict) -> str:
    """Short text report; the line formats are fixed so the report can be checked.

    Lines: title, 'Thresholds: min_depth=D min_quality=Q', 'Priority genes: A, B, ...',
    'Variants: N', one 'decision: count' line per decision, a blank line,
    'Top K variants' and then 'rank. variant | gene | impact | decision' lines.
    """
    lines = [
        "Variant triage report (synthetic teaching data)",
        f"Thresholds: min_depth={params['min_depth']} min_quality={params['min_quality']}",
        f"Priority genes: {', '.join(params['priority_genes'])}",
        f"Variants: {len(results)}",
    ]
    for decision in DECISIONS:
        count = sum(1 for r in results if r["decision"]==decision)
        lines.append(f"{decision}:{count}")

    k = params["top_k"]
    lines.append("")
    lines.append(f"Top {k} variants")

    for rank, r in enumerate(rank_variants(results, k), start=1):
        lines.append(f"{rank}. {r['variant']} | {r['gene']} | {r['impact']} | {r['decision']}")

    return "\n".join(lines) + "\n"


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
