import matplotlib.pyplot as plt

def draw_line_DDA(x1, y1, x2, y2):
    # Calculate differences
    dx = x2 - x1
    dy = y2 - y1

    # Find the number of steps
    steps = max(abs(dx), abs(dy))

    # Calculate increments
    x_inc = dx / steps
    y_inc = dy / steps

    # Initialize starting point
    x, y = x1, y1

    # Plot the starting point
    plt.plot(round(x), round(y), marker='o', color='black')

    # Draw the line
    for _ in range(steps):
        x += x_inc
        y += y_inc
        plt.plot(round(x), round(y), marker='o', color='black')

    # Show the plot
    plt.title('DDA Line Drawing Algorithm')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Example usage
draw_line_DDA(1, 2, 8, 10)
