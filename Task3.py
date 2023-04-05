def arg_rules(type_: type, max_length: int, contains: list):
    def outer_wrap(func):
        def inner_wrap(arg):
            if type(arg) != type_:
                return False
            if len(arg) > max_length:
                return False
            for i in contains:
                if i not in arg:
                    return False
            return func(arg)
        return inner_wrap
    return outer_wrap


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'