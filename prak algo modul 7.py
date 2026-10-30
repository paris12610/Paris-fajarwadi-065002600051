def cek_faktor(angka, pembagi):
    """Fungsi 1: Mengecek apakah angka habis dibagi oleh pembagi tertentu"""
    if angka % pembagi == 0:
        return True
    return False

def tentukan_prima(n):
    """Fungsi 2: Menentukan apakah suatu bilangan adalah prima"""
    if n <= 1:
        return False
    
    # Melakukan pengecekan faktor dari 2 hingga n-1
    for i in range(2, n):
        if cek_faktor(n, i):
            return False
    return True

# --- Program Utama ---
if __name__ == "__main__":
    angka_input = int(input("Masukkan angka: "))
    
    if tentukan_prima(angka_input):
        print(f"{angka_input} adalah bilangan Prima")
    else:
        print(f"{angka_input} bukanlah bilangan Prima")
        
        
        
        
        
#latihan kedua

def tentukan_ordinal(angka):
    """
    Fungsi dengan parameter untuk menentukan akhiran ordinal number
    berdasarkan digit terakhir angka.
    """
    digit_terakhir = angka % 10
    
    if digit_terakhir == 1:
        return 'st'
    elif digit_terakhir == 2:
        return 'nd'
    elif digit_terakhir == 3:
        return 'rd'
    else:
        return 'th'

# ==================== PROGRAM UTAMA ====================
print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    angka = int(input("masukkan angka: "))
    
    # Memanggil fungsi dengan parameter angka
    suffix = tentukan_ordinal(angka)
    
    # Menampilkan hasil sesuai format output
    print(f"({angka}, '{suffix}')")
    
    # Kondisi untuk menghentikan perulangan jika user memasukkan angka 0
    if angka == 0:
        break

print("terima kasih telah menggunakan program saya")
