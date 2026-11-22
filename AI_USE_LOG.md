# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Assignment 1
- Group Members: 
    - NUR ATHIRAH BINTI ABASA, A24CS0158
    - NUR ALIA AISHAH BINTI NAZRI SAKRI, A24CS0152 
    - AFINA SOLEHA BATRISYIA BINTI MOHD HISAFUDIN, A24CS0034
    - FAKHIRA ANISA BINTI MOHD RADZI, A24CS0070
- Group ID: G04
- AI level: 1
- Tools cited: 
    - Member 1: OpenAI (2026). ChatGPT (GPT-6). Retrieved 21 November 2026 from https://chatgpt.com
    - Member 2: OpenAI (2026). ChatGPT (GPT-6). Retrieved 21 November 2026 from https://chatgpt.com
    - Member 3: Google (2026). Gemini. Retrieved 22 November 2026 from https://gemini.google.com
    - Member 4: DeepSeek (2026). DeepSeek-V4.1-Flash. Retrieved 22 November 2026 from https://www.deepseek.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1 - Member 1: NUR ATHIRAH BINTI ABASA

- Date: 21/11/2026, 0130
- Tool: OpenAI ChatGPT (GPT-6), accessed 21 November 2026, https://chatgpt.com
- Purpose: explain
- Prompt: "HELP ME ON HOW TO IMPLEMENTS THIS FUNCTIONS WITH CLEAR STEP BY STEP EXPLANATIONS" (with the pasted T2 question)
- Output: ChatGPT reviewed the implementation and highlighted syntax, rule ordering, input handling and reason-format requirements.
- Verified by: Reviewed the feedback against the assignment requirements and ran python -m py_compile src/a1_triage.py.
- My change: Used the explanation to understand the requirements and independently implemented the function.
- Used in: src/a1_triage.py — classify_variant(), triage()


## Entry 2 - Member 2: NUR ALIA AISHAH BINTI NAZRI SAKRI

- Date: 22 NOVEMBER 2026
- Tool:  OpenAI ChatGPT (GPT-6), accessed 22 November 2026, https://chat.openai.com
- Purpose: explain
- Prompt: "How can I count variant impacts while excluding variants with an exclude decision? Can you explain the logic step by step?"
- Output: AI explained how to loop through a list of dictionaries, skip excluded variants and count the remaining impact categories.
- Verified by: Compared the explanation with the impact counting requirements in the assignment.
- My change: Used the explanation to understand the filtering and counting process for my function.
- Used in: src/a1_triage.py - impact_counts().

## Entry 3 - Member 2: NUR ALIA AISHAH BINTI NAZRI SAKRI

- Date: 22 NOVEMBER 2026
- Tool:  OpenAI ChatGPT (GPT-6), accessed 22 November 2026, https://chat.openai.com
- Purpose: explain
- Prompt: "How do I group variants by gene and calculate the average depth for each gene using Python dictionaries?"
- Output: AI explained how to group records, calculate totals and counts, and find the mean depth for each gene.
- Verified by: Checked the explanation using the variant records in data/variants.csv.
- My change:  Applied the concept to understand how gene summaries and mean depth calculations work.
- Used in: src/a1_triage.py - gene_summary().

## Entry 4 - Member 2: NUR ALIA AISHAH BINTI NAZRI SAKRI

- Date: 22 NOVEMBER 2026
- Tool:  OpenAI ChatGPT (GPT-6), accessed 22 November 2026, https://chat.openai.com
- Purpose: explain
- Prompt: "explain how dictionary data works in Python and how I can use it to count the number of variants under each decision?"
- Output: AI explained how dictionaries store key-value pairs and how to update counts using loops.
- Verified by: Reviewed the explanation and compared it with the decision categories in the assignment.
- My change: Used the explanation to understand how decision counts should be organised before implementing the function.
- Used in: src/a1_triage.py - decision_counts().

## Entry 5 - Member 3: AFINA SOLEHA BATRISYIA BINTI MOHD HISAFUDIN

