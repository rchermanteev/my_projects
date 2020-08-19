from ..utils import get_vocabulary


class TestUtils:
    def test_get_vocabulary(self):
        test_vocabulary = get_vocabulary()
        assert type(test_vocabulary) is dict
        assert test_vocabulary is not None
