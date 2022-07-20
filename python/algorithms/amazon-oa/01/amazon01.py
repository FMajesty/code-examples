from typing import List
import timeit


def sort_orders(order_list: List[str]):
    prime, non_prime = [], []
    for order in order_list:
        if order.split()[1].isnumeric():
            non_prime.append(order)
        else:
            prime.append(order)
    prime.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return prime + non_prime


entry = [
    'zld 93 12', 'fp kindle book', '125 echo dot second generation', '10a echo show', '17g 12 25 6',
    'ab1 kindle book'
]

print('result:', sort_orders(entry))
print('total elements:', len(entry)*1_000_000)
print('sort_orders:', timeit.timeit(lambda: sort_orders(entry), number=1_000_000))
