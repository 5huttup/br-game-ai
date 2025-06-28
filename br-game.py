import random
#from unittest.mock import DEFAULT

ITEMS = ["saw", "cig", "pill", "beer", "chug", "glass", "adren", "inv", "phone"]

MIN_HP = 2
MAX_HP = 5
BLANK = 0
LIVE = 1
MIN_ITEMS_GIVE = 2
MAX_ITEMS_GIVE = 5
MAX_ITEMS = 9
MIN_BULLETS = 2
MAX_BULLETS = 8
DAMAGE = 1
S_DAMAGE = 2


class Player:
    def __init__(self, hp = 2, items = [], chugged = False):
        self.hp = hp
        self.items = items
        self.chugged = chugged

class Enemy:
    def __init__(self, hp = 2, items = [], chugged = False, current_bullet_knowledge = -1, count_blank_knowledge = -1,
                 count_live_knowledge = -1, bullets_knowledge = [-1, -1, -1, -1, -1, -1, -1, -1], bullets_count = -1, turn_counter = -1):
        self.hp = hp
        self.items = items
        self.chugged = chugged
        self.current_bullet_knowledge = current_bullet_knowledge
        self.count_blank_knowledge = count_blank_knowledge
        self.count_live_knowledge = count_live_knowledge
        self.bullets_knowledge = bullets_knowledge
        self.bullets_count = bullets_count
        self.turn_counter = turn_counter

class Gun:
    def __init__(self, damage = 1, bullets = [0, 0, 0, 0, 0, 0, 0, 0], inverted = False):
        self.damage = damage
        self.bullets = bullets
        self.current_bullet = bullets[0]
        self.inverted = inverted

    def generate_bullets(self):
        length = random.randint(int(MIN_BULLETS), int(MAX_BULLETS))

        while True:
            result = [random.randint(int(BLANK), int(LIVE)) for _ in range(length)]
            if not (all(x == 0 for x in result) or all(x == 1 for x in result)):
                self.bullets = result
                self.current_bullet = result[0]
                return result

    def getBulletsCountBlank(self):
        return self.bullets.count(0)

    def getBulletsCountLive(self):
        return self.bullets.count(1)

    def resetGun(self):
        self.damage = 1
        if len(self.bullets) > 1:
            del self.bullets[0]
            self.current_bullet = self.bullets[0]
        elif len(self.bullets) > 0:
            del self.bullets[0]
        self.inverted = False
        print("CURRENT BULLETS - " + str(len(self.bullets)))

    def getCurrentBullet(self):
        return self.current_bullet

    def invertCurrentBullet(self):
        if self.current_bullet == 0:
            self.current_bullet = 1
        elif self.current_bullet == 1:
            self.current_bullet = 0


def getItemsPlayer(Player):
    past_items = Player.items
    while True:
        if len(past_items) < 7:
            Player.items = past_items + random.sample(ITEMS, random.randint(int(MIN_ITEMS_GIVE), int(MAX_ITEMS_GIVE)))
            if len(Player.items) < MAX_ITEMS:
                return Player.items
        elif len(past_items) == 7:
            Player.items = past_items + random.sample(ITEMS, 1)
            return Player.items
        else:
            return Player.items

def getItemsEnemy(Enemy):
    past_items = Enemy.items
    while True:
        if len(past_items) < 7:
            Enemy.items = past_items + random.sample(ITEMS, random.randint(int(MIN_ITEMS_GIVE), int(MAX_ITEMS_GIVE)))
            if len(Enemy.items) < MAX_ITEMS:
                return Enemy.items
        elif len(past_items) == 7:
            Enemy.items = past_items + random.sample(ITEMS, 1)
            return Enemy.items
        else:
            return Enemy.items

def useSawPlayer(Gun, Player):
    Player.items.remove("saw")
    Gun.damage = 2
    print("Saw used, gun damage = 2 now")

def useSawPlayerForEnemy(Gun, Player):
    Player.items.remove("saw")
    Gun.damage = 2
    print("Saw used Enemy, gun damage = 2 now")

def useSawEnemy(Gun, Enemy):
    Enemy.items.remove("saw")
    Gun.damage = 2
    print("Saw used Enemy, gun damage = 2 now")

