plingplongs = (
    (3, 'Pling'),
    (5, 'Plang'),
    (7, 'Plong'),
)


def convert(number: int) -> str:
    result = ''
    for f, p in plingplongs:
        if number % f == 0:
            result += p
    return result if result else str(number)


assert convert(28) == 'Plong'
assert convert(30) == 'PlingPlang'
assert convert(34) == '34'
