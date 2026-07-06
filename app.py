import streamlit as str
import google.generativeai as genai

# Konfigurasi Tema & Tampilan Halaman Streamlit
str.set_page_config(
    page_title="Ditzyy AI v2.0",
    page_icon="🔮",
    layout="centered"
)

# Judul Aplikasi
str.title("🔮 Ditzyy AI v2.0")
str.caption("Asisten Pintar & Catatan Portabel Anda — Murni Menggunakan Python")

# Mengambil API Key secara aman dari Streamlit Secrets atau Sidebar
if "GEMINI_API_KEY" in str.secrets:
    api_key = str.secrets["GEMINI_API_KEY"]
else:
    api_key = str.sidebar.text_input("Masukkan Gemini API Key Anda:", type="password")

# Validasi API Key
if not api_key:
    str.warning("Silakan masukkan Gemini API Key Anda di bagian Sidebar atau Streamlit Secrets untuk memulai!")
    str.stop()

# Hubungkan ke Google Gemini API
genai.configure(api_key=api_key)

# Menggunakan model versi terbaru (Stabil & Bebas Error 404)
# Perbaikan utama dari error sebelumnya yang menggunakan '-latest'
model = genai.GenerativeModel('gemini-2.5-flash')

# Inisialisasi Riwayat Obrolan agar tidak hilang saat refresh
if "messages" not in str.session_state:
    str.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya Ditzyy AI. Ada yang bisa saya bantu hari ini? ✨"}
    ]

# Tampilkan riwayat obrolan di layar
for msg in str.session_state.messages:
    with str.chat_message(msg["role"]):
        str.markdown(msg["content"])

# Input Teks dari Pengguna
if user_prompt := str.chat_input("Ketik pertanyaan Anda di sini..."):
    # Tampilkan chat pengguna
    with str.chat_message("user"):
        str.markdown(user_prompt)
    
    # Simpan ke riwayat
    str.session_state.messages.append({"role": "user", "content": user_prompt})

    # Kirim ke AI dan dapatkan respons
    with str.chat_message("assistant"):
        try:
            # Memberikan instruksi sifat/karakter sistem secara langsung dalam prompt
            system_instruction = "Kamu adalah Ditzyy AI, asisten yang cerdas, ramah, dan asyik diajak mengobrol. "
            full_prompt = f"{system_instruction}\n\nUser: {user_prompt}"
            
            response = model.generate_content(full_prompt)
            ai_reply = response.text
            
            str.markdown(ai_reply)
            str.session_state.messages.append({"role": "assistant", "content": ai_reply})
            
        except Exception as e:
            str.error(f"Terjadi kesalahan koneksi API: {e}")
