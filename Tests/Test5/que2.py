n = int(input("Enter the number of coins: "))

coins = list(map(int, input("Enter the coin numbers: ").split()))

missing_coin = 0

for coin in coins:
    missing_coin ^= coin

print(f"Sample Output: {missing_coin}")