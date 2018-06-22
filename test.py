
musicians = {"Gaslight Anthem": ["Handwritten", "59 Sound", "Red Violins"],
             "Blindside": ["Silence", "Pitiful", "About a Burning Fire"],
             "Enter Shikari": ["Solidarity", "Constellations,", "Mothership"]}

print(musicians)
n = input("Pick a musician from the list")

if n in musicians:
    musician = musicians[n]
    print(musician)

