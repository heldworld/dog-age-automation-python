class Dog:
#initialize
    def __init__(self, dogAge, humanAge):
        self.dogAge = dogAge
        self.humanAge = humanAge
        
#classify based on equivalent human age
    def human_age_calc(self):
        if 0 < self.dogAge <= 1:
            self.humanAge = self.dogAge * 15
        elif 1 < self.dogAge <= 5:
            self.humanAge = self.dogAge * 11 + 2
        elif 5 < self.dogAge <= 15:
            self.humanAge = self.dogAge * 8 - 3
            return self.humanAge
        else:
            print ("The calculator only supports ages 0–15.")
        
#give class to each human age       
    def dog_class(self):
        if 0< self.humanAge < 20:
            self.ageGP = "Young"
        elif 20 <= self.humanAge <= 39:
            self.ageGP = "Adult"
        else:
            self.ageGP = "Senior"
        print(f"Your Dog equivalent Human Age is {self.humanAge} and classified as {self.ageGP}")
#The Argument
while True:
    try:
        dogAge = float(input("Enter dog age (0–15): "))
        if 0 < dogAge <= 15:
            break
        else:
            print("Only numbers between 0 and 15 are allowed.")
    except ValueError:
        print("Invalid input. Only numbers (0–15) are allowed.")
dog1 = Dog(dogAge, humanAge)

dog1.human_age_calc()
dog1.dog_class()

    
    