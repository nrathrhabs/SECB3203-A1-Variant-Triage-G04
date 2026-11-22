# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Assignment 1: Variant Triage Service
- Student name: AFINA SOLEHA BATRISYIA BINTI MOHD HISAFUDIN 
- Matric no: A24CS0034
- Group ID: G04
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 22 November 2026 from [https://gemini.google.com](https://gemini.google.com)

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 21 November 2026, 11:33 PM
- Tool: Google (2026). Gemini. Retrieved 22 November 2026 from https://gemini.google.com
- Purpose: hint, review
- Prompt: "In `rank_variants`, I tried writing `r = r.row['decision'] != 'exclude'` and calling `.strip().lower()` on `IMPACT_ORDER`, and I got syntax and NameError issues with my sort key. How do I fix this?"
- Output: "You need a list comprehension `[r for r in results if r['decision'] != 'exclude']` to filter out excluded rows. Apply `.strip().lower()` to each variant's `r['impact']` instead of `IMPACT_ORDER`, put commas between all 5 items in your `_rank_key` return tuple, and pass `key=_rank_key` into `sorted()`."
- Verified by: Checked the sorting rules against the assignment specification and ran 'ruff check src'.
- My change: Replaced 'r.row' with a list comprehension, fixed '.strip().lower()' to target 'r['impact']', added missing commas in the tuple, and wrote the complete 'rank_variants' function.
- Used in: src/a1_triage.py(rank_variants)


## Entry 1

- Date: 22 November 2026, 12:21 AAM
- Tool: Google (2026). Gemini. Retrieved 22 November 2026 from https://gemini.google.com
- Purpose: review
- Prompt: "In `results_to_csv`, I redefined `CSV_COLUMNS` inside the function and wrote `results [str(r[col]) for col in CSV_COLUMNS]` without a loop or return statement. What am I missing?"
- Output: "`CSV_COLUMNS` is already defined at the top of `src/a1_triage.py`, so you don't need to re-type it. Start a `lines` list with `[','.join(CSV_COLUMNS)]`, loop over `for r in results:` to append `','.join(str(r[col]) for col in CSV_COLUMNS)` for each row, and `return '\n'.join(lines) + '\n'`."
- Verified by: Checked the CSV header and newline rules in the assignment brief and run 'ruff check src'
- My change: Removed the duplicate 'CSV_COLUMNS' definition inside the function, added the 'for' loop to build 'lines', and added the 'return' statement.
- Used in: src/a1_triage.py(results_to_csv)

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->

## Group signatures

- Signed: Afina Soleha Batrisyia, A24CS0034, 22 November 2026