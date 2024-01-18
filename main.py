from classes import HeadHunterAPI, SuperJobAPI, JSONSaver
from utils import sample_by_salary_to, sample_by_salary_from, get_all_found_vacancies, get_top_N_vacancies_by_salary

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
json_saver = JSONSaver()


def user_interaction():
    user_answer = int(input(f''' Где искать вакансии? \n1. HeadHunter\n2. SuperJob\n'''))
    user_answer_keyword = input(' Ключевое слово\n')

    hh_vacancies = hh_api.get_vacancies(user_answer_keyword)
    superjob_vacancies = superjob_api.get_vacancies(user_answer_keyword)
    json_saver.add_vacancy(hh_vacancies)
    json_saver.add_vacancy(superjob_vacancies)

    user_answer_action = int(input(""" Выберите действие: \n1. Выборка по зарплате (мах)\n2. Выборка по зарплате (мин)
3. Получить все найденные вакансии\n4. Получить топ N вакансий по зарплате\n"""))

    if user_answer_action == 1:
        if user_answer == 1:
            return sample_by_salary_to(hh_vacancies, user_answer)
        elif user_answer == 2:
            return sample_by_salary_to(superjob_vacancies, user_answer)
        else:
            user_interaction()

    if user_answer_action == 2:
        if user_answer == 1:
            return sample_by_salary_from(hh_vacancies, user_answer)
        elif user_answer == 2:
            return sample_by_salary_from(superjob_vacancies, user_answer)
        else:
            user_interaction()

    if user_answer_action == 3:
        if user_answer == 1:
            return get_all_found_vacancies(hh_vacancies, user_answer)
        elif user_answer == 2:
            return get_all_found_vacancies(superjob_vacancies, user_answer)
        else:
            user_interaction()

    if user_answer_action == 4:
        if user_answer == 1:
            return get_top_N_vacancies_by_salary(hh_vacancies, user_answer)
        elif user_answer == 2:
            return get_top_N_vacancies_by_salary(superjob_vacancies, user_answer)
        else:
            user_interaction()
    else:
        print("Вы не выбрали действие")

if __name__ == "__main__":
    user_interaction()