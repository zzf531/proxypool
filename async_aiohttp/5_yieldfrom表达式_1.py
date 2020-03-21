def test(n):
    i = 0
    while i < n:
        yield i
        i += 1

# 委派生成器
def test_yield_from(n):
    print("test_yield_from start")
    yield from test(n)
    print("test_yield_from doing")
    yield from test(n)
    print("test_yield_from end")


for i in test_yield_from(3):
    print(i, '___')
