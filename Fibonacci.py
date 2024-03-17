def generate_fibonacci_series(n_terms):
    """
    Generate the Fibonacci series up to the nth term.
    """
    series = [0, 1]  # Begin with the initial terms of the series
    
    # Generate Fibonacci series up to the nth term
    for i in range(2, n_terms):
        prev_prev_term, prev_term = series[-2], series[-1]
        next_term = prev_prev_term + prev_term
        series.append(next_term)
    
    return series

def print_fibonacci_series(fib_series):
    """
    Print the Fibonacci series.
    """
    print("Fibonacci series:")
    for term in fib_series:
        print(term, end=", ")  # Print each term separated by comma
    print("\b\b ")  # Remove the last comma and space

def main():
    """
    Main function to get user input and print Fibonacci series.
    """
    print("Welcome to the Unique Fibonacci Series Generator!")
    print("This program generates the Fibonacci series up to a specified term.")
    print("")

    # Ask the user to input the value of n_terms
    while True:
        try:
            n_terms = int(input("Enter the number of terms in the Fibonacci series: "))
            if n_terms <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

    # Generate Fibonacci series
    fibonacci_series = generate_fibonacci_series(n_terms)
    
    # Print the generated Fibonacci series
    print_fibonacci_series(fibonacci_series)

if __name__ == "__main__":
    main()
