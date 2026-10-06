import pygame
import random
import math

from .fruit import Fruit


# Game colors
WHITE = (255, 255, 255)
BOMB_BLACK = (30, 30, 30)
FRUIT_COLORS = [
    (220, 60, 60),
    (230, 140, 40),
    (230, 200, 40),
    (90, 180, 90),
]


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.fruits = []
        self.trail = []

        # Task 1: previous mouse position for segment collision
        self.previous_mouse_pos = None

        # Default / Medium difficulty
        self.spawn_interval = 55
        self._spawn_timer = 0
        self.bomb_chance = 0.15
        self.speed_scale = 1.0

        self.lives = 3
        self.score = 0

        self.game_over = False
        self.game_over_input_received = False

        # Task 3
        self.difficulty = "Medium"

        # Fonts
        self.font = pygame.font.SysFont("Arial", 28)
        self.game_over_font = pygame.font.SysFont("Arial", 64, bold=True)
        self.score_font = pygame.font.SysFont("Arial", 36)
        self.menu_font = pygame.font.SysFont("Arial", 30, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 24)

    # =========================================================
    # TASK 3 - DIFFICULTY
    # =========================================================

    def apply_difficulty(self, difficulty):
        self.difficulty = difficulty

        if difficulty == "Easy":
            self.spawn_interval = 70
            self.bomb_chance = 0.10
            self.speed_scale = 0.90

        elif difficulty == "Medium":
            self.spawn_interval = 55
            self.bomb_chance = 0.15
            self.speed_scale = 1.00

        elif difficulty == "Hard":
            self.spawn_interval = 40
            self.bomb_chance = 0.25
            self.speed_scale = 1.10

    def reset_game(self, difficulty):
        self.apply_difficulty(difficulty)

        self.fruits.clear()
        self.trail.clear()

        self.previous_mouse_pos = None

        self._spawn_timer = 0
        self.lives = 3
        self.score = 0

        self.game_over = False
        self.game_over_input_received = False

    # =========================================================
    # GAME EVENTS
    # =========================================================

    def handle_event(self, event):

        # -------------------------
        # GAME OVER MENU
        # -------------------------
        if self.game_over:

            # Keyboard controls
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    self.reset_game("Easy")

                elif event.key == pygame.K_2:
                    self.reset_game("Medium")

                elif event.key == pygame.K_3:
                    self.reset_game("Hard")

                elif event.key == pygame.K_4:
                    self.game_over_input_received = True

                elif event.key == pygame.K_ESCAPE:
                    self.game_over_input_received = True

            # Mouse controls
            elif event.type == pygame.MOUSEBUTTONDOWN:

                x, y = event.pos

                easy_rect = self.get_menu_rect(0)
                medium_rect = self.get_menu_rect(1)
                hard_rect = self.get_menu_rect(2)
                exit_rect = self.get_menu_rect(3)

                if easy_rect.collidepoint(x, y):
                    self.reset_game("Easy")

                elif medium_rect.collidepoint(x, y):
                    self.reset_game("Medium")

                elif hard_rect.collidepoint(x, y):
                    self.reset_game("Hard")

                elif exit_rect.collidepoint(x, y):
                    self.game_over_input_received = True

            return

        # -------------------------
        # NORMAL GAMEPLAY
        # -------------------------
        if event.type == pygame.MOUSEMOTION:
            self._handle_motion(event.pos)

    # =========================================================
    # TASK 1 - FAST SWIPE COLLISION
    # =========================================================

    def _handle_motion(self, pos):

        if self.previous_mouse_pos is not None:

            for fruit in self.fruits:

                if not fruit.sliced:

                    if fruit.intersects_segment(
                        self.previous_mouse_pos,
                        pos
                    ):
                        self._slice(fruit)

        self.previous_mouse_pos = pos

        self.trail.append(pos)

        if len(self.trail) > 15:
            self.trail.pop(0)

    # =========================================================
    # SLICING
    # =========================================================

    def _slice(self, fruit):

        if fruit.sliced:
            return

        fruit.sliced = True

        # Bomb -> Game Over
        if fruit.kind == "bomb":

            self.game_over = True
            self.trail.clear()

        # Normal fruit -> score
        else:

            self.score += 1

    # =========================================================
    # INPUT
    # =========================================================

    def handle_input(self):
        pass

    # =========================================================
    # UPDATE
    # =========================================================

    def update(self):

        # Stop gameplay after Game Over
        if self.game_over:
            return

        # Spawn timer
        self._spawn_timer += 1

        if self._spawn_timer >= self.spawn_interval:

            self._spawn_timer = 0

            self.spawn_fruit()

        still_alive = []

        for fruit in self.fruits:

            fruit.update()

            if fruit.sliced:
                continue

            # Fruit went below screen
            if fruit.off_screen(self.height):

                # Only normal fruit costs a life
                if fruit.kind == "fruit":
                    self.lives -= 1

                continue

            still_alive.append(fruit)

        self.fruits = still_alive

        # No lives -> Game Over
        if self.lives <= 0:

            self.lives = 0
            self.game_over = True
            self.trail.clear()

    # =========================================================
    # SPAWN FRUIT / BOMB
    # =========================================================

    def spawn_fruit(self):

        x = random.randint(60, self.width - 60)

        y = self.height + 30

        vy = -random.uniform(13, 16) * self.speed_scale

        vx = random.uniform(-2, 2)

        gravity = 0.35

        # Original project representation:
        # "fruit" or "bomb"
        if random.random() < self.bomb_chance:

            kind = "bomb"

        else:

            kind = "fruit"

        fruit = Fruit(
            x,
            y,
            vx,
            vy,
            gravity,
            kind=kind
        )

        # Preserve original visual style
        if kind == "bomb":

            fruit.color = BOMB_BLACK

        else:

            fruit.color = random.choice(FRUIT_COLORS)

        self.fruits.append(fruit)

    # =========================================================
    # TASK 3 - MENU RECTANGLES
    # =========================================================

    def get_menu_rect(self, index):

        button_width = 220
        button_height = 45

        x = self.width // 2 - button_width // 2

        y = 250 + index * 55

        return pygame.Rect(
            x,
            y,
            button_width,
            button_height
        )

    # =========================================================
    # RENDER
    # =========================================================

    def render(self, screen):

        # -----------------------------------------------------
        # Normal gameplay
        # -----------------------------------------------------

        for fruit in self.fruits:

            color = getattr(
                fruit,
                "color",
                WHITE
            )

            pygame.draw.circle(
                screen,
                color,
                (
                    int(fruit.x),
                    int(fruit.y)
                ),
                fruit.radius
            )

        # Blade trail
        if len(self.trail) >= 2:

            pygame.draw.lines(
                screen,
                WHITE,
                False,
                self.trail,
                3
            )

        # Score
        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (10, 10)
        )

        # Lives
        lives_text = self.font.render(
            f"Lives: {self.lives}",
            True,
            WHITE
        )

        screen.blit(
            lives_text,
            (
                self.width - lives_text.get_width() - 20,
                10
            )
        )

        # Difficulty
        difficulty_text = self.small_font.render(
            f"Difficulty: {self.difficulty}",
            True,
            WHITE
        )

        screen.blit(
            difficulty_text,
            (
                10,
                45
            )
        )

        # -----------------------------------------------------
        # GAME OVER SCREEN
        # -----------------------------------------------------

        if self.game_over:

            # Dark transparent overlay
            overlay = pygame.Surface(
                (
                    self.width,
                    self.height
                ),
                pygame.SRCALPHA
            )

            overlay.fill(
                (0, 0, 0, 190)
            )

            screen.blit(
                overlay,
                (0, 0)
            )

            # GAME OVER
            game_over_text = self.game_over_font.render(
                "GAME OVER",
                True,
                WHITE
            )

            screen.blit(
                game_over_text,
                (
                    self.width // 2
                    - game_over_text.get_width() // 2,
                    45
                )
            )

            # Final Score
            final_score_text = self.score_font.render(
                f"Final Score: {self.score}",
                True,
                WHITE
            )

            screen.blit(
                final_score_text,
                (
                    self.width // 2
                    - final_score_text.get_width() // 2,
                    120
                )
            )

            # Choose difficulty
            choose_text = self.small_font.render(
                "Choose Difficulty",
                True,
                WHITE
            )

            screen.blit(
                choose_text,
                (
                    self.width // 2
                    - choose_text.get_width() // 2,
                    195
                )
            )

            # Menu buttons
            self.draw_menu_button(
                screen,
                "1 - EASY",
                0
            )

            self.draw_menu_button(
                screen,
                "2 - MEDIUM",
                1
            )

            self.draw_menu_button(
                screen,
                "3 - HARD",
                2
            )

            self.draw_menu_button(
                screen,
                "4 - EXIT",
                3
            )

    # =========================================================
    # DRAW MENU BUTTON
    # =========================================================

    def draw_menu_button(
        self,
        screen,
        text,
        index
    ):

        rect = self.get_menu_rect(index)

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            rect
        )

        pygame.draw.rect(
            screen,
            WHITE,
            rect,
            2
        )

        text_surface = self.menu_font.render(
            text,
            True,
            WHITE
        )

        screen.blit(
            text_surface,
            (
                rect.centerx
                - text_surface.get_width() // 2,
                rect.centery
                - text_surface.get_height() // 2
            )
        )