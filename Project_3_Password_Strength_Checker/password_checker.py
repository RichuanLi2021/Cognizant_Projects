def psd_checker(prompt: str):
    special_chars = ['$', '@', '#', '%']
    while True:
        password = input(prompt).strip()
        msg_list = []

        if len(password) < 8:
            msg_list.append("at least 8 chars")

        if not any(char in special_chars for char in password):
            msg_list.append("include at least one special character")

        if not any(char.isupper() for char in password):
            msg_list.append("include at least one character in upper case")

        if not any(char.islower() for char in password):
            msg_list.append("include at least one character in lower case")

        if not any(char.isdigit() for char in password):
            msg_list.append("include at least one digit")

        if msg_list:
            if len(msg_list) > 1:
                error_msg = ", ".join(msg_list[:-1]) + " and " + msg_list[len(msg_list) - 1]
            else:
                error_msg = msg_list[0]
            print(f"Your password needs to {error_msg}")
            continue

        print("Your password is strong! 💪")
        break

def main():
    psd_checker("Enter a password: ")


if __name__ == "__main__":
    main()