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
        title = Text("完全弹性碰撞", font="KaiTi", size=2).next_to([0, 1.5, 0], DOWN)
        title2 = Text("速度速算", font="KaiTi", size=1.5).next_to(title, DOWN)
        self.play(Write(title)), self.play(Write(title2))
        self.wait(2)
        self.play(Unwrite(title), Unwrite(title2))
        self.wait(1)


class Scene003(Scene):
    def construct(self):
        ground = Line(start=[-8, -1, 0], end=[8, -1, 0], color=BLUE)
        ob1 = Square(2, color=GREEN)
        ob1.shift([-1, 0, 0])
        ob2 = Square(2, color=RED)
        ob2.shift([4, 0, 0])
        md1 = Dot()
        md1.shift([-1, 0, 0])
        md2 = Dot()
        md2.shift([4, 0, 0])
        m1 = Tex("$m_{1}=3$").next_to(md1, UP)
        v1v = Vector(LEFT * 0.5)
        v1v.move_to(md1, RIGHT)
        v1 = Tex("$v_{1}=1$").next_to(md1, DOWN)
        m2 = Tex("$m_{2}=1$").next_to(md2, UP)
        v2v = Vector(LEFT * 2.5)
        v2v.move_to(md2, RIGHT)
        v2 = Tex("$v_{2}=5$").next_to(md2, DOWN)

        self.play(Create(ground))
        self.play(Create(ob1), Create(ob2))
        self.play(GrowFromCenter(md1), GrowFromCenter(md2))
        self.wait()
        self.play(Write(v1), Write(v2), Write(m1), Write(m2), GrowArrow(v1v), GrowArrow(v2v))
        self.wait(0.5)

        gro1 = VGroup(m1, v1, v1v, md1, ob1)
        gro2 = VGroup(m2, v2, v2v, md2, ob2)
        self.play(gro1.animate.shift([-0.75, 0, 0]), gro2.animate.shift([-3.75, 0, 0]), rate_func=linear, run_time=0.5)
        Law1 = Tex("$ m_{1}v_{1}+m_{2}v_{2} = m_{1}v'_{1}+m_{2}v'_{2} $")
        Law1.shift([0, -1.5, 0])
        Law2 = Tex("$\\frac{1}{2} m_{1}v_{1}^{2} + \\frac{1}{2} m_{2}v_{2}^{2} = \\frac{1}{2} m_{1}v_{1}^{'2} + "
                   "\\frac{1}{2} m_{2}v_{2}^{'2}$")
        Law2.next_to(Law1, DOWN)
        self.play(Write(Law1), Write(Law2))
        self.wait(0.5)

        v1p = Tex("$v'_{1}=3$").next_to(md1, DOWN)
        v1vp = Vector(LEFT * 1.5)
        v1vp.move_to(md1, RIGHT)
        v2p = Tex("$v'_{2}=-1$").next_to(md2, DOWN)
        v2vp = Vector(RIGHT * 0.5)
        v2vp.move_to(md2, LEFT)

        self.play(Transform(v1, v1p), Transform(v2, v2p), Transform(v1v, v1vp), Transform(v2v, v2vp))
        self.play(gro1.animate.shift([-25.75, 0, 0]), gro2.animate.shift([8.75, 0, 0]), rate_func=linear, run_time=4)
        self.play(FadeOut(Law1), FadeOut(Law2))


