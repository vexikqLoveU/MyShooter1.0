from pygame import *
from GameSprite import *
from Player import *
from Enemy import *
def main():

    mixer.init()
    mixer.music.load('space.ogg')
    mixer.music.play()
    fire_sound = mixer.Sound('fire.ogg')
    font.init()
    font1 = font.SysFont('Arial', 35)
    win = font1.render('YOU WIN!', True, (255, 255, 255))
    lose = font1.render('YOU LOSE!', True, (180, 0, 0))


    bulls_reload = False
    bulls = 30
    frames = 0
    lost = 0
    img_back = "galaxy.jpg" 
    img_hero = "rocket.png" 
    img_enemy = 'ufo.png'

    win_width = 800
    win_height = 600
    display.set_caption("Shooter")
    window = display.set_mode((win_width, win_height))
    background = transform.scale(image.load(img_back), (win_width, win_height))
    monsters = sprite.Group()
    for i in range(1,6):
        monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 3), win_width, win_height, window)
        monsters.add(monster)
    ship = Player(img_hero, 5, win_height - 100, 80, 100, 10, win_width, win_height, window)
    clock = time.Clock()
    lost1 = 0
    bullets = sprite.Group()
    asteroids = sprite.Group()
    for i in range(1, 3):
        asteroid = Enemy('asteroid.png', randint(80, win_width - 80), -40, 50, 40, randint(1, 5), win_width, win_height, window)
        asteroids.add(asteroid)

    finish = False

    run = True 

    while run:
        frames += 1
        for e in event.get():
            if e.type == QUIT:
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE and bulls_reload == False and bulls != 0:
                    fire_sound.play()
                    bullets.add(ship.fire())
                    bulls -= 1
                
                    



        if not finish:


            
            window.blit(background,(0,0))
            lost_text = font1.render('Пропущено:' + str(lost), True, (255, 255, 255))
            window.blit(lost_text, (10,10))
            lost_text1 = font1.render('Сбито кацапов:' + str(lost1), True, (255, 255, 255))
            window.blit(lost_text1, (10,30))
            lost_text2 = font1.render('Пуль в обойме:' + str(bulls), True, (255, 255, 255))
            window.blit(lost_text2, (10, 50))
            if bulls == 0 and bulls_reload == False:
                frames = 0
                bulls_reload = True
            if bulls_reload == True and frames >= 120:
                bulls_reload = False
                bulls = 30

            ship.update()
            bullets.update()
            asteroids.update()
            for m in monsters:
                lost += m.update()
            collides = sprite.groupcollide(monsters, bullets, True, True)
            collides1 = sprite.groupcollide(asteroids, bullets, False, True)
            for c in collides:
                monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5), win_width, win_height, window)
                monsters.add(monster)
                lost1 += 1
            if sprite.spritecollide(ship, monsters, False) or lost >= 10:
                finish = True
                window.blit(lose, (200, 200))
            if sprite.spritecollide(ship, asteroids, False):
                finish = True
                window.blit(lose, (200, 200))
            if lost1 >= 20:
                finish = True
                window.blit(win, (200, 200))

            ship.reset()
            asteroids.draw(window)
            monsters.draw(window)
            bullets.draw(window)
            display.update()

            clock.tick(60)

if __name__ == '__main__':
    main()