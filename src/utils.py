def filter_vacancies(vacancies: list, filter_words: list) -> list:
    """Фильтрует вакансии по ключевым словам"""
    return [
        v
        for v in vacancies
        if v.get("description") and any(word.lower() in v["description"].lower() for word in filter_words)
    ]


def get_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    """Получает вакансии в заданном диапазоне зарплат."""
    min_salary, max_salary = map(int, salary_range.split("-"))
    filtered_vacancies = []

    for v in vacancies:
        salary = v["salary"]
        if isinstance(salary, dict):
            salary_from = salary.get("from", 0) or 0
            salary_to = salary.get("to", float("inf")) or float("inf")
            if (salary_from >= min_salary and salary_from <= max_salary) or (
                salary_to >= min_salary and salary_to <= max_salary
            ):
                filtered_vacancies.append(v)

    return filtered_vacancies


def sort_vacancies(vacancies: list) -> list:
    """Сортирует вакансии по зарплате."""
    return sorted(
        vacancies,
        key=lambda x: (
            (x["salary"].get("to") if isinstance(x["salary"], dict) else 0) or 0,
            (x["salary"].get("from") if isinstance(x["salary"], dict) else 0) or 0,
        ),
        reverse=True,
    )


def get_top_vacancies(vacancies: list, n: int) -> list:
    """Получает топ n вакансий"""
    return vacancies[:n]


def print_vacancies(vacancies):
    """Выводит вакансии"""
    for v in vacancies:
        print(v)
