cost = float(input("Enter your total price: "))
money = float(input("Enter your money: "))
costx = cost
moneyx = money
money_dict = {1000:0, 500:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0, 0.5:0, 0.25:0, 0.1:0}

if money < cost:
    print("Not enough money")
else:
    moneyx = money - cost
    print("The exchanged money = %.2f" %moneyx)
    if moneyx >= 1000.0:
        num = moneyx // 1000
        money_dict[1000] = num
        moneyx = moneyx - (num * 1000)
    if moneyx >= 500.0:
        num = moneyx // 500
        money_dict[500] = num
        moneyx = moneyx - (num * 500)
    if moneyx >= 100.0:
        num = moneyx // 100
        money_dict[100] = num
        moneyx = moneyx - (num * 100)
    if moneyx >= 50.0:
        num = moneyx // 50
        money_dict[50] = num
        moneyx = moneyx - (num * 50)
    if moneyx >= 20.0:
        num = moneyx // 20
        money_dict[20] = num
        moneyx = moneyx - (num * 20)
    if moneyx >= 10.0:
        num = moneyx // 10
        money_dict[10] = num
        moneyx = moneyx - (num * 10)
    if moneyx >= 5.0:
        num = moneyx // 5
        money_dict[5] = num
        moneyx = moneyx - (num * 5)
    if moneyx >= 2.0:
        num = moneyx // 2
        money_dict[2] = num
        moneyx = moneyx - (num * 2)
    if moneyx >= 1.0:
        num = moneyx // 1.0
        money_dict[1] = num
        moneyx = moneyx - (num * 1)
    if moneyx >= 0.5:
        num = moneyx // 0.5
        money_dict[0.5] = num
        moneyx = moneyx - (num * 0.5)
    if moneyx >= 0.25:
        num = moneyx // 0.25
        money_dict[0.25] = num
        moneyx = moneyx - (num * 0.25)
    if moneyx >= 0.1:
        num = moneyx // 0.1
        money_dict[0.1] = num
        moneyx = moneyx - (num * 0.1)
    if moneyx < 0.1:
        print("Cannot exchange money = %.2f" %moneyx)


print("The change amount is: ")
for i in money_dict:
    if money_dict[i] >= 1.0:
        print("Note ", i, " = ", money_dict[i], " note")

