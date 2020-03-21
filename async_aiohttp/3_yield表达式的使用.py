def test():
    print("generator start")
    n = 1
    while True:
        yield_expression_value = yield n  # 包含yield表达式的函数将不再是一个函数
        print("yield_expression_value = %d" % yield_expression_value)
        n += 1

# __next__()方法: 作用是启动或者恢复generator的执行，相当于send(None)
# send(value)方法：作用是发送值给yield表达式。启动generator则是调用send(None)


# ①创建generator对象; 创建test类实例
generator = test()
print(type(generator))

print("\n---------------\n")

# ②启动generator
next_result = generator.__next__()
print("next_result = %d" % next_result)

print("\n---------------\n")

# ③发送值给yield表达式
send_result = generator.send(666)
print("send_result = %d" % send_result)
