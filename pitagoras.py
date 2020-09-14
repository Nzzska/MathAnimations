from manimlib.imports import *
import os
import pyclbr

class MyObjects():

    # --- MATH EQUATION STUFF ---

    #plain variables
    a = TextMobject('$a$')
    b = TextMobject('$b$')
    c = TextMobject('$c$')
    questionMark = TextMobject('?')
    questionMark.set_color(RED)

    #squares
    aSquared = TextMobject('$a^2$')
    bSquared = TextMobject('$b^2$')
    cSquared = TextMobject('$c^2$')

    #Pythagorean equation(s)
    pythagoreanEquation = TextMobject('$a^2 + b^2 = c^2$')
    aSquaredEquation = TextMobject('$a^2 = c^2 - b^2$')
    bSquaredEquation = TextMobject('$b^2 = c^2 - a^2$')

    #Pythagorean equation(s) square roots
    cEqualsToEquation = TextMobject('$c = /sqrt{a^2 + b^2}$')
    aEqualsToEquation = TextMobject('$a = /sqrt{c^2 - b^2}$')
    bEqualsToEquation = TextMobject('$b = /sqrt{c^2 - a^2}$')

    # --- SHAPES ---
    def rightAngleTriangle(self, a, b, xCoordinate, yCoordinate):
        multiplier = 0.1
        hypotenuse = math.sqrt(a * a + b * b)
        rightTriangle = Polygon(
            np.array([
                xCoordinate, 
                yCoordinate, 
                0
            ]),
            np.array([
                xCoordinate + b, 
                yCoordinate, 
                0 
            ]),
            np.array([
                xCoordinate, 
                yCoordinate + a, 
                0
            ]),
            color = WHITE
        )
        rightAngle = Polygon(
            np.array([
                xCoordinate,
                yCoordinate, 
                0
            ]),
            np.array([
                xCoordinate, 
                yCoordinate + a * multiplier, 
                0
            ]),
            np.array([
                xCoordinate + a * multiplier, 
                yCoordinate + a * multiplier, 
                0
            ]),
            np.array([
                xCoordinate + a * multiplier, 
                yCoordinate, 
                0
            ]),
            color = WHITE
        )
        returnDictionary = {
            "triangle": rightTriangle,
            "angle": rightAngle,
            "hypotenuse": hypotenuse
        }

        return returnDictionary

    def colouredLine(self, startX, startY, finishX, finishY, colorLine):
        start = np.array([startX, startY, 0])
        finish = np.array([finishX, finishY, 0])
        line = Line(start, finish, color = colorLine)

        return line



    # --- TEXT ---

    pythagorasQuote = TextMobject (
        """Seniausi ir trumpiausi žodžiai - "taip" arba "ne" - \n
        yra tie kurie reikalauja daugiausiai laiko apsvarstyti""")
    pythagorasCaption = TextMobject('Pitagoras Samietis 5a. pr. kr.')
    realLifeCaption = TextMobject(
        """ Jeigu mes, norėtume sukonstruoti tokio tipo inkilą, \n
        kokio ilgio reikėtu gaminti stogelį kurio ilgis yra atkarpa ED """
    )

class RealLifeExample(Scene):
    def construct(self):
        text = MyObjects().realLifeCaption
        text.shift(3*UP)
        self.play(
            FadeIn(text)
        )
        self.wait(2)
        self.play(
            FadeOut(text)
        )

class PythagorasQuoter(Scene):
    def construct(self):
        quote = MyObjects().pythagorasQuote
        quote.set_color(BLUE)
        author = MyObjects().pythagorasCaption
        author.shift(DOWN)
        author.scale(0.5)
        author.set_color(YELLOW)
        self.play(
            FadeIn(quote)
        )
        self.play(
            GrowFromEdge(author, LEFT)
        )
        self.wait(3)
        self.play(
            FadeOut(quote),
            FadeOut(author)
        )
        self.wait(1)

