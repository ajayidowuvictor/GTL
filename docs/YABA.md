# Yaba, Lagos mainland (district 7, build b53)

Seventh district of the Lagos mainland world plan. The main road now continues west past Agege into Yaba, the technology and student district: a bus terminal, the Tejuosho shopping complex, Yaba market, the E-Centre on Commercial Avenue, the Co-Creation Hub, Yaba College of Technology and Queen's College. It was built and tested on its own before any other district is started.

## What is real and what is invented

Sources (text only, no photographs were available): Wikipedia "Yaba, Lagos", Wikipedia "Yaba College of Technology", Wikipedia "Tejuosho Market".

Confirmed by those sources and used in the game:

- Yaba is described as the technological hub of Lagos. People also call it the Silicon Valley of Nigeria (a nickname used in Nigerian press).
- The Co-Creation Hub (CcHub) was founded in late 2011 by Bosun Tijani and colleagues. It became one of the pioneer startup incubators in Nigeria. Companies such as Hotels.ng and Andela came out of Yaba.
- The E-Centre is a shopping centre on Commercial Avenue and has cinemas.
- Yaba College of Technology (Yabatech) was founded in 1947 as the successor to Yaba Higher College. It gained autonomous status in 1969, was renamed Federal Polytechnic Yaba in 1979, and went back to Yaba College of Technology in 1980. It is described as Nigeria's first higher educational institution.
- Tejuosho is Yaba's market area, called the shopping centre of Lagos. A fire destroyed most of the old market. The Lagos State Government, a building firm and a bank rebuilt it as a "mega shopping plaza" in a public-private partnership, and it was commissioned in 2014. After the rebuild stall prices rose and some low-income traders complained.
- Yaba has a railway station, Mobolaji Johnson Central Station, inaugurated in 2021 on the standard-gauge line to Ibadan.
- Queen's College is a federal government girls' school in Yaba, founded in 1927 (from earlier research in this project, not re-checked this round).
- The Efik people are from Calabar in Cross River State. Afang soup and edikang ikong are leafy soups; ekpang nkukwo is a cocoyam dish.

Invented, and labelled as a guess:

- The layout. Real Yaba is a large area. The game has a 560 metre slice of main road, with Commercial Avenue and a campus drive running north from it. The real Tejuosho is on the Ojuelegba to Itire road; here it stands on the main road.
- Every shop, stall, hall, room and person. Mr Kayode, Aunty Ruth, Mama Shola, Pharmacist Bola, Mrs Adaeze, Aunty Grace, Mr Tobi, Barista Dami, Ms Fola, Dr Adeyemi and Mama Etim are made up. The Co-Creation Hub's desks and the E-Centre's shops are invented. So are the Yabatech lecture room and the school blocks around it.
- Opening hours, prices, coach fares, the coach service itself, the course fees, the day pass, and the evening market sale.
- The terminal. Real Yaba has no coach terminal that I sourced. The game puts a bus terminal there so you can travel.
- Names of departments on the campus blocks, and the Queen's College buildings.

## What is built

- About 560 m of new main road west of Agege, ending at a road-works barrier. The old Agege end barrier is gone.
- A gantry over the road reading "Herbert Macaulay Way. Yaba".
- Commercial Avenue, a street running north: the E-Centre (four floors) on the east side, the Co-Creation Hub on the west, shops, lamps, and an end barrier.
- The Yabatech drive, running north: an entrance arch, the entrepreneurship centre, the schools of engineering, art and design, and science, lawns, trees and lamps.
- North of the main road: shops, Efik Kitchen, and old walled compounds at the far end.
- South of the main road: shops, the bus yard with two tent-like roofs and four parked danfos, the Yaba Terminal building, the Tejuosho Shopping Complex (a 44 m wide building), a stall yard with a gantry sign "Yaba Market. Evening Sale", Queen's College (a walled compound, a gate, a lawn, a block and trees), shops, and old compounds.
- Four bus stops, okadas, lamps, poles and trees along the road.
- Six places you can walk into, each with staff, customers, an exit doorman and a closed board outside:
  - Yaba Terminal (5 AM to 10 PM): a ticket desk and a snack kiosk. Coach to Agege Station for 400 (45 minutes) or to Oshodi for 500 (1 hour). Snacks: puff-puff, chin chin, meat pie, water, zobo.
  - Tejuosho Shopping Complex (8 AM to 7 PM): four counters. Second-hand clothes (jeans 4,500, shirt 2,500, sneakers 8,000, handbag 6,000), a pharmacy (vitamin C, paracetamol, soap and sponge, sanitiser), a grocery (noodles, milk, biscuits, a bag of rice) and cosmetics (perfume, lotion, hair attachment). Racks of clothes and mannequins on the floor.
  - E-Centre (10 AM to 11 PM): a cinema counter (matinee 2,500, evening 3,500, ticket and popcorn 5,000; each film takes two hours) and E-Cafe (coffee, cappuccino, shawarma, milkshake).
  - Co-Creation Hub (8 AM to 8 PM): a day pass for 3,000 gives four hours at a desk and raises social. The host explains the real hub history.
  - Yabatech centre (8 AM to 5 PM): a lecture room. Short courses at 1,200 for one hour or 3,300 for three hours raise Education. Certificates open better jobs and raise shift pay, the same education number the Ojuelegba school uses.
  - Efik Kitchen (8 AM to 10 PM): afang soup, edikang ikong, fisherman soup with pounded yam, ekpang nkukwo, zobo.