def useSawEnemyForPlayer(Gun, Enemy):
    Enemy.items.remove("saw")
    Gun.damage = 2
    print("Saw used, gun damage = 2 now")

def useCigPlayer(Player, CURRENT_MAX_HP):
    Player.items.remove("cig")
    if Player.hp < CURRENT_MAX_HP:
        Player.hp += 1
        print("Cigarettes used, player's hp = " + str(Player.hp) + " now")
    else:
        Player.hp = Player.hp

def useCigPlayerForEnemy(Player, Enemy, CURRENT_MAX_HP):
    Player.items.remove("cig")
    if Enemy.hp < CURRENT_MAX_HP:
        Enemy.hp += 1
        print("Cigarettes used, Enemy's hp = " + str(Enemy.hp) + " now")
    else:
        Enemy.hp = Enemy.hp

def useCigEnemy(Enemy, CURRENT_MAX_HP):
    Enemy.items.remove("cig")
    if Enemy.hp < CURRENT_MAX_HP:
        Enemy.hp += 1
        print("Cigarettes used Enemy, Enemy's hp = " + str(Enemy.hp) + " now")
    else:
        Enemy.hp = Enemy.hp

def useCigEnemyForPlayer(Player, Enemy, CURRENT_MAX_HP):
    Enemy.items.remove("cig")
    if Player.hp < CURRENT_MAX_HP:
        Player.hp += 1
        print("Cigarettes used, player's hp = " + str(Player.hp) + " now")
    else:
        Player.hp = Player.hp

def usePillPlayer(Player, CURRENT_MAX_HP):
    Player.items.remove("pill")
    rand = random.randint(0, 1)
    if rand == 0:
        Player.hp -= 1
        print("Pill used. Unlucky! player's hp = " + str(Player.hp) + " now")
    elif rand == 1:
        Player.hp += 2
        if Player.hp > CURRENT_MAX_HP:
            Player.hp = CURRENT_MAX_HP
        print("Pill used. Lucky! player's hp = " + str(Player.hp) + " now")

def usePillPlayerForEnemy(Player, Enemy, CURRENT_MAX_HP):
    Player.items.remove("pill")
    rand = random.randint(0, 1)
    if rand == 0:
        Enemy.hp -= 1
        print("Pill used. Unlucky! Enemy's hp = " + str(Enemy.hp) + " now")
    elif rand == 1:
        Enemy.hp += 2
        if Enemy.hp > CURRENT_MAX_HP:
            Enemy.hp = CURRENT_MAX_HP
        print("Pill used. Lucky! player's hp = " + str(Enemy.hp) + " now")

def usePillEnemy(Enemy, CURRENT_MAX_HP):
    Enemy.items.remove("pill")
    rand = random.randint(0, 1)
    if rand == 0:
        Enemy.hp -= 1
        print("Pill used. Unlucky! Enemy's hp = " + str(Enemy.hp) + " now")
    elif rand == 1:
        Enemy.hp += 2
        if Enemy.hp > CURRENT_MAX_HP:
            Enemy.hp = CURRENT_MAX_HP
        print("Pill used Enemy. Lucky! Enemy's hp = " + str(Enemy.hp) + " now")

def usePillEnemyForPlayer(Player, Enemy, CURRENT_MAX_HP):
    Enemy.items.remove("pill")
    rand = random.randint(0, 1)
    if rand == 0:
        Player.hp -= 1
        print("Pill used. Unlucky! player's hp = " + str(Player.hp) + " now")
    elif rand == 1:
        Player.hp += 2
        if Player.hp > CURRENT_MAX_HP:
            Player.hp = CURRENT_MAX_HP
        print("Pill used. Lucky! player's hp = " + str(Player.hp) + " now")

def useBeerPlayer(Player, Enemy, Gun, magazine):
    Player.items.remove("beer")
    print("Beer used. Current bullet was " + str(Gun.getCurrentBullet()) + " (1 - live, 0 - blank)")
    if Gun.getCurrentBullet() == 0:
        Enemy.count_blank_knowledge -= 1
    elif Gun.getCurrentBullet() == 1:
        Enemy.count_live_knowledge -= 1
    Gun.resetGun()