class RightTriangleShowcase(Scene):
    def construct(self):
        lines = []
        showcaseTriangles = []
        variables = []
        a = [4.0, 2.5, 3.0]
        b = [1.5, 6.0, 4.0]
        x = [-2, -3, -2.25]
        y = [-2, -1, -1.5]
        aString = [str(a[0]), str(a[1]),str(a[2])]
        bString = [str(b[0]), str(b[1]), str(b[2])]

        for i in range(0, 3, 1):
            #Creating Showcase triangles
            triangle = MyObjects()
            triangle = triangle.rightAngleTriangle(
                a[i], 
                b[i], 
                x[i], 
                y[i]
            )
            showcaseTriangles.append(triangle)

            #Creating colored lines
            line1 = MyObjects()
            line2 = MyObjects()
            line3 = MyObjects()
            line1 = line1.colouredLine(
                x[i],
                y[i],
                x[i] + b[i],
                y[i],
                BLUE
            )
            line2 = line2.colouredLine(
                x[i],
                y[i],
                x[i],
                y[i] + a[i],
                BLUE
            )
            line3 = line3.colouredLine(
                x[i] + b[i],
                y[i],
                x[i],
                y[i] + a[i],
                BLUE
            )
            if i == 0:
                line3.set_color(RED)
            if i == 1:
                line1.set_color(RED)
            if i == 2:
                line2.set_color(RED)
            lines.append([line1, line2, line3])

            #CREATING CAPTIONS FOR EACH TRIANGLE

            #red question mark
            questionMark = TextMobject('?')
            questionMark.set_color(RED)

            cString = str(showcaseTriangles[i]['hypotenuse'])
            tempa = TextMobject(aString[i])
            tempb = TextMobject(bString[i])
            tempc = TextMobject(cString)
            tempa.set_color(BLUE)
            tempb.set_color(BLUE)
            tempc.set_color(BLUE)

            cOffset = 0
            if i == 2:
                tempa = questionMark
                cOffset = 0.5
            if i == 1:
                tempb = questionMark
                cOffset = 0.75
            if i == 0:
                tempc = questionMark

            tempa.next_to(showcaseTriangles[i]["triangle"], LEFT)
            tempb.next_to(showcaseTriangles[i]["triangle"], DOWN)
            tempc.next_to(showcaseTriangles[i]["triangle"])
            tempc.shift(0.5 * UP + 1 * LEFT + cOffset * LEFT)
            variables.append([tempa, tempb, tempc])
        #x.next_to(rightTriangle, DOWN)
        #Unknown C than A than B.
        self.play(
            FadeIn(showcaseTriangles[0]["triangle"]),
        )
        for i in range(0, 3, 1):
            self.play(
                Transform(
                    showcaseTriangles[0]["triangle"], 
                    showcaseTriangles[i]["triangle"]
                )
            )
            self.play(
                    FadeIn(showcaseTriangles[i]["angle"]),
                    FadeIn(lines[i][0]),
                    FadeIn(lines[i][1]),
                    FadeIn(lines[i][2])
            )
            for j in range (0, 3, 1):
                self.play(
                    FadeIn(variables[i][j])
                )
            self.wait(1)
            self.play(
                FadeOut(lines[i][0]),
                FadeOut(lines[i][1]),
                FadeOut(lines[i][2]),
                FadeOut(variables[i][0]),
                FadeOut(variables[i][1]),
                FadeOut(variables[i][2]),
                FadeOut(showcaseTriangles[i]['angle'])
            )
        self.wait(1)
