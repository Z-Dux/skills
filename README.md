# AI Agent Skills Repository

[![Skills](https://img.shields.io/badge/Skills-144-blue.svg)](catalog.json)
[![Domains](https://img.shields.io/badge/Domains-1%20(Animation)-emerald.svg)](#domains-overview)
[![Engine](https://img.shields.io/badge/Engine-Antigravity%20%7C%20Claude%20Code-purple.svg)](https://github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A centralized, professional AI agent skills repository designed to house, organize, and version procedural skills and expert runbooks for AI agents.

Every skill in this repository follows the open **Agentic Skill Specification** (`SKILL.md` with structured YAML frontmatter), optimized for progressive disclosure to preserve agent context windows while delivering deep domain expertise on demand.

---

## 🗂️ Repository Architecture

```text
skills-repo/
├── .agents/                          # Antigravity project configuration
│   ├── skills.json                   # Workspace skill discovery paths
│   └── rules/                        # Workspace-active agent guidelines
│       └── AGENTS.md                 # Disney Animation Principles guide
├── skills/                           # Domain-partitioned skills catalog
│   └── animation/                    # 144 skills: Disney's 12 Animation Principles
│       ├── 3d-spatial/
│       │   └── SKILL.md
│       ├── squash-stretch-mastery/
│       │   └── SKILL.md
│       ├── web-motion-design/
│       │   └── SKILL.md
│       └── ... (144 self-contained skill packages)
├── docs/                             # Deep-dive documentation & cross-indexes
│   └── animation/                    # Categorical guides & taxonomy
│       ├── 01-by-domain/
│       ├── 02-by-thinking-style/
│       ├── 03-by-role-persona/
│       ├── 04-by-skill-level/
│       ├── 05-by-animation-type/
│       ├── 06-by-emotional-outcome/
│       ├── 07-by-ui-element/
│       ├── 08-by-industry/
│       ├── 09-by-tool-framework/
│       ├── 10-by-time-scale/
│       ├── 11-by-principle-focus/
│       ├── 12-by-problem-type/
│       └── index.md
├── rules/                            # General & framework-specific agent rules
│   ├── AGENTS.md                     # Universal agent rules
│   └── animation-principles.md       # Animation principles rule reference
├── scripts/                          # CI & maintenance automation
│   ├── validate_skills.py            # Frontmatter & schema integrity validator
│   └── update_catalog.py             # Automated catalog.json generator
├── catalog.json                      # Machine-readable registry of all skills
├── skills.json                       # Portable skills manifest
├── CONTRIBUTING.md                   # Skill authoring guide & quality standards
└── LICENSE                           # MIT License
```

---

## 🎨 Domains Overview

### 1. Animation & Motion Design (`skills/animation/`)

Imported from the **Animation Principles** collection (originally created by Dylan Tarre), this domain teaches AI agents how to apply Disney's 12 Principles of Animation to modern user interfaces, web applications, mobile interactions, 3D environments, and games.

The 144 animation skills are organized into 12 distinct lenses:

| Lens | Description | Key Skills |
|------|-------------|------------|
| **1. By Application Domain** | Platform & medium-specific motion | `web-motion-design`, `mobile-touch`, `3d-spatial`, `game-development`, `data-visualization` |
| **2. By Thinking Style** | Mental models for motion strategy | `attention-direction`, `anticipation-payoff`, `physics-intuition`, `rhythm-pacing` |
| **3. By Role & Persona** | Specialized workflows for distinct disciplines | `frontend-developer`, `motion-designer`, `game-designer`, `creative-director` |
| **4. By Skill Level** | Calibrated explanations from novice to master | `absolute-beginner`, `intermediate`, `advanced`, `expert`, `master` |
| **5. By Animation Type** | Specific UI motion states and patterns | `entrance-animations`, `exit-animations`, `continuous-loops`, `state-changes` |
| **6. By Emotional Outcome** | Crafting precise user sentiment | `joy-delight`, `calm-relaxation`, `power-confidence`, `trust-reliability` |
| **7. By UI Element** | Interaction design for concrete components | `buttons-ctas`, `modals-dialogs`, `forms-inputs`, `accordions-dropdowns` |
| **8. By Industry** | Domain-tailored motion identities | `fintech-banking`, `e-commerce-retail`, `healthcare-medical`, `saas-productivity` |
| **9. By Tool & Framework** | Implementation code and APIs | `css-native`, `gsap-greensock`, `framer-motion`, `rive-animations`, `anime-js` |
| **10. By Time Scale** | Duration calibration & pacing | `instant-0-100ms`, `micro-100-200ms`, `medium-300-500ms`, `slow-800-1200ms` |
| **11. By Principle Focus** | Deep-dives into individual Disney principles | `squash-stretch-mastery`, `timing-mastery`, `anticipation-mastery`, `arc-mastery` |
| **12. By Problem Type** | Diagnostic & troubleshooting runbooks | `performance-optimization`, `motion-sickness`, `ux-friction`, `timing-calibration` |

Full taxonomy documentation and cross-references can be explored in [docs/animation/index.md](docs/animation/index.md).

---

## 🚀 How to Use These Skills

### In Antigravity

This repository includes native Antigravity workspace configuration in `.agents/skills.json`.

1. **Open directly in Antigravity**:
   Simply open this repository directory in Antigravity. The agent automatically scans all configured domain paths in `.agents/skills.json` and registers all skills on startup.

2. **Reference from another project**:
   Add this repository's domain path to your project's `.agents/skills.json`:
   ```json
   {
     "entries": [
       { "path": "D:/skills/skills/animation" }
     ]
   }
   ```

3. **Global Machine Configuration**:
   To make all animation skills globally available across every project on your machine, add the path to your global Antigravity configuration in `~/.gemini/config/skills.json`:
   ```json
   {
     "entries": [
       { "path": "D:/skills/skills/animation" }
     ]
   }
   ```

### In Claude Code / Open Agent Systems

Skills conform to standard `SKILL.md` format. To import skills into Claude Code:
```bash
# Symlink or copy desired skills to your project
cp -r D:/skills/skills/animation/<skill-name> ~/.claude/skills/
```

### Direct Agent Invocation

You can instruct your agent to use any skill by its identifier:

```text
"Apply the web-motion-design and buttons-ctas skills to animate this checkout button using GSAP."
```

---

## 🛠️ Repository Tooling & Automation

### Validate Skills (`scripts/validate_skills.py`)

Performs strict integrity validation across all skills in all domains:
- Verifies directory structure and `SKILL.md` presence.
- Enforces YAML frontmatter schema (`name` matching folder, non-empty `description`).
- Validates description length and third-person phrasing.
- Checks global skill ID uniqueness.
- Cross-references with `catalog.json`.

```bash
python scripts/validate_skills.py
```

### Update Catalog (`scripts/update_catalog.py`)

Parses every skill across all domains and regenerates the centralized `catalog.json` registry:

```bash
python scripts/update_catalog.py
```

---

## 🤝 Adding New Skills

See [CONTRIBUTING.md](CONTRIBUTING.md) for full instructions on authoring new skills, naming conventions, and quality standards.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).  
The Animation Principles skill collection was originally authored by [Dylan Tarre](https://github.com/dylantarre/animation-principles) and is included under the MIT License.
