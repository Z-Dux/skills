# Taste Skill (Anti-Slop Frontend Web Design)

Official documentation: [tasteskill.dev/docs](https://www.tasteskill.dev/docs)  
Upstream repository: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

**Taste Skill** (`design-taste-frontend`) is an open-source anti-slop frontend design framework for AI coding agents. It prevents models from generating generic, AI-templated landing pages with purple gradients, three-column feature cards, and cartoon icons by enforcing the design standards of top-tier company websites (such as **figma.com** and **x.ai**).

---

## 🏛️ The 9 House Rules

These rules win over everything else when designing or building landing pages:

1. **No Captions**: Never place a caption or description under any image, render, or visual. License credits go in one footer line.
2. **Every Visual Renders**: Never leave an empty ground or broken image. Test and ensure proper rendering at viewport widths 1440, 1024, 768, and 390.
3. **One Section Per Screen**: The hero section stands alone on the first screen. Every section is exactly one or two screens tall at 1440x900—no second section heading peeking in.
4. **Equal Left and Right Edges**: Maintain consistent horizontal alignment and content bounding boxes across all sections.
5. **Restrained Hover Micro-interactions**:
   - Linked cards lift 2px (`transform: translateY(-2px)`).
   - Photos zoom slightly (`scale(1.02-1.03)`) inside an `overflow: hidden` frame.
   - Buttons step on hover and press on click (`scale(0.97)`).
   - Card loops cycle in 2.5–4s.
   - Avoid generic carousels, 3D card tilts, or timed auto-switching tabs.
   - Every hero enters once on load (`data-enter`), with at most 1–2 intentional moments per page.
6. **Real Photographs & Product UI**: Use authentic, licensed photographs and genuine product screenshots instead of generic stock illustrations or AI-generated fantasy graphics.
7. **Real Full-Colour Icons**: Use authentic product icons or clean SVG diagrams (e.g., node architectures, data flow pipelines), never hand-drawn cartoonish icons.
8. **Authentic, Plain Copy**: Write in a distinct, plain voice that says what is actually sold without empty corporate buzzwords ("seamless", "revolutionize", "all-in-one").
9. **Browser Verification & Finish Gate**: Verify rendered output in a real headless browser before claiming a design task is complete.

---

## 📚 Reference Guides & System Manuals

Located in [skills/frontend-design/design-taste-frontend/references/](../../skills/frontend-design/design-taste-frontend/references):

| Reference | Scope |
|-----------|-------|
| **[system.md](../../skills/frontend-design/design-taste-frontend/references/system.md)** | Core design system principles: single typography scale, unified palette, consistent spacing |
| **[layout-v4.md](../../skills/frontend-design/design-taste-frontend/references/layout-v4.md)** | Screen-based layout rules: 1440x900 base viewport, equal margins, section heights |
| **[sections.md](../../skills/frontend-design/design-taste-frontend/references/sections.md)** | Structural layout rules for hero, features, comparison grids, and footers |
| **[sections-library.md](../../skills/frontend-design/design-taste-frontend/references/sections-library.md)** | Component library of proven, non-generic section layouts |
| **[photos.md](../../skills/frontend-design/design-taste-frontend/references/photos.md)** | Sourcing real photography, portrait/landscape ratios, and licensing attribution |
| **[icons.md](../../skills/frontend-design/design-taste-frontend/references/icons.md)** | Real product brand icons and technical SVG diagrams |
| **[cards.md](../../skills/frontend-design/design-taste-frontend/references/cards.md)** | Card container rules, internal padding, border radiuses, and border contrasts |
| **[copy.md](../../skills/frontend-design/design-taste-frontend/references/copy.md)** | Voice and tone: concrete descriptions over marketing filler |
| **[copy-voice.md](../../skills/frontend-design/design-taste-frontend/references/copy-voice.md)** | Persona definition and industry-appropriate registers |
| **[copy-tells.md](../../skills/frontend-design/design-taste-frontend/references/copy-tells.md)** | AI copy tells to eliminate ("In today's fast-paced world...", "Empower your team") |
| **[motion.md](../../skills/frontend-design/design-taste-frontend/references/motion.md)** | Motion specifications: 200–300ms easing curves, entrance physics, loop timing |
| **[moments.md](../../skills/frontend-design/design-taste-frontend/references/moments.md)** | Dealt hero moments: subtle shader or interactive moments reserved for high-impact surfaces |
| **[effects-usage.md](../../skills/frontend-design/design-taste-frontend/references/effects-usage.md)** | Strict guardrails for canvas/WebGL effects (tech, AI, and developer tools only) |
| **[perf.md](../../skills/frontend-design/design-taste-frontend/references/perf.md)** | Performance budgets: image compression, CSS transform limits, script budgets |
| **[gate.md](../../skills/frontend-design/design-taste-frontend/references/gate.md)** | Automated finish gate: Chrome DevTools Protocol inspection of the rendered page |

---

## 🛠️ Automated Scripts & Tooling

Located in [skills/frontend-design/design-taste-frontend/scripts/](../../skills/frontend-design/design-taste-frontend/scripts):

- **`gate.mjs`**: Real-browser visual gate driving headless Chrome/Edge over CDP.
- **`consistency.mjs`**: Visual consistency checker across typography, spacing, and contrast.
- **`copy-lint.mjs`**: Copy validator detecting forbidden AI marketing clichés.
- **`effects.mjs`**: Shader and canvas effect runner.
- **`photos.mjs`**: Photography downloader and resolution checker.
- **`shoot.mjs`**: Viewport screenshot capture tool at 1440, 1024, 768, and 390.

---

## 💡 How to Prompt with Taste Skill

When prompting an agent equipped with Taste Skill, provide factual business constraints rather than subjective buzzwords:

```text
"Use the design-taste-frontend skill to build the landing page for 'Acme Telemetry', an edge observability platform for Go microservices.
Pricing: $49/node/mo. Core feature: sub-millisecond trace capture. Include a live code snippet and an architectural pipeline diagram."
```
