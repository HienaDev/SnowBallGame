#alien dispara tiros laser

#• Movimento linear de objectos - viagem do ar quente e do jogador - done
#• Forças resistentes ao movimento - ar quente desacelera as bolas - done
#• Trigonometria - sen e cos, viagem do ar quente que faz tipo "ADN" - done
#• Input do teclado - movimento do alien e disparar - done
#• Rotação de objectos - bolas de neve rodam enquanto anda - done
#• Escala de objectos - bolas de neve diminuem tamanho quando sao atigindas - done
#• Utilização de imagens - alien e bolas de neve - done

import pygame, sys
import pygame.freetype
import random
from aliens_variable import *
from alien_class import *
from balls import *

def main():

    pygame.init()

    timer = 0

    GAMEDATA.start_up(res)

    fpsClock = pygame.time.Clock()

    FPS = 60

    Exit = False

    while (not Exit):

        events = pygame.event.get()

        for evt in events:

            if(evt.type == pygame.QUIT):

                pygame.quit()
                sys.exit()

            if (evt.type == pygame.KEYDOWN):

                if evt.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if evt.key == pygame.K_DOWN or evt.key == pygame.K_s: 

                    

                    if (PLAYER.lane < 5):
                        PLAYER.pos = np.add(PLAYER.pos, [0, 130])
                        PLAYER.lane += 1

                if evt.key == pygame.K_UP or evt.key == pygame.K_w: 

                    

                    if (PLAYER.lane > 1):
                        PLAYER.pos = np.add(PLAYER.pos, [0, -130])
                        PLAYER.lane -= 1

                if evt.key == pygame.K_SPACE:

                    PLAYER.active_lanes[PLAYER.lane - 1] = 1

            if (evt.type == pygame.MOUSEBUTTONDOWN):

                if (evt.button == 1):

                    pass


        
        #Draw the map
        GAMEDATA.draw_map()
        GAMEDATA.draw_buttons()
        GAMEDATA.draw_active_buttons(PLAYER.active_lanes)

        #Draw the player
        GAMEDATA.screen.blit(PLAYER.image, (PLAYER.pos))

        #Spawn a ball every 3 seconds
        if(timer % 180 == 0):

            random_lane = random.randrange(1, 6)
            BALLS.create_ball(random_lane)
            
        #Displays balls on screen
        BALLS.update_balls()
        timer += 1

        #Displays the hot air on active lanes
        for shot in PLAYER.shots:
            
            for ray in shot:

                pygame.draw.circle(GAMEDATA.screen, red, (ray.pos[0], ray.pos[1] + 5 * math.cos(ray.a)), 2)
                
                if (ray.pos[0] > 850):
                    
                    for x in range(0, 4):
                        
                        if lanes[x][1] < ray.pos[1] < lanes[x + 1][1]:

                            PLAYER.active_lanes[x] = 0
 



        #If lane is active keep shooting air, else delete the air
        if PLAYER.active_lanes[0] == 1:

            PLAYER.shoot_air(1)
        else:

            PLAYER.delete_ray(1)
        
        if PLAYER.active_lanes[1] == 1:

            PLAYER.shoot_air(2)
        else:

            PLAYER.delete_ray(2)
        
        if PLAYER.active_lanes[2] == 1:

            PLAYER.shoot_air(3)
        else:

            PLAYER.delete_ray(3)

        if PLAYER.active_lanes[3] == 1:

            PLAYER.shoot_air(4)
        else:

            PLAYER.delete_ray(4)

        if PLAYER.active_lanes[4] == 1:

            PLAYER.shoot_air(5)
        else:

            PLAYER.delete_ray(5)



        #Draws the glass window
        GAMEDATA.draw_glass()


        GAMEDATA.update()



        fpsClock.tick(FPS)

    
main()