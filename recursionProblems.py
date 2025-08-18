
def func(name, times):
    if times == 0:
        return
    
    print(name)
    func(name, times - 1)

func("Hello", 3)


def triangular(i):
    if i <= 1:
        return 1
    
    return i + triangular(i - 1)

print(triangular(5))