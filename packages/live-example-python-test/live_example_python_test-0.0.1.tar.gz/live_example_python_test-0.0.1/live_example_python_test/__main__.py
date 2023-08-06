from live_example_python_test import count_seconds


@count_seconds
def foo():
    print("FOO")


if __name__ == '__main__':
    foo()