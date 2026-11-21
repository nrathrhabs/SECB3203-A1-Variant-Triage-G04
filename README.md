# Variant Triage Service (SECB3203 Assignment 1)

> Replace the text in this template. The README must let a stranger install, run and test the
> project with the exact commands below. All data are synthetic teaching data, not clinical data.

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
<activate command for your system>
pip install -r requirements.txt
```

## Run

<Write the exact command. The course command is: python src/a1_triage.py data/variants.csv data/params.json results>
<Say which files appear in results/.>

Run the service using:
python src/a1_triage.py data/variants.csv data/params.json results

The program saves its output files in the results/ directory. These files contain the triage results and summary information.



## Test and lint

```
python -m pytest
ruff check src
```

## Our parameters

Our thresholds, priority genes and top_k are in data/params.json (Minimum depth (min_depth): 12

Minimum quality (min_quality): 80

Priority genes: ATM, PTEN, EGFR, APC and BRCA2

Top K (top_k): 5).
They are read at run time and passed to the functions; they are not typed into the rules.


## Design

<Link to docs/design.md and say in two sentences what it contains.>

## Limitations

<At least two honest limitations, for example: rules use depth, quality and impact only; the data are synthetic.>
The triage decisions are based only on the available depth, quality, gene and impact information.

The project uses synthetic teaching data and must not be used for real clinical decisions.

The rule-based approach may not cover every possible genetic variant or clinical situation.


## Who did what

| Member | Main contributions | Commits |
|---|---|---|
| NUR ALIA AISHAH BINTI NAZRI SAKRI | NAZRI SAKRI

decision_counts(), impact_counts(), gene_summary() in src/a1_triage.py; docs/design.md | <number> |

## AI use

AI was used as a learning and assistance tool during the assignment. Details of the interactions are recorded in AI_USE_LOG.md.