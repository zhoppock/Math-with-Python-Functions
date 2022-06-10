def doubleYourMoney(x):
  return x+x

def tripleYourMoney(y):
  return y*3

cash = input("How much money do you have? $")

new_cash=doubleYourMoney(int(cash))
print("Now you doubled your original cash to $" + str(new_cash) + "!")

newer_cash=tripleYourMoney(int(cash))
print("Now you tripled your original cash to $" + str(newer_cash) + "!")