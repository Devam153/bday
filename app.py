import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Page configuration
st.set_page_config(
    page_title="Happy Birthday My Love!",
    page_icon="🎂",
    layout="wide"
)

# Load Lottie animation from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Custom CSS for animations + bigger centered surprise button + card flip
st.markdown("""
<style>
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
        margin-bottom: 2rem;
        font-family: 'Brush Script MT', cursive;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.15);
        position: relative;
        display: inline-block;
        transform-origin: center;
    }
    .heart {
        color: #FF6B6B;
        animation: float 3s ease-in-out infinite;
        display: inline-block;
        margin: 0 10px;
    }
    .message {
        animation: fadeIn 1.6s ease-out;
        padding: 20px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(6px);
        margin: 20px 0;
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
    }
    .stButton > button:active {
        transform: translateY(2px) scale(0.995) !important;
    }
    .center-btn {
        display:flex; justify-content:center; margin-top:10px; margin-bottom:16px;
    }

    /* Card flip animation (opens automatically) */
    .card-wrap { display:flex; justify-content:center; }
    .card {
        width: 380px;
        height: 220px;
        perspective: 1200px;
        position: relative;
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
        flex-direction:column; text-align:center; padding:18px; box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    }
    .card-back h2 { margin:0; font-size:1.8rem; }
    .card-back p { margin-top:8px; font-size:1.05rem; }

    /* footer hearts spacing */
    .footer-hearts { text-align:center; margin-top:50px; }
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="birthday-title">🎉 Happy Birthday My Love! 💖</h1>', unsafe_allow_html=True)

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Load and display ROSE animation instead of rocket
    lottie_rose = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0nLkdf.json")
    lottie_confetti = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_6cftgagt.json")
    lottie_sparkles = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_6m7kqzaf.json")
    
    if lottie_rose:
        st_lottie(lottie_rose, speed=1, height=220, key="rose")

    # Sweet card that "opens" automatically revealing the message
    st.markdown(
        f"""
        <div class="card-wrap">
          <div class="card">
            <div class="card-inner">
              <div class="card-side card-front">Tap to Open 💌</div>
              <div class="card-side card-back">
                <h2>Happy Birthday, My Love!</h2>
                <p>May today be full of small moments that make you smile — just like you make me smile every day.</p>
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Centered big surprise button
    st.markdown('<div class="center-btn">', unsafe_allow_html=True)
    if st.button("🎉 Click for Birthday Surprise!", key="surprise"):
        st.balloons()
        st.snow()
        # an extra gentle confetti-like effect via Lottie when available
        if lottie_confetti:
            st_lottie(lottie_confetti, speed=1, height=220, key="confetti-popup")
    st.markdown('</div>', unsafe_allow_html=True)

    # sparkles Lottie after the button (optional)
    if lottie_sparkles:
        st_lottie(lottie_sparkles, speed=1, height=140, key="sparkles")

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