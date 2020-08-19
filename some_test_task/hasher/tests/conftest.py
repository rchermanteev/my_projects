import pytest


@pytest.fixture(scope="function")
def init_data_to_test_hasher():
    print("\n   > Case setup")
    test_vocabulary = {}
    with open("./tests/data/test_vocabulary.txt", "r") as file:
        for i in file.readlines():
            key, val = i.strip().split(':')
            test_vocabulary[int(key)] = val
    yield test_vocabulary
    print("\n   > Case teardown")
