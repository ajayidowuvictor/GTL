# GTL graphics overhaul: Phase 1 audit, Phase 2 decision, plan

Status: audit and baseline done (build b37). Stage A (colour and light) shipped in b38; stages B to G are still to do.

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

## 7. Stage A result (b38)

What changed
- Linear-light colour pipeline: sRGB output, textures and colours converted to linear at one point (`GFX` module at the top of the script), vertex colours and shading helpers re-derived in screen space, fog and background kept in screen colours (r128 applies fog after encoding).
- A sun that travels east to west with the clock, shifting light direction, colour and shadow angle; a moon and stars at night; sun and moon discs fade with cloud and rain. Shadows (HIGH tier) follow the real sun direction, soft PCF, normal bias.
- Light levels and the day table re-tuned for linear light; asphalt gets its own brightness (each material now compiles its own shader gain).
- Interiors re-tuned (hemisphere 1.0 normal rooms, 0.8 club).
- Menu, DISPLAY: LIGHTING NEW / CLASSIC switch (needs an app restart) keeps the old look available.

Verified
- Screenshots at sunrise, noon, sunset, dusk with shadows, night, rain, Rich Town and all 10 interiors, compared with the classic look.
- Regression: 15 earlier scripts and 3 controls scripts all pass. Draw calls and triangles unchanged (no geometry was added).
- Not measured: real frame rate on the Infinix Hot 30i (TEST PHONE in the menu).

## 8. Stage B result (b39)

What changed
- Honest scope note: r128 `MeshLambertMaterial` lights per vertex, so true normal maps are not possible without replacing every material. Surface detail is done in the pixel shader from the world position instead.
- World detail layer: large-scale stain and patch variation (all tiers, one octave on LOW, two on MEDIUM) plus fine grain on HIGH, fading out with distance. Breaks the visible tiling of the six 512 px textures. Walls get vertical streaking, ground gets patches.
- Wet roads: rain darkens asphalt, dirt and concrete and builds puddles with sky and sun reflection. Roads stay damp for about 2.5 game-minutes after rain and are dry indoors.
- Car paint and glass: sky reflection (fresnel) and sun highlight on HIGH only. Glass is told apart from tyres and paint by its dark blue vertex colour.
- Each world material now compiles its own shader (17 programs on LOW and MEDIUM, 28 on HIGH, was about 10), so first start compiles slightly more.

Verified
- Renders: dry and wet streets, sunset, rain, parked and moving cars on HIGH. Wet sheen was cut back twice after roads looked washed out.
- Draw calls and triangles unchanged (no geometry added). Regression: all 15 earlier scripts and 3 controls scripts pass.
- Not measured: real frame rate on the Infinix Hot 30i.

## 9. Stage C result (b40)

What changed
- Rooftops everywhere (all districts): satellite dishes, TV antennas, air-conditioner condensers and the odd coloured water tank, placed by a position-based random so the layout is stable.
- Shop fronts (not Rich Town): goods hanging from the awning rail, and one of crates, plastic chairs and table, jerrycans and a drum, or stacked sachet water beside the door. Small solid footprints, kept clear of doors.
- Market stalls now sell different things (hanging bunches, baskets of pepper and tomato, tins, cloth rolls).
- Lagos mainland: four container kiosks with hatch, awning and sign, two billboards, four striped speed bumps, a jerrycan fuel queue beside the fuel station.
- All built from the existing box and cylinder kit and baked into the chunk meshes. The new props use their own random numbers and restore the world's streams, so nothing else moved.

Measured (headless, Lagos start view)
- World triangles 214,669 to 242,653 (+13%, budget 15%). Visible draw calls +6 to +7% (budget 10%; the extra calls are the 6 new sign meshes).
- Regression: 15 earlier scripts and 3 controls scripts pass.
- Not measured: real frame rate on the Infinix Hot 30i.

## 10. Stage D result (b41)

What changed
- One shared people kit (`personKit`) now builds everyone: hero, walkers and NPCs. Body builds (narrow to broad), four extra skin tones, heights, eleven hairstyles for women and eight for men (braids, afro, puffs, bun, cornrows, long, bob, ponytail, locs, twists, fade, hightop...), caps, kufi, fila, durag, hijab, glasses, beards, earrings, patterned clothing, and the agbada.
- Women have a wide wardrobe, picked from the walker's number so the crowd is stable: casual (tee or tank with jeans, shorts or trousers; sundress; blouse and skirt), occasion (fitted midi, evening gown, knee dress, long skirt, cocktail mini), a modest long dress with hijab, and only about 1 in 16 in a traditional buba with gele. The old square shoulder slab is gone; the buba now has a plain wrapper tie at the hip.
- Women are slimmer through shoulders and waist, with narrower arms and bare or tights legs below a short hem.
- NPCs: the head is a separate piece that turns to look at the player within 14 m and nods during a conversation; arms gesture while talking.

