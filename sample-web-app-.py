import streamlit as st
import streamlit.components.v1 as components

# HTML, CSS, and JavaScript code
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
            overflow: hidden;
            transition: background-image 0.5s;
        }
        .heart-button {
            position: relative;
            width: 100px;
            height: 100px;
            background-color: #ff6f91;
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
            width: 100px;
            height: 100px;
            background-color: #ff6f91;
            border-radius: 50%;
            top: -50px;
            left: 0;
        }
        .heart-button::after {
            left: 50px;
            top: 0;
        }
        .heart-button span {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(45deg);
            font-size: 14px;
            color: white;
            font-weight: bold;
        }
        .heart-button:active {
            transform: rotate(-45deg) scale(0.95);
        }
        .falling-heart {
            position: absolute;
            width: 50px;
            height: 50px;
            background-color: #ff6f91;
            transform: rotate(-45deg);
            opacity: 0;
            animation: fall 2s forwards;
        }
        .falling-heart::before,
        .falling-heart::after {
            content: '';
            position: absolute;
            width: 50px;
            height: 50px;
            background-color: #ff6f91;
            border-radius: 50%;
            top: -25px;
            left: 0;
        }
        .falling-heart::after {
            left: 25px;
            top: 0;
        }
        @keyframes fall {
            0% {
                opacity: 1;
                top: 0;
            }
            100% {
                opacity: 0;
                top: 100vh;
            }
        }
        .hidden {
            display: none;
        }
        .background-image {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://example.com/purple_hearts_roses.jpg');
            background-size: cover;
            background-position: center;
            opacity: 0;
            transition: opacity 0.5s;
            z-index: -1;
        }
        .background-image.visible {
            opacity: 1;
        }
    </style>
</head>
<body>
    <div class="background-image" id="backgroundImage"></div>
    <button class="heart-button" id="heartButton" onclick="shedHearts()">
        <span>I'm sorry</span>
    </button>
    <button class="heart-button hidden" id="forgiveButton" onclick="showBackground()">
        <span>I'm sorry, will you forgive me?</span>
    </button>
    <script>
        function shedHearts() {
            const heartButton = document.getElementById('heartButton');
            heartButton.classList.add('hidden');
            createFallingHeart(-100);
            createFallingHeart(100);
            setTimeout(() => {
                document.getElementById('forgiveButton').classList.remove('hidden');
            }, 2000);
        }
        function createFallingHeart(offsetX) {
            const heart = document.createElement('div');
            heart.className = 'falling-heart';
            heart.style.left = `calc(50% + ${offsetX}px)`;
            document.body.appendChild(heart);
            setTimeout(() => {
                heart.remove();
            }, 2000);
        }
        function showBackground() {
            document.getElementById('backgroundImage').classList.add('visible');
        }
    </script>
</body>
</html>
"""

# Embed the HTML into the Streamlit app
components.html(html_code, height=600)