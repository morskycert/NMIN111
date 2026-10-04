# /usr/bin/env python3
# prime factorization


# najvacsi mozny delitel celeho cisla n je integer u sqrt(n)
def main():
    n = int(input())
    d = 2
    while d * d <= n:
        while n % d == 0:
            print(d)
            n //= d
        d += 1

    if n > 1:
        print(n)


main()
