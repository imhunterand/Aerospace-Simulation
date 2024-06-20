import pygame

class Display:
    def __init__(self, screen):
        self.screen = screen

    def draw_plane(self, plane):
        pygame.draw.circle(self.screen, (255, 0, 0), plane.position.astype(int), 10)

    def draw_target(self, target):
        pygame.draw.circle(self.screen, (0, 255, 0), target.position.astype(int), 10)

    def draw_missiles(self, missiles):
        for missile in missiles:
            pygame.draw.circle(self.screen, (255, 255, 0), missile.position.astype(int), 5)

    def draw_hud(self, plane):
        font = pygame.font.Font(None, 36)
        velocity_text = font.render(f"Velocity: {np.linalg.norm(plane.velocity):.2f}", True, (255, 255, 255))
        position_text = font.render(f"Position: {plane.position}", True, (255, 255, 255))
        altitude_text = font.render(f"Altitude: {plane.position[1]:.2f}", True, (255, 255, 255))
        
        self.screen.blit(velocity_text, (10, 10))
        self.screen.blit(position_text, (10, 50))
        self.screen.blit(altitude_text, (10, 90))
