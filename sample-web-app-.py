import streamlit as st
from streamlit.components.v1 import html

# Streamlit app configuration
st.set_page_config(page_title="Heart Button", layout="centered")

# HTML and CSS for the heart-shaped button and background
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
            transition: background-color 0.5s;
        }

        .heart-button {
            position: relative;
            width: 150px;
            height: 150px;
            background-color: #ff6f91;
            margin: 0;
            border: none;
            cursor: pointer;
            transform: rotate(-45deg);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s;
        }

        .heart-button::before,
        .heart-button::after {
            content: '';
            position: absolute;
            width: 150px;
            height: 150px;
            background-color: #ff6f91;
            border-radius: 50%;
            top: -75px;
            left: 0;
        }

        .heart-button::after {
            left: 75px;
            top: 0;
        }

        .heart-button span {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(45deg);
            font-size: 18px;
            color: white;
            font-weight: bold;
        }

        .heart-button:active {
            transform: rotate(-45deg) scale(0.95);
        }

        .background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #8a2be2, #dda0dd);
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.5s;
            z-index: -1;
        }

        .background.active {
            opacity: 1;
        }
    </style>
</head>
<body>
    <div class="background" id="background"></div>
    <button class="heart-button" onclick="activateBackground()">
        <span>I'm sorry</span>
    </button>

    <script>
        function activateBackground() {
            document.getElementById('background').classList.add('active');
        }
    </script>
</body>
</html>
"""

# Render the HTML and CSS in Streamlit
st.markdown("### Heart Button")
st.components.v1.html(html_code, height=600, scrolling=False)
