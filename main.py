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