- Date: 21 November 2026, 11:33 PM
- Tool: Google (2026). Gemini. Retrieved 22 November 2026 from https://gemini.google.com
- Purpose: hint, review
- Prompt: "In `rank_variants`, I tried writing `r = r.row['decision'] != 'exclude'` and calling `.strip().lower()` on `IMPACT_ORDER`, and I got syntax and NameError issues with my sort key. How do I fix this?"
- Output: "You need a list comprehension `[r for r in results if r['decision'] != 'exclude']` to filter out excluded rows. Apply `.strip().lower()` to each variant's `r['impact']` instead of `IMPACT_ORDER`, put commas between all 5 items in your `_rank_key` return tuple, and pass `key=_rank_key` into `sorted()`."
- Verified by: Checked the sorting rules against the assignment specification and ran 'ruff check src'.
- My change: Replaced 'r.row' with a list comprehension, fixed '.strip().lower()' to target 'r['impact']', added missing commas in the tuple, and wrote the complete 'rank_variants' function.
- Used in: src/a1_triage.py(rank_variants)


## Entry 6 - Member 3: AFINA SOLEHA BATRISYIA BINTI MOHD HISAFUDIN

- Date: 22 November 2026, 12:21 AAM
- Tool: Google (2026). Gemini. Retrieved 22 November 2026 from https://gemini.google.com
- Purpose: review
- Prompt: "In `results_to_csv`, I redefined `CSV_COLUMNS` inside the function and wrote `results [str(r[col]) for col in CSV_COLUMNS]` without a loop or return statement. What am I missing?"
- Output: "`CSV_COLUMNS` is already defined at the top of `src/a1_triage.py`, so you don't need to re-type it. Start a `lines` list with `[','.join(CSV_COLUMNS)]`, loop over `for r in results:` to append `','.join(str(r[col]) for col in CSV_COLUMNS)` for each row, and `return '\n'.join(lines) + '\n'`."
- Verified by: Checked the CSV header and newline rules in the assignment brief and run 'ruff check src'
- My change: Removed the duplicate 'CSV_COLUMNS' definition inside the function, added the 'for' loop to build 'lines', and added the 'return' statement.
- Used in: src/a1_triage.py(results_to_csv)


## Entry 7 - Member 4: FAKHIRA ANISA BINTI MOHD RADZI

- Date: 22/11/2026, 12:34 AM
- Tool: DeepSeek (2026). DeepSeek-V4.1-Flash. Retrieved 22 November 2026 from https://www.deepseek.com
- Purpose: explain
- Prompt: "do i really need to test case folding and what boundary cases should i use for the thresholds"
- Output: It explained that I needed tests for 11/12/13 for depth and 79/80/81 for quality. It also confirmed that case folding (testing `aTm`) is strictly required by the assignment brief.
- Verified by: Re-read the assignment requirements and ran pytest to test all functions
- My change: Wrote at least 8 including 3 boundary test functions using actual params.json values
- Used in: tests/test_a1_triage.py

## Entry 8 - Member 4: FAKHIRA ANISA BINTI MOHD RADZI

- Date: 22/11/2026 3:23 AM
- Tool: DeepSeek (2026). DeepSeek-V4.1-Flash. Retrieved 22 November 2026 from https://www.deepseek.com
- Purpose: review
- Prompt: "i saw a pylance warning that the reason variable is not accessed in boundary tests. do i really need to assert the reason, or can i just ignore it?"
- Output: It explained that while the test would pass, asserting the reason protects the group's marks for R2 (recording a reason for every decision). It suggested either asserting a keyword like `assert "depth" in reason` or renaming the variable to `_` to suppress the warning.
- Verified by: I added the `assert "depth" in reason` and `assert "quality" in reason` lines to my boundary tests, confirmed the Pylance warning disappeared, and ran pytest.
- My change: I accepted the suggestion to assert the reason and added assertions checking for the specific rule words (depth/quality).
- Used in: tests/test_a1_triage.py

