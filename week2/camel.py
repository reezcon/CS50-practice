def main():
    camel = input("CamelCase: ")
    print("snake_case: ", snake_case(camel))

def snake_case(camel):
    snake = ""
    for char in camel:
        if char.isupper(): 
            snake += "_" + char.lower()
        else: 
            snake += char.lower()
    return snake

main()