from manim import *

class KeplersThirdLaw(Scene):
    def construct(self):
        # Introduction text
        title = Text("Kepler's Third Law", font_size=48)
        subtitle = MathTex("T^2" , "\\propto", "a^3", font_size=36).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(2)

        # Remove title and subtitle
        self.play(FadeOut(title), FadeOut(subtitle))
        

        # Create an ellipse to represent an orbit
        orbit = Ellipse(width=6, height=4, color=BLUE)
        self.play(Create(orbit))
        
        
        watermark = MathTex("\\text{Made by Vincent Ng}", color=GREY).scale(0.8).to_corner(DL)
        self.play(FadeIn(watermark))
        # Create the planet and label star
        star = Dot(orbit.get_center(), color=YELLOW, radius=0.2)
        star_label = MathTex("Star").next_to(star, LEFT)
        self.play(Create(star), Write(star_label))

        # Label the semi-major axis (a)
        semi_major_axis = Line(orbit.get_center(), orbit.get_right(), color=YELLOW)
        a_label = MathTex("a").next_to(semi_major_axis, DOWN)
        self.play(Create(semi_major_axis), Write(a_label))

        # Place a planet on the orbit and animate its motion
        planet = Dot(orbit.get_right(), color=RED)
        self.play(Create(planet))

        # Animate the planet moving along the orbit
        planet_orbit = orbit.copy().set_opacity(0)  # Invisible path for the planet
        self.play(MoveAlongPath(planet, planet_orbit, rate_func=linear, run_time=8))

        # Indicate one complete orbit and label it as T (orbital period)
        t_label = MathTex("T").next_to(planet, RIGHT)
        self.play(Write(t_label))
        self.wait(1)

        # Show the relationship T^2 ∝ a^3
        relation = MathTex("T^2", "\\propto", "a^3").to_edge(DOWN)
        self.play(Write(relation))
        self.wait(2)



        # Group all elements to fade out together

        all_elements = VGroup(watermark, orbit, star, star_label, semi_major_axis, a_label, planet, t_label, relation)

        # Fade out all elements together
        self.play(FadeOut(all_elements))

        # End scene

# To render the scene, you would typically run:
# manim -pql main.py KeplersThirdLaw

