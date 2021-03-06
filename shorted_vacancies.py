import work_with_file as helpers

if __name__ == '__main__':
    source_path = input('Please input path to a source file: ')
    final_path = input('Please input path to a destination file: ')
    list_of_vacancies = helpers.read_from_file(source_path)
    shorted_vacancies = {}

    for vacancy in list_of_vacancies:
        shorted_vacancies[vacancy] = {'profession': list_of_vacancies[vacancy]['profession'],
                                      'candidat': list_of_vacancies[vacancy]['candidat']
                                      }

        if list_of_vacancies[vacancy]['payment']:
            shorted_vacancies[vacancy]['payment'] = list_of_vacancies[vacancy]['payment']
        elif not list_of_vacancies[vacancy]['payment_from'] == 0 and not list_of_vacancies[vacancy]['payment_from'] == 0:
            shorted_vacancies[vacancy]['payment'] = (list_of_vacancies[vacancy]['payment_from'] + list_of_vacancies[vacancy]['payment_from']) / 2
        else:
            shorted_vacancies[vacancy]['payment'] = list_of_vacancies[vacancy]['payment_from']

    helpers.save_to_file(final_path, shorted_vacancies)
    print('Vacancies saved!')