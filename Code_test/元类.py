class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__show_name__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__show_name__'].append(k)
                count += 1
        attrs['__del_name__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_name(self, call):
        # str = eval('"{}()".format(call)')
        for proxy in eval("self.{}()".format(call)):
            print(proxy)
            print("---")
        return str

    def crawl_1(self):
        for i in range(1, 4):
            yield i

    def crawl_2(self):
        for i in ['a', 'b', 'c']:
            yield i


crawl = Crawler()
for i in range(crawl.__del_name__):
    callback = crawl.__show_name__[i]
    print('类名:', callback)
    proxise = crawl.get_name(callback)
    print(proxise)
