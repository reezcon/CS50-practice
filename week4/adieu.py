import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")  
        if name == "":
            break
        else:
            names.append(name)
    except EOFError:
        break

print("Adieu, adieu, to " + p.join(names))