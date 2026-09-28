def ft_filter(function, iterable):
    ("""Return an iterator yielding those items of iterable for which """
     """function(item)\nis true. If function is None, return the items """
     """that are true.""")
    if function is None:
        for item in iterable:
            if item:
                yield item
    else:
        for item in iterable:
            if function(item):
                yield item


def main():
    """Demonstrate ft_filter with sample generator usage."""
    result = list(ft_filter(lambda x: x % 2 == 0, range(10)))
    print(result)


if __name__ == "__main__":
    main()
