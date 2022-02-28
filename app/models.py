import random
from pynames import GENDER, LANGUAGE
from pynames.generators.elven import DnDNamesGenerator

elven_generator = DnDNamesGenerator()


class MagicPeople:

    def __init__(self):
        self.name = elven_generator.get_name_simple(GENDER.MALE, LANGUAGE.RU)
        self.answer_history = {}
        self.answer = {}
        self.trust_value = {}

    def answer_random(self, name):
        self.answer[name] = random.randint(10, 99)
        all_answer = self.answer_history.setdefault(name, [])
        all_answer.append({'answer_history': self.answer[name]})

    def raiting(self, name):
        return self.trust_value.setdefault(name, 0)

    def change_raiting(self, name, number):
        self.trust_value[name] = self.raiting(name) + number

    def check(self, user_answer, name):
        if user_answer == self.answer[name]:
            self.change_raiting(name, 1)
        else:
            self.change_raiting(name, -1)


class Controller:

    def __init__(self):
        self.magicpeople = [MagicPeople() for i in range(2, 6)]

    def answer(self, name):
        return [{
            'psy_name': item.name,
            'psy_num': item.answer_random(name),

        } for item in self.magicpeople]

    def check(self, number, name):
        for item in self.magicpeople:
            item.check(number, name)
        return self.add_all(name)

    def add_answer(self, name):
        for item in self.magicpeople:
            item.answer_random(name)
        return self.add_all(name)

    def add_all(self, name):
        return [{
            'magic_name': item.name,
            'magic_number': item.answer_history.get(name),
            'magic_trust': item.raiting(name),
        } for item in self.magicpeople]
