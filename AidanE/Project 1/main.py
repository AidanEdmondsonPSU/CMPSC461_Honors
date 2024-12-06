def main():
    n = 10  # Number of terms in the Fibonacci sequence
    a, b = 0, 1
    print(a, b, end=" ")
    for _ in range(n - 2):
        a, b = b, a + b
        print(b, end=" ")

if __name__ == "__main__":
	main()
