import os
import pygame

pygame.init()

screen_width = 640 
screen_height = 480 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("bubble game")
clock = pygame.time.Clock()

###기본설정

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images") 

background = pygame.image.load(os.path.join(image_path, "background.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = (screen_width / 2) - (character_width / 2)
character_ypos = screen_height - character_height - stage_height

character_to_x = 0
character_speed = 5

weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []#한번에 여러발
weapon_speed = 10

ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

ball_speed_y = [-18, -15, -12, -9]

balls = []

balls.append({
    "pos_x" : 50,
    "pos_y" : 50, 
    "img_idx" : 0, 
    "to_x": 3,
    "to_y": -6, 
    "init_spd_y": ball_speed_y[0]})

weapon_to_remove = -1
ball_to_remove = -1

#글씨 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks() # 시작 시간 정의

game_result = "Game Over"

running = True
while running:
    dt = clock.tick(30)

    ###이벤트 처리
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: 
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: 
                weapon_xpos = character_xpos + (character_width / 2) - (weapon_width / 2)
                weapon_ypos = character_ypos
                weapons.append([weapon_xpos, weapon_ypos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    ###캐릭터 위치 정의
                
    character_xpos += character_to_x

    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width

    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] #무기 위치 y좌표가 위로
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
    
    #공 위치 
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #벽 튕김
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        #바닥 튕김
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
       

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    #캐릭터 rect
    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #공 rect
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        
        if character_rect.colliderect(ball_rect):
            running = False
            break

        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            #무기 rect
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

      
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx 
                ball_to_remove = ball_idx 

                if ball_img_idx < 3:
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    #왼쪽 튕김
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx": ball_img_idx + 1,
                        "to_x": -3, 
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})

                    #오른쪽 튕김
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), 
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1, 
                        "to_x": 3, 
                        "to_y": -6, 
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})

                break
        else: 
            continue 
        break 

    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    ###화면 업데이트
    
    screen.blit(background, (0, 0))
    
    for weapon_xpos, weapon_ypos in weapons:
        screen.blit(weapon, (weapon_xpos, weapon_ypos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_xpos, character_ypos))
 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update()

msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()


pygame.time.delay(2000)

pygame.quit()
