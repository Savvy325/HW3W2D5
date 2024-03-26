# 1. Exceptional Weather Forecast
# Task 1: Start
# Task 2: Temperature Conversion
# Task 3: User Experience
def temp():
    try:
        fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
    except ZeroDivisionError:
        print("Get that zero out of here")
    except OverflowError:
        print("I'm too full no more numbers")
    except ValueError:
        print("That's not a number")
    else:
        print(f"The converted temperature is: {celsius} Celsius ")
    finally:
        print(f"Thank you for using our amazing weather forecast application!")
temp()