import streamlit as str

# 1. Inisialisasi status login jika belum ada
if "logged_in" not in str.session_state:
    str.session_state.logged_in = False
    str.session_state.is_developer = False

# 2. Fungsi untuk memeriksa proses login
def cek_login(username, password):
    # Mengambil password aman dari Streamlit Secrets
    admin_password = str.secrets.get("DEVELOPER_PASSWORD", "rahasia123")
    
    if username == "admin" and password == admin_password:
        str.session_state.logged_in = True
        str.session_state.is_developer = True
        str.success("Selamat datang kembali, Developer! 🛠️")
        str.rerun()
    elif username == "user" and password == "ditzyy":
        str.session_state.logged_in = True
        str.session_state.is_developer = False
        str.success("Selamat datang di Ditzyy AI! ✨")
        str.rerun()
    else:
        str.error("Username atau Password salah! ❌")

# 3. Tampilan Halaman Login (Hanya muncul jika belum login)
if not str.session_state.logged_in:
    str.subheader("🔑 Silakan Masuk Terlebih Dahulu")
    
    input_user = str.text_input("Username:")
    input_pass = str.text_input("Password:", type="password")
    
    if str.button("Masuk"):
        cek_login(input_user, input_pass)
        
    str.stop() # Menghentikan sisa kode di bawahnya agar tidak muncul sebelum login

# --- KODE UTAMA DITZYY AI KAMU DIMULAI DI SINI ---
# Di bawah sini kamu bisa memasukkan logika chat yang sudah kita buat sebelumnya.

import streamlit as str

# ⚙️ 1. Konfigurasi Halaman Utama
str.set_page_config(
    page_title="Ditzyy AI v2.0",
    page_icon="logo.png",  # Memakai logo gambar kustom kamu
    layout="centered"
)

# 🔑 2. Inisialisasi Status Login di Latar Belakang
if "logged_in" not in str.session_state:
    str.session_state.logged_in = False
    str.session_state.is_developer = False

# 🔐 3. Fungsi Pemeriksaan Akun
def cek_login(username, password):
    # Mengambil password admin aman dari Streamlit Secrets, jika belum ada defaultnya 'admin123'
    admin_password = str.secrets.get("DEVELOPER_PASSWORD", "admin123")
    
    if username == "admin" and password == admin_password:
        str.session_state.logged_in = True
        str.session_state.is_developer = True
        str.success("Selamat datang kembali, Master Developer! 🛠️")
        str.rerun()
    elif username == "user" and password == "ditzyy":
        str.session_state.logged_in = True
        str.session_state.is_developer = False
        str.success("Selamat datang di Ditzyy AI! ✨")
        str.rerun()
    else:
        str.error("Username atau Password salah! ❌")

# 🖥️ 4. Tampilan Halaman Login (Hanya muncul jika belum login)
if not str.session_state.logged_in:
    str.title("🔮 Ditzyy AI Gerbang Masuk")
    str.subheader("Silakan masuk dengan akun kamu")
    
    input_user = str.text_input("Username 🧑‍💻")
    input_pass = str.text_input("Password 🔑", type="password")
    
    if str.button("Masuk"):
        cek_login(input_user, input_pass)
        
    str.stop() # Menghentikan kode di bawah agar tidak bocor sebelum login

# --- 🚀 KODE UTAMA APLIKASI SELEPAS LOGIN ---

# Contoh membedakan fitur berdasarkan status pengembang
if str.session_state.is_developer:
    str.sidebar.title("🛠️ Panel Developer")
    str.sidebar.info("Kamu masuk sebagai Pengembang. Akses sistem penuh diaktifkan.")
    # Kamu bisa menambahkan tombol khusus developer di sini nanti!
else:
    str.sidebar.title("✨ Menu Pengguna")
    str.sidebar.info("Kamu masuk sebagai Pengguna Biasa.")

# 🔮 Tampilan Chat Utama Ditzyy AI kamu
str.title("🔮 Ditzyy AI v2.0")
str.write("Asisten Pintar & Catatan Portabel Anda — Murni Menggunakan Python")

# Kotak chat pembuka
with str.chat_message("assistant", avatar="logo.png"):
    str.write("Halo! Saya Ditzyy AI. Ada yang bisa saya bantu hari ini? ✨")

# (Logika percakapan/chat dengan Gemini API kamu bisa dilanjutkan di bawah sini)
