import pylab as plt
import numpy as np


def add_lang_to_vacancies(vacancies_dict, lang_dict):
    for vac in vacancies_dict:
        vacancies_dict[vac]['type'] = []
        for lang in lang_dict:
            if not vacancies_dict[vac]['profession'].find(lang) == -1:
                vacancies_dict[vac]['type'].append(lang)

            elif vacancies_dict[vac]['candidat'] and not vacancies_dict[vac]['candidat'].find(lang) == -1:
                vacancies_dict[vac]['type'].append(lang)


def add_total_payment_per_lang(dict_vacancies, dict_lang_stats):
    for vacancy in dict_vacancies:

        if len(dict_vacancies[vacancy]['type']) == 0:
            dict_lang_stats['Other']['total_payment'] += dict_vacancies[vacancy]['payment']
        else:
            for lang_vacancy in dict_vacancies[vacancy]['type']:
                for lang_dict in dict_lang_stats:
                    if lang_vacancy == lang_dict:
                        dict_lang_stats[lang_dict]['total_payment'] += dict_vacancies[vacancy]['payment']


def count_vacancies_per_lang(dict_vacancies, dict_lang_stats):
    for vacancy in dict_vacancies:

        if len(dict_vacancies[vacancy]['type']) == 0:
            dict_lang_stats['Other']['number'] += 1
        else:
            for lang_vacancy in dict_vacancies[vacancy]['type']:
                for lang_dict in dict_lang_stats:
                    if lang_vacancy == lang_dict:
                        dict_lang_stats[lang_dict]['number'] += 1


def avg_payment_per_lang(dict_lang_stats):
    for lang in dict_lang_stats:
        dict_lang_stats[lang]['avg_payment'] = int(dict_lang_stats[lang]['total_payment']) \
                                               / int(dict_lang_stats[lang]['number'])


def print_stats(dict_lang_stats):
    for lang in dict_lang_stats:
        print('%s - %i' % (lang, dict_lang_stats[lang]['avg_payment']))


def show_plot(dict_lang_stats):
    y_data = []
    objects = []

    for lang in dict_lang_stats:
        objects.append(lang)
        y_data.append(languages[lang]['avg_payment'])

    y_pos = np.arange(len(objects))
    plt.bar(y_pos, y_data, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Salary')
    plt.title('Programming language salary')

    plt.show()
