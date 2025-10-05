# app.py
# Streamlit app: "Happy Birthday" surprise page
# Single-file app. Save as app.py and run with `streamlit run app.py`.

import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Happy Birthday 💖", layout="wide", initial_sidebar_state="collapsed")

# --- Sidebar (quick personalization) ---
st.sidebar.header("Personalize")
name = st.sidebar.text_input("Name", "My Love")
accent = st.sidebar.color_picker("Accent color", "#ff4da6")
personal = st.sidebar.text_area("Add a short personal message (optional)", f"Happy Birthday, {name}! You mean the world to me.")

# --- Main layout ---
st.markdown(
    f"""
    <style>
    /* page background */
    .stApp {{
      background: radial-gradient(circle at 10% 10%, {accent} 0%, #fff 40%);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    }}

    /* center container */
    .centered {{
      display:flex; align-items:center; justify-content:center; height:75vh; flex-direction:column;
      gap:10px; text-align:center;
    }}

    .title {{
      font-size:72px; font-weight:900; letter-spacing: -1px;
      background: linear-gradient(90deg, #fff, rgba(255,255,255,0.6));
      -webkit-background-clip: text; background-clip: text; color: transparent;
      filter: drop-shadow(0 6px 20px rgba(0,0,0,0.15));
      animation: float 3s ease-in-out infinite;
    }}

    .subtitle {{ font-size:28px; margin-top:6px; max-width:900px; color:#333; }}

    @keyframes float {
      0% { transform: translateY(0px); }
      50% { transform: translateY(-8px) rotate(-1deg); }
      100% { transform: translateY(0px); }
    }

    /* floating hearts */
    .hearts {{ position: absolute; left:0; top:0; width:100%; height:100%; pointer-events:none; overflow:hidden; }}
    .hearts i {{ position:absolute; font-style:normal; animation: rise 6s linear infinite; opacity:0.9; }}
    @keyframes rise {
      0% { transform: translateY(120vh) scale(0.6); }
      100% { transform: translateY(-40vh) scale(1); }
    }

    /* surprise button style inside the component */
    .surp { padding:12px 20px; border-radius:12px; font-weight:700; border:none; cursor:pointer; }
    </style>

    <div class="centered">
      <div class="title">Happy Birthday, {name} <span style="font-size:0.9em">🎉💖</span></div>
      <div class="subtitle">{personal}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Confetti + floating hearts + surprise button injected as HTML/JS ---
# This HTML includes a "Surprise" button that triggers confetti + a short chime.
confetti_and_hearts = f"""
<div id="wrap" style="position:relative; width:100%; height:220px;">
  <div class="hearts">
    <i style="left:4%; font-size:28px; animation-duration:7s;">💘</i>
    <i style="left:18%; font-size:34px; animation-duration:6s;">💖</i>
    <i style="left:32%; font-size:24px; animation-duration:8s;">💕</i>
    <i style="left:48%; font-size:30px; animation-duration:6.5s;">💞</i>
    <i style="left:66%; font-size:26px; animation-duration:7.5s;">💓</i>
    <i style="left:82%; font-size:36px; animation-duration:5.8s;">❤️</i>
  </div>
  <div style="display:flex; justify-content:center; align-items:center; height:220px;">
    <button id="surprise" class="surp" style="background:linear-gradient(90deg,{accent},#fff);">Click for a surprise ✨</button>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
const btn = document.getElementById('surprise');
btn.onclick = () => {
  // multiple bursts of confetti
  const duration = 2500;
  const end = Date.now() + duration;
  (function frame() {
    confetti({
      particleCount: 8,
      angle: 60,
      spread: 55,
      origin: { x: 0 }
    });
    confetti({
      particleCount: 8,
      angle: 120,
      spread: 55,
      origin: { x: 1 }
    });
    if (Date.now() < end) {
      requestAnimationFrame(frame);
    }
  }());

  // short chime using WebAudio
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.type = 'sine';
    o.frequency.setValueAtTime(880, ctx.currentTime);
    g.gain.setValueAtTime(0.0001, ctx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.2, ctx.currentTime + 0.01);
    o.connect(g); g.connect(ctx.destination);
    o.start();
    o.frequency.exponentialRampToValueAtTime(660, ctx.currentTime + 0.12);
    g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.8);
    setTimeout(()=>o.stop(), 900);
  } catch(e) { console.log('Audio blocked', e); }
};
</script>
"""

# Render the interactive HTML (height tuned so it looks good on the page)
html(confetti_and_hearts, height=260)

# --- Footer: helpful quick actions ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.write("**Quick notes & tips**")
    st.markdown("- Use the sidebar to change the name, accent color, and personal message.")
    st.markdown("- Click the **Click for a surprise** button to shower the page with confetti.")
    st.markdown("- To make it extra special: add a photo or custom GIF by editing this file and embedding an `<img>` tag inside the HTML portion.")

# small playful CTA
st.markdown("<div style='text-align:center; margin-top:6px; color:#444;'>Made with a lot of love ❤️ — feel free to edit, personalise and deploy!</div>", unsafe_allow_html=True)
