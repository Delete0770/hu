
string = "Barbara had een bar, waar ze rabarbar verkocht, en die daarom de rabarbarbarbarabar werd genoemd."
new_string = string.replace("rabarbar", "rabarber")

print(string)
print(new_string)

string2 = "Niemand verwacht de Spaanse Inquisitie!# In feite, zij die de Spaanse Inquisitie wel verwachten..."
hashmark = string2.find("#")
print(string2)
print(string2[0:hashmark])