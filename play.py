import streamlit as st
from streamlit.runtime.state import session_state
from streamlit_webrtc import webrtc_streamer,VideoProcessorBase
from ultralytics import YOLO
import cv2
import av
import random

model = YOLO("yolov8n.pt")

all_objects=model.names

game_item_mappings = {
    0: "person", 1: "bicycle", 2: "car", 5: "bus", 9: "traffic light", 10: "fire hydrant",
    11: "stop sign", 13: "bench", 24: "backpack", 25: "umbrella", 26: "handbag", 28: "suitcase",
    32: "sports ball", 36: "skateboard", 38: "tennis racket", 39: "bottle", 41: "cup", 45: "bowl",
    46: "banana", 47: "apple", 48: "sandwich", 49: "orange", 50: "broccoli", 51: "carrot",
    53: "pizza", 54: "donut", 55: "cake", 56: "chair", 57: "couch", 58: "potted plant",
    60: "dining table", 62: "tv", 63: "laptop", 65: "remote", 67: "cell phone", 73: "book",
    74: "clock", 75: "vase", 77: "teddy bear", 79: "toothbrush"
}
game_items = list(game_item_mappings.values())

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.prev_targets = set()
    st.session_state.target = random.choice(game_items)
    st.session_state.selected = False


if st.session_state.total < 5 and st.button("Give Up"):
    st.session_state.total += 1
    st.session_state.selected = False


if st.session_state.selected==False and st.session_state.total<5:
    while st.session_state.selected==False:
        new_target=random.choice(game_items)
        while new_target in st.session_state.prev_targets:
            new_target=random.choice(game_items)
        st.session_state.selected=True
        st.session_state.target = new_target
        st.session_state.prev_targets.add(new_target)

if st.session_state.total < 5:
    st.subheader(f"🔎 Find: `{st.session_state.target}`")
else:
    st.success(f"🏁 Game Over! Final Score: {st.session_state.score}/{st.session_state.total}")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    results = model(img)[0]
    annotated=results.plot()
    boxes = results.boxes
    for box in boxes:
        class_id = int(box.cls.item())
        class_name = all_objects[class_id]
        if class_name == st.session_state.target:
            st.session_state.score += 1
            st.session_state.total += 1
            st.session_state.selected = False
    return av.VideoFrame.from_ndarray(annotated, format="bgr24")

st.title("Play")

webrtc_streamer(key="sample",video_frame_callback=video_frame_callback,media_stream_constraints={"video": True, "audio": False})