class Scene004(Scene):
    def construct(self):
        ground = Line(start=[-8, -1, 0], end=[8, -1, 0], color=BLUE)
        ob1 = Square(2, color=GREEN)
        ob1.shift([-1, 0, 0])
        ob2 = Square(2, color=RED)
        ob2.shift([4, 0, 0])
        md1 = Dot()
        md1.shift([-1, 0, 0])
        md2 = Dot()
        md2.shift([4, 0, 0])
        m1 = Tex("$m_{1}=3$").next_to(md1, UP)
        v1v = Vector(LEFT * 0.5)
        v1v.move_to(md1, RIGHT)
        v1 = Tex("$v_{1}=1$").next_to(md1, DOWN)
        m2 = Tex("$m_{2}=1$").next_to(md2, UP)
        v2v = Vector(LEFT * 2.5)
        v2v.move_to(md2, RIGHT)
        v2 = Tex("$v_{2}=5$").next_to(md2, DOWN)

        self.add(ground)
        self.add(ob1), self.add(ob2)
        self.play(GrowFromCenter(md1), GrowFromCenter(md2))
        self.wait()
        self.add(v1), self.add(v2), self.add(m1), self.add(m2), self.play(GrowArrow(v1v), GrowArrow(v2v), run_time=0.1)
        self.wait(0.2)

        gro1 = VGroup(m1, v1, v1v, md1, ob1)
        gro2 = VGroup(m2, v2, v2v, md2, ob2)
        self.play(gro1.animate.shift([-0.75, 0, 0]), gro2.animate.shift([-3.75, 0, 0]), rate_func=linear, run_time=0.1)

        v1p = Tex("$v'_{1}=3$").next_to(md1, DOWN)
        v1vp = Vector(LEFT * 1.5)
        v1vp.move_to(md1, RIGHT)
        v2p = Tex("$v'_{2}=-1$").next_to(md2, DOWN)
        v2vp = Vector(RIGHT * 0.5)
        v2vp.move_to(md2, LEFT)

        self.play(Transform(v1, v1p), Transform(v2, v2p), Transform(v1v, v1vp), Transform(v2v, v2vp), run_time=0)
        self.play(gro1.animate.shift([-25.75, 0, 0]), gro2.animate.shift([8.75, 0, 0]), rate_func=linear, run_time=0.8)


class Scene005(Scene):
    def construct(self):
        line1 = Text("两物块直接相撞", font="SimSun").next_to([0, 4, 0], DOWN)
        line2 = Text("因为无能量损失", font="SimSun").next_to(line1, DOWN)
        line3 = Text("即完全弹性碰撞", font="SimSun").next_to(line2, DOWN)
        line4 = Text("考虑加入弹簧后", font="SimSun").next_to(line3, DOWN)
        line5 = Text("初末态能量守恒", font="SimSun").next_to(line4, DOWN)
        line6 = Text("是完全弹性碰撞", font="SimSun").next_to(line5, DOWN)
        line7 = Text("则如下关系成立", font="SimSun").next_to(line6, DOWN)
        line8 = Text("直接碰=弹簧碰", font="SimSun").next_to(line7, DOWN)
        title = Text("弹簧—<v-t>图像分析", font="KaiTi").scale(2)

        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line3))
        self.play(Write(line4), Unwrite(line1))
        self.play(Write(line5), Unwrite(line2))
        self.play(Write(line6), Unwrite(line3))
        self.play(Write(line7), Unwrite(line4))
        self.play(Write(line8), Unwrite(line5))
        self.play(Unwrite(line6))
        self.play(Unwrite(line7))
        self.play(Unwrite(line8), Write(title))
        self.wait()
        self.play(Unwrite(title))


