class groups():
    def __init__(self, group_number, number_of_people):
        self.group_number = group_number
        self.number_of_people = number_of_people
        self.lessons = 4
    def Report(self):
        print('В группе ' + str(self.group_number) + ' на ' + str(self.lessons) + ' пары пришло ' + str(self.number_of_people) + ' человек(а).')

group1 = groups('11-210', 8)
group2 = groups('11-209', 11)

print(group1.group_number)
print(group1.number_of_people)
print(group2.lessons)

group1.Report()
group2.Report()
