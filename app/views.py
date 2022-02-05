import random
from django.shortcuts import render
from django.views.generic import TemplateView


class Main():
    def index(self):
        if self.session.session_key == None:
            self.session.cycle_key()
        return render(self, 'start.html')

    def start(self):
        return render(self, 'index.html')


class MagicPeople1():

    def __init__(self, name):
        self.name = name
        self.answer_history = []

    def answer(self):
        answer = self.random_number()
        self.answer_history.append(answer)
        return answer

    def random_number(self):
        return random.randint(10, 99)










"""


class MagicPeople(Main):
    def magic(self):
        object_for_people = ['Адам', 'Евген']
        self.session['magicpeople'] = object_for_people
        magicpeople = self.session.get('magicpeople')
        return magicpeople


class Functions(MagicPeople):
    def randfunc(self):
        magic_people = self.session.get('magicpeople')
        if magic_people == None:
            magic_people = MagicPeople.magic(self)
        else:
            pass
        object_for_answer = []
        for item in magic_people:
            rand = random.randint(10, 99)
            object_for_answer.append(rand)
        self.session['magicanswer'] = object_for_answer
        magic_answer = self.session.get('magicanswer')
        magic_people_answer = dict(zip(magic_people, magic_answer))
        true_answer = self.session.get('true_answer', 0)
        true_answer2 = self.session.get('true_answer2', 0)
        right_answer = self.session.get('right_answer', 0)
        right_answer2 = self.session.get('right_answer2', 0)
        true_answer_all = [true_answer, true_answer2]
        right_answer_all = [right_answer, right_answer2]
        context = {
            'all_answer': magic_people_answer,
            'true_answer_all': true_answer_all,
            'right_answer_all': right_answer_all,
        }
        return render(self, 'index.html', context)

    def check(self):
        """ #Получение данных для вывода на страницу"""
"""
        mstnmb = int(self.GET['fnmb'])
        magic_answer = self.session.get('magicanswer')
        magic_people = self.session.get('magicpeople')
        """ #Ранее загаданные числа """
"""
        history_of_number = []
        history_of_number_all = self.session.get('history_of_number')
        len_history = len(str(history_of_number_all))
        if len_history == 2:
            history_of_number.append(history_of_number_all)
        else:
            pass
        if history_of_number_all == None:
            history_of_number.append(mstnmb)
            self.session['history_of_number'] = mstnmb
        elif len_history == 2:
            history_of_number.append(mstnmb)
            test = history_of_number
            self.session['history_of_number'] = test
        else:
            history_of_number = history_of_number_all
            history_of_number.append(mstnmb)
        """#История ответов экстрасенсов"""
"""
        history_of_answer = []
        history_of_number_all_answer = self.session.get('history_of_answer')
        if history_of_number_all_answer == None:
            for item in magic_answer:
                history_of_answer.append(item)
                self.session['history_of_answer'] = history_of_answer
        else:
            for item in magic_answer:
                history_of_answer = history_of_number_all_answer
                history_of_answer.append(item)

        history_first = []
        history_second = []
        history_first_all = self.session.get('history_first')
        history_second_all = self.session.get('history_second')
        if history_first_all == None:
            history_first.append(magic_answer[0])
            self.session['history_first'] = history_first
            history_second.append(magic_answer[1])
            self.session['history_second'] = history_second
        else:
            history_first = history_first_all
            history_second = history_second_all
            history_first.append(magic_answer[0])
            self.session['history_first'] = history_first
            history_second.append(magic_answer[1])
            self.session['history_second'] = history_second
        """#Достоверность и колличесво угадывания"""
"""
        true_answer = self.session.get('true_answer', 0)
        true_answer2 = self.session.get('true_answer2', 0)
        right_answer = self.session.get('right_answer', 0)
        right_answer2 = self.session.get('right_answer2', 0)
        count = 0
        for item in magic_answer:
            count += 1
            if mstnmb == item:
                if count == 1:
                    true_answer = self.session.get('true_answer', 0)
                    self.session['true_answer'] = true_answer + 1
                    right_answer = self.session.get('right_answer', 0)
                    self.session['right_answer'] = right_answer + 1
                else:
                    true_answer2 = self.session.get('true_answer2', 0)
                    self.session['true_answer2'] = true_answer2 + 1
                    right_answer2 = self.session.get('right_answer2', 0)
                    self.session['right_answer2'] = right_answer2 + 1
            else:
                if count == 1:
                    true_answer = self.session.get('true_answer', 0)
                    self.session['true_answer'] = true_answer - 1
                else:
                    true_answer2 = self.session.get('true_answer2', 0)
                    self.session['true_answer2'] = true_answer2 - 1

        magic_people_answer = dict(zip(magic_people, magic_answer))
        true_answer_all = [true_answer, true_answer2]
        right_answer_all = [right_answer, right_answer2]
        self.session['number'] = mstnmb
        number = self.session.get('number', 0)
        context = {
            'mstnmb': number,
            'all_answer': magic_people_answer,
            'history_number': history_of_number,
            'true_answer_all': true_answer_all,
            'right_answer_all': right_answer_all,
            'history_first': history_first,
            'history_second': history_second,
        }
        return render(self, 'index.html', context)
"""