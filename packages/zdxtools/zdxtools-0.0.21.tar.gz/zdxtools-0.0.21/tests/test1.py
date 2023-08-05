from pypi_update.src.zdxtools.dx_tools import decorator

class a :
    @decorator.ExceptionD
    def test(self):
        data = {
            'a':1,
            '222':'2',
            'getsig':'213123',
        }
        int(data)


if __name__ == '__main__':
    b = a()
    b.test()