class InitialScene(Scene):
    def construct(self):
        a = MyObjects.a
        b = MyObjects.b
        c = MyObjects.c
        equation = TextMobject('$a^2 + b^2 = c^2$')
        equation.move_to(2*RIGHT)
        xline = Line(3*LEFT + 2*DOWN , 1*LEFT + 2*DOWN, color = BLUE)
        yline = Line(3*LEFT + 2*DOWN , 3*LEFT + 2*UP, color = BLUE)
        cline = Line(3*LEFT + 2*UP, 1*LEFT + 2*DOWN, color = RED)
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
        a.next_to(rightTriangle, DOWN)
        b.next_to(rightTriangle, LEFT)

        self.add(
            rightTriangle,
            rightAngle
            )
        self.wait(1)
        self.play(
            GrowFromCenter(c),
            GrowFromCenter(a),
            GrowFromCenter(b)
            )
        self.wait(1)
        self.play(
            ApplyMethod(a.set_color, BLUE),
            FadeIn(xline),
            ApplyMethod(b.set_color, BLUE),
            FadeIn(yline)
        )
        self.play(Rotating(a),Rotating(b))
        self.play(
            ApplyMethod(c.set_color, RED),
            FadeIn(cline)
        )
        self.play(Rotating(c))
        self.wait(1)
        self.play(
            ApplyMethod(a.move_to, RIGHT + UP),
            ApplyMethod(b.move_to, 2*RIGHT + UP),
            ApplyMethod(c.move_to, 3*RIGHT + UP)
        )
        self.wait(2)
        self.play(FadeIn(equation))
        #aSquaredEquation = TextMobject('$a^2 = c^2 - b^2$')
        aEquation = MyObjects().aSquaredEquation
        aEquation.move_to(equation)
        aEquation.shift(DOWN)
        bEquation = MyObjects().bSquaredEquation
        bEquation.move_to(aEquation)
        bEquation.shift(DOWN)
        self.wait(2)
        self.play(
            FadeIn(aEquation),
            FadeIn(bEquation)
        )

AXES_UNIT_SIZE = 2.5
RANGE = 3.1
 
class UnitCircle(Scene):
    CONFIG = {
        "axes_config": {
            "x_axis_config": {
                "x_min": -RANGE/2,
                "x_max": RANGE/2,
                "unit_size": AXES_UNIT_SIZE,
                "include_numbers": True
            },
            "y_axis_config": {
                "label_direction": UP,
                "x_min": -RANGE/2,
                "x_max": RANGE/2,
                "unit_size": AXES_UNIT_SIZE,
                "include_numbers": True
            },
        },
    }
    def construct(self):
        self.axes   = axes   = self.get_axes()
        self.axes.add(axes.get_axis_labels("Cos(\\theta)", "Sin(\\theta)"))
        self.axes.axis_labels.shift(0.5 * RIGHT)
        self.axes.axis_labels.set_color(ORANGE)
        self.ghost_circle = ghost_circle = self.get_ghost_circle()
        self.radius = radius = self.get_radius(0)
        self.angle  = angle  = self.get_angle()
        self.angle.set_color(ORANGE)
        self.h = h = self.get_h()
 
        circle_group = VGroup(radius, angle, h)
 
        def update_group(vg, alpha):
            theta = interpolate(0,4*PI,alpha) % (2*PI)
            r,a,h = vg
            r.become(self.get_radius(theta))
            a.become(self.get_angle(theta))
            h.become(self.get_h())
 
        self.add(axes,ghost_circle,radius,angle,h)
        self.play(
            UpdateFromAlphaFunc(
                circle_group,
                update_group,
                run_time=18,
                rate_func=linear,
            )
        )
        self.wait()
 
    def get_axes(self):
        axes = Axes(**self.axes_config)
        # FIX Y LABELS
        y_labels = axes.get_y_axis().numbers
        for label in y_labels:
            label.rotate(-PI/2)
        return axes
 
    def get_ghost_circle(self):
        return Circle(
            radius=self.axes.x_axis_config["unit_size"],
            color=GRAY,
            stroke_opacity=0.5
        )
 
    def get_radius(self,theta=0):
        return Line(
            self.ghost_circle.get_center(),
            self.ghost_circle.point_at_angle(theta),
            color=ORANGE
        )
 
    def get_angle(self,theta=0):
        return Arc(
            radius=self.ghost_circle.radius*0.18,
            arc_center=self.ghost_circle.get_center(),
            start_angle=0,
            angle=theta,
        )
 
    def get_h(self):
        return Line(
            self.radius.get_end(),
            [self.radius.get_end()[0],0,0]
        )

if __name__ == "__main__":
    module_name = 'pitagoras'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            #Does not play files
            os.system("manim pitagoras.py %s -l" % item.name)