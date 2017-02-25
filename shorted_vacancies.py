import work_with_file as helpers

source_path = 'dict.txt'  # input('Please input path to a source file: ')
final_path = 'dict2.txt'  # input('Please input path to a destination file: ')
list_of_vacancies = helpers.read_from_file(source_path)
shorted_vacancies = {}

for vacancy in list_of_vacancies:
    shorted_vacancies[vacancy] = {'profession': list_of_vacancies[vacancy]['profession'],
                                  'candidat': list_of_vacancies[vacancy]['candidat'],
                                  'payment': list_of_vacancies[vacancy]['payment'],
                                  'payment_from': list_of_vacancies[vacancy]['payment_from'],
                                  'payment_to': list_of_vacancies[vacancy]['payment_to']
                                  }

helpers.save_to_file(final_path, shorted_vacancies)
print('Vacancies saved!')