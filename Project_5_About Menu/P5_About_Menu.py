import numbers
import turtle

# step 2
def factorial_num(num: int) -> int:
    if num < 0:
        raise ValueError("cannot be negative!")
    if num in (0, 1):
        return 1
    return num * factorial_num(num - 1)

# step 3: brute-force search --> time complexity o(n^2)
def fibonacci_nth(nth: int) -> int:
    if nth < 0:
        raise ValueError("cannot be negative!")

    if nth == 0:
        return 0

    if nth == 1:
        return 1

    return fibonacci_nth(nth - 1) + fibonacci_nth(nth - 2)
# step 4: DP --> time complexity o(n)
def dp_fibonacci_nth(nth: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {}

    if nth < 0:
        raise ValueError("cannot be negative!")
    if nth in memo:
        return memo[nth]

    if nth == 0:
        return 0
    if nth == 1:
        return 1

    # memorize
    memo[nth] = dp_fibonacci_nth(nth - 1, memo) + dp_fibonacci_nth(nth - 2, memo)
    return memo[nth]

## Recursive Fractal Pattern (Bonus)
import turtle


def draw_tree(branch_len: float, t: turtle.Turtle):
    if branch_len < 10:
        return

    # Draw the main branch
    t.forward(branch_len)

    # Draw right subtree
    t.right(20)
    draw_tree(branch_len - 15, t)

    # Reset and draw left subtree
    t.left(40)
    draw_tree(branch_len - 15, t)

    # Restore original orientation
    t.right(20)
    t.backward(branch_len)

## input checker it will take in the prompt
# and then check if the use enters the valid input or not,
# if not it would prompt to re-enter, any non-number type input will be injected with a value error
def input_checker(prompt: str) -> int:
    rangelist: list[int] = [1, 2, 3, 4]
    while True:
        pick = input(prompt).strip()
        try:
            value = int(pick)
            if value not in rangelist:
                print(f"{value} is out of range.")
            else:
                return value
        except ValueError:
            print(f"Invalid input: {pick!r}. Please enter a number within the range {rangelist}.")

# step 5
def menu_select(prompt: str):
    valid_input = input_checker(prompt)
    match int(valid_input):
        case 1:
           f_num = int(input("Enter a number to find its factorial: ").strip())
           result = factorial_num(f_num)
           print(f"The factorial of {f_num} is {result}.")
        case 2:
           fib_nth = int(input("Enter the position of the Fibonacci number: ").strip())
           result = dp_fibonacci_nth(fib_nth)
           print(f"The {fib_nth}th Fibonacci number is {result}.")
        case 3:
            # Setup turtle screen
            screen = turtle.Screen()
            screen.bgcolor("skyblue")
            screen.title("A simple fractal tree drawing!")

            # Create turtle
            t = turtle.Turtle()
            t.color("green")
            t.speed("fastest")
            t.left(90)  # Point upward
            t.up()
            t.backward(100)
            t.down()

            # Draw the tree
            draw_tree(100, t)

            # Finish
            turtle.done()
        case 4:
            print("Bye Bye")
            return
        case _:
            print("you've gotta pick something")

def main():
    return menu_select("Welcome to the Recursive Artistry Program! "
                "Choose an option: "
                "1. Calculate Factorial "
                "2. Find Fibonacci "
                "3. Draw a Recursive Fractal "
                "4. Exi > ")

if __name__ == "__main__":
    main()