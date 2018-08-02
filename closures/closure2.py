def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 6, 5, 7, 4, 3, 9]
group = {2, 3, 5}
sort_priority(numbers, group)

print(numbers)