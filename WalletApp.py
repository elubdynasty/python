"""
- Must include 1 class
- Must have some sort of main menu and accept user input to route logic flow
- Needs to have the following functionality:
   - Check Balance
   - Deposit
   - Withdrawal
   - Exit
- Must manage balance accurately(balance should reflect transactions).

"""


class Wallet:

  balance_amt = 0

  def __init__(self):
    self.name = input('Please enter your name: \n')

  def username_input(self):

    return f'Hi {self.name}, What can I help you with today?'

  def deposit(self, amt):
    self.balance_amt += amt
    return self.balance_amt

  def withdrawal(self, amt):
    self.balance_amt -= amt
    return self.balance_amt
  
  def cur_bal(self):
    print(f'Hi {self.name}, your current balance is ${self.balance_amt}')


thewallet = Wallet()
print(thewallet.username_input())

while True:
  options = input(""" Press the first letter of the ff. options
                      Balance
                      Deposit
                      Withdrawal
                      Exit: """)

  if options.lower() == 'b':
    thewallet.cur_bal()

  elif options.lower() == 'd':
    thewallet.deposit(
      int(input('Please enter the amount you want to deposit: ')))
    thewallet.cur_bal()

  elif options.lower() == 'w':

    amt = int(input('Please enter the amount you want to withdraw: '))

    if amt < thewallet.balance_amt:

      thewallet.withdrawal(amt)
      thewallet.cur_bal()
    
    else:
      print('Insufficient balance')

  elif options.lower() == 'e':

    print('Thanks for banking @ Wallet App, Goodbye!')
    exit(0)
