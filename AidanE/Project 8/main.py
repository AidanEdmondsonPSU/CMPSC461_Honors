def main():
    p = float(input("Principal amount: "))
    r = float(input("Rate of interest: "))
    t = float(input("Time in years: "))
    simple_interest = (p * r * t) / 100
    print("Simple Interest:", simple_interest)

if __name__ == "__main__":
    main()
