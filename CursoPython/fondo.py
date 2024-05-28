import random

# Character choices for colors
color_chars = "#.*@"

# Create a list of random lines
lines = []
for _ in range(1500):
    start_x = random.randint(0, 1279)
    start_y = random.randint(0, 719)
    end_x = random.randint(0, 1279)
    end_y = random.randint(0, 719)

    # If end_x and start_x are equal, regenerate end_x
    if end_x == start_x:
        end_x = random.randint(0, 1279)  # Generate a new end_x

    color = color_chars[random.randint(0, len(color_chars) - 1)]
    slope = (end_y - start_y) / (end_x - start_x)
    y_intercept = start_y - slope * start_x
    lines.append((start_x, start_y, end_x, end_y, color, slope, y_intercept))