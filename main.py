pers1_name = input("Whats your name? : ")
pers1_wallet = input(pers1_name + ", How much money u have? : ")

pers2_name = input("Whats your name? : ")
pers2_wallet = input(pers2_name + ", How much money u have? : ")

pers3_name = input("Whats your name? : ")
pers3_wallet = input(pers3_name + ", How much money u have? : ")

if float(pers1_wallet) > float(pers2_wallet) > float(pers3_wallet):
    print(pers1_name + " is the richest")
elif float(pers2_wallet) > float(pers1_wallet) > float(pers3_wallet):
    print(pers2_name + " is the richest")
elif float(pers3_wallet) > float(pers1_wallet) > float(pers2_wallet):
    print(pers3_name + " is the richest")
else:
    print("no one is the richest")
