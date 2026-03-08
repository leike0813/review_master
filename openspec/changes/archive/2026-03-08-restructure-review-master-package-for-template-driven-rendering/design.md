# Design: restructure-review-master-package-for-template-driven-rendering

## Summary

This change separates runtime concerns into three layers:

1. `SKILL.md` as a short operational entrypoint
2. `references/` as instruction-only documentation
3. `assets/` as static runtime resources for schema and rendering

The DB-first runtime contract stays intact, but the schema source and render skeletons move out of Python code.

## Decisions

### 1. Keep `SKILL.md` short

`SKILL.md` should no longer contain exhaustive stage details or view-by-view template explanations. It should only define the runtime contract, the phase sequence, environment gating, and where the detailed rules live.

### 2. Move schema to YAML

The SQLite schema source of truth moves to `assets/schema/review-master-schema.yaml`. The Python runtime reads this YAML and executes the listed statements. This keeps schema evolution inspectable without embedding SQL literals in code.

### 3. Move view skeletons to Jinja2 templates

Markdown rendering moves to `assets/templates/*.md.j2`, coordinated by `assets/templates/render-manifest.yaml`. The templates retain explanatory text because the rendered views are primarily user-facing and can also provide lightweight context back to the Agent.

### 4. Retire `workflow-state.md`

Workflow state is operational rather than user-facing. It remains in SQLite only. The validator's `instruction_payload` becomes the primary machine-readable surface for current state. Users continue reading the rendered Markdown work products, not a separate state file.

### 5. Add explicit runtime-environment gating

Before script-driven execution begins, the Agent must verify that the host Python environment satisfies the runtime dependencies. If not, the Agent must ask the user whether installation is approved. If installation is rejected, the workflow falls back to Agent-authored Markdown rendering while SQLite remains the source of truth.

## Implementation Notes

- `workspace_db.py` becomes a resource loader plus DB/query/render orchestrator.
- `init_artifact_workspace.py` initializes from YAML schema and renders from Jinja2 templates.
- `validate_artifact_consistency.py` keeps DB-first validation, but render output comes from template assets instead of hardcoded strings.
- `references/` is reorganized around six stage documents plus cross-stage references.
- Existing reference files that only described rendered views are removed.

## Risks

- The scripts now depend on `PyYAML` and `Jinja2`. This is intentional and must be reflected in `SKILL.md` and `helper-scripts.md`.
- Playbook sample workspaces and validator output fixtures must be updated so they no longer expect `workflow-state.md`.

## Validation

- `openspec validate restructure-review-master-package-for-template-driven-rendering --type change --strict`
- `mypy` on the updated runtime scripts
- `init_artifact_workspace.py` should initialize a new workspace from YAML and templates
- `validate_artifact_consistency.py` should re-render the Markdown views from template assets
- The two example final workspaces must continue to validate successfully
