from manim import *

class TransitPhotometry(Scene):
    def construct(self):
        # Introduction text
        title = Text("Transit Photometry", font_size=48)
        self.play(Write(title))
        self.wait(2) 
        self.play(FadeOut(title))
        
        
        watermark = MathTex("\\text{Made by Vincent Ng}", color=GREY).scale(0.8).to_corner(UL)
        self.play(FadeIn(watermark))

        # Create a star and planet
        star = Circle(radius=1, color=YELLOW, fill_opacity=1)
        planet = Circle(radius=0.2, color=BLUE, fill_opacity=1).move_to(LEFT * 4)

        # Create light curve axis
        axes = Axes(
            x_range=[0,10,1],
            y_range=[0.8,1.2,0.1],
            axis_config={"color":GREY},
            tips=False,           
        ).scale(0.7).to_edge(DOWN)
        

        x_label = axes.get_x_axis_label("Time", edge=RIGHT, direction=DOWN, buff=0.4)
        y_label = axes.get_y_axis_label("Brightness", edge=UP, direction=LEFT, buff=0.4)

        # Initial light curve (a flat line at brightness = 1)
        light_curve = axes.plot(lambda t: 1, color=RED)

        self.play(Create(star), Create(planet))
        self.wait(1)
        self.play(Create(axes), Write(x_label), Write(y_label), Create(light_curve))
        self.wait(1)

        # Move planet across the star and update the light curve
        def get_light_curve():
            curve = VMobject()
            curve.set_points_as_corners([
                axes.c2p(0, 1),
                axes.c2p(2, 1),
                axes.c2p(3, 1),
                axes.c2p(4, 0.9),
                axes.c2p(5, 0.9),
                axes.c2p(6, 0.9),
                axes.c2p(7, 1),
                axes.c2p(10, 1)
            ])
            return curve

        self.play(
            AnimationGroup(
                MoveAlongPath(planet, Line(LEFT * 4, RIGHT * 4), rate_func=linear, run_time=6),
                ReplacementTransform(light_curve, get_light_curve(), run_time=6),
                lag_ratio=0
            )
        )
        self.wait(2)

        all_elements = VGroup(star, planet, axes, x_label, y_label, watermark, light_curve)
        self.play(FadeOut(all_elements), FadeOut(get_light_curve()))
                  

