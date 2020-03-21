class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['__chow_name__'] = []
        attrs['__v__'] = []
        count = 0
        for k, v in attrs.items():
            attrs['__chow_name__'].append(k)
            attrs['__v__'].append(v)
            count += 1
        attrs['__del_count__'] = count
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    def crawl_1(self):
        pass

    def crawl_2(self):
        pass

    def crawl_3(self):
        pass

crawl = MyList()
for i in range(crawl.__del_count__):
    callback = crawl.__chow_name__[i]
    v = crawl.__v__[i]
    print('类名:', callback,   v)
    # proxise = crawl.get_name(callback)
    # print(proxise)
