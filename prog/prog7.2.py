
def search():
    var1 = input("== Zoekfunctie ==\n"
                "Naam: ")
    var2 = telefoonboek.get(var1)
    print("Telefoonnummer: ", var2)

telefoonboek = {}

var1 = input("Naam: ")
var2 = input("Nummer: ")

telefoonboek.update({var1:var2})

for person in telefoonboek:
    print(person + ": " + telefoonboek[person])

search()