def hitung_biaya_parkir(durasi):
    # Tarif dasar parkir
    tarif_awal = 3000
    # Tarif per jam setelah 2 jam pertama
    tarif_lebih_dari_2jam = 1500
    # Biaya tambahan jika parkir lebih dari 24 jam (belum digunakan dalam logika)
    lebih_dari_24jam = 10000

    # Validasi input durasi (jika durasi kurang dari atau sama dengan 0)
    if durasi <= 0:
        print("Maaf, durasi yang Anda masukkan tidak valid.")
    
    # Jika durasi parkir kurang dari atau sama dengan 2 jam
    if durasi <= 2:
        biaya = tarif_awal 
    # Jika durasi parkir lebih dari atau sama dengan 24 jam
    elif durasi >= 24:
        # Biaya dihitung berdasarkan tarif awal dan tarif tambahan per jam
        biaya = tarif_awal + tarif_lebih_dari_2jam * (durasi - 2) + lebih_dari_24jam
    else:
        # Biaya dihitung untuk durasi antara 3 hingga 23 jam
        biaya = tarif_awal + tarif_lebih_dari_2jam * (durasi - 2) 
        
# mengembalikkan hasil perhitungan biaya parkir
    return biaya

# input dari pengguna
try:
    # Meminta input durasi parkir dari pengguna
    durasi = int(input("Masukkan durasi parkir Anda: "))
    
    # Validasi tambahan untuk memastikan durasi tidak negatif
    if durasi < 0:
        print("Durasi yang Anda masukkan tidak valid.")
    else:
        # Memanggil fungsi untuk menghitung biaya parkir
        biaya = hitung_biaya_parkir(durasi)
        # Menampilkan hasil biaya parkir
        print(f"Biaya parkir untuk {durasi} jam adalah Rp: {biaya}")
# Menangkap kesalahan jika input bukan angka
except ValueError:
    print("Angka yang Anda masukkan tidak valid.")
