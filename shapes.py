# animate an array of shapes transforming into one another
# shapes to transform: square, circle, triangle, rectangle, pentagon, hexagon, octagon, star, cross, ellipse, heart, arrow


from manim import *


class ShiftShapes(Scene):
    def construct(self):
        shapes_title = Text('Shapes')
        self.play(Write(shapes_title)) # animate title
        self.wait(3)
        self.play(FadeOut(shapes_title)) # remove title

        shapes = VGroup(
            Square(),
            Square(),
            Circle(),
            RegularPolygon(8),
            Triangle(),
            Rectangle(),
            Star(),
            Cross(),
            RegularPolygon(6),
            Ellipse(),
            Arrow(),
            RegularPolygon(5),
        )

        shape_names_array = [
            'square',
            'square',
            'circle',
            'octagon',
            'triangle',
            'rectangle',
            'star',
            'cross',
            'hexagon',
            'ellipse',
            'arrow',
            'pentagon',
        ]

        def loopShapesAndNames():
            # show first shape, then transform into next shape
            shapes.scale(3)
            for i in range(len(shapes) - 1):
                # make size large
                self.play(Transform(shapes[i], shapes[i + 1]))
                # clear the previous shape
                self.wait(3)
                self.remove(shapes[i])

            # show shape names, then transform into next shape name
            for i in range(len(shape_names_array) - 1):
                shape_name = Text(shape_names_array[i])
                self.wait(1)
                self.play(Transform(shape_name, Text(shape_names_array[i + 1])))
                self.wait(3)
                self.remove(shape_name)

        loopShapesAndNames()

if __name__ == '__main__':
    module_name = os.path.basename(__file__)
    command_A = 'manim'
    command_B = module_name
    command_C = 'ShiftShapes'
    command_D = '-pqm'
    command = command_A + ' ' + command_B + ' ' + command_C + ' ' + command_D
    os.system(command)
