# Computer Village, Otigba, Ikeja (district 3, build b49)

Third district of the Lagos mainland world plan. It sits west of Oshodi along the main road and was built and tested on its own before any other district is started.

## What is real and what is invented

Sources (text only, no photographs were available): BusinessDay "Inside Computer Village, Nigeria's largest phone hub", TechCabal "Computer Village in the age of social media", Discover Lagos on Otigba Computer Village, Wikipedia "Computer Village" (via search results).

Confirmed by those sources and used in the game:

- It is a big ICT market in Ikeja that began as shops on Otigba Street in the late 1990s.
- Reached from a bus stop ("Ikeja Along") on the Lagos-Abeokuta Expressway, with a local government headquarters at the entrance, a bus terminal further down, and then a stretch of shops where the cluster begins. A pathway beside the railway line leads to it.
- Cars parked on one side of the road with loudspeakers on their roofs advertising phones, watches and medicines.
- Retail shops, a wholesale core, roadside repairers working at a table under a big umbrella, mobile street sellers, and online sellers who work from the market.
- Phones, laptops and accessories (earphones, memory cards, USB cords). A 32GB memory card was quoted at N4,000 and a durable phone at about N50,000, so the game uses those prices.
- Self-taught repair technicians, parts wholesalers, very crowded streets, touts and scams.
- It is an organic, unplanned market (no formal layout) and has been under repeated relocation plans. The game shows the market as the sources describe it and does not model a move.

Not confirmed by those sources, so invented and labelled as a guess:

- The exact street layout. The game uses one main road with a crossing "Otigba Street" 9 m wide, shops on both sides and umbrella tables down each pavement.
- All shop names, building shapes and every person's name. The four plaza places are modelled on kinds of business the sources describe, not on named real shops.
- Opening hours: the sources do not state them. The game uses 8 AM to 7 PM for the wholesale plaza and repair centre, 9 AM to 8 PM for the online hub, and 7 AM to 9 PM for the canteen.
- The railway line is a landmark behind the market. There are no trains and it cannot be used.

## What is built

- 320 m of new main road west of Oshodi (x = -540 to -860), ending in a road-works barrier. The whole main road from the Origin crossroad to here is about 1,100 m and can be driven end to end.
- Otigba Street: a 9 m street crossing the main road at x = -700, with 32 umbrella tables (phone and repair) down the pavements, 16 shops of 2 to 3 floors on both sides, no traffic lights.
- At the entrance: the Ikeja Local Government Secretariat (with a corps member on duty), the Ikeja Along bus terminal with parked danfos, two bus stops.
- About 90 shop-and-flat blocks with phone and computer shop names, four larger plaza buildings, a second rank behind, roadside umbrella tables, okada, cars with roof loudspeakers.
- Four places you can walk into, each with staff, customers and an exit:
  - Otigba Wholesale Plaza (8 AM to 7 PM): six counters, display islands. Sells a phone case, earphones, a 32GB memory card, a power bank, a budget phone. Wholesale assistant shift (no requirements).
  - Otigba Repair Centre (8 AM to 7 PM): engineers' benches. Screen replacement, battery swap, software fix. Phone repair technician shift (education level 1).
  - Otigba Online Sellers Hub (9 AM to 8 PM): packing tables, parcel shelves, a photo corner. Photo shoot, live selling session. Order packer shift (no requirements).
  - Ikeja Along Canteen (7 AM to 9 PM): jollof and plantain, rice and stew, indomie and egg, drinks.
- Street people: Uche (roadside engineer, under an umbrella), Alhaji Shehu (loudspeaker car seller of watches and speakers), a corps member at the secretariat, a bay attendant, an Otigba Street guide.
- Shops show a CLOSED board outside and refuse entry out of hours. If closing time arrives while you are inside you are shown out.
- About 40 walkers on daily schedules (commuters at rush hours, buyers and traders in market hours) and walkers inside every room.
- Careers: wholesale assistant N3,400, phone repair technician N5,500, order packer N3,000 per shift base (same shift system and education pay bonus as before).
- Phone: all new places appear in the ride list. They are also valid gig and delivery spots.
- Traffic: 17 more vehicles on the long main road, all obeying the Ojuelegba and Agege lights.
- Minimap: the Computer Village stretch has its own strip, including the railway.

## Tests (script names in the build pipeline)

- Signals: 300 seconds simulated, zero vehicles cross a stop line on red at Ojuelegba or Agege on the longer road.
- Interiors: no overlap with other rooms, every person reachable, door reachable, never walking through furniture; street path to every outside person.
- Hours: each place refuses entry before opening and shows the board, accepts entry when open, closes you out at closing time.
- Services, jobs and rides: canteen, memory card price, repair, photo shoot, street purchases; the three shifts start and pay; careers unlock at the right education level; every new place is in the ride list; walkers follow the clock.
- Whole existing regression suite re-run on the new build.

## Measured cost

Triangles drawn at the lowest quality tier from the Origin crossroad facing west: 133,700 in b48, 140,000 now. Inside the new district: 38,000 to 79,000 depending on the view. Each new district adds a little to the far-distance cost of the busiest view; this is a real increase and the phone speed is unmeasured. Only a real phone can say whether it stays smooth.

## Known limits

- Only the Ojuelegba and Agege arms and the main road carry traffic. Otigba Street, the plaza fronts and the canteen yard have none.
- The railway cannot be used and there are no trains.
- Shops share the same few fronts; only the four plaza places can be entered.
- Seated poses do not exist yet, so diners stand or walk.
- Real photographs of Computer Village were not used. If you send some, the shop fronts and the street layout can be corrected from them.
