# Design - Variant Triage Service

Write this BEFORE you write the code, then keep it up to date. It is marked by the lecturer.
Use your own words, your own thresholds and your own data. Delete the guidance in italics.

Group ID: G04      
Thresholds from data/params.json:
 min_depth = 12, 
 min_quality = 80, 
 top_k = 5

## 1. Decomposition


| Question | Our answer |
|----------|---|
| Input    | A CSV file containing variant information (variant ID, gene, chromosome, position, reference allele, alternate allele, depth, quality and impact), together with parameters from params.json. |
| Output   | A list of classified variants with a decision and reason for each variant, decision counts, impact counts, gene summaries, ranked variants, a CSV output file and a text report.|
| Constraints (named thresholds, what happens at exactly the threshold) | Minimum depth is 12, minimum quality is 80 and top_k is 5. Variants with depth below 12 or quality below 80 are excluded. Values exactly equal to the thresholds pass the respective checks. |
| Rule order and why the order matters | Rules are checked in order: low depth, low quality, priority gene with high/moderate impact, priority gene with low/modifier impact, non-priority gene with high/moderate impact, and non-priority gene with low/modifier impact. The order matters because the first matching rule determines the decision. |
| Out of scope | The system uses synthetic teaching data only. It does not provide medical advice, diagnose diseases, recommend treatment or replace professional clinical judgement. |

## 2. Pseudocode or flowchart of classify_variant

START

Read variant information and parameters.

Convert depth and quality into numbers.
Normalize gene and impact text for comparison.

IF depth < min_depth:
    RETURN exclude, "low depth"

ELSE IF quality < min_quality:
    RETURN exclude, "low quality"

ELSE IF gene is a priority gene
        AND impact is high or moderate:
    RETURN prioritize

ELSE IF gene is a priority gene
        AND impact is low or modifier:
    RETURN review

ELSE IF gene is not a priority gene
        AND impact is high or moderate:
    RETURN review

ELSE IF gene is not a priority gene
        AND impact is low or modifier:
    RETURN exclude

END

## 3. Hand trace

*Trace the first six rows of YOUR data/variants.csv (v1 to v6) with YOUR thresholds, then two more rows of
your choice that reach rules 3 to 6. Do it by hand BEFORE you run your code, then compare with your code.*

| Variant | Gene | Depth | Quality | Impact | Rule that fires | Decision | Reason |
|---|---|---:|---:|---|---|---|---|
| v1 | APC | 9 | 90 | low | Rule 1 | exclude | low depth |
| v2 | KRAS | 10 | 90 | high | Rule 1 | exclude | low depth |
| v3 | TP53 | 11 | 90 | modifier | Rule 1 | exclude | low depth |
| v4 | ATM | 30 | 79 | modifier | Rule 2 | exclude | low quality |
| v5 | EGFR | 30 | 80 | moderate | Rule 3 | prioritize | priority gene with significant impact |
| v6 | MYC | 30 | 81 | moderate | Rule 5 | review | non-priority gene with significant impact |
| v7 | PTEN | 23 | 90 | modifier | Rule 4 | review | priority gene with low/modifier impact |
| v8 | PTEN | 17 | 78 | low | Rule 2 | exclude | low quality |
| v9 | KRAS | 30 | 94 | modifier | Rule 6 | exclude | non-priority gene with low/modifier impact |


## 4. Test plan

| Test case | Input / Condition | Expected result |
|---|---|---|
| Normal - prioritize | Priority gene ATM, depth 30, quality 90, high impact | prioritize |
| Normal - review | Non-priority gene KRAS, depth 30, quality 90, high impact | review |
| Normal - exclude | Non-priority gene KRAS, depth 30, quality 90, low impact | exclude |
| Boundary - minimum depth | Depth exactly 12, quality 90 | Pass depth check |
| Boundary - below minimum depth | Depth 11, quality 90 | exclude due to low depth |
| Boundary - above minimum depth | Depth 13, quality 90 | Pass depth check |
| Boundary - minimum quality | Depth 30, quality exactly 80 | Pass quality check |
| Boundary - below minimum quality | Depth 30, quality 79 | exclude due to low quality |
| Boundary - above minimum quality | Depth 30, quality 81 | Pass quality check |
| Empty input | Empty variant list | Return an empty result list and zero counts |
| k = 0 | Request top 0 variants | Return an empty ranked list |
| k larger than data | Request more variants than available | Return all eligible variants |
| Invalid k | Negative k value | Raise ValueError |
| Awkward input | Gene " ATM " and impact " MODERATE " | Normalize text before comparison |

## 5. Work plan

Member: Nur Alia Aishah

Assigned task: Implement decision_counts(), impact_counts() and gene_summary(). Prepare and maintain docs/design.md and record AI usage in AI_USE_LOG.md.

Review:Run relevant tests, check output and request teammate review.



The group will work on separate Git branches for assigned tasks. Each member will test their own functions before creating a pull request. Other group members will review the changes, check the test results and discuss any corrections before merging into the main branch.