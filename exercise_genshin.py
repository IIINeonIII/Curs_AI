characters_information = {
    "Furina": {"element": "hydro",
               "rarity" : ".."},
    "Alhaitham": {"element": "dendro",
                  "rarity" : ".."},
    "Ororon": {"element": "electro",
               "rarity" : "."},
    "Chasca": {"element": "anemo",
               "rarity" : ".."},
    "Shenhe": {"element": "cryo",
               "rarity" : ".."},
    "Escofier": {"element": "cryo",
                 "rarity" : ".."},
    "Yelan": {"element": "hydro",
              "rarity" : ".."},
    "Fischl": {"element": "electro",
               "rarity" : "."},
    "Bennet": {"element": "pyro",
               "rarity" : "."},
    "Raiden Shogun": {"element": "electro",
                      "rarity" : ".."},
    "Eula": {"element": "cryo",
             "rarity" : ".."},
    "Xinshou": {"element": "hydro",
                "rarity" : "."},
    "Kazuha": {"element": "anemo",
               "rarity" : ".."},
    "Kokomi": {"element": "hydro",
               "rarity" : ".."},
    "Mualani": {"element": "hydro",
                "rarity" : ".."},

}

# search_element = input("Enter an element (e.g., hydro, pyro, cryo): ").strip().lower()

#matching_characters = []
#for character, info in characters_information.items():
#    if info["element"].lower() == search_element:
#        matching_characters.append(character)


#count = len(matching_characters)


#if count == 0:
#    print(f"\nNo characters found with the element '{search_element}'.")
#elif count == 1:
#    print(f"\nOne character found with the element '{search_element}': {matching_characters}")
#else:
#    print(f"\nThere are {count} character(s) with the element '{search_element}': {matching_characters}")

for name, info in characters_information.items():
    print(f"{name} has the element: {info['element']}")

for name, info in characters_information.items():
    if info['rarity'] == ".":
        info['rarity'] = "4 star"
    elif info['rarity'] == "..":
        info['rarity'] = "5 star"

for name, info in characters_information.items():
    print(f"{name}: {info}")


for info in characters_information.values():
    info.update({"equipment value": 0})

print(characters_information["Furina"])

for display in characters_information:
    print(display)

list_of_elements = []
for element in characters_information.values():
    list_of_elements.append(element['element'])
print(set(list_of_elements))

if characters_information["Furina"]["equipment value"] == 0:
    characters_information["Furina"]["equipment value"] = 25

print(characters_information["Furina"])

than_25 = bool
if characters_information["Furina"]["equipment value"] < 25:
    than_25 = True

if than_25 == True:
    print("Furina is undergeared")