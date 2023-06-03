def currency():
     with open(r"C:\Users\HP\Desktop\currency.txt","r") as file:
          lines = file.readlines()
     amountinp = float(input("PLEASE ENTER THE AMOUNT TO BE CONVERTED:"))
     currencydict = {}
     for line in lines:

          parsed = line.split("\t")
          currencydict[parsed[0]] =parsed[1]
          for item in currencydict.keys():
               print(item)
     inpcurrency = input("PLEASE ENTER THE NAME OF THE CURRENCY YOU WANT TO CALCULATE RUPEES IN:")
     print(f"{amountinp} INR is equal to {amountinp *float(currencydict[inpcurrency])} {inpcurrency}")









currency()






