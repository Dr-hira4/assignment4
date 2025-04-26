import math

def main():
    ab = float(input("enter the length of the side AB:"))
    ac = float(input("enter the length of the side BC:"))

    bc = math.sqrt(ab**2 + ac**2)

    print(f"The length og the hypotenuse is {bc}")

if __name__ == "__main__":
    main()