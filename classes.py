from abc import ABC, abstractmethod
import requests
import json


class Api(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями """

    @abstractmethod
    def get_vacancies(self, argument):
        pass

    def sort_vacancies_city(self, keyword, answer):
        pass


class HeadHunterAPI(Api):
    """ Класс, наследующиеся от абстрактного класса, для работы с платформой HeadHunter """

    def get_vacancies(self, argument):
        params = {
            "text": argument,
            "per_page": 100,
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        response_text = response.json()
        return response_text['items']

    def sort_vacancies_city(self, keyword: str, answer: str):
        filter_list = []
        vacancy = self.get_vacancies(keyword)
        for i in vacancy:
            if i['area']['name'] == answer.title():
                filter_list.append(vacancy)
            else:
                continue
        return filter_list


class SuperJobAPI(Api):
    """ Класс, наследующиеся от абстрактного класса, для работы с платформой SuperJob """

    def get_vacancies(self, argument):
        HEADERS = {"X-Api-App-Id": "v3.r.137779454.03a3101e56ddef6574069e8514f18708821f164d.727f7a2952779f32e69e2bd4e8703c8f6dcf6518"}
        params = {
                  'keyword': argument,
                  'count': 100    # Кол-во вакансий на 1 странице
                    }
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=HEADERS, params=params)
        response_text = response.json()
        return response_text['objects']


class Vacancy:
    """
    Класс для работы с вакансиями
    Атрибуты - название вакансии, ссылка на вакансию, зарплата, требования
    Методы - сравнение вакансий между собой по зарплате и валидация данных
    """

    def __init__(self, job_title, area_name, salary, job_url):
        self.job_title = job_title
        self.area_name = area_name
        self.salary = salary
        self.job_url = job_url

    def __str__(self):
        return f"{self.job_title}, {self.area_name}, {self.salary}, {self.job_url}"

    def __gt__(self, other):
        return self.salary > other.salary


class JSONSaver_abc(ABC):
    """
    Абстрактный класс, который имеет методы - добавления вакансий в файл,
    получения данных из файла по указанным критериям,
    удаления информации о вакансиях
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass


class JSONSaver(JSONSaver_abc):
    """ Класс для сохранения информации о вакансиях в JSON-файл """

    def add_vacancy(self, vacancy):
        with open('vacancy.txt', 'w', encoding='utf-8') as file:
            s = json.dumps(vacancy, ensure_ascii=False)
            file.write(s)