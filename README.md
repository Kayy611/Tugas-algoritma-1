# Tugas-algoritma-1
tugas1 algoritma dan pemograman


SOAL 1
TABEL FUNGSI SOAL 1


| Nama Fungsi | Parameter | Mengembalikan Nilai (Ya/Tidak) | Tugas yang Dikerjakan |
| nilai_akhir | tugas, uts, uas | Ya (Non-void) | hasil kalkulasi nilai akhir berdasarkan bobot tugas 30%, UTS 30%, dan UAS 40%)
| nilai_huruf | nilai_akhir | Ya (Non-void) | Mengonversi angka nilai akhir menjadi predikat nilai huruf (A, B, C, D, E)
| keterangan_lulus | nilai_huruf | Ya (Non-void) | Status kelulusan mahasiswa berdasarkan nilai huruf (minimal huruf C)
| tampilkan_rekap | data_mahasiswa | Tidak (Void) | Tabel rekapitulasi nilai, rata-rata nilai kelas, dan jumlah total mahasiswa yang lulus


PERHIYUNGAN MANUAL
1.Aryy (Tugas: 80, UTS: 70, UAS: 90)  
​Nilai Akhir: (80 x 0.30) + (70 x 0.30) + (90 x 0.40) = 24 + 21 + 36 = 81.00
​Nilai Huruf: Karena 81 berada pada rentang 70 < 85, maka nilai hurufnya adalah B.  
​Hasil Verifikasi: Keluaran program menghasilkan Nilai Akhir 81.00 dengan Nilai Huruf B (Sesuai).
​2.Guna (Tugas: 75, UTS: 80, UAS: 65)  
​Nilai Akhir: (75 x 0.30) + (80 x 0.30) + (65 x 0.40) = 22.5 + 24 + 26 = 72.50
​Nilai Huruf: Karena 72.5 berada pada rentang 70 < 85, maka nilai hurufnya adalah B.  
​Hasil Verifikasi: Keluaran program menghasilkan Nilai Akhir 72.50 dengan Nilai Huruf B (Sesuai).


TAMBAHAN FITUR
1.menambahkan fungsi non void baru contoh cari_mahasiswa_tertinggi(data mahasiswa) untuk membandingkan nilai akhir dan mengembalikan data mahasiswa dengan maksimal


FUNGSI YNG TIDAK PERLU DISENTUH
nilai_akhir , nilai_huruf , dan keterangan_lulus karena fungsi ini sudah mengerjakan satu tugas spesifik dan dappat digunakan kembali secara langsung di dalam fungsi pencari nilai tertinggi tanpa mengubah logikanya.



SOAL 2
TABEL FUNGSI SOAL 2


| Nama Fungsi | Parameter | Mengembalikan Nilai (Ya/Tidak) | Tugas yang Dikerjakan |
| hitung_biaya_berat | berat | Ya (Non-void) | Menghitung besaran biaya berdasarkan berat paket (Rp10.000 untuk <= 2 kg, penambahan Rp4.000/kg berikutnya)
| hitung_biaya_jarak | jarak | Ya (Non-void) | Menentukan tambahan biaya jarak (Rp0 jika <= 20 km, Rp5.000 jika > 20 km)
| hitung_ongkir_akhir | berat, jarak, status_anggota | Ya (Non-void) | Menghitung subtotal ongkir, mengecek potongan diskon anggota 10%, dan mengembalikan rincian biaya secara lengkap
| cetak_semua_struk | daftar_pesanan | Tidak (Void) | Mencetak format struk belanja per pelanggan serta mengakumulasi total pendapatan harian toko


PERHITUNGAN MANUAL
Perhitungan Manual Ongkir Akhir
​Sari(berat:5kg, jarak:25km,anggota:bukan)
Biaya berat:10.000 + (5 - 2) x 4.000 = 10.000
Biaya jarak: 25 > 20,biayanya rp.5000
subtotal:22.000 + 5.000 = 27.000(tidak ada potongan karena bukan anggota)
ongkir akhir:rp 27.000 (program menghasilkan yang sama)
Tono (berat:5kg,jarak:25km,anggota:ya)
biaya berat:rp.22.000 , biaya jarak:rp.5.000
subtotal:22.000 + 5.000 = 27.000
potongan anggota(10%) 0.10 x 27.000 = 2.700
ongkir akhir:27.000 - 2.700 = rp.24.300
(program menghasilkan angka yang sama)
Umar (berat:2kg,jarak:30km,anggota:ya)
biaya berat:2kg = rp10.000
biaya jarak: 30>20 =rp 5.000
subtotal:10.000 + 5.000 = 15.000
ongkir akhir:15.000 - 1.500 =rp 13.500(program terbukti berhasil)


BAGIAN KODE YANG HARUS DIUBAH
jika toko mengubah batas jarak menjadi 15km dan biaya tambahan jarak menjadi rp 7.000:
hitung_biaya_jarak(jarak)
def hhitung_biaya_jarak(jarak):
   if jarak <=15: (diubah dari 20 menjadi 15)
   return 0
   else:
        return 7000 (diubah dari 5000 ke 7000)
Karena kode telah dikelompokkan secara modular kek dalam fungsi tersendiri,saya hanya perlu mengubah 1 fungsi aja tanpa menyentuh program main atau inti,ini membuktikan pemisahan tugas membuat kode jauh lebih mudah di ubah.
