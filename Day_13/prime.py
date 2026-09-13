def is_prime(n):
    """Checks if a given number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Optimized check using 6k +/- 1 rule up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes_in_range(start, end):
    """Generates all prime numbers within a specified range [start, end]."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Demonstration / Testing 
if __name__ == "__main__":
    # 1. Test individual prime checker (including edge cases 0 and 1)
    test_numbers = [0, 1, 2, 3, 4, 17, 18, 97]
    print("Prime Checker Tests:")
    for num in test_numbers:
        print(f"Is {num} prime? -> {is_prime(num)}")

    print("\n----------------------------------------\n")

    # 2. Test prime range generator
    start_range = 10
    end_range = 50
    print(f"Prime numbers between {start_range} and {end_range}:")
    print(generate_primes_in_range(start_range, end_range))
