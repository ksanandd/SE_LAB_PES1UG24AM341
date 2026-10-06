import math


class Fruit:
    def __init__(self, x, y, vx, vy, gravity, radius=28, kind="fruit"):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.gravity = gravity
        self.radius = radius
        self.kind = kind
        self.sliced = False

    def update(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy

    def contains_point(self, x, y):
        return math.hypot(
            self.x - x,
            self.y - y
        ) <= self.radius

    def intersects_segment(self, start, end):
        """
        Detect whether a mouse swipe intersects the fruit.

        Uses the shortest distance from the fruit center
        to the complete swipe segment, with a small extra
        margin to make fast swipes reliable.
        """

        x1, y1 = start
        x2, y2 = end

        dx = x2 - x1
        dy = y2 - y1

        # No movement: normal point collision.
        if dx == 0 and dy == 0:
            return self.contains_point(x2, y2)

        segment_length_squared = dx * dx + dy * dy

        # Projection of fruit center onto swipe segment.
        t = (
            (self.x - x1) * dx
            + (self.y - y1) * dy
        ) / segment_length_squared

        # Clamp projection to the actual segment.
        t = max(0.0, min(1.0, t))

        closest_x = x1 + t * dx
        closest_y = y1 + t * dy

        distance = math.hypot(
            self.x - closest_x,
            self.y - closest_y
        )

        # Extra margin makes fast swipes more reliable.
        # It is still small enough to avoid obvious
        # accidental slicing of nearby objects.
        hit_radius = self.radius + 10

        return distance <= hit_radius

    def off_screen(self, height):
        return self.y - self.radius > height