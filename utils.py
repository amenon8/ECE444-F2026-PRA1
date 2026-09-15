class utils:
    def reversed(number):
        if not isinstance(number, int):
            raise TypeError("expected an int")
        return int(str(number)[::-1])

    def formatter(number):
        if not isinstance(number, int):
            raise TypeError("expected an int")
        return bin(number), oct(number)