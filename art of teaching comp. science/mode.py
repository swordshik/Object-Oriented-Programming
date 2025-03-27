
def finding_mode(lst):
    counts = [lst.count(i) for i in lst]
    max_count = max(counts)

    maxs = [i for i in set(lst) if lst.count(i) == max_count]
    
    if len(maxs) > 1:
        return 'There is no mode.'
    else:
        return maxs[0]


numbers = [float(i) for i in input('Write a list of numbers:\n').split()]

print(finding_mode(numbers))