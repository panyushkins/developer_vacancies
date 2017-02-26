import work_with_file
import helpers

if __name__ == '__main__':
    languages = {'Swift': {'number': 0, 'total_payment': 0},
                 'C++': {'number': 0, 'total_payment': 0},
                 'SQL': {'number': 0, 'total_payment': 0},
                 'Python': {'number': 0, 'total_payment': 0},
                 'C#': {'number': 0, 'total_payment': 0},
                 'Java': {'number': 0, 'total_payment': 0},
                 'PHP': {'number': 0, 'total_payment': 0},
                 'Other': {'number': 0, 'total_payment': 0}}

    vacancies = work_with_file.read_from_file(input('Please input path to a source file: '))

    helpers.add_lang_to_vacancies(vacancies, languages)
    helpers.count_vacancies_per_lang(vacancies, languages)
    helpers.add_total_payment_per_lang(vacancies, languages)
    helpers.avg_payment_per_lang(languages)
    helpers.print_stats(languages)
    helpers.show_plot(languages)
