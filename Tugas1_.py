
def nilai_akhir(tugas, uts, uas):
    "Nilai akhir berdasarkan bobot tugas (30%), UTS (30%), dan UAS (40%)."
    return (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)


def nilai_huruf(nilai_akhir):
    "Nilai huruf berdasarkan rentang nilai akhir yang diperoleh."
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 10:
        return "D"
    else:
        return "E"


def keterangan_lulus(nilai_huruf):
    "Status kelulusan mahasiswa berdasarkan syarat minimal nilai huruf C."
    if nilai_huruf in ["A", "B", "C"]:
        return 'Lulus'
    else:
        return 'Tidak Lulus'


def tampilkan_rekap(data_mahasiswa):
    "Tabel rekapitulasi nilai, rata-rata nilai akhir kelas, dan jumlah mahasiswa lulus."
    print("=" * 65)
    print(f"{"Nama":<10} | {"Nilai Akhir":<11} | {"Nilai Huruf":<11} | {"Keterangan":<12}")
    print("=" * 65)
    
    total_nilai_akhir = 0
    jumlah_lulus = 0
    jumlah_mahasiswa = len(data_mahasiswa)
    
    for mhs in data_mahasiswa:
        nama = mhs['nama']
        na = nilai_akhir(mhs['tugas'], mhs['uts'], mhs['uas'])
        nh = nilai_huruf(na)
        ket = keterangan_lulus(nh)
        
        total_nilai_akhir += na
        if ket == 'Lulus':
            jumlah_lulus += 1
            
        print(f"{nama:<10} | {na:<11.2f} | {nh:<11} | {ket:<12}")
        
    print("=" * 65)
    rata_rata_kelas = total_nilai_akhir / jumlah_mahasiswa if jumlah_mahasiswa > 0 else 0
    print(f"Rata-rata Nilai Akhir Kelas : {rata_rata_kelas:.2f}")
    print(f"Banyaknya Mahasiswa Lulus    : {jumlah_lulus} dari {jumlah_mahasiswa} mahasiswa")
    print("=" * 65)


def main():
    "Alur utama program rekapitulasi nilai mahasiswa."
    daftar_mahasiswa = [
        {"nama": "Aryy", "tugas": 80, "uts": 70, "uas": 90},
        {"nama": "Ayu", "tugas": 90, "uts": 85, "uas": 88},
        {"nama": "Pande", "tugas": 60, "uts": 45, "uas": 50},
        {"nama": "Guna", "tugas": 75, "uts": 80, "uas": 65},
        {"nama": "Putu", "tugas": 30, "uts": 40, "uas": 35}
    ]
    
    tampilkan_rekap(daftar_mahasiswa)


if __name__ == "__main__":
    main()