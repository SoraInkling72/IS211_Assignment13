def fibonnaci(n):
    if n < 0:
        print("Please do not put negative integers")
    elif n == 0:
        return
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
    # this is base case
    # the first three would be based on the length of the two strings
    ##################
    if len(s1) == 0 and len(s2) == 0:
        print(s1, s2, "equal")
        return 0
    elif len(s1) != 0 and len(s2) == 0:
        print(s1, s2, "not equal")
        return -1
    elif len(s1) == 0 and len(s2) != 0:
        print(s1, s2, "not equal")
        return 1
    elif s1[0] < s2[0]:
        print(s1, s2, "not equal")
        return -1
    elif s1[0] > s2[0]:
        print(s1, s2, "not equal")
        return 1
    ##################
    # recursive case
    else:
        return compareTo(s1[1:], s2[1:])


def compareTo(s1, s2):
    # this is base case
    # ####################
    if len(s1) == 0 and len(s2) == 0:
        print(s1, s2, "equal")
        return 0
    elif len(s1) != 0 and len(s2) == 0:
        print(s1, s2, "not equal")
        return -1
    elif len(s1) == 0 and len(s2) != 0:
        print(s1, s2, "not equal")
        return 1
    elif s1[0] < s2[0]:
        print(s1, s2, "not equal")
        return -1
    elif s1[0] > s2[0]:
        print(s1, s2, "not equal")
        return 1
    ##################
    # write recursive case here
    else:
        print(s1[0], s2[0], "both strings are equal")
        return compareTo(s1[1:], s2[1:])


# why 'len(s1) == 0 and len(s2) == 0' works
# if you pass empty s1 and s2, it will directly return 0
compareTo("", "")

# if two strings are identical
result = compareTo("apple", "apple")

# here you need to check the result and print overall result, like
if result == 0:
    print("both strings are equal")