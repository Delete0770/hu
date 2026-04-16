telefoonboek = {}

var1 = input("naam: ")
var2 = input("nummer: ")

telefoonboek.update({var1:var2})

for person in telefoonboek:
    print(person + ": " + telefoonboek[person])

