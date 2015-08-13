def factor(n): #factor an integer, suppose n=10
    s = set() #start with an empty set
    for i in xrange(1, n /2): # which would be between 1 and 10
        if n % i == 0: #iteration 1: if 10 % 1 == 0, yes. iteration 2: if 10%2 ==0,yes. iteration 3: if 10%3 == 0, no. loop ends
            if (i != n/i): # if 1 != 10/1. iteration 2: if 2 != 5
                s.add(i) #add 1, add 2
                s.add(n / i) #add 10/1 = 10, add 5
            else:
                s.add(i)

    sent =  '%d has %d factors: ' % (n,len(s))
    name = '%s%s' % (sent, sorted(s))
    return name

