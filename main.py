import pygame
from plane import Plane
from missile import Missile
from target import Target
from display import Display
import numpy as np

# Inisialisasi Pygame
pygame.init()

# Pengaturan layar
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Aerospace War Simulation')

# Membuat objek pesawat, target, dan display
plane = Plane()
targets = [Target(np.array([600, 300])), Target(np.array([200, 100])), Target(np.array([400, 500]))]
display = Display(screen)
missiles = []

# Loop utama
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mengambil input kontrol
    keys = pygame.key.get_pressed()
    plane.update_position(keys)

    # Peluncuran rudal manual
    if keys[pygame.K_SPACE]:
        missile = Missile(plane.position.copy(), plane.velocity.copy())
        missiles.append(missile)

    # Peluncuran rudal otomatis
    if keys[pygame.K_a]:
        if targets:
            missile = Missile(plane.position.copy(), plane.velocity.copy())
            missile.set_target(targets[0].position)  # Target pertama dalam daftar
            missiles.append(missile)

    # Update posisi rudal
    for missile in missiles:
        missile.update_position()

    # Mengupdate tampilan
    screen.fill((0, 0, 0))  # Bersihkan layar
    display.draw_plane(plane)
    for target in targets:
        display.draw_target(target)
    display.draw_missiles(missiles)
    display.draw_hud(plane)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
