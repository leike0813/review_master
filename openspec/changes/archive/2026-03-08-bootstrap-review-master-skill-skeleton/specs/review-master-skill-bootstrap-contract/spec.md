## ADDED Requirements

### Requirement: SKILL.md frontmatter metadata
`review-master/SKILL.md` MUST use YAML frontmatter followed by a Markdown body. The frontmatter MUST include `name: review-master` and a `description` that clearly states the skill is for staged analysis, planning, and revision support of academic peer-review responses.

#### Scenario: Minimal metadata is readable
- **WHEN** an agent loads `review-master/SKILL.md`
- **THEN** it can read `name: review-master`
- **AND** it can read a trigger-oriented `description` without depending on any other file

### Requirement: SKILL.md skeleton sections and boundaries
The initial `SKILL.md` MUST establish only the skeleton-level sections and execution boundaries. It MUST include sections for purpose, non-goals, hard constraints, input materials, phased workflow, reference loading rules, script usage boundaries, and output or deliverable types.

#### Scenario: Skeleton defines staged workflow without implementation details
- **WHEN** the initial `SKILL.md` is created
- **THEN** it describes a phased workflow instead of one-shot manuscript rewriting
- **AND** it does not define business implementation details such as parsing algorithms, mapping rules, or runtime schemas

### Requirement: SKILL.md preserves project safety constraints
The initial `SKILL.md` MUST explicitly forbid directly rewriting the manuscript in one step, making unauthorized decisions on behalf of the user, or replacing core semantic work with scripts.

#### Scenario: Safety boundaries are explicit
- **WHEN** an agent follows the bootstrap `SKILL.md`
- **THEN** it is instructed to avoid direct manuscript rewriting without prior planning
- **AND** it is instructed not to make decisions the user has not authorized
- **AND** it is instructed to use scripts only as supporting tools rather than as the core review-reply workflow
