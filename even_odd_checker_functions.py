def get_integer_input():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Try again.")

def check_even_odd(n):
    return f"{n} is an {'Even' if n % 2 == 0 else 'Odd'} number."

if __name__ == "__main__":
    print(check_even_odd(get_integer_input()))
