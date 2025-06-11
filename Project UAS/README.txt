# BFS Algorithm Visualizer (Streamlit App)

## 👨‍💻 Author:
- Muhammad Fadhli (140810230056)
- Hafizh Fadhl Muhammad (140810230070)
- Farhan Zia Rizky (140810230074)

---

## 📦 Struktur Folder
```
📁 bfs_visualizer/
├── app.py
├── bfs_path.txt        # (akan dihasilkan saat menyimpan jalur)
├── README.txt          # (panduan penggunaan)
```

---

## 🚀 Cara Menjalankan Aplikasi (Local)
1. Pastikan Python 3.x sudah terinstall di perangkatmu.
2. Install library yang dibutuhkan:
   ```bash
   pip install streamlit matplotlib networkx
   ```
3. Jalankan aplikasi dengan perintah:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment Online (Streamlit Cloud)
1. Buat akun gratis di [https://streamlit.io/](https://streamlit.io/)
2. Push project ini ke GitHub (berisi `app.py`, `README.txt`)
3. Hubungkan repository GitHub ke Streamlit Cloud
4. Deploy dan akses aplikasi melalui link Streamlit

---

## 🧠 Fitur Aplikasi
- Input graf format `A-B, B-C`
- Visualisasi interaktif jalur BFS
- Statistik simpul dan edge
- Navigasi langkah BFS (First, Prev, Next, Last)
- Simpan hasil jalur ke file
- Tampilan UI modern (tema gelap + kontrol sidebar)

---

## ✅ Output
- Jalur terpendek (jika target ditemukan)
- File `bfs_path.txt` berisi jalur yang ditelusuri BFS

---

Terima kasih telah menggunakan aplikasi ini!