def say_hi():
    return 'Hi Students'

def show_msg():
        return say_hi()

def cube(b):
        def square(a):
                return a ** 2
        return square(b)*b

print(show_msg())
print(cube(9))