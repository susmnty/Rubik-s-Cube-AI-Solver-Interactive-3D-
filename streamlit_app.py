import streamlit as st
import streamlit.components.v1 as components

# Read moves from file
with open("moves.txt", "r") as f:
    moves = f.read()

# Send moves as query string or variable
html_path = "cube_visualizer/index.html"
components.html(open(html_path, 'r').read(), height=600, width=800)