def finding_mode(lst):
    mode = max(set(lst), key = lst.count)
    return mode

numbers = [float(i) for i in input().split()]
print(finding_mode(numbers))