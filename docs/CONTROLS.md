# GTL controls: movement, camera and tap-to-move (b37)

GTL is a three.js game in one file (`www/index.html`), packaged for Android with Capacitor.
There is no Unity, no Rigidbody, no CharacterController and no NavMesh in this project. The
existing hand-written controller was extended in place, so there is still exactly one
movement system.

## What was already there (kept)

| Area | Existing behaviour | Status |
|---|---|---|
| Input | Virtual stick (touch, left pad), WASD / arrows, Shift to run, RUN button, mouse drag or right-pad drag to look, Q / E to turn the camera, F to enter or exit a car, T for the phone, Esc / P for the menu | Unchanged |
| Physics | Circle (radius `PR` = 0.38 m) against axis-aligned boxes (`solids[]`), push-out resolution, car and traffic push | Unchanged, now sub-stepped |
| Animation | Procedural walk / run swing, idle breathing, lean into turns | Kept, driven by the speed actually moved |
| Camera | Orbit camera, simple wall check, fixed distance | Replaced by the camera below |
| Look sensitivity | Menu button with 3 levels | Now 5 levels, old setting is migrated |

## New behaviour

**Movement**
- Smooth acceleration and braking (walk 3.4 m/s, run 6.4 m/s). Full walking speed takes about 0.3 s, a stop takes about 0.4 s.
- The heading turns at a limited rate (11 rad/s when slow, slower when running), so direction changes are curved, not instant.
- A reversal (for example W then S) brakes first, pivots, then accelerates the other way.
- The character always faces the direction it is travelling. When turning on the spot the legs shuffle.
- Collision is sub-stepped (at most 0.18 m per step), so a thin wall cannot be tunnelled even at 20 FPS.
- The walk animation follows the speed the character really moved, so pushing into a wall does not run on the spot.

**Camera**
- Mouse wheel, keyboard and two-finger pinch zoom. Zoom is remembered between sessions.
- The camera is stopped by walls and furniture. It pulls in at once and eases back out.
- In tight spots it also tilts upward to keep the character in view, never goes below the floor or above a room's ceiling, and hides the character if the lens would sit inside his head.
- Optional auto camera that swings behind the character while walking.

**Tap / click to move**
- Click (mouse) or tap (right half of a touchscreen) the ground. A yellow ring marks the destination.
- Walks around obstacles using a 0.25 m grid path finder, with the wall clearance of the player's body. Gaps of 1 m or wider are used.
- Click a person to walk up to them and start talking. Click the doorman to walk to a building and go in.
- Any keyboard or stick input cancels it. If the character gets stuck it re-plans once, then stops.
- Long routes (more than 28 m) run, then walk the last 7 m.

**Buildings**
- Inside a building, walk into the green EXIT door to leave. Talking to the doorman still works as before.
- Cameras indoors are limited by the room ceiling and walls, and the zoom range is tighter indoors.

## Input bindings

| Input | Action |
|---|---|
| W A S D / arrow keys | Move (relative to the camera) |
| Shift (or RUN button) | Run |
| Left touch pad | Virtual stick |
| Mouse drag (left or right button) / right touch pad drag | Rotate camera and tilt |
| Q / E | Rotate camera left / right |
| Mouse wheel | Zoom |
| `+` / `=` (or numpad +) | Zoom in |
| `-` (or numpad -) | Zoom out |
| `0` (or numpad 0) | Reset zoom |
| Two-finger pinch on the right pad | Zoom |
| Click / tap the ground (no drag) | Walk there (when TAP MOVE is ON) |
| Click / tap a person | Walk there and talk |
| Walk into the EXIT door indoors | Leave the building |
| F | Enter or exit a car (unchanged) |
| T | Phone (unchanged) |
| Esc or P | Menu (unchanged) |

Menu, SETTINGS, CONTROLS section:

| Button | Choices | Saved as |
|---|---|---|
| LOOK | VERY SLOW, SLOW, NORMAL, FAST, VERY FAST (0.5, 0.7, 1, 1.5, 2.2 times) | `gtl_look2` |
| MOVE | 80%, 100%, 125% of walk and run speed | `gtl_ctrl` |
| TAP MOVE | ON / OFF (default ON on a computer, OFF on a touch phone) | `gtl_ctrl` |
| INVERT Y | OFF / ON | `gtl_ctrl` |
| AUTO CAMERA | OFF / ON | `gtl_ctrl` |

Advanced values live in the `CTRL` object near the top of the controls block:
`accel` (16 m/s²), `decel` (22 m/s²), `turn` (11 rad/s), `walk` (3.4), `run` (6.4), `zoomSens` (1).

## Dependencies

- three.js r128 (`vendor/three.min.js`, already used). New use: `THREE.Raycaster`, `THREE.Plane`, `THREE.RingGeometry`.
- Browser APIs: Pointer Events, `wheel` events, `localStorage` (all optional, wrapped in try/catch).
- No new files at runtime, no new libraries, no network.

