import streamlit as st
import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Live PDF Editor", layout="wide")
st.title("✏️ Live PDF Editor")

# File upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    st.write(f"### {len(pdf_doc)} pages detected")
    
    # Select page
    page_num = st.number_input("Select Page", min_value=1, max_value=len(pdf_doc), value=1) - 1
    page = pdf_doc[page_num]
    
    # Convert PDF page to image for display
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Extract text blocks
    text_blocks = page.get_text("blocks")
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    # Store edited text positions
    text_positions = {}
    
    for i, block in enumerate(text_blocks):
        x, y, w, h, text, *_ = block
        draw.rectangle([x, y, x + w, y + h], outline="red", width=2)
        text_positions[i] = (x, y)
    
    # Display the PDF page image with highlighted text areas
    st.image(img, caption="Click on text to edit")
    
    # Editable text input
    edited_text = {}
    for i, block in enumerate(text_blocks):
        edited_text[i] = st.text_input(f"Edit Text {i+1}", block[4])
    
    # Button to update PDF
    if st.button("Save Changes"):
        for i, block in enumerate(text_blocks):
            x, y = text_positions[i]
            page.insert_text((x, y), edited_text[i], fontsize=12, color=(0, 0, 0))
        
        # Save modified PDF
        pdf_bytes = io.BytesIO()
        pdf_doc.save(pdf_bytes)
        pdf_bytes.seek(0)
        
        st.download_button("Download Edited PDF", pdf_bytes, file_name="edited.pdf", mime="application/pdf")
else:
    st.info("Upload a file to get started")
