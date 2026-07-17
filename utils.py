def get_aqi_status(aqi):

    if aqi == 1:
        return (
            "🟢 Good",
            "Air quality is good. Enjoy outdoor activities."
        )

    elif aqi == 2:
        return (
            "🟡 Fair",
            "Air quality is acceptable. Sensitive individuals should take care."
        )

    elif aqi == 3:
        return (
            "🟠 Moderate",
            "People with respiratory issues should reduce prolonged outdoor activities."
        )

    elif aqi == 4:
        return (
            "🔴 Poor",
            "Avoid prolonged outdoor activities. Consider wearing a mask."
        )

    else:
        return (
            "🟣 Very Poor",
            "Stay indoors if possible. Avoid outdoor exercise."
        )