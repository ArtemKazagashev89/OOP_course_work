from abc import ABC, abstractmethod


class API(ABC):
    @abstractmethod
    def get_vacancies(self, query):
        pass
