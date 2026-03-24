# fusion_layer.py
# Pure Python Fusion Layer - Safe for GitHub
# Crystal Clingenpeel & Grok – March 2026

def fuse_face_body_voice(face_emotion="neutral", face_conf=0.5,
                         body_posture="open posture", body_conf=0.5,
                         voice_tone="calm", voice_conf=0.5,
                         verbal_text="", proximity_m=5.0):
    
    base_stress = (face_conf * 0.5 + body_conf * 0.3 + voice_conf * 0.2)
    
    threat_keywords = ["anger", "contempt", "fear", "disgust", "defensive", "guarded", "tense"]
    is_threat_face = any(t in face_emotion.lower() for t in threat_keywords)
    is_threat_body = any(t in body_posture.lower() for t in threat_keywords)
    is_threat_voice = any(t in voice_tone.lower() for t in ["angry", "shaky", "tense", "aggressive"])
    
    if is_threat_face and is_threat_body and is_threat_voice:
        fused_stress = base_stress * 1.6
    elif is_threat_face and is_threat_body:
        fused_stress = base_stress * 1.4
    else:
        fused_stress = base_stress * 1.2 if face_emotion.lower() in body_posture.lower() else base_stress * 0.7
    
    fused_stress = min(1.0, max(0.0, fused_stress))
    
    if fused_stress > 0.85:
        decision = "high-alert"
        action = "passive shield + call authorities"
    elif fused_stress > 0.65:
        decision = "de-escalate"
        action = "create distance + calm speech"
    elif fused_stress > 0.35:
        decision = "cautious"
        action = "monitor + short responses"
    else:
        decision = "normal"
        action = "full helpful mode"
    
    return fused_stress, decision, action
