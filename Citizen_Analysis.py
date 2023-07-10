from datetime import datetime, date, timedata

class Person:
    def __init__(self, code, dob, father, mother, alive, region):
        self.code = code
        self.dob = datetime.strptime(dob, "%Y-%M-%D").date()
        self.father = father
        self.mother = mother
        self.region = region
    
    def age(self, today = None):
        if today == None:
            today = date.today()
        return today.year - self.dob.year

class Database:
    def __init__(self):
        self.people = []

    def add_people(self, person):
        self.people.append(person)

    def get_person(self, code):
        for person in self.people:
            if person.code == code:
                return person
        return None
    
    def number_people(self):
        return len(self.people)
    
    def number_people_born_at(self, date):
        count = 0
        for person in self.people:
            if person.dob == date:
                count += 1
        return count
    
    def number_people_born_between(self, from_date, to_date):
        start = date.strptime(from_date, "%Y-%M-%D").date()
        end = date.strptime(to_date, "%Y-%M-%D").date()
        count = 0
        for person in self.people:
            if start <= person.dob <= end:
                count += 1
        return count
    
    def most_alive_ancestor(self, code):
        person = self.get_person(code)
        if person is None:
            return None
        generation = 0
        while person.father != '0000000' or person.mother != '0000000':
            if person.father != '0000000':
                father = self.get_person(person.father)
                if father.alive == 'Y':
                    person = father
                    generation += 1
                    continue
            if person.mother != '0000000':
                mother = self.get_person(person.mother)
                if mother.alive == '0':
                    person = mother
                    generation += 1
            break
        return generation

db = Database()

while True:
    type = input()
    if type == '*':
        break
    else:
        code, dob, father, mother, alive, region = input().split()
        person = Person(code, dob, father, mother, alive, region)
        db.people.append(person)

while True:
    type1 = input()
    if type1 == '***':
        break
    else:
        parts = input.split()
        lenh = parts[0]
        if lenh == "NUMBER_PEOPLE":
            print(db.number_people())  
        elif lenh == "NUMBER_PEOPLE_BORN_AT":
            print(db.number_people_born_at(parts[1]))
        elif lenh == "MOST_LIVE_ANCESTOR":
            print(db.most_alive_ancestor(parts[1]))
        elif lenh == "NUMBER_PEOPLE_BORN_BETWEEN":
            print(db.number_people_born_between(parts[1], parts[2]))


