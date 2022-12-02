
class Character:
    def __init__(self, type_character='Бродяга', hp=250, battle_cry='-ТЕ, КТО ОСТАНУТСЯ В ЖИВЫХ, БУДУТ ЗАВИДОВАТЬ МЕРТВЫМ!'):
        self.type_character = type_character
        self.battle_cry = battle_cry
        self.hp = hp
        self.count = 0
        self.heal = 40

    def first_quest(self):
        print(f'Привет {self.type_character}, рады тебя видеть! Помоги нам одолеть банду разбойников.')


class Battle(Character):

    def first_quest(self):
        super().__init__()
        print(f'Хорошо, но за помощь вы должны заплатить. А то мои {self.hp} очков здоровья скоро начнут исчезать....')
        print(self.battle_cry)

    def kick(self, k):
        self.hp -= k
        print(f'Очков здоровья - {self.hp}')

    def say_ending_battle_cry(self):
        self.battle_cry = '-Ура победа!'
        print(self.battle_cry)
        self.count += 1


class Prop(Battle or Character):
    def __init__(self, x=20):
        super().__init__()
        self.x = x

    def healing(self, x):
        if x <= self.heal:
            self.hp += x
            self.heal -= x
            print(f'Здоровье восстановлено на {str(x)}. Итого здоровья - {self.hp}')


class Ending(Prop):

    def first_quest(self):
        if self.count == 1:
            print('-Спасибо что помогли храбрый воин! Вот обещанная награда')

    def heald(self):
        print(f'Очков исцеления - {str(self.heal)}')


first_step = Character('Викинг')
second_step = Battle()
third_step = Ending()
step = Prop(250)

first_step.first_quest()
second_step.first_quest()
second_step.kick(34)
second_step.say_ending_battle_cry()
step.healing(23)
third_step.first_quest()
third_step.heald()
