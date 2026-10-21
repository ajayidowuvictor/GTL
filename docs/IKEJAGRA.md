# Ikeja GRA, Lagos mainland (district 14, build b61)

Fourteenth district of the Lagos mainland world plan, and the first one that is a branch road off the main road. A gantry on the main road reads "Oba Akinjobi Way. Ikeja GRA". Turn north there and you enter a walled estate with a spine street, three cross streets, a park, a tennis club, a Speaker's lodge and five buildings you can walk into.

## What is real and what is invented

Sources (text only, no photographs were available): The Guardian Nigeria, "Ikeja GRA: Telltale signs of a Government Rejected Area" (2022); Wikipedia "Ikeja"; an office listing for Rev Ogunbiyi Street (used only to confirm the area is a mix of homes and offices).

Confirmed by those sources and used in the game, worded as "a 2022 report says":

- A GRA is a Government Reserved Area, an estate set aside for government officials and usually linked with upscale living.
- Ikeja GRA is in Ikeja, the capital of Lagos State, about fifteen minutes by car from the State House at Alausa.
- In the 1980s and 1990s it was known for bungalows, a few duplexes and a quiet residential feel. Today it is a busy commercial zone with walled apartment blocks and tall detached buildings among the homes.
- The official residence of the Speaker of the Lagos State House of Assembly is in Ikeja GRA.
- Roads named in the report: Oba Akinjobi Way, Adekunle Fajuyi Way, Remi Fani-Kayode Avenue, Sobo Arobiodu Street, Oduduwa Way. The report calls several of them badly damaged and blames flooding on poor drainage.

Invented, and labelled as a guess in the game where a person says it:

- The street plan. In the game there is one spine street with three cross streets. Only the names Oba Akinjobi Way, Sobo Arobiodu Street and Remi Fani-Kayode Avenue are real names; where they are in this layout is a guess. Jacaranda Close is made up.
- Every house, villa, shop, chambers, clinic, chapel, bistro, park and tennis court. The Speaker's lodge, its gate and its guard are invented. The lodge has no named occupant.
- Every person: Mr Bayo, Miss Folake, Nurse Joy, Pharmacist Oduya, Mrs Eke, Mr Bello, Barr. Tunde Adeyemi, Miss Ife, Mr Emeka, Mrs Adebisi, Mallam Idris, Coach Segun, the estate guard and the lodge guard.
- All prices, opening hours, pay rates and the effects of food, treatment and rest.
- Puddles on the streets: a nod to the flooding in the report, not a map of real flood spots.

## What is built

- The first branch road. The world used to be a strip 132 m wide (z from -66 to +66). The strip is still the same everywhere, except for a window between x = -1285 and x = -1065 where the playable area now reaches 314 m north. The old red-and-white barrier at the end of the strip there is gone.
- The estate: boundary wall with a gate on the main road, a spine street and three cross streets with pavements, zebra crossings, lamps, verge trees, street signs and junction boards, and walled lots (cheap villas, grand houses, and open-front public lots).
- Five places you can walk into, each with staff, customers, an exit doorman and a closed board outside:
  - The Bistro (11 AM to 11 PM): bar with drinks (chapman, zobo and others), a kitchen (jollof and chicken, grilled fish and others), a free live band for one hour, and facts about the GRA.
  - GRA Family Clinic (8 AM to 8 PM): reception with dressing and rest (800) or full treatment (3,500) which heals you, and a pharmacy hatch (water, glucose drink and other basics).
  - Superstore (8 AM to 9 PM): a till (bread, noodles and other groceries) and a bakery counter (meat pie, doughnut, cold drink).
  - Law chambers (8 AM to 5 PM): a lawyer whose legal retainer (12,000) clears your police heat, plus facts, and a secretary with tea and biscuits.
  - Chapel (6 AM to 8 PM): a verger, free "sit and rest" for half an hour, and refreshments from the choir.
- Outside: a gate guard, the Speaker's lodge guard, a suya stand (4 PM to midnight), the tennis club (a set is 3,000, daylight only) and a coach.
- Careers: bistro waitress 4,600, clinic receptionist 5,400 (needs Education Level 1), superstore cashier 4,000, chambers clerk 6,200 (needs Education Level 2), chapel assistant 3,200.
- Phone: nine new places in the GoRide list and ten new taxi stops.
- Walkers: 25 people on the streets, in the park and in the rooms, on daily schedules.
- Minimap: the strip map is swapped for an estate map (roads, park, tennis club, estate outline, buildings, labels) while you are in the estate.
- Traffic and police: cars, police and pedestrians respect the new limits.

## Tests (script names in the build pipeline)

- test61a: the limit function (-314 inside the window, -66 outside), free-spot, player and car clamps, a 0.5 m flood fill from the main road showing the streets are reached and no walkable cell leaks past the estate walls, every door person, the guards, the suya stand and the coach reachable on foot, every new taxi stop reachable, tap-to-move paths, the police flow field leading a chaser up the spine, the flow grid open on the new roads and shut outside the window, the minimap swap, for each of the five buildings the open and closed dialogs, walking in and the exit onto a free spot, every person's body, items and career valid, clinic healing, lawyer retainer, tennis hours, a till shift, and walkers standing on free ground.
- test61b: all nine new places appear in GoRide, each has a free spot beside the person, real rides to three of them land the player on free ground next to the person, and a ride out of the estate is allowed.
- The whole earlier regression (district tests from Makoko to Contracts, plus the b60 suites) re-run on the new build.

## Known limits

- The estate is a slice about 220 m wide and 250 m deep, not the real Ikeja GRA, which is much bigger.
- Only the five buildings, the suya stand, tennis club and lodge gate have people. The villas are walled lots you cannot enter.
- Only the main road carries traffic. The estate streets are for walking and driving yourself.
- Seated poses do not exist yet, so people in the bistro, chapel and chambers stand or walk.
- The older tests that checked "the west end of the road is shut" or the old Makoko gate are obsolete and were updated or ignored (they check things that were deliberately changed in earlier builds).
- Real photographs of Ikeja GRA were not used. If you send some, the fronts and the layout can be corrected from them.
