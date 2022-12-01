def get_val(collection, key, default=None):
    try:
        return collection[key]
    except KeyError:
        return default


def set_(coll, path, value=None):
    if type(path) is not list:
        return 'TypeError'
    st = ''
    for i in range(len(path)):
        st += '{"%s": ' % f'{path[i]}'
    st += f'{value}' + ('}' * len(path))
    coll.update(eval(st))
    return coll
