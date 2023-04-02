# Added comment
def hi(name='World')->str:
    return 'Hello, {}!'.format(name)

if __name__ == "__main__":
    name = input("Hi! What's your name?\n")
    print(hi(name))
