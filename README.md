# UAS Komputer Grafik

## Identitas Mahasiswa
Nama  : Arif Rahmat Riski  
NIM   : 24146092  
Mata Kuliah : Komputer Grafik  

---

## Deskripsi Program
Program ini dibuat menggunakan bahasa pemrograman Python dengan bantuan library Pygame dan PyOpenGL.

Program menampilkan dua objek grafis yaitu kubus 3D dan persegi 2D pada satu layar. Kedua objek dapat dimanipulasi menggunakan keyboard dengan berbagai transformasi geometri.

Program dibuat untuk memenuhi tugas Ujian Akhir Semester mata kuliah Komputer Grafik.

---

## Penjelasan Program

Program menggunakan:
- Python sebagai bahasa pemrograman utama
- Pygame untuk membuat window dan membaca input keyboard
- PyOpenGL untuk menampilkan objek grafis 2D dan 3D

Pada program ini terdapat dua objek utama:

### 1. Kubus 3D
Kubus ditampilkan pada sisi kiri layar. Kubus dapat dilakukan beberapa transformasi yaitu:
- Translasi (pergeseran posisi)
- Rotasi (perputaran objek)
- Scaling (perubahan ukuran objek)

### 2. Persegi 2D
Persegi ditampilkan pada sisi kanan layar. Persegi dapat dilakukan transformasi yaitu:
- Translasi
- Rotasi
- Scaling
- Shearing (kemiringan objek)
- Refleksi (pencerminan objek)

---

## Kontrol Keyboard

### Kontrol Kubus 3D
W / S  : Geser atas / bawah  
A / D  : Geser kiri / kanan  
Q / E  : Geser maju / mundur  
I / K  : Rotasi sumbu X  
J / L  : Rotasi sumbu Y  
U / O  : Rotasi sumbu Z  
+ / -  : Perbesar / Perkecil ukuran  

---

### Kontrol Persegi 2D
Arrow Key : Geser posisi  
R / T : Rotasi  
Z / X : Perbesar / Perkecil ukuran  
H / Y : Shearing  
F : Refleksi sumbu X  
G : Refleksi sumbu Y  

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Install library yang dibutuhkan dengan perintah:

pip install pygame  
pip install PyOpenGL PyOpenGL_accelerate  

3. Jalankan program dengan perintah:

python uas_komputer_grafik.py  

---

## Output Program
Program akan menampilkan:
- Kubus 3D di sebelah kiri layar
- Persegi 2D di sebelah kanan layar

---

## Link Repository Github
(Tambahkan link Github di sini setelah upload)

---

## Kesimpulan
Program ini menunjukkan implementasi transformasi geometri pada objek 2D dan 3D menggunakan Python dan OpenGL secara interaktif melalui keyboard.
