# Design - Variant Triage Service

Write this BEFORE you write the code, then keep it up to date. It is marked by the lecturer.
Use your own words, your own thresholds and your own data. Delete the guidance in italics.

Group ID: <your group id>      Thresholds from data/params.json: min_depth = <...>, min_quality = <...>, top_k = <...>

## 1. Decomposition

| Question | Our answer |
|---|---|
| Input | |
| Output | |
| Constraints (named thresholds, what happens at exactly the threshold) | |
| Rule order and why the order matters | |
| Out of scope | |

## 2. Pseudocode or flowchart of classify_variant

*Give either structured pseudocode (indentation, IF / ELSE, RETURN) or a flowchart (a picture file
committed in docs/ and linked here, or a Mermaid block). Show all six rules.*

## 3. Hand trace

*Trace the first six rows of YOUR data/variants.csv (v1 to v6) with YOUR thresholds, then two more rows of
your choice that reach rules 3 to 6. Do it by hand BEFORE you run your code, then compare with your code.*

| Variant | Gene | Depth | Quality | Impact | Rule that fires | Decision | Reason |
|---|---|---|---|---|---|---|---|
| v1 | | | | | | | |

## 4. Test plan

*List the cases you will test: normal, boundary (exactly at YOUR thresholds, one below, one above), invalid or
awkward input (empty list, k = 0, k larger than the data, messy text). One line per case.*

## 5. Work plan

*Who builds which function, in which order, and how you will review each other's code.*
