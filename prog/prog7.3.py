# gebruik if statment

def search():
    var1 = input("== Zoekfunctie ==\n"
                "Naam: ")
    var2 = telefoonboek.get(var1)
    print("Telefoonnummer: ", var2)


def delete():
    var = input("== Verwijder ==\n"
                "Naam: ")
    telefoonboek.pop(var)

telefoonboek = {}

var1 = input("naam: ")
var2 = input("nummer: ")

telefoonboek.update({var1:var2})

for person in telefoonboek:
    print(person + ": " + telefoonboek[person])

search()
delete()
print(telefoonboek)