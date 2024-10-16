import pytest

from src.json_saver import JsonSaver
from src.vacancy import Vacancy


@pytest.fixture
def json_saver():
    return JsonSaver(filename="test_vacancies.json")


def test_add_vacancy(json_saver):
    vacancy = Vacancy("Вакансия 1", "http://example.com", 100000, "Описание 1")
    json_saver.add_vacancy(vacancy)
    vacancies = json_saver.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]["title"] == "Вакансия 1"


def test_delete_vacancy(json_saver):
    vacancy = Vacancy("Вакансия 2", "http://example.com", 100000, "Описание 2")
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)
    vacancies = json_saver.get_vacancies()
    assert len(vacancies) == 1
