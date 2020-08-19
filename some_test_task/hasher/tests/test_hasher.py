from ..hasher import Hasher


class TestHasher:
    def test_input_data(self, init_data_to_test_hasher):
        h = Hasher(1, init_data_to_test_hasher)
        print(h.__hash__())
        assert type(h.__hash__()) == str

    def test_entropy(self, init_data_to_test_hasher):
        h = Hasher(1, init_data_to_test_hasher, word_count_in_hash=3, number_of_hashes=1_000_000)
        assert len(set(h.__hash__())) == 1_000_000

    def test_eq_hash(self, init_data_to_test_hasher):
        h1 = Hasher(1, init_data_to_test_hasher)
        h2 = Hasher(1, init_data_to_test_hasher)
        assert h1.__hash__() == h2.__hash__()
