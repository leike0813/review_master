# Proposal: restructure-review-master-package-for-template-driven-rendering

## Summary

Restructure the published `review-master` package so the runtime no longer depends on hardcoded schema and Markdown skeletons inside Python scripts. Keep `SKILL.md` as the single entrypoint, move detailed stage instructions into `references/`, and move schema plus render templates into `assets/`.

## Why

The current DB-first runtime works, but it has two structural problems:

- `SKILL.md` mixes high-level contract and low-level execution details.
- `workspace_db.py` still hardcodes both SQLite schema statements and Markdown render skeletons.

This makes the package harder to maintain, harder to evolve safely, and harder to inspect outside Python code.

## What Changes

- Slim `review-master/SKILL.md` down to goals, non-goals, six-stage flow, core runtime contract, environment gating, script summary, and reference index.
- Reorganize `review-master/references/` so it contains only stage instructions and a small set of cross-stage reference documents.
- Externalize runtime schema into `review-master/assets/schema/review-master-schema.yaml`.
- Externalize render configuration and Markdown templates into `review-master/assets/templates/`.
- Stop rendering `workflow-state.md`; workflow state remains in SQLite and is surfaced through validator output and direct DB reads.
- Update the runtime scripts to read YAML schema and Jinja2 templates from `assets/`.
- Update playbooks and sample workspaces to match the new rendered-view contract.

## Impact

This is a structural refactor, not a workflow redesign.

- The runtime remains DB-first.
- `review-master.db` remains the only source of truth.
- Markdown views remain read-only.
- The SQLite business schema and stage logic stay the same.
- Agent SQL writes remain direct; no write helper script is introduced.