## Modified files

| File | Change |
|---|---|
| `www/index.html` | Controls block (`CTRL`, zoom, spatial index, camera collision, path finder, tap-to-move, door exit); input handlers (look, pinch, click); `update()` movement and animation speed; `updateCamera()`; menu buttons; room records now store ceiling height and door x; version string b37 |
| `docs/CONTROLS.md` | This file |

## Tests (all passing for b37)

Automated in headless Chromium against the real game page, advancing the game with fixed 1/60 s steps so results do not depend on how fast the test machine renders.

| Test | Result |
|---|---|
| Flat ground: walk reaches 90% speed in 0.28 s, run reaches 6.4 m/s, stop in under 0.5 s | pass |
| Turning 90 degrees at walking speed: heading step under 0.15 rad per frame, speed stays above 2.6 m/s | pass |
| Reversal: brakes below 0.9 m/s, then goes back to 3.4 m/s without a heading jump | pass |
| Six zig-zags, then stop: finite position, speed exactly 0 | pass |
| Facing follows the heading from standstill | pass |
| 0.3 m wall at 20 FPS (run): no tunnelling | pass |
| Pushing head-on into a wall: animation speed 0.15 (no running on the spot) | pass |
| Sliding along a wall at a shallow angle | pass |
| 1.0 m and 0.8 m doorways by keyboard, straight and at an angle | pass |
| Path finder through a 1.0 m doorway, unreachable goal, cancel by keyboard | pass |
| All 10 interiors: every person reachable by tap-to-move, minimum clearance to furniture 0.38 m (equal to the body radius, never inside), exit door reachable | pass |
| Camera sweep: 113 positions (every room including corners and the door, 60 spots beside tall outdoor walls) x 24 yaws x 3 pitches x 3 zooms = 24,408 views: camera never inside a solid, never below floor, never above ceiling | pass |
| Camera squeezed against a wall: pulls in, tilts up, recovers in the open, character shown again | pass |
| Wheel, `+`, `-`, `0`, pinch (real touch events), clamps and persistence | pass |
| Mouse drag, five sensitivities (0.5x, 1x, 2.2x measured), invert Y | pass |
| Real mouse click sets a destination; TAP MOVE OFF ignores it; drag is not a click | pass |
| Click a person: walks up and the conversation opens | pass |
| Walking into the EXIT door leaves the building | pass |
| Auto camera swings behind within 0.25 rad | pass |
| Menu buttons cycle and persist; 125% move speed gives 4.25 m/s | pass |
| Regression: the full earlier suite (phone, ambitions, menus, fares, gigs, cops, vehicles, Rich Town, interiors, convoy, club, mall, showroom) | pass |

Known limits
- Collision is circle against box only. Slopes, stairs and moving platforms do not exist in this world.
- Path finding sees buildings and furniture, not cars or people, so a parked car in the way is handled by the normal push-out.
- Tap-to-move works only on the ground plane. Clicking a wall or the sky is ignored.
- Walking through an outdoor shop door is still done through the doorman, because outdoor buildings are solid boxes.

## Icon controls (b62)

Every on-screen button is now a round or rounded-square icon button, in the style of GTA San Andreas. There is no visible text on any of them. The old text is kept as a visually hidden label and as the button's `aria-label`, so screen readers and the tests still find it.

| Button | Icon | Notes |
|---|---|---|
| Run (hold) | runner | yellow, bottom right |
| Gas (hold, in a car) | up arrow over a pedal | green |
| Brake and reverse (hold, in a car) | stop sign with a bar | red |
| Horn (hold, in a car) | speaker with sound waves | yellow |
| Fire (hold, in a fight) | crosshair | red |
| Change weapon | two arrows | small, above Fire |
| Menu | three bars | top right |
| Phone | phone | top right, left of Menu, keeps the unread badge |
| Clock | time text | the only text left, because the time is data |

The big round action button changes its icon by what is near you:

| Action | Icon | Colour |
|---|---|---|
| Talk | speech bubble | cream |
| Enter (a car) | steering wheel | cream |
| Exit (the car) | door with an arrow | cream |
| Take the car | key | red |
| Lift wallet | wallet | red |
| Demand payment | banknote | red |

Red means the action is a crime. The first two times each action appears, a short toast says what the icon means. The count is kept in the browser (`gtl_acthint`). The intro screen shows the same icons next to each control.

Tests (`test62a`): every button has an icon, a hidden label and an aria-label; no button shows visible text; every action state has the right icon and the red crime colour; the icons are all different; no two buttons overlap, every touch button is at least 44 px and inside the screen, on foot, in a fight and in a car, at 900x450, 800x360, 640x360 and 360x640; real pointer presses still hold gas, brake, horn and run, and the exit, phone and menu icons still work.
