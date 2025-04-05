import streamlit as st
from streamlit.components.v1 import html
import time

# Setting halaman
st.set_page_config(page_title="🎰 Gacha Waifu", page_icon="💘")

# Judul
st.title("🎰 Gacha Waifu Generator")

# Input nama user
nama = st.text_input("Masukkan namamu dulu ya:")

# Tombol gacha
if st.button("Gacha Sekarang!"):
    if nama:
        with st.spinner("Menggacha waifu terbaik untukmu..."):
            time.sleep(3)  # Delay deg-degan

        st.success(f"{nama}, waifumu hari ini adalah... 💖")

        time.sleep(1.5)  # Biar lebih dramatis sebelum muncul iframe

        # Link Rickroll autoplay
        video_url = "https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&mute=0&rel=0"

        # Tampilkan video autoplay pakai HTML iframe
        html(f"""
        <iframe width="800" height="450"
        src="{video_url}"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen></iframe>
        """, height=470)

        st.caption("🎶 *Never gonna give you up...*")
    else:
        st.warning("Masukkan nama dulu dong~")