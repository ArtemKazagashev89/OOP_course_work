import requests

from src.abc_api import API


class HH(API):
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query: str) -> list:
        """Получает вакансии с платформы hh.ru по заданному запросу."""
        params = {"text": query, "per_page": 50}
        response = self._request_api(params)
        return response.get("items", [])

    def _request_api(self, params: dict) -> dict:
        """Отправляет запрос к API hh.ru"""
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
