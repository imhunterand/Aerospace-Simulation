# This file can include functions related to controls, for example:
def handle_input(keys, plane):
    if keys[pygame.K_UP]:
        plane.acceleration[1] -= 0.1
    if keys[pygame.K_DOWN]:
        plane.acceleration[1] += 0.1
    if keys[pygame.K_LEFT]:
        plane.acceleration[0] -= 0.1
    if keys[pygame.K_RIGHT]:
        plane.acceleration[0] += 0.1
