def main():
    n = get_number()
    print_meow(n)

def get_number():
    while True:
        n = int(input("Enter the number? "))
        if n > 0:
            return n

def print_meow(n):
    for _ in range(n):
        print("meow")

if __name__ == '__main__':
    main()
