text = input('Type in string to count word frrequency: ')

text_list = text.split()
unique_items = list(set(text_list))

for item in unique_items:
    unique_item_repeat = [unique_item for unique_item in text_list if unique_item==item]
    print(f'{item}:{len(unique_item_repeat)}')