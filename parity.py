def main():
    x = int(input("What is z? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    return n % 2 == 0
# return True if n % 2 == 0 else False
main()