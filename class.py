class Budget:
    def __init__(self, category,amount):
        self.category = category
        self.amount = amount

    def Deposit(self, deposit):
        print('__'*20)
        balance = self.amount
        self.amount = self.amount + deposit
        print(f'Your new balance for {self.category} is {self.amount}')

    def Withdraw(self, withdraw):
        print('=**='*20)
        self.withdraw = withdraw
        if withdraw > self.amount:
            print('Insufficient funds')
        else:
            new_balance = self.amount
            self.amount = self.amount - withdraw
        print(f'You withdrew {withdraw} from {self.category}')
        print(f'Your new balance for {self.category} is {self.amount}')

    def Transfer(self,cat_transfer,transfer):
        print('=='*20)
        if transfer > self.amount:
            print('Insufficient funds to transfer')
        else:

            letis = self.amount - transfer
            cat_transfer.amount  = cat_transfer.amount + transfer

            output = f'You transfered ${transfer} to {cat_transfer.category} budget\n'
            output += f'from {self.category} budget and your remaining Balance is {letis} for {self.category} budget'

            print(output)





food = Budget("food", 1000)
clothing = Budget("clothing", 2000)
entertainment = Budget("entertainment", 1000)

food.Deposit(500)
clothing.Deposit(500)
entertainment.Deposit(500)

food.Withdraw(500)
clothing.Withdraw(500)
entertainment.Withdraw(500)

food.Transfer(clothing,500)
clothing.Transfer(entertainment,500)
entertainment.Transfer(food,500)

