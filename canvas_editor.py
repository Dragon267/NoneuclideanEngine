import pygame
import os
import math

# Initialize Pygame
pygame.init()

# Set up the canvas dimensions
canvas_width, canvas_height = 800, 600

def process(point):
    x = point[0] / canvas_width
    y = point[1] / canvas_height

    lon = x * (2 * math.pi) - math.pi
    lat = y * math.pi - math.pi / 2

    return (lon, lat)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a surface (canvas) for drawing
canvas = pygame.display.set_mode((canvas_width, canvas_height))
canvas.fill(WHITE)
pygame.display.set_caption("Drawing Canvas")

# Create a list to store the shapes
shapes = []

# Create the directory for logs if it doesn't exist
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

# Flag to track if the mouse button is pressed
mouse_pressed = False

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Start drawing a new shape
                mouse_pressed = True
                # Create a new shape as a list of points
                current_shape = []
                shapes.append(current_shape)
                # Save the position of the initial point
                point = event.pos
                current_shape.append(point)
                print("Point added:", point)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                # Finish drawing the current shape
                mouse_pressed = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_pressed:
                # Draw lines while dragging the mouse
                point = event.pos
                current_shape.append(point)
                print("Point added:", point)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # Save the points to a file
                file_path = os.path.join(logs_dir, "points.txt")
                with open(file_path, "w") as file:
                    for shape in shapes:
                        for point in shape:
                            (x,y) = process(point)
                            file.write(f"{x} {y}\n")
                        file.write("\n")  # Add a newline between shapes
                print("Points saved to:", file_path)

    # Clear the canvas
    canvas.fill(WHITE)

    # Draw the shapes on the canvas
    for shape in shapes:
        if len(shape) > 1:
            pygame.draw.lines(canvas, BLACK, False, shape)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

