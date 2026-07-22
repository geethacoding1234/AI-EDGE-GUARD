# ============================================
# Fuel Efficiency Calculator
# ============================================

def calculate_fuel_efficiency(rpm, speed, vibration):

    efficiency = max(
        8,
        24 - (rpm / 1000) * 2 - vibration + (speed / 60)
    )

    return round(efficiency, 2)


# ============================================
# Maintenance Countdown
# ============================================

def maintenance_countdown(health):

    remaining = max(0, int(health * 10))

    return remaining


# ============================================
# Smart Maintenance Recommendation
# ============================================

def maintenance_recommendations(
    engine,
    battery,
    rpm,
    oil,
    coolant,
    vibration,
    tire,
    current
):

    recommendations = []

    if engine > 100:
        recommendations.append(
            "🌡 High Engine Temperature - Inspect cooling system."
        )

    if battery < 11.5:
        recommendations.append(
            "🔋 Battery voltage is low. Recharge or replace battery."
        )

    if rpm > 4500:
        recommendations.append(
            "⚙ High RPM detected. Avoid prolonged high-speed driving."
        )

    if oil < 35:
        recommendations.append(
            "🛢 Low oil pressure. Check engine oil."
        )

    if coolant > 105:
        recommendations.append(
            "💧 Coolant temperature is high."
        )

    if vibration > 5:
        recommendations.append(
            "📳 Excessive engine vibration detected."
        )

    if tire < 28:
        recommendations.append(
            "🛞 Tire pressure is low."
        )

    if current > 40:
        recommendations.append(
            "🔌 High battery current detected."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "✅ Vehicle is operating normally."
        )

    return recommendations


# ============================================
# Sensor Health Status
# ============================================

def sensor_health(engine, battery):

    if engine > 100 or battery < 11:

        return "Critical"

    elif engine > 90 or battery < 12:

        return "Warning"

    else:

        return "Healthy"
