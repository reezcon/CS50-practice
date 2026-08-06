grocery = {}

while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery.update({item: 1})
    except EOFError:
        print()
        break
    
sorted_grocery = dict(sorted(grocery.items()))

for item, count in sorted_grocery.items():
    print(f"{count} {item}")