def useBeerPlayerForEnemy(Player, Enemy, Gun, magazine):
    Player.items.remove("beer")
    print("Beer used. Current bullet was " + str(Gun.getCurrentBullet()) + " (1 - live, 0 - blank)")
    if Gun.getCurrentBullet() == 0:
        Enemy.count_blank_knowledge -= 1
    elif Gun.getCurrentBullet() == 1:
        Enemy.count_live_knowledge -= 1
    Gun.resetGun()


def useBeerEnemy(Enemy, Gun, magazine):
    Enemy.items.remove("beer")
    print("Beer used Enemy. Current bullet was " + str(Gun.getCurrentBullet()) + " (1 - live, 0 - blank)")
    if Gun.getCurrentBullet() == 0:
        Enemy.count_blank_knowledge -= 1
    elif Gun.getCurrentBullet() == 1:
        Enemy.count_live_knowledge -= 1
    Gun.resetGun()

def useBeerEnemyForPlayer(Enemy, Gun, magazine):
    Enemy.items.remove("beer")
    print("Beer used Enemy. Current bullet was " + str(Gun.getCurrentBullet()) + " (1 - live, 0 - blank)")
    if Gun.getCurrentBullet() == 0:
        Enemy.count_blank_knowledge -= 1
    elif Gun.getCurrentBullet() == 1:
        Enemy.count_live_knowledge -= 1
    Gun.resetGun()

def useChugPlayer(Player, Enemy):
    Player.items.remove("chug")
    print("Chug used. Enemy chugged for one turn")
    Enemy.chugged = True

def useChugPlayerForEnemy(Player):
    Player.items.remove("chug")
    print("Chug used Enemy. Player chugged for one turn")
    Player.chugged = True

def useChugEnemy(Player, Enemy):
    Enemy.items.remove("chug")
    print("Chug used Enemy. Player chugged for one turn")
    Player.chugged = True

def useChugEnemyForPlayer(Enemy):
    Enemy.items.remove("chug")
    print("Chug used. Player chugged for one turn")
    Enemy.chugged = True

def useGlassPlayer(Player, Gun):
    Player.items.remove("glass")
    print("Glass used. Current bullet is " + str(Gun.getCurrentBullet()) + " (1 - live, 0 - blank)")

def useGlassPlayerForEnemy(Player, Enemy, Gun):
    Player.items.remove("glass")
    print("Glass used Enemy. Enemy know current bullet")
    Enemy.current_bullet_knowledge = Gun.getCurrentBullet()

def useGlassEnemy(Enemy, Gun):
    Enemy.items.remove("glass")
    print("Glass used Enemy. Enemy know current bullet")
    Enemy.current_bullet_knowledge = Gun.getCurrentBullet()

def useGlassEnemyForPlayer(Enemy, Gun):
    Enemy.items.remove("glass")
    print("Glass used. Current bullet is " + str(Gun.getCurrentBullet()) + " (1 - live, 0 - blank)")

def useAdrenPlayer(Player, Enemy):
    Player.items.remove("adren")
    print("Adrenaline used. Now you can use opponent's item\n Enemy's items list: " + str(Enemy.items))
    item_name = input("Enter item which you want to use: ")
    if item_name in Enemy.items and item_name != "adren":
        actionsEnemyForPlayer[item_name]()
    elif item_name == "adren":
        print("You can't use enemy's adrenaline")
    else:
        print("Incorrect item. You can't try again.")

def useAdrenEnemy(Player, Enemy):
    Enemy.items.remove("adren")
    print("Adrenaline used Enemy. Now Enemy can use opponent's item\n Player items list: " + str(Player.items))

def useInvPlayer(Player, Gun):
    Player.items.remove("inv")
    Gun.invertCurrentBullet()
    Gun.inverted = True
    print("Invertor used. Curent bullet inverted")

def useInvPlayerForEnemy(Player, Gun):
    Player.items.remove("inv")
    Gun.invertCurrentBullet()
    Gun.inverted = True
    print("Invertor used Enemy. Curent bullet inverted")

def useInvEnemy(Enemy, Gun):
    Enemy.items.remove("inv")
    Gun.invertCurrentBullet()
    Gun.inverted = True
    print("Invertor used Enemy. Curent bullet inverted")

