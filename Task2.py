def stop_words(words: list):
    def outer_wrap(func):
        def in_wrap(*args, **kwargs):
            res = func(*args, **kwargs)
            for word in words:
                res = res.replace(word, '*')
            return res
        return in_wrap
    return outer_wrap


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"