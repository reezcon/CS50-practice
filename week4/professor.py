import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y
        tries = 0

        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))

                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {answer}")

    print("Score: ", score)



def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    try:
        if level == 1:
            num = random.randint(0, 9)
        elif level == 2:
            num = random.randint(10, 99)
        elif level == 3:
            num = random.randint(100, 999)

    except ValueError:
        pass
    return num

if __name__ == "__main__":
    main()
