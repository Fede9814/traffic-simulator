import pygame

# - init -

pygame.init()

screen = pygame.display.set_mode((800, 600))

# - objects -

curr_time = pygame.time.get_ticks()

# first time check at once
check_time = curr_time

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
             running = False

    # - updates -

    curr_time = pygame.time.get_ticks()

    if curr_time >= check_time:
        print('time to check weather')

        # TODO: run function or thread to check weather

        # check again after 2000ms (2s)
        check_time = curr_time + 2000

    # - draws -
        # empty

    # - FPS -

    clock.tick(30)

# - end -

pygame.quit()