from src.hh_api import HH


def test_get_vacancies():
    hh_api = HH()
    vacancies = hh_api.get_vacancies("водитель")
    assert isinstance(vacancies, list)
