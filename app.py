import streamlit as st
import google.generativeai as genai
import os

# 1. Konfigurasi halaman utama Ditzyy AI
st.set_page_config(
    page_title="Ditzyy AI - Smart Platform",
    page_icon="🔮",
    layout="centered"
)

# 2. Judul utama murni menggunakan komponen teks Python
st.title("🔮 Ditzyy AI v2.0")
st.caption("Asisten Pintar & Catatan Portabel Anda — Murni Menggunakan Python")

# 3. Sistem File lokal untuk penyimpanan catatan permanen
NAMA_FILE_CATATAN = "catatan_ditzyy.txt"

def baca_catatan():
    if os.path.exists(NAMA_FILE_CATATAN):
        with open(NAMA_FILE_CATATAN, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def simpan_catatan(teks):
    with open(NAMA_FILE_CATATAN, "w", encoding="utf-8") as f:
        f.write(teks)

# 4. Pengaturan Menu dan API Key di Sidebar (Sisi Samping)
st.sidebar.header("⚙️ Pengaturan Aplikasi")
api_key = st.sidebar.text_input("Masukkan Gemini API Key:", type="password")

# Navigasi Menu dropdown bawaan Streamlit (Bukan HTML)
pilihan_menu = st.sidebar.selectbox("Pilih Fitur:", ["💬 AI Chatbot", "📝 Catatan Pintar", "ℹ️ Tentang Aplikasi"])

# 5. Logika Halaman Berdasarkan Menu yang Dipilih
if pilihan_menu == "💬 AI Chatbot":
    st.subheader("💬 Ngobrol dengan Ditzyy AI")
    
    if api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            # Membuat memori pesan agar tidak hilang saat halaman memuat ulang
            if "messages" not in st.session_state:
                st.session_state.messages = [
                    {"role": "assistant", "content": "Halo! Saya Ditzyy AI. Apa yang bisa saya bantu hari ini? ✨"}
                ]
                
            # Menampilkan riwayat obrolan di layar
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
                
            # Input teks dari pengguna
            if user_input := st.chat_input("Ketik pertanyaan Anda di sini..."):
                st.chat_message("user").write(user_input)
                st.session_state.messages.append({"role": "user", "content": user_input})
                
                # Proses respon pintar dari AI Google
                with st.chat_message("assistant"):
                    with st.spinner("Ditzyy AI sedang mengetik..."):
                        response = model.generate_content(user_input)
                        st.write(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                        
        except Exception as e:
            st.error(f"Terjadi kesalahan koneksi API: {e}")
    else:
        st.info("💡 Silakan masukkan **Gemini API Key** Anda di kolom sebelah kiri untuk mulai mengaktifkan fitur AI Chatbot.")

elif pilihan_menu == "📝 Catatan Pintar":
    st.subheader("📝 Ruang Catatan Permanen")
    catatan_sekarang = baca_catatan()
    
    # Kotak besar tempat mengetik memo/catatan
    isi_teks = st.text_area("Tulis ide, memo, atau daftar tugas Anda di bawah ini:", value=catatan_sekarang, height=250)
    
    # Tombol simpan murni Python
    if st.button("💾 Simpan Permanen", type="primary"):
        simpan_catatan(isi_teks)
        st.success("Catatan Anda berhasil disimpan secara aman di sistem!")

elif pilihan_menu == "ℹ️ Tentang Aplikasi":
    st.subheader("ℹ️ Mengenal Ditzyy AI")
    st.write("Aplikasi ini dibuat 100% menggunakan kode Python terintegrasi. Anda tidak perlu menyusun tabel, mengatur ukuran grid, atau pusing memikirkan kode CSS/HTML.")
    st.info("Sistem akan menyesuaikan secara otomatis (*responsive design*) sehingga tampilannya tetap proporsional baik dibuka lewat browser PC maupun Chrome di HP Anda.")
