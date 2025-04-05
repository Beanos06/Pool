from manim import *
from math import pi
from calculs import approximate_limit_series, get_series
import numpy as np

b = 6
a = 3
theta = pi/6

class Scene1(Scene):
    def construct(self):
        convergence_point = get_series(b=b, theta=theta)
        t = ValueTracker(3)

        grid = Axes(
            x_range=(0,9),
            y_range=(0,7),
            x_length=9,
            y_length=7,
        )

        axis_labels = grid.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45)
        )


        table = Square(side_length=6, stroke_width=4, color=GREEN, fill_opacity=0.5).shift(LEFT*1.5 + DOWN*0.5)
        ball = Dot(color=WHITE, fill_opacity=1).move_to(grid @ (a,0,0))
        ball_transparent_initial = Dot(color=RED, fill_opacity=1).move_to(grid @ (a,0,0))
        a_text_initial = Tex(f"a={a}").scale(0.55).next_to(grid @ (a,0,0), direction=UP)

        self.play(Create(grid, run_time=1))
        self.add(axis_labels)
        self.play(DrawBorderThenFill(table, run_time=1))
        self.play(FadeIn(ball, run_time=1))
        self.play(FadeIn(ball_transparent_initial,))
        self.play(FadeIn(a_text_initial))
        run_time = 2

        side = 1
        previous_x = a
        previous_y = 0
        for i in range(1,5):
            run_time -= 0.2
            if run_time <= 0:
                run_time = 0.1

            if side == 1: # Bottom side
                x = b
                y = approximate_limit_series(b, i, theta)
            if side == 2:
                x = b-approximate_limit_series(b, i, theta)
                y = b
            if side == 3:
                x = 0
                y = b-approximate_limit_series(b, i, theta)
            if side == 4:
                x = approximate_limit_series(b, i, theta)
                y = 0
                side = 0
            
            new_pos = grid.coords_to_point(x, y)
            self.play(ball.animate.move_to(new_pos), run_time=run_time)
            grid += Dot(color=WHITE, fill_opacity=0.5).move_to(grid @ (x,y,0))
            trail = Line(grid @ (previous_x,previous_y), grid @ (x,y), stroke_opacity=0.5, stroke_width=1)
            grid += trail
            side += 1
            previous_x = x
            previous_y = y

        self.wait(3)

        side = 1
        run_time = 1.5
        previous_x = a
        previous_y = 0
        for i in range(4,52):
            run_time -= 0.2
            if run_time <= 0:
                run_time = 0.1

            if side == 1: # Bottom side
                x = b
                y = approximate_limit_series(b, i, theta)
            if side == 2:
                x = b-approximate_limit_series(b, i, theta)
                y = b
            if side == 3:
                x = 0
                y = b-approximate_limit_series(b, i, theta)
            if side == 4:
                x = approximate_limit_series(b, i, theta)
                y = 0
                side = 0

            new_pos = grid.coords_to_point(x, y)
            self.play(ball.animate.move_to(new_pos), run_time=run_time)
            grid += Dot(color=WHITE, fill_opacity=0.5).move_to(grid @ (x,y,0))
            grid += Line(grid @ (previous_x,previous_y), grid @ (x,y), stroke_opacity=0.5, stroke_width=1)
            side += 1
            previous_x = x
            previous_y = y
        
        a_text_final = Tex(f"a={round(convergence_point, 3)}...").scale(0.55).next_to(grid @ (convergence_point,0,0), direction=DOWN)
        self.play(FadeIn(a_text_final))
        self.wait(3)

            