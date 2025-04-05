from manim import *
from math import pi
from calculs import approximate_limit_series, get_convergence_point_1
import numpy as np

b = 6
a = 2
theta = pi/6

class Scene1(Scene):
    def construct(self):
        convergence_point = get_convergence_point_1(b=b, theta=theta)

        grid = Axes(
            x_range=(0,9),
            y_range=(0,7),
            x_length=9,
            y_length=7,
        )

        axis_labels = grid.get_axis_labels(
            MathTex("x").scale(0.7), MathTex("y").scale(0.7)
        )

        table = Square(side_length=6, stroke_width=4, color=GREEN, fill_opacity=0.5).shift(LEFT*1.5 + DOWN*0.5)
        ball = Dot(color=WHITE, fill_opacity=1).move_to(grid @ (a,0,0))
        ball_transparent_initial = Dot(color=YELLOW, fill_opacity=1).move_to(grid @ (a,0,0))
        a_text_initial = MathTex(f"a={a}").scale(0.55).next_to(grid @ (a,0,0), direction=UP)

        self.play(Create(grid, run_time=1))
        self.add(axis_labels)
        self.play(DrawBorderThenFill(table, run_time=1))
        self.play(FadeIn(ball, run_time=1))
        self.play(FadeIn(ball_transparent_initial,))
        self.play(FadeIn(a_text_initial))
        run_time = 2

        LINE_WIDTH = 4

        # FIRST PART OF THE ANIMATION
        side = 1
        previous_x = a
        previous_y = 0
        for i in range(1,5):

            approximated_value = approximate_limit_series(a=a, b=b, j=i, theta=theta)

            run_time -= 0.2
            if run_time <= 0:
                run_time = 0.1

            if side == 1: # Right side
                x = b
                y = approximated_value
                line1 = Line(grid @ (x,0), grid @ (x,y), stroke_width=LINE_WIDTH, stroke_color=RED)
                line2 = Line(grid @ (a,0), grid @ (b,0), stroke_width=LINE_WIDTH, stroke_color=BLUE)
                line1_text = MathTex(f"r_{side}").next_to(line1, RIGHT).scale(0.5).set_color(RED)
                line2_text = MathTex("(b-a)").next_to(line2, DOWN, buff=0.1).scale(0.5).set_color(BLUE)
            if side == 2: # Top side 
                x = b-approximated_value
                y = b
                line1 = Line(grid @ (x,b), grid @ (b,b), stroke_width=LINE_WIDTH, stroke_color=RED)
                line2 = Line(grid @ (b,previous_y), grid @ (b,y), stroke_width=LINE_WIDTH, stroke_color=BLUE)
                line1_text = MathTex(f"r_{side}").next_to(line1, UP).scale(0.5).set_color(RED)
                line2_text = MathTex("b-r_1").next_to(line2, RIGHT, buff=0.1).scale(0.5).set_color(BLUE)
            if side == 3: #Left Side
                x = 0
                y = approximated_value
                line1 = Line(grid @ (x,b), grid @ (previous_x,b), stroke_width=LINE_WIDTH, stroke_color=BLUE)
                line2 = Line(grid @ (0,b), grid @ (0,y), stroke_width=LINE_WIDTH, stroke_color=RED)
                line1_text = MathTex(f"r_{side}").next_to(line1, LEFT).scale(0.5).set_color(RED)
                line2_text = MathTex("b-r_2").next_to(line2, UP, buff=0.1).scale(0.5).set_color(BLUE)
            if side == 4: # Bottom side
                x = approximated_value
                y = 0
                line1 = Line(grid @ (previous_x,0), grid @ (x,0), stroke_width=LINE_WIDTH, stroke_color=RED)
                line2 = Line(grid @ (0,previous_y), grid @ (0,0), stroke_width=LINE_WIDTH, stroke_color=BLUE)
                line1_text = MathTex(f"r_{side}").next_to(line1, DOWN).scale(0.5).set_color(BLUE)
                line2_text = MathTex("b-r_3").next_to(line2, LEFT, buff=0.1).scale(0.5).set_color(RED)
                side = 0
            
            new_pos = grid.coords_to_point(x, y)
            self.play(ball.animate.move_to(new_pos), run_time=run_time)
            grid += Dot(color=WHITE, fill_opacity=0.5).move_to(grid @ (x,y,0))
            self.add(line1)
            self.add(line2)
            self.add(line1_text)
            self.add(line2_text)

            trail = Line(grid @ (previous_x,previous_y), grid @ (x,y), stroke_opacity=0.5, stroke_width=1)
            grid += trail
            side += 1
            previous_x = x
            previous_y = y

        self.wait(3)
        
        # SECOND PART OF THE ANIMATION
        side = 1
        run_time = 1.5
        for i in range(5,52):
            run_time -= 0.2
            if run_time <= 0:
                run_time = 0.1
            
            approximated_value = approximate_limit_series(a=a, b=b, j=i, theta=theta)
            
            if side == 1: # Bottom side
                x = b
                y = approximated_value
            if side == 2:
                x = b-approximated_value
                y = b
            if side == 3:
                x = 0
                y = b-approximated_value
            if side == 4:
                x = approximated_value
                y = 0
                side = 0

            new_pos = grid.coords_to_point(x, y)
            self.play(ball.animate.move_to(new_pos), run_time=run_time)
            grid += Dot(color=WHITE, fill_opacity=0.5).move_to(grid @ (x,y,0))
            grid += Line(grid @ (previous_x,previous_y), grid @ (x,y), stroke_opacity=0.5, stroke_width=1)
            side += 1
            previous_x = x
            previous_y = y
        
        final_point = Dot().move_to(grid @ (convergence_point,0,0))
        a_text_final = MathTex(f"{round(convergence_point, 4)}...").scale(0.55).next_to(final_point, direction=UP)
        self.play(Write(a_text_final), run_time=1)
        self.wait(4)