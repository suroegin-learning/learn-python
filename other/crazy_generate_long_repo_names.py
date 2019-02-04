from num2words import num2words

NUMBERS = 1_000_000

position_name_and_size = [
    (i, n, len(n))
    for i, n
    in enumerate([
        num2words(name,
                  ordinal=True,
                  lang='en').replace(" and ", "-and-").replace(", ", "-").replace(" ", "-")
        for name
        in range(1, NUMBERS+1)
    ], 1)
]

# Show total result
# print(position_name_and_size)

# Show max length name, it's number and position
print(max([x for x in position_name_and_size], key=lambda y: y[2]))