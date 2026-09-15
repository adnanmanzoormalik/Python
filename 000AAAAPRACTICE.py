def multiplier(x):

    def multiply(y):
        return x * y

    return multiply

double = multiplier(2)
a = double(2)
print(a)