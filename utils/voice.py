"""
EdgeGuard AI Voice Module
Temporary implementation
"""

def speak(message):
    print(f"[VOICE]: {message}")

def vehicle_voice_alert(status):

    if status == "Healthy":
        print("🔊 Vehicle is healthy. No maintenance required.")

    elif status == "Maintenance Required":
        print("🔊 Maintenance required. Please inspect the vehicle.")

    elif status == "Critical Fault":
        print("🔊 Critical fault detected! Stop the vehicle immediately.")

    else:
        print(f"🔊 {status}")
