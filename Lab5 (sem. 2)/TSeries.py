from abc import ABC, abstractmethod

class TSeries(ABC):
    def __init__(self, first_term: float):
        __first_term = first_term

    @abstractmethod
    def get_nth_term(self, n: int) -> float:
        pass

    @abstractmethod
    def get_sum_of_n_terms(self, n: int) -> float:
        pass