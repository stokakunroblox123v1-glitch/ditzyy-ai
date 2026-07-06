import streamlit as str
import google.generativeai as genai

# Konfigurasi Tampilan Web
str.set_page_config(page_title="Ditzyy AI v2.0", page_icon="🔮", layout="centered")

# Judul Utama
str.title("🔮 Ditzyy AI v2.0")
str.caption("Asisten Pintar & Catatan Portabel Anda — Murni Menggunakan Python")

# Sidebar untuk Pengaturan API Key
with str.sidebar:
    str.header("⚙️ Pengaturan Aplikasi")
    api_key = str.text_input("Masukkan Kunci API Gemini:", type="password", help="Dapatkan API key gratis Anda di Google AI Studio")
    fitur = str.selectbox("Pilih Fitur:", ["Chatbot AI", "Catatan Portabel"])

# Cek apakah API Key sudah diisi
if not api_key:
    str.info("💡 Silakan masukkan Gemini API Key Anda di kolom sebelah kiri untuk mulai mengaktifkan fitur AI Chatbot.", icon="💡")
else:
    # Mengaktifkan Google Gemini AI dengan model terbaru yang stabil
    genai.configure(api_key=api_key)
    
    if fitur == "Chatbot AI":
        str.subheader("💬 Ngobrol dengan Ditzyy AI")
        
        # Simpan riwayat chat di memori halaman web
        if "messages" not in str.session_state:
            str.session_state.messages = [{"role": "assistant", "content": "Halo! Saya Ditzyy AI. Ada yang bisa saya bantu hari ini? ✨"}]
        
        # Tampilkan chat lama
        for msg in str.session_state.messages:
            with str.chat_message(msg["role"]):
                str.write(msg["content"])
        
        # Input chat baru dari user
        if user_input := str.chat_input("Ketik pertanyaan Anda di sini..."):
            str.session_state.messages.append({"role": "user", "content": user_input})
            with str.chat_message("user"):
                str.write(user_input)
                
            # Minta jawaban ke Google Gemini AI
            try:
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                response = model.generate_content(user_input)
                
                with str.chat_message("assistant"):
                    str.write(response.text)
                str.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                str.error(f"Terjadi kesalahan koneksi API: {e}")
                
    elif fitur == "Catatan Portabel":
        str.subheader("📝 Catatan Portabel Anda")
        str.write("Tulis apa pun di sini, catatan Anda akan tersimpan selama halaman ini tidak di-refresh.")
        
        if "catatan" not in str.session_state:
            str.session_state.catatan = ""
            
        isi_catatan = str.text_area("Tulis catatan Anda:", value=str.session_state.catatan, height=250)
        str.session_state.catatan = isi_catatan
        
        if str.button("Hapus Semua Catatan"):
            str.session_state.catatan = ""
            str.rerun()
          
