
# kasir

foods = []
prices = []
total = 0
kembalian = 0
while True:
    food = input("Masukkan Nama Makanan (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Masukkan Harga Makanan {food}: Rp."))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: Rp.{total}")
uang_pembeli = float(input("Masukkan Uang Pembeli : Rp."))
kembalian = uang_pembeli - total
print(f"Uang Kembalian Pembeli Adalah: Rp {kembalian}") 