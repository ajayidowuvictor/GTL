# Ojuelegba and Surulere (district 1, build b47)

First district of the Lagos mainland world plan. Built and tested on its own before any other district is started.

## What is real and what is invented

Sources (text only, no photographs were available):

- Ojuelegba: a major crossing linking the Mainland to the Island, commuters from Yaba, Mushin and Surulere converge, an overhead bridge, heavy congestion, busy nightlife, near Agege Motor Road. (Wikipedia, "Ojuelegba")
- Surulere: residential streets behind the busy roads, sport and schools.

Not confirmed by those sources, so invented and labelled as a guess:

- Exact number and angle of approach roads (the game uses a clean four-way cross).
- Bus stop positions, shop names, street names (for example "Ayo Close"), and every person's name.
- The flyover is a landmark only. It is closed at both ends ("extension works") and cannot be driven.

## What is built

- 230 m of new road west of the old barricade (the mainland used to end near x = -66, it now reaches x = -268).
- A signalled four-arm junction. East-west is the main road, north-south is Ojuelegba Road. Its lights run offset from the Origin crossroad.
- Zebra crossings on all four arms, stop lines, signal poles with working lamps, a traffic warden.
- About 50 shop-and-flat blocks (2 to 3 floors), market lane stalls, roadside traders, okada and danfo, two bus stops, a quiet residential street (Ayo Close) with a church and a mosque, a school compound.
- Four places you can walk into, all with staff, customers and an exit:
  - Ojuelegba Supermarket (7 AM to 9 PM): groceries, bread and tea, water, toiletries. Cashier shift.
  - Iya Basira Buka (7 AM to 10 PM): jollof, amala, pepper soup, zobo. Waiter shift.
  - Surulere Medical Centre (8 AM to 8 PM): check-up, malaria test, ward rest. Clinic assistant shift.
  - Ojuelegba Community Secondary School (8 AM to 5 PM): study hours for fees, three certificate levels.
- Shops show a CLOSED board outside and refuse entry out of hours. If closing time arrives while you are inside you are shown out.
- 35 walkers on daily schedules (commuters at rush hours, traders in market hours, students at school breaks, quiet at night).
- Careers: waiter (no requirement), supermarket cashier (needs certificate level 1), clinic assistant (needs level 2). Every certificate level adds 4 per cent to all shift pay.
- Phone: all five places appear in the ride list. They are also valid gig and delivery spots.
- Traffic: 15 more vehicles on the new road and the cross road, all obeying the new lights.

## Tests (script names in the build pipeline)

- Signals: 300 seconds simulated, zero vehicles cross a stop line on red, all four arms flow, cars queue at red.
- Interiors: no overlap with other rooms, every person reachable, door reachable, never walking through furniture.
- Hours: each place refuses entry before opening and shows the board, accepts entry when open, closes you out at closing time.
- School and jobs: fees charged, levels at 3 / 8 / 16 study hours, careers unlock, pay bonus, saved game keeps study hours, waiter shift pays.
- Whole existing regression suite re-run on the new build.

## Measured cost

Triangles drawn at the lowest quality tier, same camera position facing west from the Origin crossroad: 105,000 before, 134,000 now. Inside the district: 68,000 to 104,000 depending on where you look. Draw calls at the junction: about 110. This is a real increase and the phone speed is unmeasured; only a real phone can say whether it stays smooth.

## Known limits

- The north and south arms end at the world edge (z = 66) with a road-works barrier.
- Only the four signalled arms carry traffic. Ayo Close and the market lane have none.
- The flyover cannot be driven.
- The minimap is compressed (550 m across a 480 pixel strip), so small shops show as blocks.
- Seated poses do not exist yet, so diners stand or walk.
- Real photographs of Ojuelegba were not used. If you send some, the shop fronts and street furniture can be corrected from them.
