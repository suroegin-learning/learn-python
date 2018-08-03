from num2words import num2words

NUMBERS = 1_000_000

max_length = [0, None, None]

for number in range(NUMBERS):
    generated_text = num2words(number,
                               ordinal=True,
                               lang='en')\
        .replace(" and ", "-and-")\
        .replace(", ", "-")\
        .replace(" ", "-")

    if len(generated_text) > max_length[0]:
        max_length[0] = len(generated_text)
        max_length[1] = generated_text
        max_length[2] = number

print(max_length)
