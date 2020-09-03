from manimlib.imports import *
import os
import pyclbr

class InitialScene(Scene):
    def construct(self):
        x = TextMobject('x')
        y = TextMobject('y')
        c = TextMobject('c')
        equation = TextMobject('$x^2 + y^2 = c^2$')
        equation.move_to(2*RIGHT)
        xline = Line(3*LEFT + 2*DOWN , 1*LEFT + 2*DOWN, color = RED)
        yline = Line(3*LEFT + 2*DOWN , 3*LEFT + 2*UP, color = BLUE)
        cline = Line(3*LEFT + 2*UP, 1*LEFT + 2*DOWN, color = YELLOW)
        xs = TextMobject('$x^2$')
        ys = TextMobject('$y^2$')
        cs = TextMobject('$c^2$')
        rightTriangle = Polygon(
            np.array([-3,-2,0]),
            np.array([-3,2,0]),
            np.array([-1,-2,0]),
            color = WHITE
            )
        rightAngle = Polygon(
            np.array([-3,-2,0]),
            np.array([-2.75, -2.0, 0]),
            np.array([-2.75, -1.75, 0]),
            np.array([-3, -1.75, 0]),
            color = WHITE
        )
        c.move_to(1.5*LEFT)
        x.next_to(rightTriangle, DOWN)
        y.next_to(rightTriangle, LEFT)

        self.add(
            rightTriangle,
            rightAngle
            )
        self.wait(1)
        self.play(
            GrowFromCenter(c),
            GrowFromCenter(x),
            GrowFromCenter(y)
            )
        self.wait(1)
        self.play(
            ApplyMethod(x.set_color, RED),
            FadeIn(xline),
            ApplyMethod(y.set_color, BLUE),
            FadeIn(yline)
        )
        self.play(Rotating(x),Rotating(y))
        self.play(
            ApplyMethod(c.set_color, YELLOW),
            FadeIn(cline)
        )
        self.play(Rotating(c))
        self.wait(1)
        self.play(
            ApplyMethod(x.move_to, RIGHT + UP),
            ApplyMethod(y.move_to, 2*RIGHT + UP),
            ApplyMethod(c.move_to, 3*RIGHT + UP)
        )
        self.wait(5)
        self.play(FadeIn(equation))


if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'manim_tutorial_P37'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("python -m manim manim_tutorial_P37.py %s -l" % item.name)  #Does not play files