def consumer():
    print("[CONSUMER] start")
    c = 'start'
    while True:
        # print('yield前面停止')
        n = yield c
        # print('yield后面停止')
        if not n:
            print("n is empty草你妈")
            continue
        print("消费者 %s" % n)
        c = "200 ok"


def producer(c):
    # 启动generator
    start_value = c.send(None)
    print('start的值:', start_value)
    # print('start_value的值')
    n = 0
    while n < 3:
        n += 1
        print("[生产者] 生产者  %d" % n)
        r = c.send(n)
        print('[生产者] 消费者 return: %s' % r)
    # 关闭generator
    c.close()


# 创建生成器
c = consumer()
# 传入generator
producer(c)
