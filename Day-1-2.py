def Sum(n):
        if n <= 0: return 0
        return (n)+Sum(n//3-2)


print(sum(Sum(i//3-2) for i in list(map(int, input().split()))))