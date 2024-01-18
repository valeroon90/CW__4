from classes import Vacancy


def sample_by_salary_to(api_vac, user_choice): # Функция выборки по зарплате (мах)
    if user_choice == 1:
        vac = [v for v in api_vac if v.get('salary') is not None and v.get('salary').get('to') is not None]
        vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['to'],
                       area_name=v['area']['name']) for v in vac]

        vac = sorted(vac, reverse=True)
        [print(v) for v in vac]

    elif user_choice == 2:
        vac = [Vacancy(job_title=v['profession'], job_url=v['link'], salary=v['payment_to'],
                       area_name=v['town']['title']) for v in api_vac]

        vac = sorted(vac, reverse=True)
        [print(v) for v in vac]


def sample_by_salary_from(api_vac, user_choice): # Функция выборки по зарплате (мин)
    if user_choice == 1:
        vac = [v for v in api_vac if v.get('salary') is not None and v.get('salary').get('from') is not None]
        vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
                       area_name=v['area']['name']) for v in vac]

        vac = sorted(vac, reverse=True)

        [print(v) for v in vac]
    elif user_choice == 2:
        vac = [Vacancy(job_title=v['profession'], job_url=v['link'], salary=v['payment_from'],
                       area_name=v['town']['title']) for v in api_vac]

        vac = sorted(vac, reverse=True)
        [print(v) for v in vac]


def get_all_found_vacancies(api_vac, user_choice): # Функция получить все найденные вакансии
    if user_choice == 1:
        vac = [v for v in api_vac if v.get('salary') is not None and v.get('salary').get('from') is not None]
        vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
                       area_name=v['area']['name']) for v in vac]

        [print(v) for v in vac]
    elif user_choice == 2:
        vac = [Vacancy(job_title=v['profession'], job_url=v['link'], salary=v['payment_from'],
                       area_name=v['town']['title']) for v in api_vac]

        [print(v) for v in vac]


def get_top_N_vacancies_by_salary(api_vac, user_choice): # Функция получить топ N вакансий по зарплате
    top_n = int(input('Введите N\n'))
    if user_choice == 1:
        vac = [v for v in api_vac if v.get('salary') is not None and v.get('salary').get('from') is not None]
        vac = [Vacancy(job_title=v['name'], job_url=v['alternate_url'], salary=v['salary']['from'],
                       area_name=v['area']['name']) for v in vac]
        vac = sorted(vac, reverse=True)

        [print(v) for v in vac[:top_n]]
    elif user_choice == 2:
        vac = [Vacancy(job_title=v['profession'], job_url=v['link'], salary=v['payment_from'],
                       area_name=v['town']['title']) for v in api_vac]
        vac = sorted(vac, reverse=True)

        [print(v) for v in vac[:top_n]]