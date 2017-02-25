from work_with_api import make_superjob_request
from work_with_file import save_to_file

api_key = input('Please, enter your Superjob API key:')
file_path = input('Please, input a path for file with results: ')
dict_of_vacancies = {}

for times_of_requests in range(10):
    parameters = {'keyword': 'разработчик', 'page': times_of_requests}
    returned_vacancies = make_superjob_request(api_key, 'vacancies', parameters)
    for vacancy in returned_vacancies['objects']:
        dict_of_vacancies[vacancy['id_client']] = vacancy

save_to_file(file_path, dict_of_vacancies)
print('File saved!')