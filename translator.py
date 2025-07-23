def translate_sign(hand_landmarks):
    # Example: Detect "thumbs up" gesture
    thumb_tip = hand_landmarks.landmark[4]  # THUMB_TIP
    index_tip = hand_landmarks.landmark[8]  # INDEX_FINGER_TIP
    wrist = hand_landmarks.landmark[0]      # WRIST
    middle_tip = hand_landmarks.landmark[12]  # MIDDLE_FINGER_TIP

    # Detect "thumbs up" gesture
    if thumb_tip.y < wrist.y and index_tip.y > wrist.y:
        return "Thumbs Up Detected"

    # Detect "victory" (V) sign gesture
    # Both index and middle fingers up, thumb and other fingers down
    if (
        index_tip.y < wrist.y and
        middle_tip.y < wrist.y and
        thumb_tip.y > wrist.y
    ):
        return "Victory Sign Detected"

    return ""