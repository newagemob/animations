# draw archimedes spiral within the bounds of the camera, animate a line being drawn

import math
from manim import *

class ArchimedesSpiral(Scene):
    def construct(self):
        # create a spiral
        spiral = VGroup()

        for i in range(800):
            # calculate the angle
            angle = (360 / 100) * i
            # calculate the radius
            radius = i * 0.1
            # calculate the x and y coordinates
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            # create a point
            point = Dot(point=(x, y, 0))
            # add the point to the spiral
            spiral.add(point)

        # scale down the spiral
        spiral.scale(0.166)

        # draw a line between the points
        self.play(Create(spiral))
        # highlight the spiral line gradient from red to blue -- use Mobject.animate.set_color_by_gradient
        self.play(spiral.animate.set_color_by_gradient(RED, GREEN))

        self.wait(3)

        # transform spiral into a line that waves
        self.play(Transform(spiral, Line(start=(-12, -5, 0), end=(12, 5, 0))))
        self.wait(3)
        self.remove(spiral)
        self.play(Transform(Line(start=(-12, -5, 0), end=(12, 5, 0)), RegularPolygon(6)))
        
        # self.play(Transform(spiral, Circle()))
        self.wait(3)
        

if __name__ == '__main__':
    module_name = os.path.basename(__file__)
    command_A = 'manim'
    command_B = module_name
    command_C = 'ArchimedesSpiral'
    command_D = '-pqm'
    command = command_A + ' ' + command_B + ' ' + command_C + ' ' + command_D
    os.system(command)
