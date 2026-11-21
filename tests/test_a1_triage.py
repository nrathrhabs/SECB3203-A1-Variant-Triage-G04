"""Own tests for Assignment 1: Variant Triage Service """

import pytest
from a1_triage import (
    classify_variant, triage, rank_variants, 
    load_params, load_variants
)

PARAMS = load_params("data/params.json")
ROWS = load_variants("data/variants.csv")


# normal case (testing a gene that is in the priority list)
def test_priority_gene():
    row = {"gene": "EGFR", "depth": "30", "quality": "90", "impact": "moderate"}
    decision, reason = classify_variant(row, PARAMS)
    assert decision == "prioritize"
    assert "EGFR" in reason or "moderate" in reason


# boundary cases
def test_boundary_depth_below():
    # depth is 11 (below 12)
    row = {"gene": "TP53", "depth": "11", "quality": "99", "impact": "high"}
    decision, reason = classify_variant(row, PARAMS)
    assert decision == "exclude"
    assert "depth" in reason


def test_boundary_depth_at():
    # depth is exactly 12
    row = {"gene": "TP53", "depth": "12", "quality": "99", "impact": "high"}
    decision, reason = classify_variant(row, PARAMS)
    assert decision == "review" 


def test_boundary_depth_above():
    # depth is 13 (above 12)
    row = {"gene": "TP53", "depth": "13", "quality": "99", "impact": "high"}
    decision, reason = classify_variant(row, PARAMS)
    assert decision == "review"


def test_boundary_quality_below():
    # quality is 79 (below 80)
    row = {"gene": "ATM", "depth": "50", "quality": "79", "impact": "modifier"}
    decision, reason = classify_variant(row, PARAMS)
    assert decision == "exclude"
    assert "quality" in reason


def test_boundary_quality_at():
    # quality is exactly 80
    row = {"gene": "EGFR", "depth": "50", "quality": "80", "impact": "moderate"}
    decision, reason = classify_variant(row, PARAMS)
    assert decision == "prioritize"


def test_boundary_quality_above():
    # quality is 81 (above 80)
    row = {"gene": "EGFR", "depth": "50", "quality": "81", "impact": "moderate"}
    decision, reason = classify_variant(row, PARAMS)
    assert decision == "prioritize"


# awkward input tests
def test_messy_text_and_case_folding():
    # testing messy text and case folding
    row = {"gene": "  aTm  ", "depth": "50", "quality": "99", "impact": "  HIGH  "}
    decision, reason = classify_variant(row, PARAMS)
    assert decision == "prioritize"


def test_empty_list():
    # testing triage and rank_variants with an empty list
    results = triage([], PARAMS)
    assert results == []
    
    ranked = rank_variants(results, k=5)
    assert ranked == []


def test_k_larger_than_data():
    # testing rank_variants with k larger than the data
    results = triage(ROWS, PARAMS)
    ranked = rank_variants(results, k=1000)
    non_excluded_count = len([r for r in results if r["decision"] != "exclude"])
    assert len(ranked) == non_excluded_count


# invalid input test
def test_negative_k_raises_error():
    # testing rank_variants with negative k using pytest.raises
    results = triage(ROWS, PARAMS)
    with pytest.raises(ValueError):
        rank_variants(results, k=-1)