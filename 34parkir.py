def hitung_biaya_parkir(durasi, jenis_kendaraan):
    # Tarif dasar untuk dua jam pertama
    tarif_awal = 3000
    # Tarif per jam setelah dua jam pertama untuk masing-masing jenis kendaraan
    tarif_per_jam_motor = 1000
    tarif_per_jam_mobil = 1500
    # Biaya tambahan jika parkir melebihi 24 jam
    tambahan_24_jam = 10000

    # Menentukan tarif per jam berdasarkan jenis kendaraan
    if jenis_kendaraan == "sepeda motor":
        tarif_per_jam = tarif_per_jam_motor
    elif jenis_kendaraan == "mobil":
        tarif_per_jam = tarif_per_jam_mobil
    else:
        # Jika jenis kendaraan tidak valid, kembalikan pesan kesalahan
        return "Jenis kendaraan tidak valid."

    # Menghitung biaya parkir berdasarkan durasi
    if durasi <= 2:
        # Untuk durasi 2 jam atau kurang, hanya dikenakan tarif awal
        biaya = tarif_awal
    elif durasi <= 24:
        # Untuk durasi lebih dari 2 jam tetapi kurang atau sama dengan 24 jam
        biaya = tarif_awal + tarif_per_jam * (durasi - 2)
    else:
        # Untuk durasi lebih dari 24 jam, tambahkan biaya tambahan
        biaya = tarif_awal + tarif_per_jam * (durasi - 2) + tambahan_24_jam

    # Mengembalikan hasil perhitungan biaya parkir
    return biaya

# Input dari pengguna
try:
    # Meminta input durasi parkir dari pengguna
    durasi = int(input("Masukkan durasi parkir (dalam jam): "))
    # Meminta input jenis kendaraan dari pengguna
    jenis_kendaraan = input("Masukkan jenis kendaraan (sepeda motor/mobil): ").lower()

    # Validasi untuk durasi negatif
    if durasi < 0:
        print("Durasi yang Anda masukkan tidak valid.")
    else:
        # Memanggil fungsi untuk menghitung biaya parkir
        biaya = hitung_biaya_parkir(durasi, jenis_kendaraan)
        # Jika fungsi mengembalikan pesan kesalahan, tampilkan pesan tersebut
        if isinstance(biaya, str):
            print(biaya)
        else:
            # Jika berhasil, tampilkan total biaya parkir
            print(f"Biaya parkir untuk {durasi} jam dengan {jenis_kendaraan} adalah Rp: {biaya}")
except ValueError:
    # Menangkap kesalahan jika input durasi bukan angka
    print("Input durasi harus berupa angka.")
