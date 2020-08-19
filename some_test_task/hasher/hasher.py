class Hasher:
    def __init__(self,
                 object,
                 vocabulary: dict,
                 word_count_in_hash: int = 1,
                 separator: str = "",
                 number_of_hashes: int = 1):

        self._object = str(object)
        self._vocabulary = vocabulary
        self._size_vocabulary = len(vocabulary) - 1

        if 1 <= word_count_in_hash <= 10:
            self._word_count_in_hash = word_count_in_hash
        else:
            raise ValueError("Введите корректное число слов в хэше (1 - 10)")

        self._separator = separator
        self._number_of_hashes = number_of_hashes

    def _get_hash(self, obj):
        if self._word_count_in_hash == 1:
            return self._vocabulary[hash(obj) % self._size_vocabulary]
        else:
            list_words = [self._vocabulary[hash(obj + f"{noise}") % self._size_vocabulary] for
                          noise in range(self._word_count_in_hash)]
            return f"{self._separator}".join(list_words)

    def __hash__(self):
        if self._number_of_hashes == 1:
            return self._get_hash(self._object)
        else:
            return [self._get_hash(self._object + f"{shift}") for shift in range(self._number_of_hashes)]
