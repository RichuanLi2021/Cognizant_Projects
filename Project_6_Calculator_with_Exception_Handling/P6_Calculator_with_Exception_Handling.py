import logging

logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s: %(message)s"
)

def input_checker(prompt: str) -> int:
    while True:
        picker = input(prompt).strip()
        try:
            pick = int(picker)
            if 1 <= pick <= 5:
                return pick
            else:
                print(f"{pick} is out of range; please enter 1–5.")
        except ValueError as e:
            print(f"Invalid input: '{picker}' is not a number. Try again.")
            logging.error("ValueError in menu choice: %s", e)

def get_number(prompt: str) -> float:
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError as e:
            print(f"Invalid input: '{text}' is not a valid number. Try again.")
            logging.error("ValueError in numeric input: %s", e)

def main() -> None:
    menu_options = {
        1: "Addition",
        2: "Subtraction",
        3: "Multiplication",
        4: "Division",
        5: "Exit"
    }

    print("Welcome to the Error-Free Calculator!")

    while True:
        for key, name in menu_options.items():
            print(f"{key}. {name}")
        choice = input_checker("Choose an operation (1–5): ")

        # 2) Handle exit
        if choice == 5:
            print("Goodbye!")
            break

        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")

        if choice == 1:
            result = a + b
            print(f"Result: {a} + {b} = {result}\n")

        elif choice == 2:
            result = a - b
            print(f"Result: {a} – {b} = {result}\n")

        elif choice == 3:
            result = a * b
            print(f"Result: {a} × {b} = {result}\n")

        else:
            try:
                result = a / b
            except ZeroDivisionError as e:
                print("Oops! Division by zero is not allowed.\n")
                logging.error("ZeroDivisionError occurred: %s", e)
            except Exception as e:
                print(f"Unexpected error during division: {e}\n")
                logging.error("Unexpected error: %s", e)
            else:
                print(f"Result: {a} ÷ {b} = {result}\n")
            finally:
                # Always runs, even after a ZeroDivisionError
                print("Division operation complete.\n")

if __name__ == "__main__":
    main()