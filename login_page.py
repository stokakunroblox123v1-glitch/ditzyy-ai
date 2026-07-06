import streamlit as str

# ⚙️ 1. Inisialisasi Status Login (Berjalan di latar belakang)
if "sudah_login" not in str.session_state:
    str.session_state.sudah_login = False

# 🔐 2. Logika Pemeriksaan Password
def verifikasi_password(input_pass):
    # Kamu bisa mengganti password 'ditzyy123' di bawah ini sesuai keinginanmu
    if input_pass == "ditzyy123":
        str.session_state.sudah_login = True
        str.success("Akses diterima! Selamat datang. ✨")
        str.rerun()
    else:
        str.error("Password salah! Silakan coba lagi. ❌")

# 🖥️ 3. Tampilan Halaman Login
if not str.session_state.sudah_login:
    str.title("🔮 Ditzyy AI — Gerbang Masuk")
    str.write("Silakan masukkan password untuk mengakses aplikasi.")
    
    # Input password dengan tipe 'password' agar karakter tersembunyi (bintang-bintang)
    password_kamu = str.text_input("Kata Sandi / Password 🔑", type="password")
    
    if str.button("Masuk"):
        verifikasi_password(admin only)
        
    # Memastikan kode chat di bawah tidak berjalan sebelum login berhasil
    str.stop()

# --- 🚀 KODE UTAMA APLIKASI CHAT (Hanya muncul jika sudah login) ---

str.title("🔮 Ditzyy AI v2.0")
str.write("Selamat! Kamu berhasil masuk ke ruang kendali chat.")

with str.chat_message("assistant", avatar="logo.png"):
    str.write("Halo! Saya Ditzyy AI. Ruang obrolan aman sekarang aktif. Ada yang bisa saya bantu? ✨")
  
