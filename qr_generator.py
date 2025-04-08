import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.title("🔲 QR Code Generator")

text_input = st.text_input("Enter text or URL:")

if st.button("Generate QR Code") and text_input:
    qr = qrcode.make(text_input)
    buf = BytesIO()
    qr.save(buf)
    st.image(qr)
    st.download_button(
        label="Download QR Code",
        data=buf.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )
