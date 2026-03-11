## ADDED Requirements

### Requirement: Runtime language context is first-class state

The runtime workspace MUST persist the confirmed document language and working language as part of the DB-first runtime contract.

#### Scenario: language context row exists after initialization

- **WHEN** `init_artifact_workspace.py` initializes a workspace
- **THEN** the runtime schema MUST include `runtime_language_context`
- **AND** the table MUST store `document_language`, `working_language`, detection provenance, and `languages_confirmed`

### Requirement: workspace-local localization overlay overrides package defaults

The runtime MUST support workspace-local localization assets without replacing the skill package scripts.

#### Scenario: workspace messages override package messages

- **WHEN** `runtime-localization/working-messages.json` or `runtime-localization/document-messages.json` exists in the workspace
- **THEN** render and gate logic MUST prefer those files over package-default messages
- **AND** missing keys MUST fall back to the package-default message catalog

#### Scenario: optional template overrides are workspace-scoped

- **WHEN** `runtime-localization/templates/` contains a template with the same name as a packaged template
- **THEN** the renderer MUST load the workspace template first
- **AND** packaged templates MUST remain the fallback source
