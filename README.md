# Variant Triage Service (SECB3203 Assignment 1)

> All data are synthetic teaching data, not clinical data.

## Group

- Group ID: G04
- Members: NUR ATHIRAH BINTI ABASA (A24CS0158)
           NUR ALIA AISHAH BINTI NAZRI SAKRI (A24CS0152)
           FAKHIRA ANISA BINTI MOHD RADZI (A24CS0070)
           AFINA SOLEHA BATRISYIA BINTI MOHD HISAFUDIN (A24CS0034)


## What this project does

This project is a variant triage service that analyses genetic variant records using predefined rules. It takes a CSV file containing variant information and a JSON file containing parameters such as minimum depth, minimum quality, priority genes and top_k. The service classifies variants into different decisions based on these rules. It also produces summary information to help users understand the triage results.

## Set up

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

python src/a1_triage.py data/variants.csv data/params.json results

- Files that appear in results/: triage.csv and report.txt

## Test and lint

```
python -m pytest
ruff check src
```

## Our parameters

Our thresholds, priority genes and top_k are in data/params.json (min_depth: 12, min_quality: 80, priority_genes: ["ATM", "PTEN", "EGFR", "APC", "BRCA2"], top_k: 5).
They are read at run time and passed to the functions; they are not typed into the rules.


## Design

The design process is documented in docs/design.md. It contains the decomposition of the problem, the pseudocode/flowchart for the classification rules, a hand-trace table of the first few variants, and the test plan.

## Limitations

- The triage rules rely only on basic metrics (depth, quality, gene priority, and impact) and do not evaluate complex biological interactions or population frequencies.

- The data provided is synthetic and for teaching purposes only. This tool is not clinical advice.

- The tool relies entirely on the `impact` column provided in the CSV. It cannot predict impact from the raw `ref` and `alt` nucleotide changes.

## Who did what

| Member | Main contributions | Commits |
|---|---|---|
| NUR ATHIRAH BINTI ABASA (A24CS0158) | `src/a1_triage.py` (`classify_variant()`, `triage()`), `GROUP_CONTRACT.md`, `AI_USE_LOG.md` | 4 |
| NUR ALIA AISHAH BINTI NAZRI SAKRI (A24CS0152) | `src/a1_triage.py` (`decision_counts()`, `impact_counts()`, `gene_summary()`), `docs/design.md`, `AI_USE_LOG.md` | 3 |
| AFINA SOLEHA BATRISYIA BINTI MOHD HISAFUDIN (A24CS0034) | `src/a1_triage.py` (`rank_variants()`, `results_to_csv()`, `build_report()`), `AI_USE_LOG.md` | 3 |
| FAKHIRA ANISA BINTI MOHD RADZI (A24CS0070) | `tests/test_a1_triage.py`, `README.md`, `AI_USE_LOG.md` | 4 |

## AI use

The group used AI at Level 1 (Tutor) to assist with understanding assignment requirements, formatting tests, and debugging. See AI_USE_LOG.md for full details and signatures.
