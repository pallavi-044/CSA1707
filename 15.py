def play_tennis(weather, temp):
    # make inputs case-insensitive
    weather = weather.capitalize()
    temp = temp.capitalize()

    # Simple decision tree rules
    if weather == "Overcast":
        return "Yes"
    elif weather == "Sunny":
        if temp in ["Hot", "Mild"]:
            return "No"
        elif temp == "Cool":
            return "Yes"
    elif weather == "Rain":
        if temp in ["Cool", "Mild"]:
            return "Yes"
        elif temp == "Hot":
            return "No"
    return "Invalid input"

# --- User Input ---
weather = input("Enter Weather (Sunny/Overcast/Rain): ")
temp = input("Enter Temperature (Hot/Mild/Cool): ")

# --- Prediction ---
print("Play Tennis?", play_tennis(weather, temp))
