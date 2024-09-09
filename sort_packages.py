def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length
    
    # Determine if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if the package is heavy
    is_heavy = mass >= 20
    
    # Determine which stack the package should be dispatched to
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example test cases
if __name__ == "__main__":
    print(sort(100, 100, 100, 10))  # STANDARD
    print(sort(200, 100, 100, 10))  # SPECIAL (bulky due to width)
    print(sort(100, 100, 100, 25))  # SPECIAL (heavy)
    print(sort(200, 200, 200, 25))  # REJECTED (both bulky and heavy)
