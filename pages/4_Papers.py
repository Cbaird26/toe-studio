import base64
from pathlib import Path
import streamlit as st

st.title("ToE Papers")

pdf_path = Path(__file__).resolve().parents[2] / "ToE" / "Complete_Theory_of_Everything_Paper.pdf"
if pdf_path.exists():
    st.write("Open or download your paper:")
    with open(pdf_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    href = f'<a href="data:application/pdf;base64,{b64}" download="ToE_Paper.pdf">Download PDF</a>'
    st.markdown(href, unsafe_allow_html=True)
    st.write("Preview:")
    st.components.v1.html(f"""
        <iframe src="data:application/pdf;base64,{b64}" width="100%" height="800px" type="application/pdf"></iframe>
    """, height=820)
else:
    st.info("Paper not found at ToE/Complete_Theory_of_Everything_Paper.pdf") 