import streamlit as st

# Set page configuration (only once, at the top)
st.set_page_config(
    page_title="Growth Mindset Project",
    page_icon="🌟",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .title {
            color: #ff4b4b;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #444;
        }
        .stButton > button {
            width: 100%;
            border-radius: 10px;
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            padding: 8px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #e63e3e;
        }
        .quote-box {
            background-color: #ffecec;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            color: #333;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="title">🚀 Growth Mindset Challenge</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Welcome to a journey of self-improvement, innovation, and success! 🌟</p>', unsafe_allow_html=True)

st.divider()

# Quote Section
st.markdown('<h3 style="text-align:center;">🌱 Today’s Growth Mindset Quote 🌱</h3>', unsafe_allow_html=True)
st.markdown('<div class="quote-box">💡 "Success starts with a mindset—keep learning, keep growing, and never stop evolving!" 🚀🔥</div>', unsafe_allow_html=True)

st.divider()

# Challenge Section
st.markdown("<h3>🎯 What’s Your Challenge Today? 🎯</h3>", unsafe_allow_html=True)
user_input = st.text_input("Describe a Challenge:", placeholder="Write your challenge here...")

if user_input:
    st.success(f"🎯 You are facing: {user_input}. Keep pushing forward toward your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

st.divider()

# Reflection Section
st.markdown("<h3>📝 Reflection on Your Learning</h3>", unsafe_allow_html=True)
reflection = st.text_area("Write your reflection here:", placeholder="Reflect on what you learned today...")

if reflection:
    st.success(f"🌟 Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

st.divider()

# Achievements Section
st.markdown("<h3>🎉 Celebrate Your Wins! 🎉</h3>", unsafe_allow_html=True)
achievement = st.text_input("Share something you've recently accomplished:", placeholder="Write about your success...")

if achievement:
    st.success(f"🌟 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share now.")

st.divider()

# Footer Section
st.markdown("""
    <hr style="border:1px solid #ddd;">
    <p style="text-align:center; font-size:16px; color:#555;">💪 Every expert was once a beginner. Keep learning, keep pushing, and success will follow! 🚀✨</p>
    <p style="text-align:center; font-size:14px; color:#777;">©️ Created by Asadullah ✨</p>
""", unsafe_allow_html=True)
