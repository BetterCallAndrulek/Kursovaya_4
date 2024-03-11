from src.vacancy import Vacancy
from src.jsonsaver import JSONSaver

'''Class JSONSaver test'''
def test_show_add_delete_vacancy():
    count = 0
    jsonsaver = JSONSaver()
    before = jsonsaver.show()
    vacancy1 = Vacancy('Volodya', 'aya', 'aya', 'Hochu Rabotat')
    vacancy2 = Vacancy('Vanya', 'dada', 'dada', 'I ya toshe...')
    jsonsaver.add_vacancy(vacancy1.__dict__)
    jsonsaver.add_vacancy(vacancy2.__dict__)
    for i in jsonsaver.show():
        if i['description'] == 'Hochu Rabotat' or i['description'] == 'I ya toshe...':
            count += 1
    assert count == 2
    jsonsaver.delete_vacancy(vacancy1.__dict__)
    jsonsaver.delete_vacancy(vacancy2.__dict__)
    assert before == jsonsaver.show()