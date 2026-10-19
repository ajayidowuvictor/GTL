# Ikeja, Lagos mainland (district 5, build b51)

Fifth district of the Lagos mainland world plan. The main road now continues west past Computer Village into a stretch of Ikeja: a busy Allen Avenue crossing, a leafy Government Reserved Area (GRA) street, a golf club lawn and a shopping mall. It was built and tested on its own before any other district is started.

## What is real and what is invented

Sources (text only, no photographs were available): the Ikeja Record article "Allen Avenue: inside Lagos's most famous street" (partly paywalled, so only the opening was read), the Estate Intel article on residential real estate in Ikeja GRA, and Wikipedia "Ikeja City Mall".

Confirmed by those sources and used in the game:

- Allen Avenue is famous for its nightlife and is a business district with offices. It is described as active around the clock. Hawkers and vehicles crowd Allen junction by day, and traffic is heavy. It links to Toyin Street, Opebi, Adeniyi Jones and Alausa (the seat of government).
- Ikeja GRA is a high-income neighbourhood in Ikeja, first reserved for top government officials and now mixed-use, with homes, offices, restaurants, lounges, supermarkets and hotels. The article names the Marriott, Sheraton and Radisson Blu hotels, the Ikeja High Court and a golf club. Several company head offices are there. It is close to the Murtala Muhammed airports.
- Ikeja City Mall is in Alausa. It opened on 14 December 2011 with about 23,000 square metres over two floors and more than 90 stores, with a Shoprite supermarket and a five-screen Silverbird cinema as anchors.

Not confirmed by those sources, so invented and labelled as a guess:

- The layout. Real Allen Avenue is a long street with a roundabout. The game has a simplified signalled crossing, "Allen Junction", with a short Allen Avenue running north and south. The real GRA street grid, the real golf club's location and the real mall's position are not reproduced. The GRA street, the villas, the golf lawn and the mall's position on the road are all invented.
- Every shop, bank, hotel and restaurant name. "Allen Avenue Bank" is a made-up bank, not a real one. The real hotel and supermarket brands the sources mention are not used.
- Opening hours (bank 8 AM to 4 PM, supermarket 8 AM to 9 PM, night lounge 8 PM to 5 AM, hotel all day and night, GRA restaurant 11 AM to 11 PM, mall 9 AM to 10 PM), all prices, the 6 percent fixed deal and every person's name. The mall's cinema, boutique and food court are inspired by the real mall but are not its real tenants.
- The nightlife is shown only as a lounge with a bar, a DJ booth and a dance floor. The Ikeja Record article also describes sex work on the street. The game does not show it.

## What is built

- About 470 m of new main road west of Computer Village, ending at a road-works barrier. The old end barrier at the edge of Computer Village is gone.
- Allen Junction: a signalled crossing with zebra crossings, its own traffic lights (the same phases as the Origin crossroad), and Allen Avenue running 65 m north and 65 m south with shop frontages, a gantry sign over the northern arm and traffic in both directions.
- Allen Avenue frontage: a supermarket, a hotel, a bank and a night lounge, all enterable, and a long row of named shops, restaurants and boutiques on the south arm.
- GRA street: a tree-lined road with five walled compounds, villas, lawns and a gate hut with a security man. Three more walled villas stand on the main road beyond it.
- A golf club lawn with a fairway, bunkers, a pond, flags, a clubhouse and a fenced, gated front with a marshal who explains it.
- Ikeja City Mall: a long two-floor building with a pavement canopy, and a car park behind it.
- Six places you can walk into, each with staff, customers, an exit doorman and a closed board outside:
  - Allen Avenue Bank (8 AM to 4 PM): teller counter, cash machines, queue seats. Invest 20,000 or 100,000, withdraw, or lock 20,000 or 50,000 for 6 days at 6 percent. This uses the same invested and fixed-savings money as the NairaPay phone app.
  - Allen Supermarket (8 AM to 9 PM): aisles of shelves, fridges, checkouts. Bread, noodles, milk and cereal, water, snacks, toiletries.
  - Allen Night Lounge (8 PM to 5 AM): bar, DJ booth, dance floor, booths. Drinks, pepper soup, the dance floor for two hours, a VIP table. The bartender talks about Allen Avenue's nightlife.
  - Allen Avenue Hotel (all day and night): lobby, reception, buffet. Room for 8 hours, day room, shower, breakfast buffet.
  - GRA Garden Restaurant (11 AM to 11 PM): round tables with cloths, a garden corner. Jollof and chicken, grilled fish, egusi, pepper soup, a candlelit dinner. The head waiter tells how the GRA began.
  - Ikeja City Mall (9 AM to 10 PM): an atrium with a fountain, a cinema ticket counter, a fashion boutique and a food court. Movie tickets (two hours), shirts, shoes, perfume, shawarma, pizza, smoothies.
