def main():

    expression = input("Expression: ").strip().lower()

    x, y, z = expression.split(" ")

    x, z = int(x), int(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        result = 0
    
    print(f"{result:.1f}")

main()
