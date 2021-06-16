# Infinite radical
from manim import *


class Scene001(Scene):
    def construct(self):
        text1 = Text("Manim", color=RED, size=2.5)
        ann = Annulus(3, 3.5, 1, 0, color=BLUE)
        self.play(DrawBorderThenFill(ann), DrawBorderThenFill(text1))
        self.play(text1.animate.scale(0), ann.animate.scale(0))
        self.wait(0.5)


class Scene002(Scene):
    def construct(self):
        question = MathTex("\\sqrt{1+2\\sqrt{1+3\\sqrt{1+4\\sqrt{1+5\\sqrt{1+\\cdots } } } } } {\\Large =} {\\huge ?} ")
        self.play(DrawBorderThenFill(question), run_time=5, rate_functions=linear)
        self.wait(3)
        self.play(question.animate.to_edge(UP))


class Scene003(Scene):
    def construct(self):
        question = MathTex("\\sqrt{1+2\\sqrt{1+3\\sqrt{1+4\\sqrt{1+5\\sqrt{1+\\cdots } } } } } {\\Large =} {\\huge ?} ")
        question.to_edge(UP)
        trans1 = MathTex("n=\\sqrt{1+2\\sqrt{1+3\\sqrt{1+4\\sqrt{1+5\\sqrt{1+\\cdots } } } } }  ")
        trans1.to_edge(UP)
        trans2 = MathTex("3=\\sqrt{1+2\\sqrt{1+3\\sqrt{1+4\\sqrt{1+5\\sqrt{1+\\cdots } } } } }  ")
        l1 = MathTex(r"n^{2}=1+(n^{2}-1)")
        l2 = MathTex(r"n^{2}=1+(n-1)(n+1)")
        l3 = MathTex(r"\sqrt{n^2} = \sqrt{1+(n-1)(n+1)} ")
        l4 = MathTex(r"n=\sqrt{1+(n-1)(n+1)} ")
        self.add(question)
        self.play(ReplacementTransform(question, trans1))
        self.play(Write(l1)), self.wait(2)
        self.play(ReplacementTransform(l1, l2)), self.wait(2)
        self.play(ReplacementTransform(l2, l3)), self.wait(2)
        self.play(ReplacementTransform(l3, l4)), self.wait(2)
        self.play(l4.animate.next_to(question, DOWN, aligned_edge=LEFT))
        l5 = MathTex(r"(n+1)^{2}=1+((n+1)^{2}-1)")
        l6 = MathTex(r"(n+1)^{2}=1+(n)(n+2)")
        l7 = MathTex(r"\sqrt{(n+1)^2} = \sqrt{1+(n)(n+2)}")
        l8 = MathTex(r"n+1=\sqrt{1+(n)(n+2)}")
        self.play(Write(l5)), self.wait(2)
        self.play(ReplacementTransform(l5, l6)), self.wait(2)
        self.play(ReplacementTransform(l6, l7)), self.wait(2)
        self.play(ReplacementTransform(l7, l8)), self.wait(2)
        self.play(l8.animate.next_to(l4, DOWN, aligned_edge=LEFT))
        self.play(l8.animate.shift(4 * RIGHT)), self.wait(2)
        g1 = MathTex(r"n=\sqrt{1+(n-1)\sqrt{1+(n)(n+2)}} ").next_to(question, DOWN, aligned_edge=LEFT)
        g2 = MathTex(r"n=\sqrt{1+(n-1)\sqrt{1+(n)\sqrt{1+(n+1)(n+3)}}} ").next_to(question, DOWN, aligned_edge=LEFT)
        g3 = MathTex(r"n=\sqrt{1+(n-1)\sqrt{1+(n)\sqrt{1+(n+1)\sqrt{1+(n+2)(n+4)}}}} ").next_to(question,
                                                                                                DOWN,
                                                                                                aligned_edge=LEFT)
        gn = MathTex(r"n=\sqrt{1+(n-1)\sqrt{1+(n)\sqrt{1+(n+1)\sqrt{1+(n+2)\sqrt{1+\cdots}}}}} ").next_to(question,
                                                                                                          DOWN,
                                                                                                          aligned_edge=LEFT)
        self.play(ReplacementTransform(l4, g1), FadeOutAndShift(l8, UP)), self.wait(2)
        self.play(ReplacementTransform(g1, g2)), self.wait(2)
        self.play(ReplacementTransform(g2, g3)), self.wait(2)
        self.play(ReplacementTransform(g3, gn)), self.wait(2)
        ell = Text("......").shift([6, -0.5, 0])
        self.play(Write(ell)), self.wait(2)
        obs = Text("观察不难得出:", font="SimSun").next_to(gn, DOWN, aligned_edge=LEFT)
        anw = MathTex("n=3").next_to(obs, RIGHT, buff=0.75)
        self.play(Write(obs)), self.play(FadeInFrom(anw, LEFT))
        trans2.next_to(obs, DOWN, aligned_edge=LEFT)
        self.play(Write(trans2))
        self.play(ShowCreationThenFadeAround(anw))
        self.wait(2)