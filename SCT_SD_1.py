def celsius_to_fahrenheit(C):
    return (C * 9/5) + 32

def celsius_to_kelvin(C):
    return C + 273.15

def fahrenheit_to_celsius(F):
    return (F - 32) * 5/9

def fahrenheit_to_kelvin(F):
    return (F + 459.67) *5/9

def kelvin_to_celsius(K):
    return K - 273.15

def kelvin_to_fahrenheit(K):
    return (K * 9/5) - 459.67

def convert_temperature(temperature,from_scale,to_scale):
    if from_scale == "C" and to_scale == "F":
        return celsius_to_fahrenheit(temperature)
    elif from_scale == "C" and to_scale == "K":
        return celsius_to_kelvin
    elif from_scale == "F" and to_scale == "C":
        return fahrenheit_to_celsius
    elif from_scale == "F" and to_scale == "K":
        return fahrenheit_to_kelvin
    elif from_scale == "K" and to_scale == "C":
        return kelvin_to_celsius
    elif from_scale == "K" and to_scale == "F":
        return kelvin_to_fahrenheit
    
if __name__ == "__main__":
    temp = int(input("Enter the temperature:"))
    from_scale = str(input("Convet From : ( C , F , K)\n"))
    to_scale = str(input("Convert To : ( C , F , K)\n"))

    converted_temperature = convert_temperature(temp , from_scale , to_scale)

    if converted_temperature is not None:
        print(f"{temp}°{from_scale} is equal to {converted_temperature:.2f}°{to_scale}")
    else:
        print("Invalid Temperature Scale.")