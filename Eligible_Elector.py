# Project - Eligible Elector
"""
    1. User input an age
    2. Call function to verify if age is above or under 18
    3. Always tell the margin of age when it is under 18
"""

class EligibleElector:
    def __init__(self, age: int):
        self.age = age

    def age_checker(self):
        if self.age >= 18:
            print("Congratulations! You are eligible to vote. Go make a difference!")
            return self.age
        else:
            gap = 18 - self.age
            print(f"Oops! You’re not eligible yet. But hey, only {gap} more years to go!")
            return self.age


while True:
    yourAge = int(input("How old are you? "))

    getItWork = EligibleElector(yourAge)
    result = getItWork.age_checker()

    doAgain = input("Do you wanna try again? (Enter Y to proceed and N to exit): ")
    if doAgain == "N":
        break


