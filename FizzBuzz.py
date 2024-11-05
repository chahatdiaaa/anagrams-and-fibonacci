def fibonacci(n):
    
    def check_divisibility(x):
        if x == 0:
            return x # it's the start of the Fibonacci sequence
        elif x % 3 == 0:
            return 'Fizz'
        elif x % 5 == 0:
            return 'Buzz'
        elif x % 3 == 0 and x % 5 == 0:
            return 'FizzBuzz'
        else:
            return x
        
    # Initialize an empty list to hold the Fibonacci sequence with "FizzBuzz" logic    
    sequence = []

    # Starting with first two Fibonacci numbers
    a, b = 0, 1
     # creating loop n times to generate the first n numbers in the Fibonacci sequence
    for _ in range(n):
        # Checking divisibility for the current Fibonacci number (a) and add to the sequence
        sequence.append(check_divisibility(a))
        #Moving to the next Fibonacci number by updating a and b
        
        a, b = b, a + b  # a takes the value of b, and b becomes the sum of a and b
    
        
    return sequence

fibonacci(50)