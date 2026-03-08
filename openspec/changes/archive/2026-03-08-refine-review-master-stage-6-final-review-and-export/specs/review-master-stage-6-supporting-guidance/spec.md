# Capability: review-master-stage-6-supporting-guidance

## ADDED Requirements

### Requirement: Stage 6 supporting guidance stays aligned across docs, schema, and views

All Stage 6 supporting guidance MUST use the same terminology for style profiles, copy variants, thread rows, marked export, and final export.

#### Scenario: Supporting docs agree on Stage 6 responsibilities

- **Given** the skill summary, Stage 6 handbook, SQL recipes, workflow-state machine, helper-scripts guide, and runtime digest
- **When** they describe Stage 6
- **Then** they must all describe the same five substeps
- **And** they must all treat Stage 6 semantic work as Agent-owned rather than script-owned

#### Scenario: Rendered views expose Stage 6 review surfaces

- **Given** a Stage 6 workspace with authored data
- **When** the read-only views are rendered
- **Then** the package must provide a style-profile view
- **And** a copy-variant view
- **And** a Markdown response-table preview
- **And** a LaTeX response-table preview
- **And** the final checklist must expose export artifact status