def useInvEnemyForPlayer(Enemy, Gun):
    Enemy.items.remove("inv")
    Gun.invertCurrentBullet()
    Gun.inverted = True
    print("Invertor used. Curent bullet inverted")

def usePhonePlayer(Player, Gun):
    Player.items.remove("phone")
    random_index = random.randint(0, len(Gun.bullets) -1)
    value = Gun.bullets[random_index]
    print("Phone used. Bullet number " + str(random_index + 1) + " is " + str(value) + " (0 - blank, 1 - live)")

def usePhonePlayerForEnemy(Player, Enemy, Gun):
    Player.items.remove("phone")
    random_index = random.randint(0, len(Gun.bullets) -1)
    value = Gun.bullets[random_index]
    print("Phone used Enemy. Enemy know Bullet number * is **** (0 - blank, 1 - live)")
    Enemy.bullets_knowledge[random_index] = value
    if random_index == 0:
        enemy.current_bullet_knowledge = Gun.bullets[random_index]

def usePhoneEnemy(Enemy, Gun):
    Enemy.items.remove("phone")
    random_index = random.randint(0, len(Gun.bullets) -1)
    value = Gun.bullets[random_index]
    print("Phone used Enemy. Enemy know Bullet number * is **** (0 - blank, 1 - live)")
    Enemy.bullets_knowledge[random_index] = value
    if random_index == 0:
        enemy.current_bullet_knowledge = Gun.bullets[random_index]

def usePhoneEnemyForPlayer(Enemy, Gun):
    Enemy.items.remove("phone")
    random_index = random.randint(0, len(Gun.bullets) -1)
    value = Gun.bullets[random_index]
    print("Phone used. Bullet number " + str(random_index + 1) + " is " + str(value) + " (0 - blank, 1 - live)")

def spawnHP(Player, Enemy):
    Player.hp = random.randint(int(MIN_HP), int(MAX_HP))
    Enemy.hp = Player.hp

