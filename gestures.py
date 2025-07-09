import mediapipe as mp
import math

# Thresholds
OK_THRESHOLD = 0.04
SPREAD_THRESHOLD = 0.04  
Y_SIGN_SPREAD_THRESHOLD = 0.30  # Thumb-pinky min distance for Y sign

def is_pointing_up(tip, pip):
    return tip.y < pip.y

def is_pointing_down(tip, pip):
    return tip.y > pip.y

def distance(lm1, lm2):
    return math.sqrt(
        (lm1.x - lm2.x)**2 +
        (lm1.y - lm2.y)**2 +
        (lm1.z - lm2.z)**2
    )

def is_finger_folded(tip, dip):
    return tip.y > dip.y  

def detect_gesture(hand_landmarks):
     # Get landmarks
    lm = hand_landmarks.landmark
    idx = mp.solutions.hands.HandLandmark

    # Define fingers
    index_tip, index_pip, index_dip = lm[idx.INDEX_FINGER_TIP], lm[idx.INDEX_FINGER_PIP], lm[idx.INDEX_FINGER_DIP]
    middle_tip, middle_pip, middle_dip = lm[idx.MIDDLE_FINGER_TIP], lm[idx.MIDDLE_FINGER_PIP], lm[idx.MIDDLE_FINGER_DIP]
    ring_tip, ring_pip, ring_dip = lm[idx.RING_FINGER_TIP], lm[idx.RING_FINGER_PIP], lm[idx.RING_FINGER_DIP]
    pinky_tip, pinky_pip, pinky_dip = lm[idx.PINKY_TIP], lm[idx.PINKY_PIP], lm[idx.PINKY_DIP]
    thumb_tip, thumb_ip, thumb_mcp = lm[idx.THUMB_TIP], lm[idx.THUMB_IP], lm[idx.THUMB_MCP]

    # Directions
    index_up = is_pointing_up(index_tip, index_pip)
    middle_up = is_pointing_up(middle_tip, middle_pip)
    ring_up = is_pointing_up(ring_tip, ring_pip)
    pinky_up = is_pointing_up(pinky_tip, pinky_pip)
    index_down = is_pointing_down(index_tip,index_pip)
    middle_down = is_pointing_down(middle_tip, middle_pip)
    ring_down = is_pointing_down(ring_tip, ring_pip)
    thumb_up = thumb_tip.y < thumb_ip.y < thumb_mcp.y

    # Folded
    index_folded = is_finger_folded(index_tip, index_dip)
    middle_folded = is_finger_folded(middle_tip, middle_dip)
    ring_folded = is_finger_folded(ring_tip, ring_dip)
    pinky_folded = is_finger_folded(pinky_tip, pinky_dip)
    thumb_folded = is_finger_folded(thumb_tip, thumb_ip)

    # Distances
    dist_index_middle = distance(index_tip, middle_tip)
    dist_middle_ring = distance(middle_tip, ring_tip)
    dist_thumb_pinky = distance(thumb_tip, pinky_tip)
    dist_thumb_index = distance(thumb_tip, index_tip)

    thumb_above = is_pointing_up(thumb_tip, middle_tip)
    

    # Gestures
    if distance(thumb_tip, index_tip) < OK_THRESHOLD and middle_up and ring_up and pinky_up:
        return "ok"

    # Scrolling (index and middle up or down depending on scrolling)
    if index_up and middle_up and not thumb_above and dist_index_middle < SPREAD_THRESHOLD:
        return "scroll_up"
    if index_down and middle_down and not thumb_up and dist_index_middle < SPREAD_THRESHOLD:
        return "scroll_down"
    
    # Volume (only index up or down depending on volume change)
    if index_up and middle_folded and pinky_folded and ring_folded:
        return "volume_up"
    if index_down and middle_up and ring_up and pinky_up:
        return "volume_down"

    # Rock sign
    if index_up and pinky_up and middle_down and ring_down:
        return "play_music"

    # Two sign: index and middle apart and up
    if index_up and middle_up and dist_index_middle >= SPREAD_THRESHOLD + 0.1 and not ring_up:
        return "previous_song"

    # Three sign: index, middle and right up and apart
    if index_up and middle_up and ring_up:
        if dist_index_middle >= SPREAD_THRESHOLD + 0.1 and dist_middle_ring >= SPREAD_THRESHOLD + 0.1:
            return "next_song"

    # Y sign: clearly extended thumb and pinky, others folded, wide spread
    if (
        thumb_up and
        pinky_up and
        index_folded and middle_folded and ring_folded and
        dist_thumb_pinky > Y_SIGN_SPREAD_THRESHOLD
    ):
        return "y_sign"
    
    # L sign: Index up, thumb to the side and everything else folded
    thumb_sideways = abs(thumb_tip.x - thumb_ip.x) > 0.05 and abs(thumb_tip.y - thumb_ip.y) < 0.05
    if index_up and thumb_sideways and middle_folded and ring_folded and pinky_folded:
        return "l_sign"
    
    # Pinky up and all are folded, similar to drinking tea
    if pinky_up and middle_folded and ring_folded and index_folded:
        return "tea"
    


    return None
