def fibonnaci(n):
    if n < 0:
        print("Please do not put negative integers")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    if s1 == s2:
        return 0
#    elif s1 < s2:

#    elif s1 > s2:


