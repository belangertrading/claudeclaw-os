# Full Eval Process (Track 2)

This is the complete evaluation process from Anthropic's skill-creator. Use for high-stakes skills where bad output has real consequences.

## When to Use Track 2

- Alert skills (output goes to paying subscribers)
- Voice writing skills (voice drift is invisible to the agent)
- Any skill where output goes to external humans
- When a skill has failed 3+ times and you need to verify the fix

## Step 1: Write Test Cases

Come up with 2-3 realistic test prompts — what a real user would actually say. Save to `evals/evals.json`:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

See `references/schemas.md` for the full schema including assertions.

## Step 2: Spawn All Runs (With-Skill AND Baseline)

For each test case, spawn TWO sub-agents in the same turn:

**With-skill run:**
```
Execute this task:
- Skill path: <path-to-skill>
- Task: <eval prompt>
- Input files: <eval files if any>
- Save outputs to: <workspace>/iteration-<N>/eval-<ID>/with_skill/outputs/
```

**Baseline run:**
- Creating a new skill → no skill at all (same prompt, no skill path)
- Improving an existing skill → snapshot the old version first, point baseline at it

Write `eval_metadata.json` for each test case with a descriptive name.

## Step 3: Draft Assertions While Runs Are In Progress

Don't wait — use the time productively. Good assertions are objectively verifiable with descriptive names. Subjective skills (writing style) are better evaluated qualitatively.

Update `eval_metadata.json` and `evals/evals.json` with assertions.

## Step 4: Capture Timing Data

When each sub-agent completes, save `total_tokens` and `duration_ms` to `timing.json`. This data only comes through the completion notification.

## Step 5: Grade, Aggregate, Launch Viewer

1. **Grade each run** — spawn grader sub-agent (see `agents/grader.md`). Save to `grading.json`. Fields: `text`, `passed`, `evidence`.

2. **Aggregate** — run:
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```

3. **Analyst pass** — read benchmark data, surface patterns. See `agents/analyzer.md`.

4. **Launch viewer:**
   ```bash
   nohup python <skill-creator-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   ```
   For iteration 2+: `--previous-workspace <workspace>/iteration-<N-1>`
   For headless: `--static <output_path>` for standalone HTML

5. **Tell the user** the viewer is open with two tabs: Outputs (qualitative) and Benchmark (quantitative).

## Step 6: Read Feedback and Improve

Read `feedback.json` after user submits reviews. Empty feedback = user thought it was fine. Focus on test cases with specific complaints.

Kill the viewer server when done: `kill $VIEWER_PID 2>/dev/null`

## Improving Between Iterations

1. **Generalize from feedback** — don't overfit to test cases. The skill runs a million times across many prompts.
2. **Keep the prompt lean** — remove things not pulling their weight.
3. **Explain the why** — Claude has good theory of mind. Explaining reasoning is more powerful than rigid MUSTs.
4. **Look for repeated work** — if all test runs independently wrote similar helper scripts, bundle that script in `scripts/`.

## The Iteration Loop

1. Apply improvements
2. Rerun all test cases into `iteration-<N+1>/`
3. Launch viewer with `--previous-workspace` pointing at previous iteration
4. Wait for user review
5. Read feedback, improve, repeat

Stop when: user is happy, feedback is all empty, or no meaningful progress.

## Advanced: Blind Comparison

For rigorous A/B between two skill versions. See `agents/comparator.md` and `agents/analyzer.md`. Optional — human review loop is usually sufficient.
