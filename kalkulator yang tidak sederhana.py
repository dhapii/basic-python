def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    while True:
        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            if choice == '1':
                print(f"Hasil: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Hasil: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Hasil: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Hasil: {num1} / {num2} = {result}")
        else:
            print("Pilihan tidak valid")

        next_calculation = input("Ingin melakukan perhitungan lain? (y/n): ")
        if next_calculation.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()
