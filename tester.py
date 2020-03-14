import pygame
import engine 

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Tester")
render_size = 7

tileset = engine.tileset("tiles.png", (5,5), render_size=render_size)

tile_map = engine.tiledmap((3,4),tileset,(0,0), render_size=render_size)
tile_map.modify_layer((0,1),1, layer_id=0)
tile_map.add_new_layer()
tile_map.modify_layer((0,1),1, layer_id=1)
tile_map.generate_collision_rects()

player = engine.entity((0, 0), (5,5), map_class=tile_map, render_size=render_size)
player_speed = 0.05
player.force_texture_rect((220,20,220))
player_movement = [0,0]

running = True
while(running):
    screen.fill((100,100,100))
    tile_map.pygame_render_map(screen, (0,0))
    player.pygame_render(screen)
    player.move(player_movement, obey_collisions=True)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_movement[1] = -player_speed
            if event.key == pygame.K_s:
                player_movement[1] = player_speed
            if event.key == pygame.K_a:
                player_movement[0] = -player_speed
            if event.key == pygame.K_d:
                player_movement[0] = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_movement[1] = 0
            if event.key == pygame.K_s:
                player_movement[1] = 0
            if event.key == pygame.K_a:
                player_movement[0] = 0
            if event.key == pygame.K_d:
                player_movement[0] = 0