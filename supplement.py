import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cross_section_plot():
    cross_section_type = input("Enter the type of cross-section (Square, Semicircle, Triangle, or Rectangle): ").lower()
    if cross_section_type not in ["square", "semicircle", "triangle", "rectangle"]:
        print("Invalid cross-section type!")
        return

    if input("Are there two functions? (y/n): ").lower() == 'y':
        # Assuming user provides two functions and we find area between them
        # In this example, just plotting a simple square
        x = np.linspace(-5, 5, 100)
        y1 = eval(input("Enter the first function: "), {'np': np},{"x":x})
        y2 = eval(input("Enter the second function: "), {'np': np})

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y1, zs=0, zdir='y')
        ax.plot(x, y2, zs=0, zdir='y')
        ax.fill_between(x, y1, y2, color='b', alpha=0.3)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title("Cross-section Plot")
        plt.show()
    else:
        bound_type = input("Enter the bound type (x= or y=): ").lower()
        if bound_type not in ['x=', 'y=']:
            print("Invalid bound type!")
            return
        bound_value = float(input(f"Enter the value of the bound ({bound_type}): "))
        if cross_section_type == "square":
            if bound_type == "x=":
                # Plotting a square cross-section along the y-axis
                y = np.linspace(-5, 5, 100)
                plt.plot([bound_value, bound_value], [-5, 5], color='b')
                plt.plot([-5, 5], [bound_value, bound_value], color='b')
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title("Square Cross-section Plot")
                plt.grid(True)
                plt.show()
            else:
                # Plotting a square cross-section along the x-axis
                x = np.linspace(-5, 5, 100)
                plt.plot([-5, 5], [bound_value, bound_value], color='b')
                plt.plot([bound_value, bound_value], [-5, 5], color='b')
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title("Square Cross-section Plot")
                plt.grid(True)
                plt.show()

def rotation_plot():
    if input("Are there two functions? (y/n): ").lower() == 'y':
        axis_of_rotation = input("Enter the axis of rotation (y=, x=, or an axis): ").lower()
        # Assuming user provides two functions and an axis of rotation
        # In this example, just plotting a simple rotation around y-axis
        x = np.linspace(-5, 5, 100)
        y1 = eval(input("Enter the first function: "), {'np': np},{"x":x})
        y2 = eval(input("Enter the second function: "), {'np': np},{"x":x})

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y1, zs=0, zdir='y')
        ax.plot(x, y2, zs=0, zdir='y')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title("3D Rotation Plot")
        plt.show()
    else:
        bound_type = input("Enter the bound type (x= or y=): ").lower()
        axis_of_rotation = input("Enter the axis of rotation (y=, x=, or an axis): ").lower()
        # Assuming user provides one function, bounds, and an axis of rotation
        # In this example, just plotting a simple rotation around y-axis
        if bound_type == 'x=':
            x = np.linspace(-5, 5, 100)
            y = eval(input("Enter the function: "), {'np': np})
            plt.plot(x, y, color='b')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title("Function Plot")
            plt.grid(True)
            plt.show()
        else:
            y_bound = float(input(f"Enter the value of the bound ({bound_type}): "))
            y = np.linspace(-5, 5, 100)
            x = eval(input("Enter the function: "), {'np': np})
            plt.plot(x, y, color='b')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title("Function Plot")
            plt.grid(True)
            plt.show()

# Main program
function_type = input("Enter the type of function (cross-section or rotation): ").lower()
if function_type == 'cross-section':
    cross_section_plot()
elif function_type == 'rotation':
    rotation_plot()
else:
    print("Invalid function type!")