class Scene006(GraphScene):
    def construct(self):
        self.x_axis_label = "$t$"
        self.y_axis_label = "$v$"
        self.x_min = 0
        self.x_max = 5
        self.y_min = -2
        self.y_max = 6
        self.y_labeled_nums = range(-2, 6, 1)
        self.graph_origin = 1.5 * DOWN + 5 * LEFT
        self.x_axis_width = 5

        self.setup_axes(True)

        l1 = self.get_graph(lambda x: 1, x_min=0, x_max=1, color=GREEN)
        l2 = self.get_graph(lambda x: 5, x_min=0, x_max=1, color=RED)
        sin1 = self.get_graph(lambda x: -1 * np.sin(PI * x - PI / 2) + 2, x_min=1, x_max=2, color=GREEN)
        sin2 = self.get_graph(lambda x: 3 * np.sin(PI * x - PI / 2) + 2, x_min=1, x_max=2, color=RED)
        l1p = self.get_graph(lambda x: 3, x_min=2, x_max=3, color=GREEN)
        l2p = self.get_graph(lambda x: -1, x_min=2, x_max=3, color=RED)

        sp1 = Text("压缩前", font="SimSun")
        sp2 = Text("压缩中", font="SimSun")
        sp3 = Text("压缩后", font="SimSun")
        sp1.shift(self.coords_to_point(4, 2))
        sp2.shift(self.coords_to_point(4, 2))
        sp3.shift(self.coords_to_point(4, 2))
        sp = Text("弹簧", font="SimSun").next_to(sp1, UP)
        sq1 = Square(side_length=2, color=GREEN)
        sq1.move_to(RIGHT * 2)
        sq2 = Square(side_length=2, color=RED)
        sq2.move_to(RIGHT * 6)
        realsp = self.get_graph(lambda x: -1 * np.sin(4 * PI * x - PI / 2) + 2, x_min=8, x_max=10, color=WHITE)
        dot = Dot(point=self.coords_to_point(1.5, 2))
        sym = Text("图像关于交点对称", font="SimSun").next_to(dot, RIGHT)
        func1 = VGroup(l1, sin1, l1p)
        func2 = VGroup(l2, sin2, l2p)
        que = Text("交点的意义？", font="SimSun").to_edge(RIGHT)
        ans = Text("共同速度", font="SimSun").to_edge(RIGHT, buff=1)
        ans.set_color_by_gradient(RED, GREEN, YELLOW, BLUE)

        self.play(Write(sp), Write(sp1), Create(sq1), Create(sq2), FadeInFrom(realsp, DOWN))
        self.play(Create(l1), Create(l2), run_time=1.5)
        self.play(Transform(sp1, sp2), run_time=0.4)
        self.play(sq1.animate.shift(RIGHT * 0.5), sq2.animate.shift(LEFT * 0.5),
                  realsp.animate.stretch(factor=0.5, dim=0),
                  rate_func=there_and_back, run_time=1.5)
        self.play(Create(sin1), Create(sin2))
        self.play(Transform(sp1, sp3), run_time=0.4)
        self.play(Create(l1p), Create(l2p))
        self.play(Unwrite(sp), Unwrite(sp1), FadeOut(sq1), FadeOut(sq2), Uncreate(realsp))
        self.play(FadeInFromLarge(dot)), self.play(Write(sym)), self.wait(0.5)
        self.play(func1.animate.set_color(YELLOW), func2.animate.set_color(YELLOW))
        self.play(func1.animate.set_color(GREEN), func2.animate.set_color(RED))
        self.play(Rotate(func1, PI), Rotate(func2, PI))
        self.play(Rotate(func1, PI), Rotate(func2, PI))
        self.play(Write(que)), self.wait(3), self.play(Transform(que, ans))
        self.wait(2)
        self.play(Unwrite(sym), Unwrite(que), Uncreate(func1), Uncreate(func2), FadeOut(dot))
        self.wait()


class Scene007(GraphScene):
    def construct(self):
        self.x_axis_label = "$t$"
        self.y_axis_label = "$v$"
        self.x_min = 0
        self.x_max = 5
        self.y_min = -2
        self.y_max = 6
        self.y_labeled_nums = range(-2, 6, 1)
        self.graph_origin = 1.5 * DOWN + 5 * LEFT
        self.x_axis_width = 5

        self.setup_axes(False)

        sin1 = self.get_graph(lambda x: -1 * np.sin(PI * x - PI / 2) + 2, x_min=1, x_max=2, color=GREEN)
        sin2 = self.get_graph(lambda x: 3 * np.sin(PI * x - PI / 2) + 2, x_min=1, x_max=2, color=RED)
        dot = Dot(point=self.coords_to_point(1.5, 2))
        self.play(Create(sin1), Create(sin2), FadeInFromLarge(dot))
        v1 = Text("1").shift(self.coords_to_point(0.5, 1))
        v1p = Text("3").shift(self.coords_to_point(2.5, 3))
        v2 = Text("5").shift(self.coords_to_point(0.5, 5))
        v2p = Text("-1").shift(self.coords_to_point(2.5, -1))
        sym = Text("2").shift(self.coords_to_point(1.5, 2))
        cov = MathTex(r"v =\frac{m_{1} v_{1} + m_{2} v_{2} }{ m_{1} + m_{2} }")
        cov2 = MathTex(r"=\frac{3 \times 1 + 1 \times 5}{3+1}=2").next_to(cov, RIGHT)
        buff1 = Text("+1", color=GREEN).shift(self.coords_to_point(1, 2))
        buff1p = Text("+1", color=GREEN).shift(self.coords_to_point(2, 3))
        buff2 = Text("-3", color=RED).shift(self.coords_to_point(1, 4))
        buff2p = Text("-3", color=RED).shift(self.coords_to_point(2, 1))
        self.play(Write(cov)), self.play(Write(cov2))
        self.wait()
        self.play(FadeOut(dot))
        self.play(FadeIn(v1)), self.play(Transform(v1, sym), FadeOutAndShift(buff1, UP))
        self.play(Transform(v1, v1p), FadeOutAndShift(buff1p, UP)), self.wait(0.5), self.play(FadeOut(v1))
        self.play(FadeIn(v2)), self.play(Transform(v2, sym), FadeOutAndShift(buff2, DOWN))
        self.play(Transform(v2, v2p), FadeOutAndShift(buff2p, DOWN)), self.wait(0.5), self.play(FadeOut(v2))
        self.play(Uncreate(sin1), Uncreate(sin2), Unwrite(cov), Unwrite(cov2))


