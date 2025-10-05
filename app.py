import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Page configuration
st.set_page_config(
    page_title="Happy Birthday My Love!",
    page_icon="🎂",
    layout="centered"  # Changed to centered layout
)

# Load Lottie animation from URL
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Custom CSS for animations + centered everything
st.markdown("""
<style>
    .main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    @keyframes gentleWave {
        0%, 100% { 
            transform: translateY(0px) rotate(-1deg) scale(1); 
        }
        25% { 
            transform: translateY(-3px) rotate(0.5deg) scale(1.02); 
        }
        50% { 
            transform: translateY(2px) rotate(-0.5deg) scale(1.01); 
        }
        75% { 
            transform: translateY(-2px) rotate(0.3deg) scale(1.015); 
        }
    }

    .birthday-title {
        font-size: 4.2rem;
        background: linear-gradient(45deg, #FF6B6B, #E1306C, #FD1D1D, #F77737, #FCAF45);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeIn 1.2s ease-out, pulse 2.5s infinite, gentleWave 4s ease-in-out infinite;
        text-align: center;
        margin: 2rem auto;
        font-family: 'Brush Script MT', cursive;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.15);
        display: block;
        width: 100%;
    }
    .heart {
        color: #FF6B6B;
        animation: float 3s ease-in-out infinite;
        display: inline-block;
        margin: 0 10px;
    }

    /* Center everything */
    .centered-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        text-align: center;
    }

    /* Big centered surprise button styling */
    .stButton > button {
        font-size: 1.9rem !important;
        padding: 18px 42px !important;
        border-radius: 14px !important;
        background: linear-gradient(90deg,#ff8ab8,#ffd86b) !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 8px 30px rgba(0,0,0,0.18) !important;
        transition: transform 0.12s ease-in-out !important;
        margin: 20px auto !important;
        display: block !important;
    }
    .stButton > button:active {
        transform: translateY(2px) scale(0.995) !important;
    }

    /* Card flip animation */
    .card-wrap { 
        display: flex !important; 
        justify-content: center !important; 
        margin: 2rem auto !important;
    }
    .card {
        width: 380px;
        height: 220px;
        perspective: 1200px;
    }
    .card-inner {
        width:100%; height:100%; position:relative; transform-style: preserve-3d;
        transition: transform 0.9s cubic-bezier(.2,.8,.2,1);
        animation: flip 0.9s forwards ease-out 0.6s;
    }
    @keyframes flip {
        from { transform: rotateY(0deg); }
        to { transform: rotateY(180deg); }
    }
    .card-side {
        position:absolute; width:100%; height:100%; left:0; top:0; border-radius:14px; display:flex; align-items:center; justify-content:center; backface-visibility:hidden; overflow:hidden;
    }
    .card-front {
        background: linear-gradient(135deg,#FF9AA2,#FFB7B2);
        color:#fff; font-size:1.6rem; font-weight:700;
    }
    .card-back {
        background: linear-gradient(135deg,#ffffff,#fff6e6);
        transform: rotateY(180deg);
        color:#333;
        flex-direction:column; text-align:center; padding:18px; 
    }
    .card-back h2 { margin:0; font-size:1.8rem; }
    .card-back p { margin-top:8px; font-size:1.05rem; }

    /* Center Lottie animations */
    .lottie-container {
        display: flex !important;
        justify-content: center !important;
        margin: 1rem auto !important;
    }
    
    /* footer hearts spacing */
    .footer-hearts { 
        text-align:center !important; 
        margin-top:50px !important;
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# Main content - Everything centered
st.markdown('<div class="centered-container">', unsafe_allow_html=True)

# Title
st.markdown('<h1 class="birthday-title">🎉 HAPPY BIRTHDAY BABY 💖</h1>', unsafe_allow_html=True)

# Rose animation - centered
st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
lottie_rose = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0nLkdf.json")
if lottie_rose:
    st_lottie(lottie_rose, speed=1, height=220, key="rose")
else:
    st.error("❌ Rose animation failed to load - but the website still works!")
    # Fallback rose emoji
    st.markdown("<h2 style='text-align: center;'>🌹</h2>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Card
st.markdown(
    """
    <div class="card-wrap">
      <div class="card">
        <div class="card-inner">
          <div class="card-side card-front">Tap to Open 💌</div>
          <div class="card-side card-back">
            <p>Hope you have a lovely day today, I wish i could spend your day with you thoda sa and take you out, but soon tho, youre so amazing,s amrt and pretty, and have a blast princess!!!</p>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Centered surprise button
if st.button("🎉 Click for Birthday Surprise!", key="surprise"):
    st.balloons()
    st.snow()
    # Confetti animation
    lottie_confetti = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_6cftgagt.json")
    if lottie_confetti:
        st_lottie(lottie_confetti, speed=1, height=200, key="confetti")

# Sparkles animation
lottie_sparkles = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_6m7kqzaf.json")
if lottie_sparkles:
    st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
    st_lottie(lottie_sparkles, speed=1, height=120, key="sparkles")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer with floating hearts
st.markdown("""
<div class="footer-hearts">
    <span class="heart">💖</span>
    <span class="heart" style="animation-delay: 0.5s">💖</span>
    <span class="heart" style="animation-delay: 1s">💖</span>
    <span class="heart" style="animation-delay: 1.5s">💖</span>
    <span class="heart" style="animation-delay: 2s">💖</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  