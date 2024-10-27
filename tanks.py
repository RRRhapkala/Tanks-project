from random import randint, random



class Tank:
    def __init__(self, health, damage, view_distance, coordinates, experience):
        self.health = health
        self.damage = damage
        self.view_distance = view_distance
        self.coordinates = coordinates
        self.experience = experience


    def move_tank(self):
        self.coordinates += 10
        return self.coordinates

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class MyTank(Tank):

    def spot_enemy(self, enemy):
        distance = abs(self.coordinates - enemy.coordinates)
        if distance <= self.view_distance:
            print('Enemy spotted! SHOOT!!!')
            return True
        else:
            return False


    def shoot(self, enemy):
        if self.spot_enemy(enemy):
            enemy.health -= self.damage
            if enemy.is_alive():
                print(f'Got him, enemy got {self.damage}, he has left {enemy.health}')
                return enemy.health
            else:
                print(f'Enemy destroyed')

    def tank_destroyed(self):
        if not self.is_alive():
            print('Tank destroyed!')



class Enemy(Tank):

    def do_damage(self, my_tank):
        if self.is_alive():
            distance = abs(my_tank.coordinates - self.coordinates)
            if self.view_distance >= distance:
                my_tank.health -= self.damage
                print(f'We got hit, - {self.damage} hp, we have {my_tank.health} hp left')
                return my_tank.health






def main():


    t34 = MyTank(50, 10, 20, 0, 0)
    enemys = [Enemy(health=50 + i, damage=10 + i, view_distance=10, coordinates=randint(40, 150), experience=0) for i in range(5)]
    for enemy in enemys:
        print(f'{enemy}, {enemy.damage}, {enemy.coordinates}')
    key_1_logger = 'go'
    while MyTank.is_alive(t34):
        key_1 = str(input("Type go to start "))
        print(key_1)
        if key_1 == key_1_logger:

            MyTank.move_tank(t34)
            print(f'{t34.coordinates}')
            MyTank.spot_enemy(t34, enemy)
            if MyTank.spot_enemy(t34, enemy):
                MyTank.shoot(t34, enemy)
            Enemy.do_damage(enemy, t34)
        else:
            print("What do you want to do?")
            continue
    MyTank.tank_destroyed(t34)



'''
move right 
move left

stay still and shoot
choose shell 
categories of tanks

'''








# loh = Enemy(40, 10, 10, 40, 0)
# t34 = MyTank(50, 20, 10, 0,0)
# t34.spot_enemy(loh)
# t34.move_tank()
# t34.spot_enemy(loh)
# t34.shoot(loh)
# t34.move_tank()
# t34.spot_enemy(loh)
# loh.do_damage(t34)
# t34.move_tank()
# t34.spot_enemy(loh)
# t34.shoot(loh)
# loh.do_damage(t34)
# t34.move_tank()
# t34.spot_enemy(loh)
# t34.shoot(loh)
# loh2 = Enemy(40, 20, 10, 50, 0)
# loh2.do_damage(t34)
# loh2.do_damage(t34)
# t34.tank_destroyed()

main()