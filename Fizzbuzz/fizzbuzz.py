def fizzbuzz():
    for num in xrange(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print "Fizzbuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num

if __name__ == '__main__':
    fizzbuzz()



