from abc import ABC, abstractmethod

class TSeries(ABC):
    @abstractmethod
    def calculate_nth_term(self, n: int) -> float:
        pass

    @abstractmethod
    def calculate_sum_of_n_terms(self, n: int) -> float:
        pass

    def get_nth_term(self, n: int) -> float:
        if n <= 0:
            raise ValueError("n must be positive int")
        return self.calculate_nth_term(n)

    def get_sum_of_n_terms(self, n: int) -> float:
        if n <= 0:
            raise ValueError("n must be positive int")
        return self.calculate_sum_of_n_terms(n)