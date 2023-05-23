# WRITE A PROGRAM USING PYTHON TO MAKE A CALCULATOR
sum1 = 0
while True:
    amount = input("ENTER THE PRICE OF ITEM(enter q when when no more items are in the list):")
    if amount!="q":
        sum1+=int(amount)
    else:
        print(f"THANKS FOR SHOPPING, HOPE YOU LIKED OUR SERVICE AND YOU FIND IT REASONABLE TO PAY AN AMOUNT OF {sum1}"
              f" RUPEES ONLY")
        break                           #always add break while you use a loop otherwise it would not end

"the code is available on github also."