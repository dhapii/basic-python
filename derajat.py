def reamur_to_kelvin(reamur):
    """Mengonversi suhu dari Reamur ke Kelvin."""
    celsius = reamur * 5 / 4
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_reamur(kelvin):
    """Mengonversi suhu dari Kelvin ke Reamur."""
    celsius = kelvin - 273.15
    reamur = celsius * 4 / 5
    return reamur

def main():
    try:
        # Konversi dari Reamur ke Kelvin
        reamur = float(input("Masukkan Reamur: "))
        kelvin = reamur_to_kelvin(reamur)
        print(f"Reamur ke Kelvin: {kelvin:.2f} Kelvin")
        
        # Konversi dari Kelvin ke Reamur
        kelvin = float(input("Masukkan Kelvin: "))
        reamur = kelvin_to_reamur(kelvin)
        print(f"Kelvin ke Reamur adalah: {reamur:.2f} Reamur")
    
    except ValueError:
        print("Input tidak valid! Harap masukkan nilai numerik.")

if __name__ == "__main__":
    main()
