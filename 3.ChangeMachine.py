amount = int(input("Total Amount: KSh "))
payment = int(input("Cash Payment: Ksh "))
change_due = payment - amount
print("Change Due: KSh", change_due)

print("Five Hundreds: ", int(change_due // 500))
bal_500 = change_due % 500
print("Two Hundreds: ", int(bal_500 // 200))
bal_200 = bal_500 % 200
print("Hundreds: ", int((bal_200 //100)))
bal_100 = bal_200 % 100
print("Fifties: ", int((bal_100//50)))
bal_50 = bal_100 % 50
print("Twenties: ", int((bal_50//20)))
bal_20 = bal_50 % 20
print("Tens: ", int((bal_20//10)))
bal_10 = bal_20 % 10
print("Fives: ", int((bal_10//5)))
bal_5 = bal_10 % 5
print("Ones: ", int((bal_5//1)))
