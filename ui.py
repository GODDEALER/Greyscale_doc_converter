import streamlit as st

def set_custom_page_config():
    st.set_page_config(
        page_title="Official Grayscale Converter",
        page_icon="🖨️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def render_header():
    st.markdown("""
        <div style='text-align:center; background-color:#003366; padding:15px; border-radius:10px;'>
            <h1 style='color:white;'>📄 Official Image Grayscale & PDF Converter</h1>
            <p style='color:#dfe6e9;'>
                Convert colourful images into grayscale format or grayscale PDF — ideal for official documentation, printing, and online form submissions.
            </p>
        </div>
        """, unsafe_allow_html=True)

def render_sidebar():
    # Sidebar section title
    st.sidebar.markdown("## ⚙️ Conversion Options")
    st.sidebar.info("Select how you want to convert your uploaded image.")

    # User can choose between grayscale image or grayscale PDF
    choice = st.sidebar.radio(
        "Choose conversion type:",
        ("🖼️ Convert to Grayscale Image", "📄 Convert to Grayscale PDF")
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("#### ℹ️ About This Tool")
    st.sidebar.markdown("""
        - Developed by **Decoder**
        - Built with **Streamlit + NumPy + Pillow + FPDF**
        - Converts your image for **official, document-ready use**
    """)

    return choice
