# Prototipe Sistem Informasi Departemen Teknik JDC (Streamlit)

Aplikasi ini menampilkan prototipe sistem informasi Departemen Teknik JDC
melalui Streamlit, sehingga dapat diakses pihak lain lewat tautan publik.

## Isi folder

| File | Fungsi |
|---|---|
| `app.py` | Aplikasi Streamlit yang menampilkan prototipe secara penuh layar |
| `prototipe.html` | File prototipe asli (semua tampilan, data contoh, dan interaksi) |
| `requirements.txt` | Daftar paket Python yang dibutuhkan |
| `.streamlit/config.toml` | Pengaturan tema dan tampilan Streamlit |

## Menjalankan di komputer sendiri

```bash
pip install -r requirements.txt
streamlit run app.py
```

Buka http://localhost:8501 di browser.

## Deploy ke Streamlit Community Cloud (gratis)

1. Buat akun di https://github.com, lalu buat repository baru,
   misalnya `prototipe-si-teknik-jdc` (pilih **Public**).
2. Unggah seluruh isi folder ini ke repository tersebut
   (**Add file → Upload files**). Pastikan folder `.streamlit` ikut terunggah.
3. Masuk ke https://share.streamlit.io menggunakan akun GitHub.
4. Klik **Create app → Deploy a public app from GitHub**, lalu isi:
   - Repository: `username/prototipe-si-teknik-jdc`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: misalnya `si-teknik-jdc` (opsional)
5. Klik **Deploy**. Setelah beberapa menit, aplikasi dapat diakses di
   tautan seperti `https://si-teknik-jdc.streamlit.app` dan bisa dibagikan.

## Memperbarui prototipe

Ganti file `prototipe.html` di repository GitHub dengan versi terbaru
(nama file harus tetap `prototipe.html`). Streamlit Cloud akan memperbarui
aplikasi secara otomatis.

## Catatan

- Data pada prototipe adalah data contoh. Perubahan yang dilakukan pengguna
  (misalnya input laporan atau approval) hanya tersimpan sementara dan
  kembali ke kondisi awal saat halaman dimuat ulang.
- Aplikasi di Streamlit Community Cloud akan "tidur" jika tidak dibuka
  beberapa hari. Pengunjung cukup menekan tombol **Yes, get this app back up**
  dan menunggu sekitar satu menit.
- Kredensial demo setiap peran tersedia di halaman login (tombol
  **Isi Otomatis**).
