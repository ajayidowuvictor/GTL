# Oshodi (district 2, build b48)

Second district of the Lagos mainland world plan. It sits west of Ojuelegba and was built and tested on its own before any other district is started.

## What is real and what is invented

Sources (text only, no photographs were available):

- Oshodi is the main transport hub of the Lagos mainland: Oshodi-Apapa and Agege Motor Road traffic meet here, with the interchange, the pedestrian skywalk linking the terminals, and the big Oshodi market of street trade and electronics. (Discover Lagos article on the Oshodi Transport Interchange; Oshodi area guide on nigeriahousingmarket; The Guardian on Oshodi market.)
- Nearby areas feed it: Mushin, Isolo, Agege, Ikeja.

Not confirmed by those sources, so invented and labelled as a guess:

- The exact layout (three terminals in a row, a plaza of four buildings, the shape of the market lanes). The real interchange has a different footprint.
- Terminal names, destinations on the ticket windows, shop names, and every person's name.
- The four plaza places you can enter (food court, drivers lounge and ticket hall, transit hotel, tech hub). They are modelled on the kinds of businesses a transport hub grows around; they are not copies of named businesses.
- The skywalk is a landmark only. It is on pillars behind the terminals and cannot be walked on.
- Tickets are shown but not sold. There are no other cities to travel to yet.

## What is built

- 270 m of new main road west of Ojuelegba, running to a road-works barrier at x = -540.
- A second signalled junction where Agege Motor Road crosses (x = -310). It has its own lights, stop lines, zebra crossings, signs and a warden. Its lights run the same phases as the Origin crossroad; the main road is green at Ojuelegba half a cycle later, so a car that leaves one green arrives at the next green.
- Three bus terminals in a row with long bay canopies, parked danfos, a signed skywalk behind them, and a rear apron with parked buses and cars (with lamps for night).
- About 80 shop-and-flat blocks (2 to 3 floors) on both sides of the road and on Agege Motor Road, market-lane stalls, an electronics stall row, roadside traders and okada, two bus stops.
- Four places you can walk into, each with staff, customers and an exit:
  - Oshodi Food Court (6 AM to 10 PM): four food stalls. Kitchen hand shift (no requirements).
  - Drivers Lounge and Ticket Hall (5 AM to 11 PM): ticket windows, waiting benches, a rest corner with a rest attendant. Ticket clerk shift (education level 1).
  - Interchange Transit Hotel (open day and night): 8 hour room, 3 hour day room, shower.
  - Oshodi Tech Hub (8 AM to 8 PM): desks, coffee bar, meetup, day pass. Junior developer shift (education level 2).
- Street people: Mama Ngozi (electronics stall, 7 AM to 7 PM), Alhaji Ganiyu (suya grill, 4 PM to 11 PM), a bay attendant, a traffic officer.
- Shops show a CLOSED board outside and refuse entry out of hours. If closing time arrives while you are inside you are shown out. The hotel never closes and has no board.
- About 40 walkers on daily schedules (commuters at rush hours, traders in market hours, travellers around the terminals all day, quiet at night) and walkers inside each room.
- Careers: kitchen hand ₦2,600, ticket clerk ₦4,200, junior developer ₦7,200 per shift base (same shift system and education pay bonus as the Ojuelegba jobs).
- Phone: all new places appear in the ride list. They are also valid gig and delivery spots.
- Traffic: 24 more vehicles on the new road and Agege Motor Road, all obeying both sets of lights.
- Minimap: the far west has its own strip so the new area is readable. Map labels that would sit on top of each other are skipped.

## Fixes made while building it

- The Ojuelegba flyover end blocks stood on the road itself (b47). They blocked your own car along the middle of the road. They are now lifted to deck level, so the whole main road can be driven.
- The stop-line rule for the Ojuelegba lights and the new ones now stops a car that overshoots the line by up to 1.2 m instead of letting it run the red.

## Tests (script names in the build pipeline)

- Signals: 300 seconds simulated, zero vehicles cross a stop line on red at Ojuelegba or Agege, all eight approaches flow, cars queue at red.
- Interiors: no overlap with other rooms, every person reachable, door reachable, never walking through furniture; street path to every outside person.
- Hours: each place refuses entry before opening and shows the board, accepts entry when open, closes you out at closing time; hotel open at 3 AM.
- Services, jobs and rides: food, room, meetup, market purchase, suya; the three shifts start and pay; careers unlock at the right education level; every new place is in the ride list; walkers follow the clock.
- Whole existing regression suite re-run on the new build.

## Measured cost

Triangles drawn at the lowest quality tier from the Origin crossroad facing west: 133,300 in b47, 133,700 now. Inside the new district: 40,000 to 98,000 depending on the view. Oshodi does not make the existing views heavier. Phone speed is unmeasured; only a real phone can say whether it stays smooth.

## Known limits

- Only the signalled arms carry traffic. The market lanes and the rear apron have none.
- Both arms of Agege Motor Road end at the world edge with a road-works barrier.
- The skywalk cannot be walked on.
- Tickets are not sold yet; there is nowhere else to travel to.
- Seated poses do not exist yet, so diners stand or walk.
- Real photographs of Oshodi were not used. If you send some, the shop fronts and the interchange layout can be corrected from them.
