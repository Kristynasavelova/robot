robot={
    "AI":"opravář",
    "Chat":"rady všeho druhu"
}

nazevRobota = input("zadejte název robota: ")
hodnota = input("zadejte hodnotu: ")
if nazevRobota in robot.items():
    print([hodnota], [nazevRobota])

