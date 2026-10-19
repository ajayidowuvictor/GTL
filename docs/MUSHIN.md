# Mushin, Lagos mainland (district 4, build b50)

Fourth district of the Lagos mainland world plan. It fills the free ground between Oshodi and Ojuelegba, north of the main road. It was built and tested on its own before any other district is started.

## What is real and what is invented

Sources (text only, no photographs were available): Wikipedia "Mushin, Lagos", Wikipedia "Ladipo Market", Wikipedia "Mushin Olosha", Wikipedia "Kalakuta Republic", the Nigeria Housing Market area guide to Mushin, and Ikeja Record on the reopening of five Mushin markets (Nov 2023).

Confirmed by those sources and used in the game:

- Mushin is a dense, trade-based district that borders Oshodi to the north and Surulere to the south, with Agege Motor Road on its eastern edge.
- Ladipo Market is a vehicle spare parts market on Ladipo Street in Papa Ajao. It sells used imported ("tokunbo") and new parts. Buyers come from across Nigeria and from other West African countries. The claim that it is the largest in Africa is a claim, not a measurement. Parts of it were demolished in 2015.
- Mushin markets named by the sources: Mushin main market, Ojuwoye, Awolowo, Irepodun and Daleko. Daleko is described as a foodstuff market. One source describes Ojuwoye as textiles and another as general goods; the game follows the textile description for its fabric market.
- Street food, neighbourhood bars, keke transport, three-storey blocks of flats replacing older "face-me-I-face-you" housing.
- The Kalakuta Republic compound stood at 14 Agege Motor Road, Idi-Oro, Mushin. It held a recording studio and a free clinic. It was attacked and burned in 1977 and is now a museum (opened 2012) with a restaurant and a hotel. The game does not recreate it. Its history is only told, in a few lines, by the band leader in the music house.

Not confirmed by those sources, so invented and labelled as a guess:

- The street layout. The real Ladipo Market is in Papa Ajao, not on the Agege Motor Road. The game puts a Ladipo-style street, "Ladipo Street", and a crossing "Idi-Oro Lane" in the free ground beside the main road, so that the district connects to its neighbours.
- All shop names (apart from the market names above), building shapes and every person's name.
- Opening hours. The sources do not state them. The game uses 8 AM to 6 PM (parts), 6 AM to 5 PM (foodstuff), 9 AM to 6 PM (fabric), and 5 PM to 3 AM (music house).
- All prices, and the 20 percent tokunbo discount on engine and tyres. These are game design.
- The music house. It is an invented venue, inspired by the district's real music history.

## What is built

- Ladipo Street: an 8 m street leaving the main road at x = -273 under a gate sign, 58 m long, with parts stalls, parked cars and a parts agent.
- Idi-Oro Lane: a 7 m lane crossing it, 75 m long, lined with parts shops, tyre stacks, engine blocks, racks of used bumpers and a roasted plantain seller.
- Nine shop-and-flat blocks of 2 to 4 floors: four are the places below, five are auto-parts shops with names like Tokunbo Engines and Brake Pad Centre.
- Four places you can walk into, each with staff, customers, an exit doorman and a closed board outside:
  - Ladipo Auto Parts Market (8 AM to 6 PM): shelving racks, tyre stacks, engine blocks. Tokunbo engine upgrade for 6,400 (Kunle charges 8,000) and tokunbo tyres for 4,800 (Kunle 6,000). The upgrade is the same one as at Kunle's workshop and changes the car's top speed and grip. Spare parts salesman shift.
  - Mushin Foodstuff Market (6 AM to 5 PM): sacks, baskets, tables of produce. Boiled yam, beans and dodo, garri and groundnut, coconut water. Foodstuff trader shift.
  - Ojuwoye Fabric and Tailors (9 AM to 6 PM): fabric shelves, tailors' benches, mannequins. Ankara cloth, a sewn outfit, alterations. Tailor's assistant shift.
  - Idi-Oro Music House (5 PM to 3 AM): bar, stage, tables. Live band night, suya, drinks. Stage hand shift. Open past midnight.
- Street people: a Ladipo parts agent, Mama Boli (roast plantain, 10 AM to 9 PM) and the Idi-Oro Lane guide.
- About 14 walkers on the streets and 14 inside the rooms, all on daily schedules. The music house crowd only comes out from 5 PM.
- Careers: spare parts salesman 3,600, foodstuff trader 2,800, tailor's assistant 3,300, stage hand 3,800 per shift base (same shift system and education pay bonus as before). None need experience.
- Phone: all new places are in the ride list and valid gig spots.
- Minimap: the Oshodi strip now runs on to Ojuelegba so all of Mushin is on one map, with its two streets drawn.

## Tests (script names in the build pipeline)

- Interiors: no overlap with other rooms, every person reachable, door reachable, never walking through furniture; street path to every outside person from the main road and from inside the street.
- Hours: each place refuses entry before opening and shows the board, accepts entry when open, closes you out at closing time (including across midnight for the music house).
- Services: yam, ankara, live band (fun, price, two hours pass), chat history, plantain; engine and tyre purchases change the car's upgrade level, cost exactly the stated price and change top speed; a buyer without cash is refused and nothing is fitted.
- Jobs and rides: the four shifts start and pay; every new place is in the ride list; walkers follow the clock.
- Signals: 300 seconds simulated, zero vehicles cross a stop line on red at Ojuelegba or Agege.
- Whole existing regression suite re-run on the new build.

## Measured cost

Triangles drawn at the lowest quality tier from the Origin crossroad facing west: 139,962 in b49, 139,918 now (unchanged, because Mushin is outside that view). Inside the new district: 84,000 on Ladipo Street and 144,000 looking east along Idi-Oro Lane, which is now the heaviest view measured. Phone speed is unmeasured. Only a real phone can say whether it stays smooth.

## Known limits

- Mushin here is a slice of about 100 m by 60 m. The real district is 17 square kilometres.
- Only the main road and the Ojuelegba and Agege arms carry traffic. Ladipo Street and Idi-Oro Lane have none.
- Only the four places can be entered. The other shops share a few fronts.
- Parked cars are static.
- The Kalakuta Republic museum is not recreated.
- Seated poses do not exist yet, so people in the music house stand or walk.
- Real photographs of Mushin were not used. If you send some, the shop fronts and layout can be corrected from them.
