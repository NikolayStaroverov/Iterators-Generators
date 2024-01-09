class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.main_position = 0
        self.sub_position = -1
        return self

    def __next__(self):
        self.sub_position+=1
        len_of_sub_list = len(self.list[self.main_position])
        len_of_main_list = len(self.list)
        if self.sub_position == len_of_sub_list:
            self.main_position+= 1
            self.sub_position = 0

        if self.main_position == len_of_main_list:
            raise StopIteration
        return self.list[self.main_position][self.sub_position]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()