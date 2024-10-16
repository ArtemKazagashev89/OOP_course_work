from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, sort_vacancies


def test_filter_vacancies():
    vacancies = [
        {"title": "Вакансия 1", "description": "Требуется водитель"},
        {"title": "Вакансия 2", "description": "Ищем тестировщика"},
        {"title": "Вакансия 3", "description": None},
    ]
    filter_words = ["водитель"]
    result = filter_vacancies(vacancies, filter_words)
    assert len(result) == 1
    assert result[0]["title"] == "Вакансия 1"


def test_get_vacancies_by_salary():
    vacancies = [
        {"title": "Вакансия 1", "salary": {"from": 100000, "to": 150000}},
        {"title": "Вакансия 2", "salary": {"from": 200000, "to": 250000}},
        {"title": "Вакансия 3", "salary": {"from": None, "to": None}},
    ]
    salary_range = "100000 - 200000"
    result = get_vacancies_by_salary(vacancies, salary_range)
    assert len(result) == 2
    assert result[0]["title"] == "Вакансия 1"


def test_sort_vacancies():
    vacancies = [
        {"title": "Вакансия 1", "salary": {"from": 100000, "to": 150000}},
        {"title": "Вакансия 2", "salary": {"from": 200000, "to": 250000}},
        {"title": "Вакансия 3", "salary": {"from": 150000, "to": 180000}},
    ]
    sorted_vacancies = sort_vacancies(vacancies)
    assert sorted_vacancies[0]["title"] == "Вакансия 2"  # Самая высокая зарплата


def test_get_top_vacancies():
    vacancies = [{"title": "Вакансия 1"}, {"title": "Вакансия 2"}, {"title": "Вакансия 3"}]
    top_n = 2
    result = get_top_vacancies(vacancies, top_n)
    assert len(result) == 2