def useBotAi(Player, Enemy, Gun, turn_who, magazine):
    used_saw = False
    used_chug = False
    used_glass = False
    used_inv = False
    used_phone = False
    enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
    enemy.bullets_count = enemy.count_blank_knowledge + enemy.count_live_knowledge

    #CIG & PILL
    if enemy.hp < CURRENT_MAX_HP and ("cig" in enemy.items or "pill" in enemy.items):
        if enemy.hp < CURRENT_MAX_HP and enemy.hp >= 1 and "cig" in enemy.items:
            useCigEnemy(enemy, CURRENT_MAX_HP)
        if enemy.hp < CURRENT_MAX_HP and enemy.hp >= 2 and "pill" in enemy.items:
            usePillEnemy(enemy, CURRENT_MAX_HP)

    #BEER
    if enemy.bullets_count > 1 and enemy.current_bullet_knowledge == -1 and "beer" in enemy.items:
        if random.choice([True, False]):
            useBeerEnemy(enemy, gun, magazine)
            magazine = len(Gun.bullets)

    #GLASS
    if used_glass != True and "glass" in enemy.items:
        useGlassEnemy(enemy, gun)
        enemy.current_bullet_knowledge = gun.getCurrentBullet()
        used_glass = True

    #PHONE
    if used_phone != True and "phone" in enemy.items and enemy.bullets_count > 1:
        usePhoneEnemy(enemy, gun)
        used_phone = True

    #CHUG
    if used_chug != True and player.chugged != True and "chug" in enemy.items:
        useChugEnemy(player, enemy)
        used_chug = True

    #INV
    if used_inv != True and enemy.current_bullet_knowledge == 0 and "inv" in enemy.items:
        useInvEnemy(enemy, gun)
        used_inv = True

    #SAW
    if used_saw != True and enemy.current_bullet_knowledge == 1 and "saw" in enemy.items:
        useSawEnemy(gun, enemy)
        used_saw = True

    #ADREN
    if "adren" in enemy.items and len(enemy.items) > 0 and player.items:
        useAdrenEnemy(player, enemy)
        # CIG & PILL
        if enemy.hp < CURRENT_MAX_HP and ("cig" in player.items or "pill" in player.items):
            if enemy.hp < CURRENT_MAX_HP and enemy.hp >= 1 and "cig" in player.items:
                useCigPlayerForEnemy(player, enemy, CURRENT_MAX_HP)
            if enemy.hp < CURRENT_MAX_HP and enemy.hp >= 2 and "pill" in player.items:
                usePillPlayerForEnemy(player, enemy, CURRENT_MAX_HP)

        # BEER
        if enemy.bullets_count > 1 and enemy.current_bullet_knowledge == -1 and "beer" in player.items:
            if random.choice([True, False]):
                useBeerPlayerForEnemy(player, enemy, gun, magazine)
                magazine = len(Gun.bullets)

        # GLASS
        if used_glass != True and "glass" in player.items:
            useGlassPlayerForEnemy(player, enemy, gun)
            enemy.current_bullet_knowledge = gun.getCurrentBullet()
            used_glass = True

        # PHONE
        if used_phone != True and "phone" in player.items and len(gun.bullets) > 1:
            usePhonePlayerForEnemy(player, enemy, gun)
            used_phone = True

        # CHUG
        if used_chug != True and player.chugged != True and "chug" in player.items:
            useChugPlayerForEnemy(player)
            used_chug = True

        # INV
        if used_inv != True and enemy.current_bullet_knowledge == 0 and "inv" in player.items:
            useInvPlayerForEnemy(player, gun)
            enemy.current_bullet_knowledge = 1
            used_inv = True

        # SAW
        if used_saw != True and enemy.current_bullet_knowledge == 1 and "saw" in player.items:
            useSawPlayerForEnemy(gun, player)
            used_saw = True

    #FIRE
    while turn_who == 1 and magazine > 0:
        if enemy.current_bullet_knowledge == 0 and gun.current_bullet == 0:
            if gun.inverted == True:
                enemy.count_live_knowledge -= 1
            else:
                enemy.count_blank_knowledge -= 1
            if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                del enemy.bullets_knowledge[0]
                if enemy.bullets_knowledge:  # Проверяем снова после удаления
                    enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                else:
                    enemy.current_bullet_knowledge = -1
            gun.resetGun()
            magazine = len(gun.bullets)
            if magazine == 0:
                turn_who = 0
        elif enemy.current_bullet_knowledge == 1 and gun.current_bullet == 1:
            player.hp -= gun.damage
            print("Enemy shot you with live. Your hp now = " + str(player.hp))
            if gun.inverted == True:
                enemy.count_blank_knowledge -= 1
            else:
                enemy.count_live_knowledge -= 1
            if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                del enemy.bullets_knowledge[0]
                if enemy.bullets_knowledge:  # Проверяем снова после удаления
                    enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                else:
                    enemy.current_bullet_knowledge = -1
            gun.resetGun()
            magazine = len(gun.bullets)
            if player.chugged != True:
                turn_who = 0
        else:
            if enemy.count_live_knowledge < enemy.count_blank_knowledge:
                if random.randint(enemy.count_live_knowledge, enemy.count_blank_knowledge) <= enemy.count_live_knowledge:
                    if gun.current_bullet == 0:
                        print("Enemy shot you with blank. Nothing happened")
                        if gun.inverted == True:
                            enemy.count_live_knowledge -= 1
                        else:
                            enemy.count_blank_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
                    elif gun.current_bullet == 1:
                        player.hp -= 1
                        print("Enemy shot you with live. Your hp now = " + str(player.hp))
                        if gun.inverted == True:
                            enemy.count_blank_knowledge -= 1
                        else:
                            enemy.count_live_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
                else:
                    if gun.current_bullet == 0:
                        print("Enemy shot himself with blank. Nothing happened")
                        if gun.inverted == True:
                            enemy.count_live_knowledge -= 1
                        else:
                            enemy.count_blank_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                    elif gun.current_bullet == 1:
                        enemy.hp -= 1
                        print("Enemy shot himself with live. His hp now = " + str(enemy.hp))
                        if gun.inverted == True:
                            enemy.count_blank_knowledge -= 1
                        else:
                            enemy.count_live_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
            elif enemy.count_blank_knowledge < enemy.count_live_knowledge:
                if random.randint(enemy.count_blank_knowledge, enemy.count_live_knowledge) <= enemy.count_blank_knowledge:
                    if gun.current_bullet == 0:
                        print("Enemy shot you with blank. Nothing happened")
                        if gun.inverted == True:
                            enemy.count_live_knowledge -= 1
                        else:
                            enemy.count_blank_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
                    elif gun.current_bullet == 1:
                        player.hp -= 1
                        print("Enemy shot you with live. Your hp now = " + str(player.hp))
                        if gun.inverted == True:
                            enemy.count_blank_knowledge -= 1
                        else:
                            enemy.count_live_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
                else:
                    if gun.current_bullet == 0:
                        print("Enemy shot himself with blank. Nothing happened")
                        if gun.inverted == True:
                            enemy.count_live_knowledge -= 1
                        else:
                            enemy.count_blank_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                    elif gun.current_bullet == 1:
                        enemy.hp -= 1
                        print("Enemy shot himself with live. His hp now = " + str(enemy.hp))
                        if gun.inverted == True:
                            enemy.count_blank_knowledge -= 1
                        else:
                            enemy.count_live_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
                if magazine == 0:
                    turn_who = 0
            else:
                if random.choice([True, False]):
                    if gun.current_bullet == 0:
                        print("Enemy shot you with blank. Nothing happened")
                        if gun.inverted == True:
                            enemy.count_live_knowledge -= 1
                        else:
                            enemy.count_blank_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
                    elif gun.current_bullet == 1:
                        player.hp -= 1
                        print("Enemy shot you with live. Your hp now = " + str(player.hp))
                        if gun.inverted == True:
                            enemy.count_blank_knowledge -= 1
                        else:
                            enemy.count_live_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
                else:
                    if gun.current_bullet == 0:
                        print("Enemy shot himself with blank. Nothing happened")
                        if gun.inverted == True:
                            enemy.count_live_knowledge -= 1
                        else:
                            enemy.count_blank_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                    elif gun.current_bullet == 1:
                        enemy.hp -= 1
                        print("Enemy shot himself with live. His hp now = " + str(enemy.hp))
                        if gun.inverted == True:
                            enemy.count_blank_knowledge -= 1
                        else:
                            enemy.count_live_knowledge -= 1
                        if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                            del enemy.bullets_knowledge[0]
                            if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                            else:
                                enemy.current_bullet_knowledge = -1
                        gun.resetGun()
                        magazine = len(gun.bullets)
                        if player.chugged != True:
                            turn_who = 0
        player.chugged = False
        if magazine == 0:
            turn_who = 0


