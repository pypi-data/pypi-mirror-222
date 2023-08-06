
def s_kunjutom(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print("с кунжутом")
    return wrapper


def bulo4ka(**kwargs):
    print("булочка", **kwargs)