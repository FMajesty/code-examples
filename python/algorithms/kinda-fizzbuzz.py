plingplongs = (
    (3, 'Pling'),
    (5, 'Plang'),
    (7, 'Plong'),
)


def convert(number: int) -> str:
    result = [p for f, p in plingplongs if number % f == 0]
    return ''.join(result) if result else str(number)


assert convert(28) == 'Plong'
assert convert(30) == 'PlingPlang'
assert convert(34) == '34'
