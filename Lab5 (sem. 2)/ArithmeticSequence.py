from TSeries import *

class ArithmeticSequence(TSeries):
    def __init__(self, first_term: float = None, common_difference: float = None):
        if first_term:
            self.__first_term = first_term
        else:
            self.__first_term = 0

        if common_difference:
            self.__common_difference = common_difference
        else:
            self.__common_difference = 0

    def calculate_nth_term(self, n: int) -> float:
        nth_term = self.__first_term + self.__common_difference * (n - 1)
        return nth_term

    def calculate_sum_of_n_terms(self, n: int) -> float:
        sum_of_n_terms = (self.__first_term + self.calculate_nth_term(n)) * n / 2
        return sum_of_n_terms

    @property
    def first_term(self) -> float:
        return self.__first_term

    @first_term.setter
    def first_term(self, f: float) -> None:
        self.__first_term = f

    @property
    def common_difference(self) -> float:
        return self.__common_difference

    @common_difference.setter
    def common_difference(self, c: float) -> None:
        self.__common_difference = c