def checkDead(Player, Enemy):
    if Player.hp < 1 or Enemy.hp < 1:
        return True
    else:
        return False


player = Player()
enemy = Enemy()
gun = Gun()

actions = {
    "saw": lambda: useSawPlayer(gun, player),
    "cig": lambda:useCigPlayer(player, CURRENT_MAX_HP),
    "pill": lambda:usePillPlayer(player, CURRENT_MAX_HP),
    "beer": lambda:useBeerPlayer(player, enemy, gun, magazine),
    "chug": lambda:useChugPlayer(player, enemy),
    "glass": lambda:useGlassPlayer(player, gun),
    "adren": lambda:useAdrenPlayer(player, enemy),
    "inv": lambda:useInvPlayer(player, gun),
    "phone": lambda:usePhonePlayer(player, gun)
}

actionsEnemyForPlayer = {
    "saw": lambda: useSawEnemyForPlayer(gun, enemy),
    "cig": lambda:useCigEnemyForPlayer(player, enemy, CURRENT_MAX_HP),
    "pill": lambda:usePillEnemyForPlayer(player, enemy, CURRENT_MAX_HP),
    "beer": lambda:useBeerEnemyForPlayer(enemy, gun, magazine),
    "chug": lambda:useChugEnemyForPlayer(player),
    "glass": lambda:useGlassEnemyForPlayer(enemy, gun),
    "inv": lambda:useInvEnemyForPlayer(enemy, gun),
    "phone": lambda:usePhoneEnemyForPlayer(enemy, gun)
}


#ROUND


