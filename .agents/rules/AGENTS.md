# Disney Animation Principles Guide

When designing or implementing animations, transitions, micro-interactions, or motion design, apply Disney's 12 Principles of Animation:

| Principle | Key Application | Web & UI Implementation |
|---|---|---|
| **Squash & Stretch** | Show impact, flexibility, and mass | `transform: scale()` on active/tap/press states while preserving volume |
| **Anticipation** | Prepare viewer for upcoming action | Subtle reverse wind-up/shrink (2-3%) before expansion or movement |
| **Staging** | Direct user attention clearly | Motion hierarchy, backdrops, focused element animates first |
| **Straight Ahead / Pose to Pose** | Choose dynamic physics vs planned keyframes | GSAP / physics springs vs structured CSS `@keyframes` |
| **Follow Through / Overlapping** | Parts move at different rates; momentum continues | Staggered child reveals (`0.05-0.1s`), overshoot on stops |
| **Slow In / Slow Out** | Natural acceleration and deceleration | Always use easing (`cubic-bezier`, `ease-in-out`), never linear for UI |
| **Arc** | Natural curved motion paths | Curved trajectories, combined transforms, bezier curves |
| **Secondary Action** | Supporting movements reinforcing primary action | Dynamic shadows, icon rotation, badge pop during primary card move |
| **Timing** | Duration conveys weight, scale, and emotion | Micro-interactions: 100-200ms; transitions: 200-400ms; page: 300-500ms |
| **Exaggeration** | Push beyond reality for clarity and punch | Intentional scale (e.g. 1.05-1.12), spring bounce, energetic overshoot |
| **Solid Drawing** | Consistent volume and 3D space | Consistent `transform-origin`, 3D perspective, no visual z-fighting |
| **Appeal** | Charisma, elegance, and tactile delight | 60/120fps smoothness, purposeful choreography, polished aesthetic |

Always respect accessibility settings: disable or reduce motion when `prefers-reduced-motion: reduce` is detected.
