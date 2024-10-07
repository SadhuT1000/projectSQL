import requests


class HH:
    """Класс работы с API hh"""

    def __init__(self):
        self.__url = "https://api.hh.ru"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"per_page": 100, "page": 0, "only_with_salary": True}
        self.employers = [
            9694561,
            4219,
            5919632,
            5667343,
            9301808,
            774144,
            10571093,
            198614,
            6062708,
            78638,
        ]

    def get_employers(self):
        """Загрузка работодателей"""
        list_employers = []
        for employer_id in self.employers:
            temp_url = f"{self.__url}/employers/{employer_id}"
            employer_data = requests.get(temp_url).json()
            list_employers.append(employer_data)

        return list_employers

    def load_vacancies(self):
        """Загрузка вакансий"""
        list_vacancy = []
        for employer_id in self.employers:
            self._params["employer_id"] = employer_id
            vacancy_url = f"{self.__url}/vacancies"
            response = requests.get(
                vacancy_url, headers=self._headers, params=self._params
            )
            vacancies = response.json()["items"]
            list_vacancy.extend(vacancies)

        return list_vacancy
