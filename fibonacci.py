# mark points on a fibonacci spiral, and draw a line between them

import math
from manim import *


fibonacci_sequence = [
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
]


class FibonacciSpiral(Scene):
    def construct(self):
        # create a fibonacci spiral
        fibonacci_spiral = VGroup()
        for i in range(len(fibonacci_sequence)):
            # calculate the angle
            angle = (360 / len(fibonacci_sequence)) * i
            # calculate the radius
            radius = fibonacci_sequence[i] * 0.1
            # calculate the x and y coordinates
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            # create a point
            point = Dot(point=(x, y, 0))
            # add the point to the fibonacci spiral
            fibonacci_spiral.add(point)

        # draw a line between the points
        self.play(Create(fibonacci_spiral))
        self.wait(3)

        # mark points on the fibonacci spiral
        for i in range(len(fibonacci_sequence)):
            # calculate the angle
            angle = (360 / len(fibonacci_sequence)) * i
            # calculate the radius
            radius = fibonacci_sequence[i] * 0.1
            # calculate the x and y coordinates
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            # create a point
            point = Dot(point=(x, y, 0))
            # add the point to the fibonacci spiral
            fibonacci_spiral.add(point)
            # mark the point
            self.play(Create(point))
            self.wait(0.5)

        # draw a line between the points
        self.play(Create(fibonacci_spiral))
        self.wait(3)

        # remove the fibonacci spiral
        self.play(FadeOut(fibonacci_spiral))
        self.wait(3)
       
if __name__ == '__main__':
    module_name = os.path.basename(__file__)
    command_A = 'manim'
    command_B = module_name
    command_C = 'FibonacciSpiral'
    command_D = '-pqm'
    command = command_A + ' ' + command_B + ' ' + command_C + ' ' + command_D
    os.system(command)
