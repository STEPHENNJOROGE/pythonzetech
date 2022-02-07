tp=float(input("enter the total price of goods bought: "))

if(tp>=1000):
  discount=(tp*5/100)
  amount=tp-discount
  print(discount)
  print(amount)
else:
  discount=0
  print("no discount")
  print(tp)

  