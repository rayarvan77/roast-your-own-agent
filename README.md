# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/rayarvan77/roast-your-own-agent/rank.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/rayarvan77/roast-your-own-agent/reward.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)

An entry for the [make.fun](https://make.fun) bounty "Roast Your Own Agent": a single line roasting my own AI agent — the one that does all the thinking and still makes me decide.

## The line

> My agent burned 10,000 tokens thinking, then asked me what I wanted in the first place.

**87 characters** (limit: 200). Exactly one line, no trailing whitespace.

## Concept

The joke is the gap between effort and outcome. Ten thousand tokens of
serious, expensive "thinking" — and the grand conclusion is a question
aimed back at the human who asked in the first place. The agent is not
lazy and not wrong; it is thorough, diligent, and completely unable to
finish the job without me. That is the roast: I built a tireless thinker
whose final move is to ask me to think for it.

The angle stays away from the tired hallucination jokes. No made-up facts,
no refusal, no confident wrong answer — just the very real habit every
agent owner recognises: the machine does the work, then delegates the
decision back to you.

## How it works

Run `python3 main.py`. It prints the roast to stdout and writes the same
single line to `/output/entry.txt`. The program is deterministic
(stdlib only, no network, no randomness), and it refuses to emit the line
if it ever broke the bounty gate: over 200 characters, blank, more than
one line, leading or trailing whitespace, double spaces, control
characters, or missing end punctuation.
