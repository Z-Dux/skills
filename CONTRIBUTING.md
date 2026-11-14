# Contributing to AI Agent Skills Repository

Thank you for contributing to the **AI Agent Skills Repository**! This repository serves as a centralized, high-quality knowledge and procedure hub for AI agents across multiple domains (Animation, Engineering, Science, Productivity, and more).

---

## Repository Architecture

Skills are organized hierarchically by domain:

```text
skills/
  <domain>/                    # e.g., animation, science, frontend, devops
    <skill-name>/              # lowercase, hyphenated unique skill ID
      SKILL.md                 # Required: Main instruction & frontmatter file
      scripts/                 # Optional: Executable helpers or automation
      examples/                # Optional: Reference implementations
      references/              # Optional: In-depth technical docs
```

---

## Authoring Standards for `SKILL.md`

Every skill must have a valid `SKILL.md` adhering to the following structure:

```markdown
---
name: skill-name-with-hyphens
description: Use when [specific triggering condition]. Third person, under 500 characters.
---

# Human-Readable Skill Title

Brief conceptual summary explaining what this skill teaches the agent.

## Quick Reference / Cheat Sheet

| Scenario / Principle | Recommended Action / Syntax |
|----------------------|-----------------------------|
| Pattern A            | Implementation detail       |

## Core Guidelines & Procedures

1. Clear, ordered step-by-step instructions.
2. Concrete examples and rules.

## Code Examples

```typescript
// Practical code snippets
```

## Common Pitfalls

- Anti-patterns to avoid.
```

### Frontmatter Requirements

- **`name`** (required): Lowercase, hyphenated string (e.g. `web-motion-design`). **Must match the folder name exactly.**
- **`description`** (required):
  - Must begin with `"Use when..."` or clearly state trigger conditions.
  - Written in third person.
  - Focuses on *when* the agent should invoke this skill, not simply summarizing general knowledge.
  - Maximum 500 characters.

---

## Adding a New Skill

1. **Choose or create a domain** under `skills/<domain>/`.
2. **Create the skill folder**: `skills/<domain>/<skill-name>/`.
3. **Write `SKILL.md`**: Follow the authoring template above.
4. **Register the domain** in `.agents/skills.json` and `skills.json` if creating a new domain:
   ```json
   {
     "entries": [
       { "path": "skills/animation" },
       { "path": "skills/<new-domain>" }
     ]
   }
   ```
5. **Update the catalog**:
   ```bash
   python scripts/update_catalog.py
   ```
6. **Validate the repository**:
   ```bash
   python scripts/validate_skills.py
   ```
   All checks must pass with `0` errors.

---

## Validation Tooling

Run the automated validator to ensure all skills adhere to naming, frontmatter, and directory standards:

```bash
python scripts/validate_skills.py
```
