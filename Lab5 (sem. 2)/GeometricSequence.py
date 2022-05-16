from TSeries import *

class GeometricSequence(TSeries):
    def __init__(self, first_term: float = None, common_ratio: float = None):
        if first_term:
            self.__first_term = first_term
        else:
            self.__first_term = 0

        if common_ratio:
            if common_ratio != 0.0:
                self.__common_ratio = common_ratio
            else:
                raise ValueError("common ratio must not be equal to 0")
        else:
            self.__common_ratio = 0

    def calculate_nth_term(self, n: int) -> float:
        nth_term = self.__first_term * self.__common_ratio ** (n - 1)
        return nth_term

    def calculate_sum_of_n_terms(self, n: int) -> float:
        if self.__common_ratio != 1:
            sum_of_n_terms = self.__first_term * (self.__common_ratio ** n - 1) / (self.__common_ratio - 1)
        else:
            sum_of_n_terms = self.__first_term * n
        return sum_of_n_terms

    @property
    def first_term(self) -> float:
        return self.__first_term

    @first_term.setter
    def first_term(self, f: float) -> None:
        self.__first_term = f

    @property
    def common_ratio(self) -> float:
        return self.__common_ratio

    @common_ratio.setter
    def common_ratio(self, c: float) -> None:
        if c != 0.0:
            self.__common_ratio = c
        else:
            raise ValueError("common ratio must not be equal to 0")
                