class Scene008(Scene):
    def construct(self):
        first = Text("首先，算出共同速度", font="SimSun").to_edge(UP)
        cov = MathTex("v").next_to(first, RIGHT)
        cov.scale(1.5)
        second = Text("接着按如下形式写出", font="SimSun").next_to(first, DOWN)
        self.play(Write(first)), self.play(Write(cov), run_time=0.5), self.play(WiggleOutThenIn(cov))
        self.play(Write(second), cov.animate.move_to(ORIGIN))
        v1 = MathTex("v_{1}").shift(LEFT * 2 + UP)
        v1p = MathTex("v'_{1}").shift(LEFT * 2 + DOWN)
        v2 = MathTex("v_{2}").shift(RIGHT * 2 + UP)
        v2p = MathTex("v'_{2}").shift(RIGHT * 2 + DOWN)
        arc1 = CurvedArrow(1.5 * LEFT + UP, 1.5 * LEFT + DOWN, color=GREEN, angle=PI)
        arc1.flip(UP), arc1.shift(1.125 * RIGHT)
        arc2 = CurvedArrow(1.5 * RIGHT + UP, 1.5 * RIGHT + DOWN, color=RED, angle=PI)
        self.play(Write(v1)), self.play(Write(v2))
        self.play(Create(arc1)), self.play(Create(arc2))
        self.play(Write(v1p)), self.play(Write(v2p))
        third = Text("然后观察差值再类比", font="SimSun").shift(2.5 * DOWN)
        rv1 = Text("1").shift(LEFT * 2 + UP)
        rv1p = Text("3").shift(LEFT * 2 + DOWN)
        rv2 = Text("5").shift(RIGHT * 2 + UP)
        rv2p = Text("-1").shift(RIGHT * 2 + DOWN)
        rcov = Text("2")
        buff1 = Text("+1", color=GREEN).shift(LEFT + 0.5 * UP)
        buff1p = Text("+1", color=GREEN).shift(LEFT + 0.5 * DOWN)
        buff2 = Text("-3", color=RED).shift(RIGHT + 0.5 * UP)
        buff2p = Text("-3", color=RED).shift(RIGHT + 0.5 * DOWN)
        self.play(Write(third), Transform(v1, rv1), Transform(v2, rv2), Transform(cov, rcov))
        self.wait(1.5)
        self.play(FadeOutAndShift(buff1, UP), run_time=1.5), self.play(FadeOutAndShift(buff1p, UP), run_time=1.5)
        self.play(Transform(v1p, rv1p))
        self.play(FadeOutAndShift(buff2, DOWN), run_time=1.5), self.play(FadeOutAndShift(buff2p, DOWN), run_time=1.5)
        self.play(Transform(v2p, rv2p))
        last = Text("最后下出结论计算得", font="SimSun").to_edge(DOWN)
        concl1 = MathTex("v'_{1}=3").shift(4.5 * RIGHT + 0.5 * UP)
        concl2 = MathTex("v'_{2}=-1").shift(4.5 * RIGHT + 0.5 * DOWN)
        self.play(Write(last)), self.play(Write(concl1), Write(concl2))
        self.play(Indicate(concl1), Indicate(concl2))
        self.wait(1)


class Scene009(Scene):
    def construct(self):
        tha = Text("谢谢观看！", font="SimSun", color=RED)
        self.play(Write(tha))
        self.play(tha.animate.scale(3))
        self.play(FadeOutAndShift(tha, DOWN))
