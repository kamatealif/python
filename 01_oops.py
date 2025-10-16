class Atm:

  # cunstructor(special power) -> super power -> that it is autometically called
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        How are you how i can help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)
        print() # for new line

        if user_input == '1':
            #create pin
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            # check balance 
            self.check_balance()
        elif user_input == '4':
            #withdraw
            self.withdraw_balance()
        else:
            exit()

    def create_pin(self):
      user_pin = input("Enter your pin: ")
      self.pin = user_pin

      user_balance = int(input("Enter balance: "))
      self.balance = user_balance

      print("Pin created successfully")
      self.menu()

    def change_pin(self):
        old_pin = input("Enter old pin")
        if old_pin == self.pin:
            #let him change the pin 
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print("Pin changed successfully...")
            self.menu()
        else:
            print("Nai karne de sakta re babaa...")
            self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print(f"Your balance is : {self.balance}")
        else:
            print("Chal nikal yaha se... ")
        self.menu()

    def withdraw_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            withdraw_amount = int(input("Enter how much you want to withdra: "))
            if withdraw_amount <= self.balance:                
                self.balance = self.balance - withdraw_amount
                print(f"Your remaining balance is {self.balance}")
            else:
                print(f"Remaining balance is: {self.balance}")
                print("Aukat se zyada nikal raha hai re tu...")
        else:
            print("Sale chor...")
        self.menu()
        
        
obj = Atm();