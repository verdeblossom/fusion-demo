# demo_app.py
# Streamlit Demo for Optimus Fusion Layer
# Upload photo → real analysis
# Crystal Clingenpeel & Grok – March 2026

import streamlit as st
from deepface import DeepFace
import mediapipe as mp
import cv2
from PIL import Image
import numpy as np

# Load fusion core
from fusion_layer import fuse_face_body_voice

st.title("🚀 Optimus Fusion Layer Demo")
st.write("Upload a photo and choose voice tone + words to see how Optimus would read the situation.")

# File uploader
uploaded_file = st.file_uploader("Upload a face or body photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Photo", use_column_width=True)
    
    # User inputs for voice and words
    col1, col2 = st.columns(2)
    with col1:
        voice_tone = st.selectbox("Voice tone", ["calm", "angry", "shaky", "quiet, very subdued", "loud, indignant"])
    with col2:
        verbal_text = st.text_input("Spoken words", value="I'm fine, really")
    
    # Run analysis
    if st.button("Analyze Photo"):
        with st.spinner("Analyzing..."):
            img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            
            # Face
            face_result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)[0]
            emo = face_result['emotion']
            dom_emotion = max(emo, key=emo.get)
            face_conf = emo[dom_emotion] / 100.0
            
            # Body (MediaPipe)
            mp_holistic = mp.solutions.holistic
            holistic = mp_holistic.Holistic(static_image_mode=True)
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = holistic.process(rgb)
            body_posture = "open posture"
            body_conf = 0.6
            if result.pose_landmarks:
                left_shoulder = result.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER]
                right_shoulder = result.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER]
                if left_shoulder.y > 0.5 and right_shoulder.y > 0.5:
                    body_posture = "defensive posture"
                    body_conf = 0.75
            
            # Fusion
            stress, decision, action = fuse_face_body_voice(
                face_emotion=dom_emotion, face_conf=face_conf,
                body_posture=body_posture, body_conf=body_conf,
                voice_tone=voice_tone, voice_conf=0.8,
                verbal_text=verbal_text,
                proximity_m=1.2
            )
            
            # Display results
            st.subheader("Analysis Results")
            st.write(f"**Dominant emotion**: {dom_emotion} ({face_conf*100:.1f}%)")
            st.write(f"**Body posture**: {body_posture} ({body_conf*100:.1f}%)")
            st.write(f"**Voice tone**: {voice_tone}")
            st.write(f"**Spoken words**: \"{verbal_text}\"")
            st.write(f"**Fused stress**: {stress:.2f}")
            st.write(f"**Decision**: {decision}")
            st.write(f"**Action**: {action}")
