def is_anagram(first_string, second_string):
    list1 = list(first_string.lower())
    list2 = list(second_string.lower())
    order(list1, 0, len(list1) - 1)
    order(list2, 0, len(list2) - 1)

    return (
        "".join(list1),
        "".join(list2),
        list1 == list2 and (first_string != "" or second_string != ""),
    )


def order(lst, start, end):
    if start < end:
        p = partição(lst, start, end)
        order(lst, start, p - 1)
        order(lst, p + 1, end)


def partição(lst, start, end):
    p = lst[end]
    limitador = start - 1

    for index in range(start, end):
        if lst[index] <= p:
            limitador = limitador + 1
            lst[index], lst[limitador] = lst[limitador], lst[index]

    lst[limitador + 1], lst[end] = lst[end], lst[limitador + 1]

    return limitador + 1


print(is_anagram("", "ovo"))
