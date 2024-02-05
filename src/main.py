import timeit
import random

coins_set = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum: int):
    coins_change = {}
    for coin in coins_set:
        count = sum // coin

        if count > 0:
            coins_change[coin] = count

        sum -= coin * count

    return coins_change


def find_min_coins(sum: int):
    min_coins_required = [0] + [float("inf")] * sum
    last_coin_used = [0] * (sum + 1)

    for s in range(1, sum + 1):
        for coin in coins_set:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    coins_change = {}
    current_sum = sum

    while current_sum > 0:
        coin = last_coin_used[current_sum]
        coins_change[coin] = coins_change.get(coin, 0) + 1
        current_sum -= coin

    return coins_change


def measure_find_coins_function(data_set, func):
    for data in data_set:
        func(data)


if __name__ == "__main__":
    data_set = [random.randint(1_000, 2_000) for _ in range(1000)]

    time_for_greedy = timeit.timeit(
        lambda: measure_find_coins_function(data_set[:], find_coins_greedy), number=10
    )
    time_for_min_coins = timeit.timeit(
        lambda: measure_find_coins_function(data_set[:], find_min_coins), number=10
    )

    print(f"|{'-'*34}|")
    print(f"{'|Алгоритм': <16} | {'Час виконання': <16}|")
    print(f"|{'-'*16}|{'-'*17}|")
    print(f"|{'Greedy': <15} | {time_for_greedy: <16.5f}|")
    print(f"|{'-'*16}|{'-'*17}|")
    print(f"|{'Min coins': <15} | {time_for_min_coins: <16.5f}|")
    print(f"|{'-'*34}|")

    print(
        f"\nGreedy в {time_for_min_coins / time_for_greedy:.2f} разів швидший за Min coins."
    )