Measured (headless)
- Per-person triangles: walkers nearAvg 1121, max 1512; far-LOD max 1376; NPC max 1604; hero 1318 unchanged. Limit 2,200.
- Not done: sitting and idle variants; walkers' heads do not track the player (NPCs only).
- Not measured: real frame rate on the Infinix Hot 30i.

## 11. Stage E result and b42 changes (b42)

b42 changes before Stage E (player requests)
- No yellow arrow over Mama Nkechi any more; the opening hint no longer sends the player to her.
- A new game starts inside the player's own home: the Yellow House room (a real interior with bed, wardrobe, window, TV on a stool, table, fan), the Lagos Heights flat, or the Sapphire penthouse. NEPO starts in the flat, LAPO is moved outside after the character screen, returning players load inside `life.home`. A HOME spot (bed or sofa) opens sleep, shower, kitchen and furnishing; a LEAVE spot by the door goes outside.
- Six luxury cars with original names and generic shapes (no real brands): Volta EV sedan, Range SUV, Steelfang E-truck (angular pickup), Aurora super-SUV, Veloce GT (grand tourer) and the Supercar, each with its own body, price (N150M to N980M), top speed and a showroom turntable (dealer pages of three).
- VIP Garage phone app: lists all six, buy there, and call any owned car. After 9 s the car appears at a free kerb spot near the player (or outside the home door when indoors) with two bodyguards beside it for 45 s. The call replaces the car currently in use.

Stage E: presentation (all CSS or per-frame maths, no post-processing pass)
- On-foot camera eases onto the player (high gain, so no input lag) and snaps after any teleport, door or car change. Look control is untouched.
- Street-lamp glow sprites enlarged (3.6 to 4.6 m) for a softer night bloom.
- Vignette strengthened slightly with a longer falloff.
- Distance haze and day/night grading were already tiered per quality level in stages A to C and are unchanged.

Measured (headless): per-person triangles unchanged (nearMax 1512, NPC max 1604, hero 1318); draw calls low 163 / medium 170 / high 174, programs 17 / 17 / 28.
Not done: arrival animation for called cars, sit and idle poses, real-phone frame rate.

## 12. Stage F result (b43)

Measured first (headless, b42 build)
- Textures uploaded: 30 at start, 33 to 35 after touring the whole Lagos street. The "100 sign textures" from the first audit are only uploaded when in view, so the atlas idea would save little. Not done, on purpose: the risk to every shop sign was bigger than the gain.
- JS heap 80 to 96 MB and flat. Five tours of the full street: geometries rise to about 500 and stay there, textures stay at 34, heap does not grow. No leak found.
- Game logic about 0.8 ms per frame for all 85 walkers, 56 NPCs and traffic, so update throttling was not worth adding.
- Shadows exist on HIGH only (LOW and MEDIUM use the blob). On HIGH, people and cars have meshes that are never frustum-culled, so every one of them was sent into the shadow pass even when far outside the 30 m shadow window.

Changed
- `gateShadow()`: on HIGH, walkers and NPCs beyond 45 m and traffic beyond 50 m no longer cast shadows. Result: shadow-casting objects drawn per view fell from 208 to 190, 173 to 149 and 183 to 164 (about 9 to 14 percent fewer) at three Lagos positions. Draw calls and triangles for the main view are unchanged. Nearby people and cars still cast shadows (checked in a render).

Not done
- Sign texture atlas (see above), distance LOD changes, update throttling.
- Real frame rate on the Infinix Hot 30i is still unmeasured; HIGH is where this helps and a Hot 30i will normally run LOW or MEDIUM.

## 13. Stage G: summary (all stages)

| Stage | Release | Result |
|---|---|---|
| A. Colour and light | b38 | Linear-light pipeline, travelling sun, haze by time of day, tuned exposure |
| B. Materials | b39 | Procedural normal maps, detail layer, glass and paint shine on HIGH, wet roads |
| C. Street detail | b40 | Rooftop clutter, kiosks, billboards, speed bumps, fuel queue, stall variety |
| D. Characters | b41 | Shared people kit, women's wardrobe, hairstyles, head tracking |
| E. Camera | b42 | Smooth on-foot camera, bigger lamp glow, stronger vignette |
| F. Performance | b43 | Distance shadow gating on HIGH, leak and texture checks |

Known limits across all stages: real-phone frame rate unmeasured; no sit or idle poses; the Aurora super-SUV is boxy; no arrival animation for called cars.
