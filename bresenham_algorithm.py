import matplotlib.pyplot as plt

def bresenham_line_draw(x1, y1, x2, y2):
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    p = 2 * dy - dx
    
    if x2 < x1:
        x_step = 1
    
    else:
        x_step = -1
        
    if y2 < y1:
        y_step = 1
        
    else: 
        y_step = -1
        
    x, y = x1, y1
    
    plt.plot(x, y, marker="o", color="black")
    
    while x != x2:
        x += x_step
        if p < 0:
            p += 2 * dy
        else:
            y += y_step
            p += 2 * (dy-dx)
        plt.plot(x, y, marker="o", color="black")
    
    plt.title("Bresenham Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()
    
    
bresenham_line_draw(1, 2, 8, 10)