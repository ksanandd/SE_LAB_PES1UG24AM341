import pygame
import random
from .fruit import Fruit


# Game Engine

WHITE = (255, 255, 255)
BOMB_BLACK = (30, 30, 30)
FRUIT_COLORS = [
    (220, 60, 60),
    (230, 140, 40),
    (230, 200, 40),
    (90, 180, 90)
]


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.fruits = []
        self.trail = []  # recent mouse positions, drawn as the "blade"

        # Stores the previous mouse position so that the complete
        # swipe segment can be checked for collision.
        self.previous_mouse_pos = None

        self.spawn_interval = 55  # frames between spawns
        self._spawn_timer = 0
        self.bomb_chance = 0.15
        self.speed_scale = 1.0

        self.lives = 3
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 28)

        # Game state
        self.game_over = False
        self.game_over_input_received = False

        # Fonts used by the Game Over screen
        self.game_over_font = pygame.font.SysFont("Arial", 64, bold=True)
        self.final_score_font = pygame.font.SysFont("Arial", 36)
        self.continue_font = pygame.font.SysFont("Arial", 24)

    def spawn_fruit(self):
        x = random.randint(60, self.width - 60)
        vy = -random.uniform(13, 16) * self.speed_scale
        vx = random.uniform(-2, 2)
        gravity = 0.35
        kind = "bomb" if random.random() < self.bomb_chance else "fruit"

        fruit = Fruit(
            x,
            self.height + 30,
            vx,
            vy,
            gravity,
            kind=kind
        )

        fruit.color = (
            BOMB_BLACK
            if kind == "bomb"
            else random.choice(FRUIT_COLORS)
        )

        self.fruits.append(fruit)

    def handle_event(self, event):
        # Once the game is over, stop normal gameplay input.
        # Wait for a key press or mouse click before exiting.
        if self.game_over:
            if event.type == pygame.KEYDOWN:
                self.game_over_input_received = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.game_over_input_received = True
            return

        if event.type == pygame.MOUSEMOTION:
            self._handle_motion(event.pos)

    def _handle_motion(self, pos):
        # Check the complete mouse movement segment from the
        # previous position to the current position.
        if self.previous_mouse_pos is not None:
            for fruit in self.fruits:
                if (
                    not fruit.sliced
                    and fruit.intersects_segment(
                        self.previous_mouse_pos,
                        pos
                    )
                ):
                    self._slice(fruit)

        # Update the previous mouse position for the next
        # mouse movement event.
        self.previous_mouse_pos = pos

        self.trail.append(pos)

        if len(self.trail) > 15:
            self.trail.pop(0)

    def _slice(self, fruit):
        fruit.sliced = True

        if fruit.kind == "bomb":
            self.game_over = True
        else:
            self.score += 1

    def handle_input(self):
        # Reserved for continuously-held-key input; this game is
        # entirely mouse-driven, so there's nothing to poll here.
        pass

    def update(self):
        # Do not update gameplay after Game Over.
        if self.game_over:
            return

        self._spawn_timer += 1

        if self._spawn_timer >= self.spawn_interval:
            self._spawn_timer = 0
            self.spawn_fruit()

        still_alive = []

        for fruit in self.fruits:
            fruit.update()

            if fruit.sliced:
                continue

            if fruit.off_screen(self.height):
                if fruit.kind == "fruit":
                    self.lives -= 1
                continue

            still_alive.append(fruit)

        self.fruits = still_alive

        if self.lives <= 0:
            self.game_over = True

    def render(self, screen):
        # Render normal gameplay while the game is active.
        if not self.game_over:
            for fruit in self.fruits:
                color = getattr(fruit, "color", WHITE)

                pygame.draw.circle(
                    screen,
                    color,
                    (int(fruit.x), int(fruit.y)),
                    fruit.radius
                )

            if len(self.trail) >= 2:
                pygame.draw.lines(
                    screen,
                    WHITE,
                    False,
                    self.trail,
                    3
                )

            score_text = self.font.render(
                f"Score: {self.score}",
                True,
                WHITE
            )
            screen.blit(score_text, (10, 10))

            lives_text = self.font.render(
                f"Lives: {self.lives}",
                True,
                WHITE
            )
            screen.blit(
                lives_text,
                (self.width - 130, 10)
            )

            return

        # -------------------------
        # GAME OVER SCREEN
        # -------------------------

        # Dark overlay so the Game Over screen is visually distinct.
        overlay = pygame.Surface(
            (self.width, self.height),
            pygame.SRCALPHA
        )
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        game_over_text = self.game_over_font.render(
            "GAME OVER",
            True,
            WHITE
        )

        final_score_text = self.final_score_font.render(
            f"Final Score: {self.score}",
            True,
            WHITE
        )

        continue_text = self.continue_font.render(
            "Press any key or click to exit",
            True,
            WHITE
        )

        game_over_rect = game_over_text.get_rect(
            center=(self.width // 2, self.height // 2 - 80)
        )

        final_score_rect = final_score_text.get_rect(
            center=(self.width // 2, self.height // 2)
        )

        continue_rect = continue_text.get_rect(
            center=(self.width // 2, self.height // 2 + 70)
        )

        screen.blit(game_over_text, game_over_rect)
        screen.blit(final_score_text, final_score_rect)
        screen.blit(continue_text, continue_rect)