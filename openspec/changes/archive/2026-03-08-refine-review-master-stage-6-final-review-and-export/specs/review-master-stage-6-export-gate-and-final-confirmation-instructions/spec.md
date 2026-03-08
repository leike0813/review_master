# Capability: review-master-stage-6-export-gate-and-final-confirmation-instructions

## ADDED Requirements

### Requirement: Stage 6 export uses a two-step gated flow

Stage 6 MUST export a marked manuscript before final clean export, and final clean export MUST require a final user confirmation.

#### Scenario: Marked manuscript comes first

- **Given** Stage 6 has assembled thread-level response rows
- **When** the Agent performs the first export step
- **Then** the docs must require a marked manuscript using the `changes` package
- **And** the docs must forbid treating that step as the final export

#### Scenario: Final clean export requires strict closure and final confirmation

- **Given** the marked manuscript has been reviewed
- **When** the Agent prepares the final export
- **Then** the docs must require a final user confirmation
- **And** the docs must require all export gates to be closed
- **And** the docs must require final outputs in:
- **And** Markdown Response Letter format
- **And** LaTeX Response Letter format
- **And** a clean manuscript format
- **And** the docs must forbid overwriting the original input files
