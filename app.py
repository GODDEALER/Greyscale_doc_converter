import streamlit as st
import numpy as np
from PIL import Image
from fpdf import FPDF
import io
from ui import set_custom_page_config, render_header, render_sidebar

# ------------------ PAGE CONFIG & HEADER ------------------
set_custom_page_config()
render_header()

# ------------------ SIDEBAR CHOICE ------------------
choice = render_sidebar()  # "Convert to Grayscale Image" or "Convert to Grayscale PDF"

# ------------------ IMAGE UPLOAD ------------------
uploaded_file = st.file_uploader("Upload an Image (JPG, PNG, JPEG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    img = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(img)

    # Convert to grayscale
    gray = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])
    gray_img = Image.fromarray(gray.astype(np.uint8))

    # Display preview
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, caption="Original Image", use_container_width=True)
    with col2:
        st.image(gray_img, caption="Grayscale Preview", use_container_width=True)

    # ------------------ LOGIC: GRAYSCALE IMAGE ------------------
    if choice == "🖼️ Convert to Grayscale Image":
        buf = io.BytesIO()
        gray_img.save(buf, format="PNG")
        buf.seek(0)  # Reset pointer

        st.download_button(
            label="📥 Download Grayscale Image",
            data=buf.read(),  # Use read() for reliability
            file_name="grayscale_image.png",
            mime="image/png"
        )

    # ------------------ LOGIC: GRAYSCALE IMAGE TO PDF ------------------
    elif choice == "📄 Convert to Grayscale PDF":
        pdf = FPDF()
        pdf.add_page()

        # Save grayscale image temporarily in memory
        img_buffer = io.BytesIO()
        gray_img.save(img_buffer, format="PNG")
        img_buffer.seek(0)

        # Resize to fit A4 width
        pdf.image(img_buffer, x=10, y=10, w=190)

        pdf_output = io.BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)

        st.download_button(
            label="📄 Download Grayscale PDF",
            data=pdf_output.read(),  # Use read() after seek(0)
            file_name="grayscale_document.pdf",
            mime="application/pdf"
        )

else:
    st.info("Please upload an image file to start.")

st.markdown("---")
st.caption("© 2025 DECODER | Built with ❤️ using Python & Streamlit")
