import random


def generate_random():
    number = random.randint(1,10)
    return number


def main():
    guessed_number = int(input("Please select a number between 1 and 10: "))
    random_number = generate_random()
    if guessed_number == random_number:
        print("Good guess!")
    else:
        print("That ain't it.")

if __name__ == "__main__":
    main()

