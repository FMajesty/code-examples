import timeit
# from array import array


def get_items(entries):
    items = []
    view_index = 0
    result = []
    previous_is_insert = False
    for entry in entries:
        if entry[0][0] == 'I':
            items.append((entry[1], int(entry[2])))
            previous_is_insert = True
        else:
            if previous_is_insert:
                items.sort(key=lambda x: (x[1], x[0]))
            result.append(items[view_index][0])
            view_index += 1
            previous_is_insert = False
    return result


entries = [
    ['INSERT', 'tevqnf', '4'], ['INSERT', 'uywhflblr', '6'], ['VIEW', '-', '-'], ['VIEW', '-', '-'],
    ['INSERT', 'munenlcqs', '7'], ['VIEW', '-', '-'], ['INSERT', 'qfhsbq', '1'], ['VIEW', '-', '-'],
    ['INSERT', 'ytpjmqol', '7'], ['VIEW', '-', '-'], ['INSERT', 'itjdg', '4'], ['INSERT', 'exdivsh', '10'],
    ['VIEW', '-', '-'], ['VIEW', '-', '-'], ['INSERT', 'rrxxjm', '9'], ['VIEW', '-', '-'], ['INSERT', 'zxetw', '2'],
    ['VIEW', '-', '-'], ['INSERT', 'lhsmr', '3'], ['INSERT', 'icmqyvro', '10'], ['VIEW', '-', '-'], ['VIEW', '-', '-'],
    ['INSERT', 'hopauezd', '5'], ['VIEW', '-', '-'], ['INSERT', 'qlcupbrw', '8'],
]

print('result:', get_items(
    (['INSERT', 'ruler', '4'], ['VIEW', '-', '-'], ['INSERT', 'notecards', '2'], ['VIEW', '-', '-'],
     ['INSERT', 'notebook', '9'], ['INSERT', 'backpack', '10'], ['INSERT', 'pens', '6'],['INSERT', 'pencils', '5'],
     ['VIEW', '-', '-'])
))
print('elements per execution:', len(entries))
print('total elements:', len(entries)*240_000)
print('get_items:', timeit.timeit(lambda: get_items(entries), number=240_000))