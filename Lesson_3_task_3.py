def thesaurus(*names):
    list_name = [*names]
    dictionary = {}
    for name in list_name:
        if name[0] not in dictionary:
            dictionary[name[0]] = []
        dictionary[name[0]].append(name)
    return dictionary


print(thesaurus('Мила', 'Диана', 'Максим', 'Владислав', 'Сергей'))