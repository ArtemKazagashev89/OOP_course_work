from abc import ABC, abstractmethod


class FileHandler(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> list:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy) -> None:
        pass
