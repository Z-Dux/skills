# House Rules: Taste Skill (Anti-Slop Frontend)

When designing, building, or polishing company, product, or landing pages, enforce these house rules (derived from [tasteskill.dev](https://www.tasteskill.dev/docs)):

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
