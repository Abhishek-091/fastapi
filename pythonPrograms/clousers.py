#  Why use nested functions?
# Encapsulation: The inner function is only used within the outer one.

# Cleaner code: Helps organize logic that's only relevant inside the outer function.

# Closures: Inner functions can access variables from the outer function, even after the outer function has finished executing.


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function

closure = outer_function(10)
print(closure(5))  # Output: 15


def greeter():
    name_inner = "Abhishek"
    def greet(name = name_inner):

        def greet_abhishek(name = name):
            return f"Hello, {name}!"

        return greet_abhishek

    return greet

lets_greet_abhishek = greeter()
greet_abhishek = lets_greet_abhishek("Akash")
print(greet_abhishek())  # Output: Hello, Abhishek!
