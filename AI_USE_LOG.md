# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Assignment 1
- Group Members: 
    - NUR ATHIRAH BINTI ABASA, A24CS0158
    - <full name, matric>
    - <full name, matric>
    - FAKHIRA ANISA BINTI MOHD RADZI, A24CS0070
- Group ID: G04
- AI level: 1
- Tools cited: 
    - Member 1: OpenAI (2026). ChatGPT (GPT-6). Retrieved 21 November 2026 from https://chatgpt.com
    - Member 2: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>
    - Member 3: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>
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

## Entry 2 - Member 2: Full Name

- Date: <Date and time of the interaction>
- Tool: <Tool name, version, access date and URL (UTM citation format)>
- Purpose: <One of: explain, hint, review, debug, generate-code, generate-text, tests-plan, other>
- Prompt: <The exact prompt you typed (paste it)>
- Output: <What the AI gave back, in 1 to 3 lines (attach the full text if you used it)>
- Verified by: <How you checked it: ran pytest, read the docs, compared with data, asked lecturer>
- My change: <What you accepted, rejected or rewrote, and why>
- Used in: <File and function, or report section, where it ended up (or 'not used')>

## Entry 3 - Member 3: Full Name

- Date: <Date and time of the interaction>
- Tool: <Tool name, version, access date and URL (UTM citation format)>
- Purpose: <One of: explain, hint, review, debug, generate-code, generate-text, tests-plan, other>
- Prompt: <The exact prompt you typed (paste it)>
- Output: <What the AI gave back, in 1 to 3 lines (attach the full text if you used it)>
- Verified by: <How you checked it: ran pytest, read the docs, compared with data, asked lecturer>
- My change: <What you accepted, rejected or rewrote, and why>
- Used in: <File and function, or report section, where it ended up (or 'not used')>


## Entry 4 - Member 4: FAKHIRA ANISA BINTI MOHD RADZI

- Date: 22/11/2026, 12:34 AM
- Tool: DeepSeek (2026). DeepSeek-V4.1-Flash. Retrieved 22 November 2026 from https://www.deepseek.com
- Purpose: explain
- Prompt: "do i really need to test case folding and what boundary cases should i use for the thresholds"
- Output: It explained that I needed tests for 11/12/13 for depth and 79/80/81 for quality. It also confirmed that case folding (testing `aTm`) is strictly required by the assignment brief.
- Verified by: Re-read the assignment requirements and ran pytest to test all functions
- My change: Wrote at least 8 including 3 boundary test functions using actual params.json values
- Used in: tests/test_a1_triage.py

