from random import randint

articles = ["the", "a", "one", "some", "any"]
nouns = ["teacher", "student", "principal", "library", "school"]
verbs = ["taught", "learned", "read", "walked", "ran"]
prepositions = ["to", "from", "over", "under", "on"]

a = randint(0, 4)
b = randint(0, 4)
c = randint(0, 4)
d = randint(0, 4)
e = randint(0, 4)
f = randint(0, 4)
g = randint(0, 4)

print(articles[a], nouns[b], verbs[c], articles[d], nouns[e], prepositions[f], verbs[g] )