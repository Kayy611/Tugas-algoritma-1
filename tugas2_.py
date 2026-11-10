def hitung_biaya_berat(berat):
    "Menghitung biaya berat paket (Rp10.000 untuk <=2 kg, +Rp4.000 per kg selebihnya)."
    if berat <= 2:
        return 10000
    else:
        return 10000 + (berat - 2) * 4000


def hitung_biaya_jarak(jarak):
    "Menghitung biaya jarak pengiriman (Rp0 jika <=20 km, Rp5.000 jika >20 km)."
    if jarak <= 20:
        return 0
    else:
        return 5000


def hitung_ongkir_akhir(berat, jarak, status_anggota):
    "Menghitung rincian biaya berat, biaya jarak, potongan anggota (10%), dan ongkos kirim akhir."
    biaya_berat = hitung_biaya_berat(berat)
    biaya_jarak = hitung_biaya_jarak(jarak)
    subtotal = biaya_berat + biaya_jarak
    
    potongan = 0
    if status_anggota.lower() == "ya":
        potongan = 0.10 * subtotal
        
    ongkir_akhir = subtotal - potongan
    return biaya_berat, biaya_jarak, potongan, ongkir_akhir


def cetak_semua_struk(daftar_pesanan):
    "Mencetak struk rincian ongkir tiap pesanan dan menghitung total pendapatan harian toko."
    total_pendapatan = 0
    
    print("=" * 55)
    print("                 STRUK PENGIRIMAN TOKO DARING                 ")
    print("=" * 55)
    
    for idx, pesanan in enumerate(daftar_pesanan, 1):
        nama = pesanan["nama"]
        berat = pesanan["berat"]
        jarak = pesanan["jarak"]
        anggota = pesanan["anggota"]
        
        b_berat, b_jarak, potongan, ongkir_akhir = hitung_ongkir_akhir(berat, jarak, anggota)
        total_pendapatan += ongkir_akhir
        
        print(f"Pesanan #{idx}")
        print(f"Nama Pelanggan  : {nama}")
        print(f"Biaya Berat     : Rp {b_berat:,.0f}")
        print(f"Biaya Jarak     : Rp {b_jarak:,.0f}")
        print(f"Potongan        : Rp {potongan:,.0f}")
        print(f"Ongkir Akhir    : Rp {ongkir_akhir:,.0f}")
        print("-" * 55)
        
    print(f"TOTAL PENDAPATAN HARI INI : Rp {total_pendapatan:,.0f}")
    print("=" * 55)


def main():
    "Alur utama program cetak struk pengiriman toko daring."
    pesanan_hari_ini = [
        {"nama": "Rina", "berat": 1, "jarak": 10, "anggota": "Bukan"},
        {"nama": "Sari", "berat": 5, "jarak": 25, "anggota": "Bukan"},
        {"nama": "Tono", "berat": 5, "jarak": 25, "anggota": "Ya"},
        {"nama": "Umar", "berat": 2, "jarak": 30, "anggota": "Ya"},
        {"nama": "Vina", "berat": 8, "jarak": 15, "anggota": "Bukan"}
    ]
    
    cetak_semua_struk(pesanan_hari_ini)


if __name__ == "__main__":
    main()