class Call_del:
    def e(call):
        str = eval('"self.{}()".format(call)')
        return str

    def crawl_daili66(self):
        print(123)


e = Call_del()
print(e('crawl_daili66'))

