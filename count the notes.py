Amount = int(input("Please Enter Amount for Withdraw"))
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10
print("notes of 100 rupees: ", note1)
print("notes of 50 rupees: ", note2)
print("notes of 10 rupees: ", note3)