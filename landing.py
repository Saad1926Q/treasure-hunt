import streamlit as st
import subprocess

st.title("🔍 Object Hunt")
st.markdown("## A Real-Time Object Detection Treasure Hunt")

st.markdown("""
Welcome to **Object Hunt**, a fun real-world object detection game using your webcam!  
Built using [YOLOv8](https://github.com/ultralytics/ultralytics) for live object recognition.

---

### 🎯 How to Play
- You'll be shown a random object to find.
- Show the object to your webcam.
- If YOLO detects it, you earn a point.
- Find 5 objects to finish the hunt.
- Press **'g'** if you're unable to find the object and want to skip it.
- Press **'q'** to quit the game entirely.

""")


st.markdown("---")
st.caption(
            'Made with ❤️ by [@saad1926q](https://github.com/Saad1926Q)'
)
st.caption("Theme inspired by [this](https://doc-theming-overview-anthropic-light-inspired.streamlit.app/)")
