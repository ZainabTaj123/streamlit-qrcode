import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.title("🔲 QR Code Generator")

text_input = st.text_input("Enter text or URL:")

if st.button("Generate QR Code") and text_input:
    # Generate QR code
    qr_img = qrcode.make(text_input)

    # Save QR code to a BytesIO buffer
    buf = BytesIO()
    qr_img.save(buf, format="PNG")
    buf.seek(0)

    # Display the QR code image
    st.image(buf, caption="Your QR Code")

    # Download button
    st.download_button(
        label="Download QR Code",
        data=buf.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )

