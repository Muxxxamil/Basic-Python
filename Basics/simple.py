class BasicProgram:
    def __init__(self, x, y, fib_sequence=[]):
        self.x = x # random variable for numbers
        self.y = y # random variable for seq of characters
        self.fib_sequence = fib_sequence

    def fact(self, x):
        if x == 1:
            return x
        else:
            return x * self.fact(x - 1)

    def isPalindrome(self, y):
        y_reverse = y[::-1]
        if y_reverse == y:
            return True
        else:
            False

    def fibonacciNumber(self, x):
        if x <= 1:
            return x
        else:
            return self.fibonacciNumber(x - 2) + self.fibonacciNumber(x - 1)

    def isPrime(self, x):
        if x <= 1:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def isEven(self, x):
        if (x % 2) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    
    obj = BasicProgram(10, "MOM")
    temp_sequence = [obj.fib_sequence.append(obj.fibonacciNumber(fib_num)) for fib_num in range(obj.x)]

    print("1). Factorial of "+ str(obj.x) + " = "+ str(obj.fact(obj.x)) + "!") 
    print("2). Is word '"+ obj.y + "' palindrome? = "+ str(obj.isPalindrome(obj.y)))
    print("3). Is "+ str(obj.x) + " prime number? = "+ str(obj.isPrime(obj.x)))
    print("4). Is "+ str(obj.x) + " even number? = "+ str(obj.isEven(obj.x)))
    print("5). Fibonacci sequence of number "+ str(obj.x) + " is = "+ str(obj.fib_sequence))
    