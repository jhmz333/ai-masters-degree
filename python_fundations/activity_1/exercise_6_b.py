def half_split_list(list_):
    # Extraer las dos listas
    list_1 = list_[: int(len(list_) / 2)]
    list_2 = list_[int(len(list_) / 2):]

    return f"{list_} -> {list_1}, {list_2}"


print(half_split_list([1, 2, 3, 4, 5, 6]))
print(half_split_list(["hello", "world", "I'm", "José"]))
