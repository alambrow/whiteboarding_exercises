def sum_of_multiples(num):
    multiples = []
    number = num
    for x in range(3, number, 3):
        if x < number:
            multiples.append(x)
    for x in range(5, number, 5):
        if x < number:
            multiples.append(x)
    print(list(set(multiples)))
    return sum(list(set(multiples)))

def test_sum_of_multiples_solution():
    assert sum_of_multiples(10) == 23
    assert sum_of_multiples(20) == 78
    assert sum_of_multiples(0) == 0
    assert sum_of_multiples(1) == 0
    assert sum_of_multiples(200) == 9168
    assert sum_of_multiples(64) == 933
