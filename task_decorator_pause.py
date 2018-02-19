from time import sleep


def pause(sec):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sleep(sec)
            return func(*args, **kwargs)
        return wrapper
    return decorator
