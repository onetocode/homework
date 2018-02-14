import time



def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        return res

    return tmp

def pause(f):
    def tmp(*args, **kwargs):
        time.sleep(3)
        return f(*args, **kwargs)

    return tmp


@timer
@pause
def func(x, y):
    return x + y
func(9, 8)