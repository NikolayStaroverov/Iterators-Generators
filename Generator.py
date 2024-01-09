import types


def flat_generator(list_of_lists):
    main_position = 0
    while main_position<len(list_of_lists):
        sub_position=0
        while sub_position<len(list_of_lists[main_position]):
            ret_value = list_of_lists[main_position][sub_position]
            yield list_of_lists[main_position][sub_position]
            sub_position+=1
        main_position+=1

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()