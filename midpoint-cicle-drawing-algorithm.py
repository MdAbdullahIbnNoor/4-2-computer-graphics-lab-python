import matplotlib.pyplot as plt

def draw_circle_midpoint(x_center, y_center, radius):
    x = radius
    y = 0
    p = 1 - radius  # Initial decision parameter for the midpoint

    # Collect coordinates in a list
    coordinates = [(x_center + x, y_center - y)]

    # Plot the initial points based on circle symmetry
    plot_symmetric_points(x_center, y_center, x, y, coordinates)

    while x > y:
        y += 1

        # Mid-point is inside or on the perimeter of the circle
        if p <= 0:
            p = p + 2*y + 1

        # Mid-point is outside the perimeter of the circle
        else:
            x -= 1
            p = p + 2*y - 2*x + 1

        # All the perimeter points have already been printed
        if x < y:
            break

        # Collect and plot the generated point in the other octants
        plot_symmetric_points(x_center, y_center, x, y, coordinates)

    # Plot the points
    plt.plot([point[0] for point in coordinates], [point[1] for point in coordinates], marker='o', linestyle='', color='black')

    # Show the plot
    plt.title('Midpoint Circle Drawing Algorithm')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def plot_symmetric_points(x_center, y_center, x, y, coordinates):
    # Plot the generated point and its reflection in the other octants
    coordinates.extend([
        (x_center + x, y_center - y),
        (x_center - x, y_center - y),
        (x_center + x, y_center + y),
        (x_center - x, y_center + y),
        (x_center + y, y_center - x),
        (x_center - y, y_center - x),
        (x_center + y, y_center + x),
        (x_center - y, y_center + x)
    ])

# Example usage
draw_circle_midpoint(0, 0, 5)
