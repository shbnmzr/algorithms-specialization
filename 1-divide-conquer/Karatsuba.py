def count_digits(number):
    string = str(number)
    return int(len(string))


def karatsuba(x, y):
    n = count_digits(x)
    m = count_digits(y)
    if n == 1 or m == 1:
        return x * y
    else:
        halves = {
            'a': x // (pow(10, n//2)),
            'b': x % (pow(10, n//2)),
            'c': y // (pow(10, n//2)),
            'd': y % (pow(10, n//2)),
        }
        results = {
            'ac': karatsuba(halves['a'], halves['c']),
            'ad': karatsuba(halves['a'], halves['d']),
            'bc': karatsuba(halves['b'], halves['c']),
            'bd': karatsuba(halves['b'], halves['d'])
        }
        return ((pow(10, (n//2)*2)) * results['ac']) + ((pow(10, n//2)) * (results['ad'] + results['bc'])) + results['bd']


def main():
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    result = karatsuba(x, y)
    print(result)
    print(x * y)
    print(x * y == result)


if __name__ == '__main__':
    main()

