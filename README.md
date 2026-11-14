# AI Agent Skills Repository

[![Skills](https://img.shields.io/badge/Skills-163-blue.svg)](catalog.json)
[![Domains](https://img.shields.io/badge/Domains-2%20(Animation%2C%20Design%20Engineering)-emerald.svg)](#-domains-overview)
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
│       ├── AGENTS.md                 # Universal Disney animation principles guide
│       └── design-engineering.md     # Emil Kowalski's animation & craft standards
├── skills/                           # Domain-partitioned skills catalog
│   ├── animation/                    # 144 skills: Disney's 12 Animation Principles
│   │   ├── 3d-spatial/SKILL.md
│   │   ├── squash-stretch-mastery/SKILL.md
│   │   └── ... (144 self-contained skill packages)
│   └── design-engineering/           # 19 skills: Emil Kowalski's Design Engineering
│       ├── animate/SKILL.md
│       ├── apple-design/SKILL.md
│       ├── choreograph/SKILL.md
│       ├── emil-design-eng/SKILL.md
│       ├── gestures/SKILL.md
│       └── ... (19 craft & motion skills with recipes and standards)
├── docs/                             # Deep-dive documentation & cross-indexes
│   ├── animation/                    # 12-category animation taxonomy & index
│   └── design-engineering/           # UI & Performance cheatsheets & catalog
│       ├── performance-cheatsheet.md
│       ├── ui-cheatsheet.md
│       └── index.md
├── rules/                            # General & framework-specific agent rules
│   ├── AGENTS.md                     # Universal agent rules
│   ├── animation-principles.md       # Disney animation principles reference
│   └── design-engineering.md         # Design engineering standards reference
├── scripts/                          # CI & maintenance automation
│   ├── validate_skills.py            # Frontmatter & schema integrity validator
│   ├── update_catalog.py             # Automated catalog.json generator
│   └── import_emil_skills.py         # Design engineering import utility
├── catalog.json                      # Machine-readable registry of all 163 skills
├── skills.json                       # Portable skills manifest
├── CONTRIBUTING.md                   # Skill authoring guide & quality standards
└── LICENSE                           # MIT License
```

---

## 🎨 Domains Overview

### 1. Design Engineering (`skills/design-engineering/`)

Curated from [Emil Kowalski's Skills for Designers and Engineers](https://github.com/emilkowalski/skills) (ex-Vercel, Linear, creator of [Sonner](https://sonner.emilkowal.ski)). These 19 skills instill taste, high craft, fluid interaction physics, and performance discipline into agentic UI workflows:

| Category | Skills | Focus |
|----------|--------|-------|
| **Motion Implementation** | `animate`, `animate-expo`, `choreograph`, `gestures` | Step-by-step motion decisions, 1:1 touch tracking, interruption, React Native/Expo |
| **Taste & Philosophy** | `emil-design-eng`, `learn-taste`, `apple-design` | The high craft bar, translating WWDC principles to web, persisting taste into `DESIGN.md` |
| **Audit & Optimization** | `review-animations`, `improve-animations`, `find-animation-opportunities`, `remove-animations` | Identifying motion opportunities, stripping over-animation, auditing codebases |
| **Performance** | `animation-performance` | Frame budget discipline, composite-only transforms, off-thread animations |
| **Testing & Iteration** | `break-ui`, `prototype` | Stress-testing UI with worst-case data; rapid variant exploration with visual pickers |
| **Libraries & Stack** | `pick-ui-library`, `ask-sonner` | Trusted component libraries, comprehensive Sonner toast recipes & troubleshooting |
| **Platforms & Native** | `mobile-native`, `write-swift` | Eliminating mobile web quirks (100vh bug, tap flash); modern Swift 6 concurrency |
| **Reference** | `animation-vocabulary` | Reverse-lookup glossary translating colloquial descriptions to exact motion terms |

**Reference Documentation & Cheatsheets**:
- [docs/design-engineering/ui-cheatsheet.md](docs/design-engineering/ui-cheatsheet.md): Essential UI craft rules (tabular numbers, tracking, active scales, eased gradients).
- [docs/design-engineering/performance-cheatsheet.md](docs/design-engineering/performance-cheatsheet.md): Rapid fixes for animation jank, list lag, and blur costs.
- [rules/design-engineering.md](rules/design-engineering.md): Emil's animation standards, frequency tables, and custom bezier curves.

---

### 2. Animation Principles (`skills/animation/`)

Imported from the **Animation Principles** collection (originally created by Dylan Tarre), this domain teaches AI agents how to apply Disney's 12 Principles of Animation across 144 focused skills:

| Lens | Description | Key Skills |
|------|-------------|------------|
| **By Application Domain** | Platform & medium-specific motion | `web-motion-design`, `mobile-touch`, `3d-spatial`, `game-development`, `data-visualization` |
| **By Thinking Style** | Mental models for motion strategy | `attention-direction`, `anticipation-payoff`, `physics-intuition`, `rhythm-pacing` |
| **By Role & Persona** | Specialized workflows for distinct disciplines | `frontend-developer`, `motion-designer`, `game-designer`, `creative-director` |
| **By Skill Level** | Calibrated explanations from novice to master | `absolute-beginner`, `intermediate`, `advanced`, `expert`, `master` |
| **By Animation Type** | Specific UI motion states and patterns | `entrance-animations`, `exit-animations`, `continuous-loops`, `state-changes` |
| **By Emotional Outcome** | Crafting precise user sentiment | `joy-delight`, `calm-relaxation`, `power-confidence`, `trust-reliability` |
| **By UI Element** | Interaction design for concrete components | `buttons-ctas`, `modals-dialogs`, `forms-inputs`, `accordions-dropdowns` |
| **By Industry** | Domain-tailored motion identities | `fintech-banking`, `e-commerce-retail`, `healthcare-medical`, `saas-productivity` |
| **By Tool & Framework** | Implementation code and APIs | `css-native`, `gsap-greensock`, `framer-motion`, `rive-animations`, `anime-js` |
| **By Time Scale** | Duration calibration & pacing | `instant-0-100ms`, `micro-100-200ms`, `medium-300-500ms`, `slow-800-1200ms` |
| **By Principle Focus** | Deep-dives into individual Disney principles | `squash-stretch-mastery`, `timing-mastery`, `anticipation-mastery`, `arc-mastery` |
| **By Problem Type** | Diagnostic & troubleshooting runbooks | `performance-optimization`, `motion-sickness`, `ux-friction`, `timing-calibration` |

Full animation taxonomy and cross-references are documented in [docs/animation/index.md](docs/animation/index.md).

---

## 🚀 How to Use These Skills

### In Antigravity

This repository includes native Antigravity workspace configuration in `.agents/skills.json` and active rules in `.agents/rules/`.

1. **Open directly in Antigravity**:
   Simply open this repository directory in Antigravity. All skills across both `animation` and `design-engineering` are immediately registered on startup.

2. **Reference from another project**:
   Add this repository's domain paths to your project's `.agents/skills.json`:
   ```json
   {
     "entries": [
       { "path": "D:/skills/skills/animation" },
       { "path": "D:/skills/skills/design-engineering" }
     ]
   }
   ```

3. **Global Machine Configuration**:
   To make all skills globally available across every project on your machine, add them to `~/.gemini/config/skills.json`:
   ```json
   {
     "entries": [
       { "path": "D:/skills/skills/animation" },
       { "path": "D:/skills/skills/design-engineering" }
     ]
   }
   ```

### In Claude Code / Open Agent Systems

Skills conform to standard `SKILL.md` format. To import skills into Claude Code:
```bash
# Symlink or copy desired skills to your project
cp -r D:/skills/skills/design-engineering/<skill-name> ~/.claude/skills/
```

### Direct Agent Invocation

Instruct your agent to activate skills by name:

```text
"Use the emil-design-eng and gestures skills to build an interruptible drawer component with 1:1 finger tracking."
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

## 📄 License & Attributions

This repository is licensed under the [MIT License](LICENSE).
- **Design Engineering Collection**: Copyright (c) 2026 [Emil Kowalski](https://github.com/emilkowalski/skills)
- **Animation Principles Collection**: Copyright (c) 2024-2026 [Dylan Tarre](https://github.com/dylantarre/animation-principles)
