from src.hh_api  import HH
from src.vacancy import Vacancy
from src.json_saver import JsonSaver
from src.utils import filter_vacancies, get_vacancies_by_salary, get_top_vacancies, sort_vacancies, print_vacancies


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    hh_api = HH()
    json_saver = JsonSaver()

    search_query = input("Введите поисковый запрос: ")


    vacancies_list = hh_api.get_vacancies(search_query)


    if not vacancies_list:
        print("Вакансии не найдены.")
        return

    for item in vacancies_list:
        if item is not None:
            salary = item.get('salary', {})
            vacancy = Vacancy(
                item['name'],
                item['alternate_url'],
                salary.get('from', None),
                item.get('snippet', {}).get('requirement', '')
            )
            json_saver.add_vacancy(vacancy)


    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (например, 100000 - 150000): ")

    filtered_vacancies = filter_vacancies(json_saver.get_vacancies(), filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)

if __name__ == "__main__":
    user_interaction()