class bankAccount():
    def __init__(self,name,ac_no,init_balance = 0):
        self.name = name
        self.ac_no = ac_no
        self.balance = init_balance
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount : {amount:.2f}")
            print(f"Current balance : {self.balance:.2f}")
        else:
            print("Deposite positive amount")

    def withdraw(self,amount):
        if amount<= self.balance:
            if amount > 0:
                self.balance -= amount
                print(f"Withdraw amount : {amount:.2f}")
                print(f"Current balance : {self.balance:.2f}")
            else:
                print("Withdraw amount should be more than 0")
        else:
            print("insufficient balance")
    
    def view(self):
        return self.balance
     
def create_account():
    name = input("Enter your name : ")
    ac = input("Enter your account no :")
    print(f"Account holder name : {name}")
    print(f"Account no : {ac}")
    return bankAccount(name,ac)


def main():
    account = create_account()#backAccount(name,ac)
    while True:
        print("1 : Show cuurent balance")
        print("2 : deposit ammount")
        print("3 : withdraw ammount")
        print("4 : exit")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            current_amt = account.view()
            print(f"Current balance : {current_amt}")
        elif choice == 2:
            deposite_amt = float(input("Enter deposite ammount : "))
            account.deposite(deposite_amt)
        elif choice == 3:
            withdraw_amt = float(input("Enter withdrawal ammount : "))
            account.withdraw(withdraw_amt)
        elif choice == 4:
            print("transaction completed")
            break
        else:
            print("Invalid choice, enter choice between 1 to 4")

main()