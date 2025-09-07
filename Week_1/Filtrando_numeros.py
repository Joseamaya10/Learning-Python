temperatures = [19, 20, 30, 35, 25, 28, 17, 11, -5, 0, -8, -10, 45, 38, -45, 58]
for temperature in temperatures:
    if temperature <= 0:
        print(f"It is freezing, the temperature is {temperature}°C")
    elif temperature < 15:
        print(f"It is cold, the temperature is {temperature}°C")
    elif temperature < 25:
        print(f"It is nice, the temperature is {temperature}°C")
    elif temperature < 35:
        print(f"It is warm, the temperature is {temperature}°C")
    elif temperature < 45:
        print(f"It is hot, the temperature is {temperature}°C")
    else:
        print(f"What the hell, this is not normal, the temperature is {temperature}°C")