- Street people: an Allen hawker (6 AM to 11 PM), Mallam Suya (5 PM to 4 AM), the GRA gate security man and the golf club marshal.
- About 20 walkers on the streets and 21 inside the rooms, all on daily schedules. Allen Avenue stays busy at night.
- Careers: bank teller 5,200 (needs Education Level 1), lounge bartender 4,400, garden restaurant waiter 4,200, hotel receptionist 4,000, supermarket stock clerk 3,500, cinema usher 3,200 per shift base (same shift system and education pay bonus as before).
- Phone: every new place and street person is in the ride list and the gig spots.
- Traffic: both main-road lanes now run the full length to the new end. Lane 0's old vehicles were shifted so they keep their places in the older districts.
- Minimap: a seventh strip for Ikeja with the junction, Allen Avenue, the GRA street, the golf lawn and the mall.
- World size: the playable width grew from 2,780 m to 3,360 m. Rooms for the new interiors sit in two new columns past the Mushin rooms.

## Tests (script names in the build pipeline)

- Interiors: no overlap with other rooms, every person reachable, door reachable, never walking through furniture; street paths to every outside person from the main road; paths along the whole new road, up and down Allen Avenue and up the GRA street.
- Hours: each place refuses entry before opening and shows the board, accepts entry when open, closes you out at closing time (including across midnight for the lounge). The hotel is open at every hour.
- Services: bread, toiletries, dance floor, hotel room, jollof, movie ticket, shirt, shawarma, hawker water, suya, the bank's invest, withdraw and lock, chat lines. Every price, need change and time cost is checked. A buyer without cash is refused and nothing moves.
- Jobs and rides: the six shifts start and pay; the teller job is refused below Education Level 1; every new place is in the ride list; walkers follow the clock.
- Signals: 300 seconds simulated, zero vehicles cross a stop line on red at Ojuelegba, Agege or Allen, and cars queue and flow at all twelve approaches.
- Walker routes and the road: no walker route runs through a solid object, and no solid blocks the main carriageway, Allen Avenue or the GRA street.
- Whole existing regression suite re-run on the new build.

## Measured cost

Triangles drawn at the lowest quality tier: the Ikeja views measured between 31,000 and 91,000. The heaviest view in the game is still the Mushin lane at about 148,000. The Origin crossroad looking west is 136,000, a little lower than in b50. Phone speed is unmeasured. Only a real phone can say whether it stays smooth.

## Known limits

- Ikeja here is a slice about 470 m long. The real district is many square kilometres. Real Allen Avenue and the real GRA are far bigger.
- Only the main road and the Allen Avenue arms carry traffic. The GRA street has none.
- Only the six places can be entered. The other shops share a few fronts.
- Parked cars are static.
- Seated poses do not exist yet, so people in the restaurant, lounge and cinema stand or walk.
- Real photographs of Ikeja were not used. If you send some, the fronts and the layout can be corrected from them.
