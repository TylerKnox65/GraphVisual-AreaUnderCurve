import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
import plotly.graph_objects as go
from numpy import sin, cos, exp, log, sqrt, pi
import ipywidgets as widgets
from IPython.display import display

class main():
    def __init__(self) -> None:
        self.type = input("Enter '1' for a 2d graph, '2' for a 3d graph: ")
        angle_slider = widgets.IntSlider(min=0, max=360, step=1, value=0)
        widgets.interactive(self.interactive_3d_plot, angle=angle_slider)
        display(angle_slider)
    def interactive_3d_plot(self,angle):
        while True:
            try:
                if self.type == "2":
                    self.boundmin = int(input("Enter minimum x bound: "))
                    self.boundmax = int(input("Enter maximum x bound: "))
                    self.boundminY = int(input("Enter minimum y bound: "))
                    self.boundmaxY = int(input("Enter maximum y bound: "))
                    X = np.linspace(self.boundmin, self.boundmax, 1000)
                    Y = np.linspace(self.boundminY, self.boundmaxY, 1000)
                    x, y = np.meshgrid(X, Y)
                    
                    Z = eval(input("Enter the function in terms of x, y can also be used to formulate a 3d curve: "))
                    
                
                

                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    ax.plot_surface(x, y, Z, cmap='viridis')
                    min_z = np.min(Z)
                    ax.view_init(30, angle)  
                    ax.plot_surface(x, y, Z - 0.1, color='skyblue', alpha=0.4)
                    ax.plot_wireframe(x, y, np.zeros_like(Z), color='black', alpha=0.5)
                    area = self.calculate_3d_area(x, y, Z)
                    print(area)
                    plt.show()
                    print("finished")
                    break
                elif self.type == "1":
                    self.basicGraph()
                    


                else:
                    raise(SystemExit)
            except Exception as e:
                print(e)
    def calculate_3d_area(self, x, y, z):
        dx = x[0, 1] - x[0, 0]  
        dy = y[1, 0] - y[0, 0]  
        #IDK IF THIS EVEN WORKS
        area = np.sum(z) * dx * dy
        return area
    def basicGraph(self):
            self.boundmin = int(input("Enter minimum x bound: "))
            self.boundmax = int(input("Enter maximum x bound: "))
            x = np.linspace(self.boundmin, self.boundmax, 10000)
            

            X = np.linspace(self.boundmin, self.boundmax, 10000)
            Y = eval(input("Enter the function in terms of x: "))
            plt.plot(X, Y)
            plt.fill_between(X, Y, color='skyblue', alpha=0.4)  # Fill the area under the curve
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Area under the curve')
            plt.grid(True)

            
            area = self.trapezoidal_rule_area(X, Y)
            plt.text(0.1, 0.9, f'Area: {area:.4f}', transform=plt.gca().transAxes)
            plt.show()
            raise(SystemExit())
    
    def trapezoidal_rule_area(self,x_values, y_values): #Uses trapazoidal function to find area under curve
        area = np.sum((x_values[1:] - x_values[:-1]) * (y_values[:-1] + y_values[1:]) / 2)
        return area
if __name__ == "__main__":
    main()
