# Variant Triage Service (SECB3203 Assignment 1)

> Replace the text in this template. The README must let a stranger install, run and test the
> project with the exact commands below. All data are synthetic teaching data, not clinical data.

## Group

- Group ID: <your group id>
- Members: <full name (matric)>, <full name (matric)>, <full name (matric)>

## What this project does

<Three or four sentences: what a variant triage service is, what goes in, what comes out.>

## Set up

```
python -m venv .venv
<activate command for your system>
pip install -r requirements.txt
```

## Run

<Write the exact command. The course command is: python src/a1_triage.py data/variants.csv data/params.json results>
<Say which files appear in results/.>

## Test and lint

```
python -m pytest
ruff check src
```

## Our parameters

Our thresholds, priority genes and top_k are in data/params.json (<write the values here>).
They are read at run time and passed to the functions; they are not typed into the rules.

## Design

<Link to docs/design.md and say in two sentences what it contains.>

## Limitations

<At least two honest limitations, for example: rules use depth, quality and impact only; the data are synthetic.>

## Who did what

| Member | Main contributions | Commits |
|---|---|---|
| <name> | <files or functions> | <number> |

## AI use

<One sentence: see AI_USE_LOG.md. Say whether the group used AI.>
