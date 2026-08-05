def main():
    print(fuel_conversion())

def fuel_conversion():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0 or x > y or x < 0 or y < 0:
                raise ValueError

            percent = round((x/y)*100)
            if percent <= 1:
                return "E"
            elif percent >= 99:
                return "F"
            else:
                return f"{percent}%"

        except (ValueError, ZeroDivisionError):
            continue

main()
