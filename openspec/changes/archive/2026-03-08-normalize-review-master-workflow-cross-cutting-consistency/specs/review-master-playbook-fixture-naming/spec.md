# Capability: review-master-playbook-fixture-naming

## ADDED Requirements

### Requirement: playbook fixture paths use formal gate-and-render naming

Playbook sample fixture directories MUST use the same formal gate-and-render terminology as the published skill docs.

#### Scenario: fixture paths do not keep historical validator naming

- **Given** sample fixtures are part of the repository's official workflow examples
- **When** a playbook references stored gate output
- **Then** the referenced directory name must use `gate-and-render-output/`
- **And** `validator-output/` must not remain the formal sample path