while True:

    round = True
    while round:
        #GENERATE
        print("ROUND RESTART")
        print("generaintg hp...")
        spawnHP(player, enemy)
        CURRENT_MAX_HP = player.hp
        print("hp generated")
        print("generaintg bullets...")
        gun.generate_bullets()
        print("bullets generated")
        enemy.count_blank_knowledge = gun.getBulletsCountBlank()
        enemy.count_live_knowledge = gun.getBulletsCountLive()
        enemy.bullets_count = enemy.count_blank_knowledge + enemy.count_live_knowledge
        enemy.bullets_knowledge = [-1, -1, -1, -1, -1, -1, -1, -1]
        player.items.clear()
        enemy.items.clear()

        magazine = len(gun.bullets)

        print("\n---START GAME---")
        print("PLAYER HP: " + str(player.hp))
        print("ENEMY HP: " + str(enemy.hp))
        print("BLANK BULLETS: " + str(gun.getBulletsCountBlank()) + ", LIVE BULLETS " + str(gun.getBulletsCountLive()))


        #ACTION
        while magazine > 0:
            player.items = getItemsPlayer(player)
            enemy.items = getItemsEnemy(enemy)
            print("PLAYER'S ITEMS: " + str(player.items))
            print("ENEMY'S ITEMS: " + str(enemy.items))

            turn_who = 0

            if checkDead(player, enemy):
                magazine = 0
            else:
                while turn_who == 0 and player.chugged == False and len(gun.bullets) > 0:
                    print("you have: " + str(player.items))
                    choice = input("choose (0 - use item, 1 - fire): ")
                    if choice == "1":
                        fire_who = input("Fire in who? (0 - me, 1 - enemy): ")
                        if fire_who == "0":
                            if gun.current_bullet == 0:
                                print("Nothing happened")
                                if gun.inverted != True:
                                    enemy.count_blank_knowledge -= 1
                                if gun.inverted == True:
                                    enemy.count_live_knowledge -= 1
                            elif gun.current_bullet == 1:
                                player.hp -= 1
                                print("Gun fired. Player HP left: " + str(player.hp))
                                if gun.inverted != True:
                                    enemy.count_live_knowledge -= 1
                                if gun.inverted == True:
                                    enemy.count_blank_knowledge -= 1
                            if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                                del enemy.bullets_knowledge[0]
                                if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                    enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                                else:
                                    enemy.current_bullet_knowledge = -1
                            gun.resetGun()
                            magazine = len(gun.bullets)
                            if enemy.chugged == False:
                                turn_who = 1
                        elif fire_who == "1":
                            if gun.current_bullet == 0:
                                print("Nothing happened")
                                if gun.inverted != True:
                                    enemy.count_blank_knowledge -= 1
                                if gun.inverted == True:
                                    enemy.count_live_knowledge -= 1
                            elif gun.current_bullet == 1:
                                enemy.hp -= 1
                                print("Gun fired. Enemy HP left: " + str(enemy.hp))
                                if gun.inverted != True:
                                    enemy.count_live_knowledge -= 1
                                if gun.inverted == True:
                                    enemy.count_blank_knowledge -= 1
                            if enemy.bullets_knowledge:  # Проверяем, не пуст ли список
                                del enemy.bullets_knowledge[0]
                                if enemy.bullets_knowledge:  # Проверяем снова после удаления
                                    enemy.current_bullet_knowledge = enemy.bullets_knowledge[0]
                                else:
                                    enemy.current_bullet_knowledge = -1
                            gun.resetGun()
                            magazine = len(gun.bullets)
                            if enemy.chugged == False:
                                turn_who = 1
                            else:
                                print("Enemy chugged. Again your turn")
                        enemy.chugged = False
                    elif choice == "0":
                        print("Your item list: " + str(player.items))
                        item_choice = input("choose item: ")
                        if item_choice in player.items:
                            actions[item_choice]()
                            if item_choice == "beer":
                                magazine = len(Gun.bullets)
                        else:
                            print("Incorrect item")

                while turn_who == 1 and magazine > 0:
                    useBotAi(player, enemy, gun, turn_who, magazine)
                    #if player.chugged == True:
                    #    useBotAi(player, enemy, gun, turn_who, magazine)
                    turn_who = 0
  
