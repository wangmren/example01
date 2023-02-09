def hanno(n, a, b, c):
    if n > 0:
        hanno(n-1, a, c, b)
        print("我是%d块，从%s到%s,%s"%(n, a, c, b))
        hanno(n-1, b, a, c)

hanno(3, 'A', 'B', 'C')