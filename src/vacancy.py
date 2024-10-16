class Vacancy:
    __slots__ = ("title", "url", "salary", "description")

    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description

    def _validate_salary(self, salary):
        """Проверяет корректность зарплаты"""
        return salary if salary else "Зарплата не указана"

    def __lt__(self, other):
        """Сравнивает зарплату с другими вакансиями"""
        return self.salary < other.salary

    def to_dict(self):
        """Преобразовывает объект вакансии в словарь"""
        return {"title": self.title, "url": self.url, "salary": self.salary, "description": self.description}

    @classmethod
    def cast_to_object_list(cls, data):
        """Преобразовsdftn список данных в список объектов вакансий."""
        return [
            cls(item["name"], item["alternate_url"], item["salary"], item.get("snippet", {}).get("requirement", ""))
            for item in data
        ]
