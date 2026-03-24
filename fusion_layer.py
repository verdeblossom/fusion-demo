# ================================================
# Optimus Fusion Layer v2.9.7 - Library-Free Version
# Pure Python - Safe for GitHub
# Face + Body + Voice + Verbal + Proximity + Crowd + Memory
# Crystal Clingenpeel & Grok – March 2026
# ================================================

def fuse_face_body_voice(face_emotion="neutral", face_conf=0.5,
                         body_posture="open posture", body_conf=0.5,
                         voice_tone="calm", voice_conf=0.5,
                         verbal_text="", proximity_m=5.0, approach_speed_mps=0.0,
                         physical_contact=False, crowd_density=0.5, crowd_movement="calm",
                         face_hash="unknown"):
    
    base_stress = (face_conf * 0.5 + body_conf * 0.3 + voice_conf * 0.2)
    
    # Threat detection
    threat_keywords = ["anger", "contempt", "fear", "disgust", "defensive", "guarded", "tense"]
    is_threat_face = any(t in face_emotion.lower() for t in threat_keywords)
    is_threat_body = any(t in body_posture.lower() for t in threat_keywords)
    is_threat_voice = any(t in voice_tone.lower() for t in ["angry", "shaky", "tense", "aggressive"])
    
    # Verbal semantics
    text_lower = verbal_text.lower()
    explicit_imminent = any(word in text_lower for word in ["hurt", "kill", "attack", "stab", "shoot", "harm"])
    if explicit_imminent:
        base_stress += 0.5
    
    # Proximity multiplier
    prox_mult = 1.0
    if proximity_m < 1.5:
        prox_mult = 1.8 if approach_speed_mps > 0 else 1.0
    elif proximity_m < 3.0:
        prox_mult = 1.6 if approach_speed_mps > 0.5 else 1.3
    base_stress *= prox_mult
    
    # Crowd multiplier
    crowd_mult = 1.0
    if crowd_density > 6:
        crowd_mult = 2.0 if "panic" in crowd_movement else 1.5
    elif crowd_density > 3:
        crowd_mult = 1.8 if "panic" in crowd_movement else 1.2
    base_stress *= crowd_mult
    
    fused_stress = min(1.0, max(0.0, base_stress))
    
    # Decision
    if fused_stress > 0.85:
        decision = "high-alert"
        action = "passive shield + call authorities" if (physical_contact or explicit_imminent) else "passive shield + verbal de-escalate"
    elif fused_stress > 0.65:
        decision = "de-escalate"
        action = "create distance + calm speech"
    elif fused_stress > 0.35:
        decision = "cautious"
        action = "monitor + short responses"
    else:
        decision = "normal"
        action = "full helpful mode"
    
    log_edge = fused_stress > 0.85 or (physical_contact and fused_stress > 0.7)
    
    return fused_stress, decision, log_edge, action

# Example usage
if __name__ == "__main__":
    stress, decision, log, action = fuse_face_body_voice(
        face_emotion="anger", face_conf=0.98,
        body_posture="aggressive approach", body_conf=0.92,
        voice_tone="angry", voice_conf=0.95,
        verbal_text="I will hurt you",
        proximity_m=0.8, approach_speed_mps=2.0,
        physical_contact=True,
        crowd_density=8.0, crowd_movement="panic surge"
    )
    print(f"Fused stress: {stress:.2f}")
    print(f"Decision: {decision}")
    print(f"Action: {action}")
    print(f"Log for fleet: {'YES' if log else 'no'}")
