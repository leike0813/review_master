# Capability: stage-6-export-patch-path

## ADDED Requirements

### Requirement: Stage 6 manuscript exports must be patch-driven and complete

Stage 6 MUST export full manuscript variants from explicit patch truth stored in the database rather than hand-assembled local excerpts.

#### Scenario: Marked manuscript export

- **GIVEN** a workspace with authored Stage 6 export patches
- **WHEN** the export script generates `marked_manuscript`
- **THEN** it outputs a complete manuscript tree to a separate export directory
- **AND** modified regions are marked with the `changes` package
- **AND** the original manuscript inputs are left unchanged

#### Scenario: Clean manuscript matches marked manuscript content

- **GIVEN** a user-confirmed `marked_manuscript`
- **WHEN** the export script generates `clean_manuscript`
- **THEN** it uses the same patch truth as the marked export
- **AND** the resulting clean manuscript matches the confirmed marked manuscript content except for removal of `changes` markup
