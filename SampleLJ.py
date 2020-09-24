from manimlib.imports import *

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

def LJ(r, epsilon, rm):
    return epsilon * ((rm/r) ** 12 - 2 * (rm/r) ** 6)

def Epsilon(epsilon):
    return -1 * epsilon

def Rm(rm):
    return rm

class PlotLJPotential(GraphScene):
    CONFIG = {
        "y_max" : 5,
        "y_min" : -5,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : 0.5,
        "graph_origin" : 4*LEFT,
        "y_axis_label": '$U(r)$', # Don't write y axis label
        "x_axis_label": '$r$',
        "epsilon": 3, #Depth of potential Well
        "rm": 3, #Distance where potential reaches it's maximum
        "axes_color": BLUE
    }

    def construct(self):
        self.setup_axes()
        plotLJ = self.get_graph(
                                    lambda x : LJ(x, self.epsilon, self.rm),
                                    color = YELLOW,
                                    x_min = 2.55,
                                    x_max = 9,
                                )
        plotEpsilon = self.get_graph(
                                    lambda x : Epsilon(self.epsilon),
                                    color = YELLOW,
                                    x_min = 0,
                                    x_max = self.rm,
                                    )
        plotRm = self.get_vertical_line_to_graph(
                                    self.rm,
                                    plotLJ,
                                    color = YELLOW
        )
        plotLJ.set_stroke(width = 3)
        plotEpsilon.set_stroke(width = 3)
        plotRm.set_stroke(width = 3)
        plotEpsilon = DashedVMobject(plotEpsilon)
        plotRm = DashedVMobject(plotRm)

        self.play(
            ShowCreation(plotLJ),
            run_time = 2
        )
        self.wait()
        self.play(
            FadeIn(plotEpsilon),
            FadeIn(plotRm),
            ShowCreation(self.epsilonTeX),
            ShowCreation(self.RmTeX),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        #width of edges
        self.x_axis.set_stroke(width = 2)
        self.y_axis.set_stroke(width = 2)
        # Additional params
        #colors
        self.x_axis.set_color(BLUE)
        self.y_axis.set_color(BLUE)
        #Labels
        #Y Labels
        self.epsilonTeX = TexMobject("\\epsilon")
        self.epsilonTeX.set_color(YELLOW)
        self.epsilonTeX.next_to(self.coords_to_point(0, - self.epsilon), 3 * LEFT)
        self.RmTeX = TexMobject("r_m")
        self.RmTeX.set_color(YELLOW)
        self.RmTeX.next_to(self.coords_to_point(self.rm, 0), UP)
        #Parametters of x labels
        init_label_x = 1
        end_label_x = 9
        step_x = 1
        #   For y
        init_label_y = -5
        end_label_y = 5
        step_y = 2
        self.x_axis.label_direction = DOWN
        self.y_axis.label_direction = LEFT
        # List of the positions of x labels
        # List of tex objects
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis),
            run_time = 3
        )