from random import randint, random



class Tank:
    def __init__(self, health, damage, view_distance, coordinates, experience):
        self.health = health
        self.damage = damage
        self.view_distance = view_distance
        self.coordinates = coordinates
        self.experience = experience


    def move_tank_forward(self):
        self.coordinates += 10
        return self.coordinates

    def move_tank_backward(self):
        self.coordinates -= 10
        return self.coordinates

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class MyTank(Tank):

    def __init__(self, health, damage, view_distance, coordinates, experience, tank_level):
        super().__init__(health, damage, view_distance, coordinates, experience)
        self.tank_level = tank_level

    def spot_enemy(self, enemy):

        spot_enemy_phrases = ['Hold your fire! Enemy spotted!',
                              'We’ve got eyes on the target!',
                              'Contact! Enemy in sight!',
                              'Coordinates locked, Hostile detected!',
                              'Get ready, Enemy tank in range!']

        distance = abs(self.coordinates - enemy.coordinates)
        if distance <= self.view_distance:
            print(f'{spot_enemy_phrases[randint(0, len(spot_enemy_phrases) - 1)]} - {enemy.enemy_category}')
            return True
        else:
            return False


    def load_shell(self):

        load_ammo_phrases = ['Commander, what’s our shell choice? ',
                             'Commander, what round are we loading? ',
                             'Commander, which ammo type are we using? ',
                             'Sir, what’s the shell for this target? ',
                             'Commander, what’s the loadout? ']

        ammunition = ['he', 'ap', 'apcr']
        he_damage = randint(15, 20)
        ap_damage = randint(8, 12)
        apcr_damage = randint(6, 10)
        ammo_chosen = input(load_ammo_phrases[randint(0, len(load_ammo_phrases) - 1)])
        if ammo_chosen == ammunition[0]:
            self.damage = he_damage
            print(f'High-explosive selected – time to clear out soft targets!')
            return True
        if ammo_chosen == ammunition[1]:
            self.damage = ap_damage
            print(f'Armor-piercing loaded! We’re going for maximum damage!')
            return True
        if ammo_chosen == ammunition[2]:
            self.damage = apcr_damage
            print(f'Switching to APCR – we need speed and precision on this one!')
            return True



    # def upgrade_tank(self):
    #     i = 0
    #     exp_levels = [20, 40, 80]
    #     health_giver = 10
    #     damage_giver = 2
    #     if self.experience >= exp_levels[i]:
    #         self.health += health_giver
    #         self.damage += damage_giver
    #         self.experience -= exp_levels[i]
    #         i += 1
    #         health_giver += 5
    #         damage_giver += 1
    #     else:
    #         print('NO')


    def shoot(self, enemy):
        if self.spot_enemy(enemy) and self.load_shell():
            enemy.health -= self.damage
            self.experience += 5                    #expirience
            if enemy.is_alive():
                print(f'Got him, enemy got {self.damage}, he has left {enemy.health}')
                return enemy.health, self.experience
            else:
                print(f'Enemy destroyed')

    def tank_destroyed(self):
        if not self.is_alive():
            print('Tank destroyed!')



class Enemy(Tank):

    def __init__(self, health, damage, view_distance, coordinates, experience, enemy_id, enemy_category):
        super().__init__(health, damage, view_distance, coordinates, experience)
        self.enemy_id = enemy_id
        self.enemy_category = enemy_category

    def do_damage(self, my_tank):

        got_damage_phrases = ['We’re hit! Armor’s holding… barely.',
                             'Took a hit! Systems still operational.',
                             'Damage sustained! Brace for impact!',
                             'They got us! Minimal damage.',
                             'We’re taking fire! Hold steady!']

        if self.is_alive():
            distance = abs(my_tank.coordinates - self.coordinates)
            if self.view_distance >= distance:
                my_tank.health -= self.damage
                my_tank.experience += 2
                print(f' {got_damage_phrases[randint(0, len(got_damage_phrases)-1)]} -{self.damage} hp, we have {my_tank.health} hp left')
                return my_tank.health



def main():

    start_phrases = ['Engine’s coming to life.',
                     'Ignition ready, engine’s roaring!',
                     'Powering up! Let’s roll!',
                     'Engine online, we are ready to go!',
                     'Starting up… All systems check!']

    move_forward_phrases = ['Advancing forward, current GPS coordinates: ',
                            'Moving out! New heading: ',
                            'Pushing forward, destination locked at ',
                            'Rolling out, heading towards ',
                            'Moving ahead. Current coordinates: ']

    keys_to_move_forward = ['forward', 'w', 'go']

    keys_to_move_backward = ['backward', 's', 'back up']

    categories_of_enemys = ['Heavy tank', 'Tank destroyer', 'Medium tank', 'Light tank']

    t34 = MyTank(1000, 10, 20, 0, 0, 0)
    enemys = [Enemy(health=50 + i, damage=10, view_distance=10, coordinates=randint(0, 250), experience=0,
                    enemy_id=0 + i, enemy_category=categories_of_enemys[randint(0, len(categories_of_enemys) - 1)]) for i in range(7)]
    for enemy in enemys:

        print(f'{enemy}, {enemy.damage}, {enemy.coordinates}, {enemy.enemy_id}, {enemy.enemy_category}')

    key_1 = str(input("Type go to start "))
    key_1_logger = 'go'

    if key_1 == key_1_logger:
        print(start_phrases[randint(0, len(start_phrases) - 1)])

        while t34.is_alive():
            key_2_logger = input(str(f'Commander, we are waiting for your instructions!: '))


            for enemy in enemys:
                match enemy.enemy_category:
                    case 'Heavy tank':
                        enemy.damage = randint(10, 15)
                    case 'Tank destroyer':
                        enemy.damage = randint(15, 18)
                    case 'Medium tank':
                        enemy.damage = randint(9, 13)
                    case 'Light tank':
                        enemy.damage = randint(7, 11)
                enemy.do_damage(t34)
                if enemy.health <= 0:
                    enemys.pop(enemys.index(enemy))

            if key_2_logger in keys_to_move_forward:
                t34.move_tank_forward()
                print(f'{move_forward_phrases[randint(0, len(move_forward_phrases) - 1)]} {t34.coordinates}')


            if key_2_logger in keys_to_move_backward:
                t34.move_tank_backward()
                print(f'{move_forward_phrases[randint(0, len(move_forward_phrases) - 1)]} {t34.coordinates}')


            # if key_2_logger == "up":
            #     t34.upgrade_tank()


            for enemy in enemys:
                t34.shoot(enemy)


            print(f'our xp is {t34.experience}, tank level is {t34.tank_level}')

        MyTank.tank_destroyed(t34)
    else:
        print("What do you want to do?")





'''

camo for enemies
choose shell 
categories of tanks

'''








# loh = Enemy(40, 10, 10, 40, 0)
# t34 = MyTank(50, 20, 10, 0,0)
# t34.spot_enemy(loh)
# t34.move_tank_forward()
# t34.spot_enemy(loh)
# t34.shoot(loh)
# t34.move_tank_forward()
# t34.spot_enemy(loh)
# loh.do_damage(t34)
# t34.move_tank_forward()
# t34.spot_enemy(loh)
# t34.shoot(loh)
# loh.do_damage(t34)
# t34.move_tank_forward()
# t34.spot_enemy(loh)
# t34.shoot(loh)
# loh2 = Enemy(40, 20, 10, 50, 0)
# loh2.do_damage(t34)
# loh2.do_damage(t34)
# t34.tank_destroyed()

main()