- Street people: the Yabatech gate guard, the Queen's College gatekeeper, a tech tour guide, a market trader (30 percent off everything from 5 PM to 9 PM), a boli (roast plantain) seller and a puff-puff hawker. Each tells the researched facts above where they apply.
- About 22 walkers on the streets, campus, bus yard, market aisle and Queen's College lawn, and 21 inside the rooms, all on daily schedules.
- Careers: coach park agent 4,000, clothes seller 3,400, cafe barista 3,900, kitchen cook 3,800, hub host 5,200 (needs Education Level 1), teaching assistant 5,800 (needs Education Level 2).
- Phone: every new place and street person is in the ride list and the gig spots.
- Traffic: both main-road lanes carry traffic over the full new length.
- Minimap: a ninth strip for Yaba with the road, both side streets, the bus yard, the college lawn and the buildings.
- World size: the playable width grew from 4,070 m to 4,760 m. Rooms for the new interiors sit in two new columns past the Agege rooms.

## Tests (script names in the build pipeline)

- Interiors: no overlap with other rooms, every person reachable and clear of furniture, exit door reachable; street paths to every outside person; paths along the whole new road, up Commercial Avenue and the drive, through the bus yard, along the market aisle and onto the college lawn.
- Hours: each place refuses entry before opening and shows the board, accepts entry when open, and closes you out at closing time (checked for Tejuosho, the E-Centre and the Yabatech centre).
- Services: every price, need change and time cost is checked, including coach tickets (cost, destination, travel time), cinema time, the hub day pass, the lectures (fee, hours, Education level), the market trader at noon and in the evening, and refusals when you are too poor or too tired.
- Jobs and rides: all six shifts start and pay; the hub host and teaching assistant jobs are refused below their Education level; every new place is in the ride list; walkers follow the clock.
- Walker routes and roads: no walker route runs through a solid object; no solid blocks the main carriageway, Commercial Avenue or the drive; a car drives the whole road in both lanes with traffic.
- Signals and the rail crossing from the Agege build: re-run, with no red-light violations and the gates working.
- Whole existing regression suite re-run on the new build.

## Measured cost

Triangles drawn at the lowest quality tier: the Yaba views measured between 25,000 and 69,000. The heaviest views in the game are still the Mushin lane at about 143,000 and the Origin crossroad looking west at about 141,000. Phone speed is unmeasured. Only a real phone can say whether it stays smooth.

## Known limits

- Yaba here is a slice about 560 m long. The real district is much bigger.
- The Yaba railway station is not built. The terminal's coaches are the way to travel.
- Coach tickets are one-way, and there is no coach from Agege or Oshodi back to Yaba. The way back is a ride or a drive.
- Only the main road carries traffic. Commercial Avenue and the campus drive have none.
- Only the six places can be entered. The other shops share a few fronts, and the campus blocks cannot be entered.
- Parked cars and danfos are static.
- Seated poses do not exist yet, so people in the cinema, the hub, the lecture room and the canteen stand or walk.
- Real photographs of Yaba were not used. If you send some, the fronts and the layout can be corrected from them.
