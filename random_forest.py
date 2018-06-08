import random


class DataUnit:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'{self.__class__.__name__}{{' + ', '.join([f'{k}: {v}' for k, v in vars(self).items()]) + '}'


DATA = (
    DataUnit(size=15, color='red', speed='quick', conclusion=False),
    DataUnit(size=12, color='blue', speed='slow', conclusion=True),
    DataUnit(size=3, color='green', speed='slow', conclusion=False),
    DataUnit(size=8, color='black', speed='quick', conclusion=True)
)


def get_bootstrapped_data(data, size):
    return [random.choice(data) for _ in range(size)]


def build_one_random_tree(data, end_key='conclusion'):
    pass


def main():
    print(*get_bootstrapped_data(DATA, 13), sep='\n')


if __name__ == '__main__':
    main()
