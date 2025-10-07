citynames = ["london", "edinburgh", "cardiff", "belfast", "glasgow"]
population = ["8908", "482", "366", "341", "635"]
# for counter in range(len(citynames)):
#     print(citynames[counter] + " has a population of " + str(population[counter]))

found = False
usercity = input("what city do you want a population for mate?: ")
for counter in range(len(citynames)):
     if usercity == citynames[counter]:
         print(citynames[counter] + " has a population of " + str(population[counter]))
         found = true

if not found:
     print("we only have 5 cities mate, that isnt one of the 5")