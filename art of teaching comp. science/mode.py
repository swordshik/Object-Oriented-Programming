
def finding_mode(lst):
    mode = max(set(lst), key = lst.count)
    return mode

numbers = [float(i) for i in input('Write a list of numbers:\n').split()]
print(f'Mode of the given list = {finding_mode(numbers)}')