import math
import random
from array import array

import pygame


class SoundManager:
    """
    Generates game sound effects at runtime using Pygame.
    No external audio files are required.
    """

    SAMPLE_RATE = 44100

    def __init__(self):
        self.enabled = False

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(
                    frequency=self.SAMPLE_RATE,
                    size=-16,
                    channels=1,
                    buffer=512
                )

            # Fruit slice sound
            self.slice_sound = self._create_tone(
                start_frequency=700,
                end_frequency=1100,
                duration=0.10,
                volume=0.35
            )

            # Bomb explosion sound
            self.bomb_sound = self._create_explosion()

            # Game over sound
            self.game_over_sound = self._create_game_over_sound()

            self.enabled = True

        except pygame.error:
            self.enabled = False

    # =========================================================
    # FRUIT SLICE SOUND
    # =========================================================

    def _create_tone(
        self,
        start_frequency,
        end_frequency,
        duration,
        volume
    ):
        sample_count = int(
            self.SAMPLE_RATE * duration
        )

        samples = array("h")

        for i in range(sample_count):

            progress = i / max(
                1,
                sample_count - 1
            )

            frequency = (
                start_frequency
                + (
                    end_frequency
                    - start_frequency
                ) * progress
            )

            envelope = 1.0

            fade_length = int(
                sample_count * 0.10
            )

            if i < fade_length:
                envelope = i / max(
                    1,
                    fade_length
                )

            elif i > sample_count - fade_length:
                envelope = (
                    sample_count - i
                ) / max(
                    1,
                    fade_length
                )

            value = (
                math.sin(
                    2 * math.pi
                    * frequency
                    * i
                    / self.SAMPLE_RATE
                )
                * 32767
                * volume
                * envelope
            )

            samples.append(
                int(value)
            )

        return pygame.mixer.Sound(
            buffer=samples.tobytes()
        )

    # =========================================================
    # BOMB EXPLOSION SOUND
    # =========================================================

    def _create_explosion(self):

        duration = 0.55

        sample_count = int(
            self.SAMPLE_RATE * duration
        )

        samples = array("h")

        for i in range(sample_count):

            time = i / self.SAMPLE_RATE

            progress = time / duration

            # Strong initial explosion followed by decay.
            envelope = (
                (1.0 - progress) ** 2
            )

            # Low-frequency rumble.
            rumble = (
                math.sin(
                    2 * math.pi
                    * 65
                    * time
                )
                * 0.65
            )

            # Second low tone gives the explosion
            # a heavier impact.
            low_boom = (
                math.sin(
                    2 * math.pi
                    * 110
                    * time
                )
                * 0.35
            )

            # Random noise creates the explosive crack.
            noise = (
                random.uniform(
                    -1.0,
                    1.0
                )
                * 0.80
            )

            # Stronger noise at the beginning,
            # then quickly fades.
            noise_envelope = max(
                0.0,
                1.0 - progress * 2.5
            )

            value = (
                rumble
                + low_boom
                + noise * noise_envelope
            )

            value *= (
                32767
                * 0.65
                * envelope
            )

            value = max(
                -32767,
                min(
                    32767,
                    value
                )
            )

            samples.append(
                int(value)
            )

        return pygame.mixer.Sound(
            buffer=samples.tobytes()
        )

    # =========================================================
    # GAME OVER SOUND
    # =========================================================

    def _create_game_over_sound(self):

        duration = 0.70

        sample_count = int(
            self.SAMPLE_RATE * duration
        )

        samples = array("h")

        notes = [
            (440, 0.00, 0.20),
            (330, 0.20, 0.20),
            (220, 0.40, 0.30),
        ]

        for i in range(sample_count):

            time = i / self.SAMPLE_RATE

            value = 0.0

            for frequency, start, length in notes:

                if start <= time < start + length:

                    local_time = (
                        time - start
                    )

                    envelope = max(
                        0.0,
                        1.0
                        - local_time / length
                    )

                    value += (
                        math.sin(
                            2 * math.pi
                            * frequency
                            * local_time
                        )
                        * 32767
                        * 0.30
                        * envelope
                    )

            samples.append(
                int(
                    max(
                        -32767,
                        min(
                            32767,
                            value
                        )
                    )
                )
            )

        return pygame.mixer.Sound(
            buffer=samples.tobytes()
        )

    # =========================================================
    # PLAY SOUNDS
    # =========================================================

    def play_slice(self):

        if self.enabled:
            self.slice_sound.play()

    def play_bomb(self):

        if self.enabled:
            self.bomb_sound.play()

    def play_game_over(self):

        if self.enabled:
            self.game_over_sound.play()