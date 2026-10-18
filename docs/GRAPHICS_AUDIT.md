# GTL graphics overhaul: Phase 1 audit, Phase 2 decision, plan

Status: audit and baseline done (build b37). No rendering code has been changed yet.

## 1. What the game is built with

| Item | Finding |
|---|---|
| Engine | three.js r128 (`vendor/three.min.js`, also `three: 0.128.0` in `package.json`). Not Babylon, not Unity. |
| Structure | One file, `www/index.html` (1.28 MB). 769 KB of it is 8 embedded base64 textures. No bundler, no TypeScript, no GLB/GLTF assets, no external models. |
| App | Capacitor 6 wraps `www/` into an APK. GitHub Actions builds it on every push to `main`. The workflow copies a local three.js so the game works offline. |
| World | Built from code. Boxes, cylinders and spheres are baked into merged meshes, one per surface type per 80 m chunk (235 world meshes, about 215k triangles in total). Only about 80 to 165 draw calls are visible at once. |
| Characters | Procedural smooth low-poly figures (hero about 1,300 triangles, walkers about 1,800, a car about 1,200). Animated by code (leg and arm swing, lean, idle breathing). 85 walkers, 56 NPCs, 47 traffic vehicles. |
| Lighting | One `HemisphereLight` (0.72) and one `DirectionalLight` (0.62). ACES tone mapping, exposure 1.18. Linear fog 30 to 100 m in a warm haze colour. |
| Materials | 1,014 `MeshLambertMaterial` (vertex colours and a texture) and 458 `MeshBasicMaterial` (sky, signs, glows). No PBR, no roughness, no normal maps. |
| Sky and time | Sky is a vertex-coloured dome plus soft cloud blobs. Time of day only changes colours and light intensity. The sun never moves across the sky: its direction is fixed, and it only follows the player when shadows are on. |
| Shadows | Real shadows exist only on the HIGH tier (one 1024 px PCF map covering 60 m). LOW and MEDIUM use a round dark blob under each character. |
| Quality tiers | LOW 0.85x resolution, MEDIUM 1.25x, HIGH 2x (capped by the phone's pixel ratio). A TEST PHONE button in the menu picks the best tier. On a touch phone the game starts on LOW; the player can change it in the menu. |
| Post-processing | None. A CSS vignette overlay only. |
| UI | HTML and CSS over the canvas (cash, clock, phone, menu, joystick, RUN). Barlow Condensed from Google Fonts with system fallbacks. Separate from the 3D, so a rendering change cannot break touch controls. |
| Movement and camera | Rewritten in b37 (smooth movement, zoom, camera collision, tap-to-move). |

## 2. Why it looks basic (cause, not guess)

1. **No colour management.** `renderer.outputEncoding` is the r128 default (linear, no sRGB). All colours and textures are authored as display colours but lit as if linear, so shading is flat and mid-tones are muddy or washed.
2. **Lambert only.** No specular, so glass, car paint, wet roads and metal all look matte.
3. **One fixed light angle.** The sun never changes direction, so the lighting does not change over the day. Only the tint does.
4. **Flat surfaces.** Walls and roads use six 512 px tiling textures with no normal or detail maps, so large surfaces repeat visibly.
5. **Low and Medium have no shadows.** That is what a mid-range phone shows by default. Buildings and people look pasted onto the ground.
6. **Boxy kit.** Facades are boxes plus decals. There are no AC units, satellite dishes, kiosks, gutters, rooftop clutter or fuel queues. The street lacks the small Lagos detail that tells a story.
7. **Characters are one body type.** Same mesh proportions and few hair, clothing and headwear variants.

## 3. Baseline measurements (headless Chromium, software GL)

Software GL cannot give a true frame rate, so frame cost is recorded as draw calls, triangles and memory, which are the same on a phone.

| Item | Result |
|---|---|
| Page load to playable | about 1.9 s to load, 4.5 s until the 3D world responds |
| JS heap after start | 73 MB |
| GPU objects | 146 geometries, 26 textures uploaded at start (over 100 distinct textures once all canvas-drawn signs exist), 10 shader programs |
| Scene | 2,305 objects, 1,472 meshes, 852 shadow casters (747 of them dynamic: people, cars, props) |
| Draw calls per view (Low / Medium / High) | Lagos street 165 / 163 / 166, Abuja 105 / 122 / 131, Port Harcourt 80 / 96 / 117, Rich Town 93 / 114 / 122, Aso Rock 85 / 94 / 104 |
| Triangles per view (Low / Medium / High) | Lagos 89k / 94k / 99k, Abuja 73k / 95k / 117k, Port Harcourt 56k / 66k / 77k, Rich Town 72k / 86k / 104k |
| Game logic per frame | about 0.7 to 1.5 ms |
| Textures | 8 embedded (6 tiling 512x512 JPEG, decals 1024x1024, foliage 512x256), plus about 100 small canvas-drawn sign textures |

Screenshots for morning, noon, dusk and night in Lagos, plus Abuja, Port Harcourt, Rich Town and Aso Rock, were captured as the visual baseline (kept outside the repo).

Not measurable here: real frame rate on an Infinix Hot 30i. After each stage the menu TEST PHONE result on the phone is the number that counts.

## 4. What must not break

Movement, camera and tap-to-move (b37), NPC dialogue, hubs and interiors, jobs, economy and wallet, phone apps, quality tiers and TEST PHONE, saves, the fade sequences, HUD and touch controls, the offline APK build, and the 14-script regression suite (plus the b37 controls tests).

## 5. Decision: stay on three.js r128

| Option | Verdict |
|---|---|
| Stay on three.js r128 | Chosen. All 7 causes above are fixable inside it. Zero migration cost, the proven APK pipeline stays. |
| Upgrade three.js to a newer release | Not now. It brings built-in colour management and newer shadow filters, but changes lighting units, colour handling and shader chunks across 1.28 MB of code. High risk, modest gain. Revisit only if a stage proves it is needed. |
| Babylon.js | Rejected. Would mean rewriting the whole game for no visual gain we cannot get in three.js. Two engines would also double memory on a phone. |
| Unity or Unreal | Rejected. Not a browser or Capacitor project, and your PC cannot host those toolchains. |
| Imported GLB models | Possible later with the matching r128 `GLTFLoader` (not in the minified build, so it has to be vendored). Not planned for characters: the procedural kit gives consistent style, tiny download and full control of Nigerian clothing and hair. I will not promise photorealistic people. |

## 6. Plan (small, tested stages; each ends with screenshots, regression and a release)

| Stage | Work | Cost and risk | Exit check |
|---|---|---|---|
| A. Colour and light | sRGB output plus linear colour conversion at the single place colours enter the meshes, re-tuned light levels, a sun that actually travels across the sky with time of day (direction, colour, long dusk shadows, moon at night), exponential distance haze tinted by time, tuned ACES exposure | Medium risk (touches the whole look), almost no performance cost | Before and after screenshots at 4 times of day, every regression script green |
| B. Materials | Procedural normal maps for asphalt, plaster and concrete, a cheap world-space detail layer to break repetition, glass and car paint with specular on HIGH only, wet-road sheen in rain | Small download (about 150 KB), HIGH tier cost only | Draw calls unchanged, no more than 10% more triangles |
| C. Lagos street detail | Modular props added to the existing building kit: AC units, satellite dishes, water tanks, balconies with grilles, kiosks and containers, fuel queue and generators, gutters and drain covers, road patches, speed bumps, posters and billboards, more varied market stalls | Merged into existing chunk meshes, so draw calls stay flat | Draw calls within 10% of baseline, triangles within 15% |
| D. Characters | More body proportions, hairstyles (low cut, afro, braids, durag), headwraps and caps, agbada, ankara and jersey patterns, wider skin tones, head that looks toward the player, talking gestures, sit and idle variants | Triangle budget per walker stays under 2,200 | Existing NPC, escort, baddie, club and mall scripts green |
| E. Camera and presentation | Small camera follow smoothing with no input lag, depth cues (stronger distance haze, subtle bloom-like glow on lights baked into the lamp sprites), vignette and grade built into the materials instead of a full-screen pass | No post-processing pass on LOW or MEDIUM | No visible input lag in the b37 tests |
| F. Performance | Merge sign textures into atlases (about 100 textures to a handful), only cast shadows from objects inside the shadow window, distance LOD and update throttling for far walkers, shadows for the nearest cars and people on MEDIUM using the cheap blob plus one soft fake, memory checks for leaks | Reduces cost; the other stages add some | Draw calls, triangles, textures and heap at or below baseline |
| G. Docs | Change list, measured results, limits | Low | This file updated |

Risks and mitigations
- The colour change in stage A touches every material. Mitigation: one conversion point, compare before and after on 12 fixed views, keep a switch to the old look until the new one is signed off.
- Mid-range Android WebView limits. Mitigation: effects on HIGH only, no post-processing pass below HIGH, stage-by-stage TEST PHONE results.
- Asset licensing: no external art is used by this plan. If any is added later, the source and licence are recorded in this folder.

Outstanding questions for the owner
- The only real-device measurement is the TEST PHONE result on the Infinix Hot 30i. That should be recorded once now, before stage A, and again after each stage.
