import time

last_gesture = None
gesture_start_time = 0
volume_step_interval = 0.2
volume_change_per_step = 0.02

def adjust_volume(gesture, volume_ctrl):
    global last_gesture, gesture_start_time
    current_time = time.time()

    if gesture == last_gesture and gesture is not None:
        if current_time - gesture_start_time >= volume_step_interval:
            current_volume = volume_ctrl.GetMasterVolumeLevelScalar()
            if gesture == "volume_up":
                new_volume = min(1.0, current_volume + volume_change_per_step)
                print("Volume Increased:", round(new_volume, 2))
                volume_ctrl.SetMasterVolumeLevelScalar(new_volume, None)
            elif gesture == "volume_down":
                new_volume = max(0.0, current_volume - volume_change_per_step)
                print("Volume Decreased:", round(new_volume, 2))
                volume_ctrl.SetMasterVolumeLevelScalar(new_volume, None)
            gesture_start_time = current_time
    else:
        last_gesture = gesture
        gesture_start_time = current_time
