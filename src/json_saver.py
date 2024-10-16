import json

from src.file_handler import FileHandler


class JsonSaver(FileHandler):

    def __init__(self, filename="vacancies.json"):
        self._filename = filename
        self.vacancies = self.load_vacancies()

    def load_vacancies(self) -> list:
        """Загружает вакансии из файла"""
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_vacancies(self) -> None:
        """Cохраняет вакансии в файл"""
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy) -> None:
        """Добавляет вакансии в файл"""
        if not any(v["title"] == vacancy.title for v in self.vacancies):
            self.vacancies.append(vacancy.to_dict())
            self.save_vacancies()

    def get_vacancies(self) -> list:
        """Получает все вакансии"""
        return self.vacancies

    def delete_vacancy(self, vacancy) -> None:
        self.vacancies = [v for v in self.vacancies if v["title"] != vacancy.title]
        self.save_vacancies()
