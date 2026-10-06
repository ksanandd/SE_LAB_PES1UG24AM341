import math


class Fruit:
    def __init__(self, x, y, vx, vy, gravity, radius=28, kind="fruit"):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.gravity = gravity
        self.radius = radius
        self.kind = kind  # "fruit" or "bomb"
        self.sliced = False

    def update(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy

    def contains_point(self, x, y):
        return math.hypot(self.x - x, self.y - y) <= self.radius

    def intersects_segment(self, start, end):
        """
        Check whether the line segment between two mouse positions
        intersects the fruit's circular hitbox.

        This prevents fast mouse swipes from passing through a fruit
        without being detected.
        """
        x1, y1 = start
        x2, y2 = end

        dx = x2 - x1
        dy = y2 - y1

        # If there is no movement between the two positions,
        # fall back to checking the single point.
        if dx == 0 and dy == 0:
            return self.contains_point(x2, y2)

        # Find the position of the closest point on the segment
        # to the center of the fruit.
        t = (
            (self.x - x1) * dx + (self.y - y1) * dy
        ) / (dx * dx + dy * dy)

        # Clamp the closest point to the actual segment.
        t = max(0.0, min(1.0, t))

        closest_x = x1 + t * dx
        closest_y = y1 + t * dy

        # Check whether the closest point is inside the fruit.
        distance = math.hypot(
            self.x - closest_x,
            self.y - closest_y
        )

        return distance <= self.radius

    def off_screen(self, height):
        return self.y - self.radius > height