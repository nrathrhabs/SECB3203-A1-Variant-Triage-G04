"""Visible tests: a few clear cases. The hidden tests use YOUR group's data and other thresholds as well."""
from a1_triage import (
    CSV_COLUMNS,
    classify_variant,
    decision_counts,
    rank_variants,
    results_to_csv,
    triage,
)

PARAMS = {"min_depth": 10, "min_quality": 80, "priority_genes": ["BRCA1", "TP53"], "top_k": 3}


def make_row(variant="v1", gene="BRCA1", depth=40, quality=95, impact="high", pos=1000):
    return {"variant": variant, "gene": gene, "chrom": "17", "pos": str(pos), "depth": str(depth),
            "quality": str(quality), "impact": impact}


def test_low_depth_is_excluded_with_a_reason():
    decision, reason = classify_variant(make_row(depth=9), PARAMS)
    assert decision == "exclude"
    assert "depth" in reason


def test_priority_gene_with_high_impact_is_prioritized():
    assert classify_variant(make_row(), PARAMS)[0] == "prioritize"


def test_other_gene_with_low_impact_is_excluded():
    assert classify_variant(make_row(gene="MYC", impact="low"), PARAMS)[0] == "exclude"


def test_triage_adds_decision_and_reason():
    results = triage([make_row(), make_row(variant="v2", depth=1)], PARAMS)
    assert [r["variant"] for r in results] == ["v1", "v2"]
    assert all("decision" in r and "reason" in r for r in results)
    assert decision_counts(results) == {"prioritize": 1, "review": 0, "exclude": 1}


def test_rank_variants_returns_at_most_k():
    results = triage([make_row(variant=f"v{i}", pos=i) for i in range(5)], PARAMS)
    assert len(rank_variants(results, 3)) == 3


def test_csv_text_starts_with_the_header():
    text = results_to_csv(triage([make_row()], PARAMS))
    assert text.splitlines()[0] == ",".join(CSV_COLUMNS)
