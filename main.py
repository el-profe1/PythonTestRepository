def hi(name='World')->str:
    return 'Hellogit fetch origin main {}!'.format(name)

def helloWorld() -> str:
    return "Hello, World!"

if __name__ == "__main__":
    name = input("Hi! What's your name?\n")
    print(hi(name))
    print(helloWorld())
