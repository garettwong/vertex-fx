# Vertex FX motion audit — 2026-07-07

Purpose: re-check X sources by **motion over time**, not thumbnails/start frames. For each source: record the actual dynamics, compare to current demo, and mark action.

## Audit method

- Used X video/image understanding for every concrete X status URL in `FX_SOURCES.md`.
- Treated profile-only links as not auditable post sources until an exact status URL is available.
- Compared the source dynamics to the local demo HTML implementation and hub/source-note copy.

## Source-by-source results

| Source | Actual video dynamics | Current demo | Verdict / action |
|---|---|---|---|
| Legacy creator/profile links `@0xca0a`, `@andersonmancini`, `@markkingsnorth`, `@playcanvas`, `@radiancefields`, `@hariswebgl`, `@0xframer` | Profile/creator references, not exact post videos. | Old generic WebGL demos. | **Not post-auditable** without exact status links. Do not claim these were video-matched. |
| `@yanliudesign` profile note / Passport | Source note lacks an exact status URL. Likely paper/passport/receipt animation: tactile stamps/doodles fly in, rotate, scale and settle with bounce. | `passport.html` is a route/boarding-pass flip pattern. | **Needs exact source status** before changing; don't guess. |
| `@GabeTognon` 2026 Framer showreel | 8s montage: Verth liquid ribbon, Nodes particle burst, Starks radial hub arcs, Aeterna dissolving particle hand, DNA helix, Avenir smoke, Aura particle wave/rainbow agents. | `aeterna-hand.html`, `starks-hub.html`, `dna-helix.html`, `aura-wave.html`. | **Match selected sub-effects.** Notes correctly say not all reel scenes were selected. |
| `@chhddavid` Shipper/BUZZ | Tool builds SaaS landing page; reusable effect is monochrome smoke/fog hero video behind headline/CTA. | `smoke-hero.html` uses live monochrome shader smoke behind SaaS hero. | **Match.** |
| `@php_martin` Wallow | Long page scroll scrubs one continuous liquid dye/bath product video forward and backward; colors evolve orange/pink/green/purple/multicolor with section timing. | `scroll-liquid-scrub.html` scroll-drives procedural ink/liquid scene, product copy and color phases. | **Acceptable concept match** without hosting/copying source video. |
| `@aurelien_gz` Marble | Living illustrated world: paddling kayaker, ripple physics, parallax hero, dark story section, feature pills/phone demo, sparkles and waving creature/easter egg. | Old `marble-ocean-play.html` was mostly cursor ripple hero. | **Weak → rebuilt** into scroll journey with paddling kayak, reactive water, parallax, feature phone and waving creature. |
| `@Website_tmplts` Clixr | Dark SaaS Webflow page; core motion is physics-like photo-card engine: grid fly-in, explosive rearrange, fanned curved layout, type reset, avatars, video/marquee, pricing, CTA. | Old `clixr-neon-saas.html` was mostly four tilt cards + static sections. | **Weak → rebuilt** into scroll-driven card engine: grid → explosion → fan → pricing → CTA. |
| `@website_tmplts` MODUS | Smooth architecture template scroll: hero parallax, about/client/project sections, dark/light transitions, animated stats, services/contact/footer. | `modus-architecture-scroll.html`. | **Match enough** for selected architecture scroll rhythm. |
| `@alexroyhe` 3Portals | Static layout with central refractive glass cube and continuously morphing colorful organic AI blob inside. | `ai-portal-glass-cube.html`. | **Match.** |
| `@zdkiel_labs` pixel effect | Image is rendered as a grid of independent animated colored squares; chaotic activation resolves into landscape with ongoing shimmer. | `pixel-mosaic-transition.html`. | **Match.** |
| `@lokidotdev` cylinder | Real-time 3D bent website surface/cylinder, rotates/unbends/distorts with reflective floor and mixed site faces. | `curved-portfolio-cylinder.html`. | **Match.** |
| `@mannatgupta146` portfolio | Horizontal gallery plus dramatic GSAP vertical strip/shutter transitions into/out of 404/minimal states. | `cinematic-strip-gallery.html`. | **Match.** |
| `@MengTo` Koisei | Long cinematic scroll: reactive petals, water ripples, pinned hero, scroll-scrubbed films, horizontal gallery, day/night dissolve, lantern embers, footer. | `river-petal-drift.html` captures procedural petals/ripples/scroll palette/chapters. | **Selected-effect match, not full-site clone.** Source note describes the selected river/petal/day-night pattern, not the entire 104s build process. |
| `@Shakib2O1` ARVIO | Continuous agency scroll with section numbers, orange highlights, staggered text, mockups, project image, testimonials, dark footer. | `agency-stepper-scroll.html`. | **Match.** |
| `@ripplix_` NewForm | Typography-integrated B&W image/data slots cycle over time; ticker appears/disappears; data → urban → data loop. | `typographic-market-collage.html`. | **Match.** |
| `@denis_uixi` Colovore | 4s photorealistic water ring/toroid loops slowly around static Edge AI Colocation hero; droplets, refraction, caustics. | `liquid-cooling-ring.html`. | **Match.** |
| `@vincemask` Taste Skill | Post meaning: anti-slop frontend framework for AI agents; video shows site/README over time, but key reusable idea is brief-read, anti-template rules and design dials controlling AI frontend taste. | Old `Taste Deck Showcase` copied surface look only. | **Wrong → rebuilt** as `anti-slop-design-switch.html` before/after comparator. |

## Fixed in this pass

1. `anti-slop-design-switch.html` added and hub now points to it.
2. `taste-deck-showcase.html` kept as a compatibility alias with corrected anti-slop content.
3. `marble-ocean-play.html` rebuilt from a static ripple toy into a scrollable living-world demo.
4. `clixr-neon-saas.html` rebuilt from static tilt cards into a scroll-driven card choreography.
5. `FX_SOURCES.md` updated for Marble, Clixr and Taste Skill so the notes describe actual video dynamics.

## Rule going forward

Do not add/fix Vertex FX from an X link until the attached video has been audited through start/middle/end motion. A thumbnail or first frame is not enough.
