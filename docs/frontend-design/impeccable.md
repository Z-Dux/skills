# Impeccable: The Design Vocabulary for Coding Agents

Official documentation: [impeccable.style/docs](https://impeccable.style/docs)  
Upstream repository: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

**Impeccable** (`impeccable`) provides a structured design vocabulary, heuristic critique engine, deterministic slop detector, and polishing playbooks for AI coding agents.

Instead of vague instructions like "make it look modern" or "make it pop", Impeccable gives the agent 24 specialized action verbs and 4 surface modes.

---

## 🧭 The 4 Surface Modes

Impeccable scales its design ambition based on the nature of the surface:

1. **Persuade**: Landing pages, marketing sites, campaigns, and pricing. High ambition, bold typography, memorable moments, and custom art direction.
2. **Operate**: Task completion surfaces—dashboards, web apps, editors, settings, and tables. Precision, high scanability, native affordances, and UI restraint outrank decoration.
3. **Read**: Documentation, changelogs, knowledge bases, and articles. Optimized for reading ergonomics: 65–75ch measures, balanced hierarchy, and clean typography.
4. **Experience**: Portfolios, showcases, and digital exhibits. The interface recedes; the featured artifact or medium leads from the first viewport.

---

## ⚡ The 24 Command Verbs

Located in [skills/frontend-design/impeccable/reference/](../../skills/frontend-design/impeccable/reference):

### 1. Steer
- **`bolder`**: Amplifies safe, bland designs into distinct visual statements with strong hierarchy.
- **`quieter`**: Tones down over-decorated, visually noisy interfaces to restore calm and focus.
- **`distill`**: Removes redundant elements, nested cards, and unnecessary visual chrome.
- **`colorize`**: Injects intentional, harmonious palettes into washed-out gray UIs.
- **`typeset`**: Calibrates typography scales, line measures (65–75ch), and tracking (-0.02em to -0.04em).
- **`layout`**: Fixes spacing rhythm, grid alignment, and visual balance.
- **`animate`**: Adds intentional state transitions, micro-interactions, and motion feedback.
- **`delight`**: Introduces authored personality and tactile delight where appropriate.
- **`overdrive`**: Pushes into high-end shaders, spring physics, and scroll-driven canvas effects.

### 2. Review & Audit
- **`critique`**: UX design review with heuristic scoring across usability, clarity, and aesthetics.
- **`audit`**: Comprehensive technical audit ranking findings from P0 (blocking) to P3 (polish).

### 3. Finish & Harden
- **`polish`**: Final high-craft pass before shipping (micro-spacing, borders, shadows, alignment).
- **`harden`**: Handles edge cases: long text overflow, empty states, error boundaries, and i18n.
- **`clarify`**: Rewrites confusing UX copy, tooltips, and labels in the product's authentic voice.
- **`adapt`**: Optimizes responsive behavior across desktop, tablet, and mobile breakpoints.
- **`optimize`**: Diagnoses and eliminates rendering bottlenecks and DOM bloat.
- **`onboard`**: Designs first-run experiences and helpful empty states.

### 4. Iterate & Set Up
- **`live`**: In-browser overlay for live variant picking and hot-swapping.
- **`generate`**: Produces multiple design variations for a named UI component.
- **`shape`**: Plans UX architecture and information flow before touching code.
- **`init`**: Captures foundational product context into `PRODUCT.md`.
- **`document`**: Extracts visual design system tokens into `DESIGN.md`.
- **`extract`**: Promotes recurring components into the shared design system.

---

## 🛡️ The Craft Floor & Anti-Slop Rules

Located in [rules/impeccable-craft.md](../../rules/impeccable-craft.md):
- **Banned defaults**: Nested cards within cards, eyebrows/kickers above headings, generic `01/02/03` numbered sections, gradient text, zero-offset halo glows, and generic emoji as icons.
- **Browser surfaces**: Custom styling for text selection, caret, scrollbars, and tabular figures.
- **Contrast**: Body text ≥4.5:1, large text ≥3:1. Tint secondary text from the background hue, never plain muddy gray.
