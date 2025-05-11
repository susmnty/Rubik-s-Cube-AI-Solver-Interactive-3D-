import streamlit as st
import streamlit.components.v1 as components

# Page title
st.title("🧠 Rubik's Cube AI Solver (Interactive)")

# Load HTML
with open("rubik_cube_3d.html", "r", encoding="utf-8") as file:
    html_code = file.read()

st.subheader("🧊 Interactive 3D Cube")
components.html(html_code, height=600)

# Manual control (for now)
st.subheader("👉 Test Rotation")
move = st.selectbox("Select Move", ["None", "Front Clockwise", "Right Clockwise", "Top Clockwise"])

if st.button("Rotate"):
    js_code = f"<script>rotateFace('{move}');</script>"
    components.html(html_code + js_code, height=600)