# Video is available on https://www.bilibili.com/video/BV11q4y1L7nm
from manim import *


class Scene001(Scene):  # Manim标题行
    def construct(self):
        text1 = Text("Manim", color=str(RED), size=int(2.5))
        ann = Annulus(3, 3.5, 1, 0, color=BLUE)
        self.play(DrawBorderThenFill(ann), DrawBorderThenFill(text1))
        self.play(text1.animate.scale(0), ann.animate.scale(0))
        self.wait(0.5)


class Scene002(Scene):  # 正文标题行
    def construct(self):
        h1 = Text("磁发散与磁聚焦", font="SimSun").scale(1.5)
        h2 = Text("点进平出、平进点出", font="KaiTi").next_to(h1, DOWN)
        incir = Circle(color=BLUE, radius=1).shift(3 * LEFT)
        outcir = Circle(color=RED, radius=1).shift(3 * RIGHT)
        anims = LaggedStart(FadeIn(h1, shift=UP), Write(h2), lag_ratio=0.6)
        self.play(anims, run_time=3)
        self.play(h1.animate.shift(2 * UP), h2.animate.shift(DOWN))
        self.play(Create(incir), Create(outcir), h1.animate.shift(12 * RIGHT), h2.animate.shift(12 * LEFT))
        self.play(incir.animate.scale(2), outcir.animate.scale(2))
        grid = NumberPlane()
        self.play(Create(grid))
        dot = Dot(color=BLUE).move_to(incir.get_center())
        cross = MathTex(r"\times").move_to(outcir.get_center())
        cross.set_color(RED)
        self.play(SpinInFromNothing(dot), SpinInFromNothing(cross))
        self.play(Indicate(dot, scale_factor=3), Indicate(cross, scale_factor=3))
        self.wait(0.5)
        protonshape = Circle(color=WHITE, radius=0.2, fill_color=BLACK, fill_opacity=1)
        positivesignal = MathTex("+").move_to(protonshape.get_center())
        proton = VGroup(protonshape, positivesignal)
        proton.shift(incir.get_center() + 2 * DOWN)
        self.play(FadeIn(proton, scale=2))
        velocity = Arrow(start=proton.get_center(), end=proton.get_center() + RIGHT, buff=0)
        v = MathTex("v").next_to(velocity, RIGHT)
        self.play(GrowArrow(velocity)), self.play(DrawBorderThenFill(v)), self.play(Indicate(velocity), Indicate(v,
                                                                                                                 scale_factor=2)), self.play(
            Unwrite(v))
        combination = VGroup(velocity, proton)
        combination.center = proton.get_center()

        path1 = Arc(start_angle=2 * PI / 3, angle=-PI / 6, radius=2, arc_center=(-2, -np.sqrt(3) - 2, 0))
        self.play(Rotating(combination, radians=PI / 6, about_point=combination.center), run_time=0.5)
        self.play(Rotating(combination, radians=-PI / 6, about_point=np.array([-2, -np.sqrt(3) - 2, 0]), run_time=0.5),
                  Create(path1, run_time=0.5, rate_func=linear))
        self.wait(0.5)
        combination.shift(LEFT + np.sqrt(3) * UP + 2 * DOWN)

        path2 = Arc(start_angle=5 * PI / 6, angle=-PI / 3, radius=2, arc_center=(-3 + np.sqrt(3), -3, 0))
        self.play(Rotating(combination, radians=PI / 3, about_point=combination.center), run_time=1)
        self.play(Rotating(combination, radians=-PI / 3, about_point=np.array([-3 + np.sqrt(3), -3, 0]), run_time=1),
                  Create(path2, run_time=1, rate_func=linear))
        self.wait(0.5)
        combination.shift(np.sqrt(3) * LEFT + DOWN)

        path3 = Arc(start_angle=PI, angle=-PI / 2, radius=2, arc_center=(-1, -2, 0))
        self.play(Rotating(combination, radians=PI / 2, about_point=combination.center), run_time=1.5)
        self.play(Rotating(combination, radians=-PI / 2, about_point=np.array([-1, -2, 0]), run_time=1.5),
                  Create(path3, run_time=1.5, rate_func=linear))
        self.wait(0.5)
        combination.shift(2 * LEFT + 2 * DOWN)

        path4 = Arc(start_angle=7 * PI / 6, angle=-2 * PI / 3, radius=2, arc_center=(-3 + np.sqrt(3), -1, 0))
        self.play(Rotating(combination, radians=2 * PI / 3, about_point=combination.center), run_time=2)
        self.play(
            Rotating(combination, radians=-2 * PI / 3, about_point=np.array([-3 + np.sqrt(3), -1, 0]), run_time=2),
            Create(path4, run_time=2, rate_func=linear))
        self.wait(0.5)
        combination.shift(np.sqrt(3) * LEFT + 3 * DOWN)

        path5 = Arc(start_angle=8 * PI / 6, angle=-5 * PI / 6, radius=2, arc_center=(-2, np.sqrt(3) - 2, 0))
        self.play(Rotating(combination, radians=5 * PI / 6, about_point=combination.center), run_time=2.5)
        self.play(
            Rotating(combination, radians=-5 * PI / 6, about_point=np.array([-2, np.sqrt(3) - 2, 0]), run_time=2.5),
            Create(path5, run_time=2.5, rate_func=linear))
        self.wait(0.5)
        self.play(FadeOut(combination))

        arrow1 = Arrow(start=(-2, -np.sqrt(3), 0), end=(-1, -np.sqrt(3), 0), buff=0)
        arrow2 = Arrow(start=(np.sqrt(3) - 3, -1, 0), end=(np.sqrt(3) - 2, -1, 0), buff=0)
        arrow3 = Arrow(start=(-1, 0, 0), end=(0, 0, 0), buff=0)
        arrow4 = Arrow(start=(np.sqrt(3) - 3, 1, 0), end=(np.sqrt(3) - 2, 1, 0), buff=0)
        arrow5 = Arrow(start=(-2, np.sqrt(3), 0), end=(-1, np.sqrt(3), 0), buff=0)

        self.play(
            LaggedStart(GrowArrow(arrow1), GrowArrow(arrow2), GrowArrow(arrow3), GrowArrow(arrow4), GrowArrow(arrow5),
                        lag_ratio=0.3))

        word1 = Text("磁发散", font="SimSun").shift(2.5 * DOWN)
        word2 = Text("点进平出", font="SimSun").shift(3.5 * DOWN)
        self.play(Write(word1)), self.play(Write(word2))
        self.play(Indicate(arrow1, scale_factor=1.2),
                  Indicate(arrow2, scale_factor=1.2),
                  Indicate(arrow3, scale_factor=1.2),
                  Indicate(arrow4, scale_factor=1.2),
                  Indicate(arrow5, scale_factor=1.2),
                  )
        word3 = Text("互相平行", font="SimSun").shift(2.5 * UP)
        self.play(Write(word3)), self.wait(0.5), self.play(word3.animate.shift(4 * DOWN), rate_func=there_and_back,
                                                           run_time=3)
        self.play(LaggedStart(arrow1.animate.shift(3 * RIGHT),
                              arrow2.animate.shift((5 - 2 * np.sqrt(3)) * RIGHT), arrow3.animate.shift(1 * RIGHT),
                              arrow4.animate.shift((5 - 2 * np.sqrt(3)) * RIGHT), arrow5.animate.shift(3 * RIGHT)))
        self.play(Unwrite(word3))

        path6 = Arc(start_angle=PI / 2, angle=-PI / 6, radius=2, arc_center=(2, -np.sqrt(3) - 2, 0))
        path7 = Arc(start_angle=PI / 2, angle=-PI / 3, radius=2, arc_center=(3 - np.sqrt(3), -3, 0))
        path8 = Arc(start_angle=PI / 2, angle=-PI / 2, radius=2, arc_center=(1, -2, 0))
        path9 = Arc(start_angle=PI / 2, angle=-2 * PI / 3, radius=2, arc_center=(3 - np.sqrt(3), -1, 0))
        path10 = Arc(start_angle=PI / 2, angle=-5 * PI / 6, radius=2, arc_center=(2, np.sqrt(3) - 2, 0))

        self.play(
            LaggedStart(Create(path6), Create(path7), Create(path8), Create(path9), Create(path10), lag_ratio=0.3))

        word4 = Text("磁聚焦", font="SimSun").shift(2.5 * DOWN)
        word5 = Text("平进点出", font="SimSun").shift(3.5 * DOWN)
        self.play(ReplacementTransform(word1, word4), ReplacementTransform(word2, word5))
        self.play(Wiggle(word4, scale_value=1.2), Wiggle(word5, scale_value=1.2))

        fade = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1, width=16, height=8)
        self.wait(2)
        self.play(FadeIn(fade))


class Scene003(Scene):  # 动画模拟
    def construct(self):
        title = Text("形成成因", font="SimSun").scale(2)
        grid = NumberPlane()
        self.play(Write(title)), self.wait(0.5)
        self.play(title.animate.shift(UP))
        w1 = Text("#1 圆心圆", font="KaiTi").next_to(title, DOWN)
        self.play(Write(w1)), self.wait(0.5)
        self.play(LaggedStart(title.animate.shift(0.5 * UP), w1.animate.shift(0.5 * UP)))
        w2 = Text("#2 半径", font="KaiTi").next_to(w1, DOWN)
        self.play(Write(w2)), self.wait(1.5)
        self.play(FadeOut(title, shift=RIGHT), FadeOut(w2, shift=RIGHT), w1.animate.to_corner(UL))
        self.wait(0.5)
        self.play(Create(grid), FadeOut(w1))
        locuscir = Circle(radius=2, color=WHITE).shift(2 * RIGHT)
        locuscir.rotate(PI, about_point=np.array([2, 0, 0]))
        w3 = Text("轨迹圆", font="SimSun").shift(2 * RIGHT)
        v0 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=0)
        self.play(GrowArrow(v0)), self.wait(0.25)
        self.play(Rotating(v0, about_point=np.array([2, 0, 0])), Create(locuscir, rate_func=linear, run_time=5))
        self.play(Write(w3)), self.wait()
        self.play(Transform(w3, locuscir)), self.remove(w3)
        ccc = Circle(radius=2, color=YELLOW)
        self.play(Rotating(locuscir, about_point=ORIGIN), Rotating(v0, about_point=ORIGIN),
                  Create(ccc, rate_func=linear), run_time=8)
        self.wait(2)
        w4 = Text("圆心圆", font="SimSun", color=YELLOW).shift(2.5 * DOWN)
        self.play(TransformFromCopy(ccc, w4))
        self.wait(2)
        w5 = Text("半径", font="SimSun", color=WHITE).scale(2)
        faderect = FullScreenFadeRectangle()
        self.play(FadeIn(faderect), Write(w5), Uncreate(grid), Unwrite(w4), Uncreate(v0)), self.wait()
        self.play(w5.animate.shift(6 * DOWN), FadeOut(faderect))
        dc = Dot(ORIGIN)
        dlc = Dot(point=np.array([(2, 0, 0)]))
        dac = Dot(point=np.array([2, 0, 0]))  # 这是（主）动点
        dfo = Dot(point=dac.get_center() + np.array([2, 0, 0]))  # 这是（从）动点，在主动点的右侧2单位
        self.play(FadeIn(dc, scale=2), FadeIn(dlc, scale=2), FadeIn(dac, scale=2), FadeIn(dfo, scale=2))
        rhombus = Polygon(dc.get_center(), dlc.get_center(), dfo.get_center(), dac.get_center(), fill_color=BLUE,
                          fill_opacity=0.4)
        dfo.add_updater(lambda m: m.become(Dot(point=dac.get_center() + np.array([2, 0, 0]))))
        rhombus.add_updater(
            lambda m: m.become(Polygon(dc.get_center(), dlc.get_center(), dfo.get_center(), dac.get_center(),
                                       fill_color=BLUE, fill_opacity=0.4)))
        self.add(dfo, rhombus)
        self.play(Rotating(dac, radians=2 * PI / 3, about_point=ORIGIN, rate_func=smooth, run_time=1.2)), self.wait(0.5)
        self.play(Rotating(dac, radians=5 * PI / 6, about_point=ORIGIN, rate_func=smooth, run_time=1.2)), self.wait(0.5)
        self.play(Rotating(dac, radians=-7 * PI / 6, about_point=ORIGIN, rate_func=smooth, run_time=1.2)), self.wait(
            0.5)
        locus = Arc(radius=2, start_angle=0, arc_center=np.array(dac.get_center()),
                    angle=-angle_between_vectors(np.array(dfo.get_center() - dac.get_center()),
                                                 np.array(dc.get_center() - dac.get_center())))
        entrarr = Arrow(start=dfo.get_center() + 1.5 * UP, end=dfo.get_center(), buff=0)
        self.play(GrowArrow(entrarr)), self.play(Create(locus))
        locus.add_updater(lambda m: m.become(Arc(radius=2, start_angle=0, arc_center=np.array(dac.get_center()),
                                                 angle=-angle_between_vectors(
                                                     np.array(dfo.get_center() - dac.get_center()),
                                                     np.array(dc.get_center() - dac.get_center())))))
        entrarr.add_updater(lambda m: m.become(Arrow(start=dfo.get_center() + 1.5 * UP, end=dfo.get_center(), buff=0)))
        self.add(locus, entrarr)
        self.play(Rotating(dac, radians=PI / 2, about_point=ORIGIN, rate_func=smooth, run_time=3)), self.wait(0.5)
        self.play(Rotating(dac, radians=-5 * PI / 12, about_point=ORIGIN, rate_func=smooth, run_time=2)), self.wait(0.5)
        locus.clear_updaters()
        magraar = Arrow(start=dlc.get_center(), end=dfo.get_center(), color=WHITE, buff=0)
        magrate = Text("磁场圆半径", font="SimSun").to_corner(DL)
        movraar = Arrow(start=dac.get_center(), end=dfo.get_center(), color=RED, buff=0)
        movrate = Text("轨迹圆半径", font="SimSun").to_corner(DR)
        cocraar = Arrow(start=dc.get_center(), end=dac.get_center(), color=YELLOW, buff=0)
        cocrate = Text("圆心圆半径", font="SimSun").to_corner(DOWN)
        rhomte = Text("菱形", font="SimSun").next_to(rhombus, UP)
        self.play(GrowArrow(magraar), Indicate(locuscir, scale_factor=1.1)), self.wait(0.8)
        self.play(ReplacementTransform(magraar, magrate)), self.wait()
        self.play(GrowArrow(movraar), Indicate(locus, scale_factor=1.1)), self.wait(0.8)
        self.play(ReplacementTransform(movraar, movrate)), self.wait()
        self.play(GrowArrow(cocraar), ApplyWave(ccc)), self.wait(0.8)
        self.play(ReplacementTransform(cocraar, cocrate)), self.wait()
        self.play(LaggedStart(magrate.animate.move_to(point_or_mobject=(-5, 3, 0)),
                              cocrate.animate.move_to(point_or_mobject=(-5, 1.5, 0)),
                              movrate.animate.move_to(point_or_mobject=(-5, 0, 0)), lag_ratio=0.4))
        self.play(ApplyWave(rhombus, run_time=1)), self.play(Write(rhomte)), self.wait(1)
        equalte = Text("各边相等", font="SimSun").next_to(rhombus, UP)
        self.play(ReplacementTransform(rhomte, equalte)), self.wait()
        equal1 = MathTex("=").rotate(PI / 2)
        equal1.next_to(magrate, DOWN)
        equal2 = MathTex("=").rotate(PI / 2)
        equal2.next_to(cocrate, DOWN)
        self.play(ReplacementTransform(equalte, equal1)), self.play(TransformFromCopy(equal1, equal2))
        self.wait(2)
        faderectangle = Rectangle(color=BLACK, width=14.4, height=8, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(faderectangle))


class Scene004(Scene):  # 过渡
    def construct(self):
        conclusion1 = Text("点进平出", font="KaiTi").shift(UP)
        conclusion1.scale(2)
        conclusion2 = Text("平进点出", font="KaiTi").shift(DOWN)
        conclusion2.scale(2)
        self.play(Write(conclusion1)), self.play(Write(conclusion2))
        self.wait(2)
        whiteboard = Rectangle(color=WHITE, height=8, width=15, fill_color=WHITE, fill_opacity=1)
        self.play(FadeOut(conclusion1, scale=2), FadeOut(conclusion2, scale=2),
                  FadeIn(whiteboard, rate_func=linear, run_time=4))


class Scene005(Scene):  # 载入文件演示
    def construct(self):
        p01 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\1.png").scale(0.5)
        p02 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\2.png").scale(0.5)
        p03 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\3.png").scale(0.5)
        p04 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\4.png").scale(0.5)
        p05 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\5.png").scale(0.5)
        p06 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\6.png").scale(0.5)
        p07 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\7.png").scale(0.5)
        p08 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\8.png").scale(0.5)
        p09 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\9.png").scale(0.5)
        p10 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\10.png").scale(0.5)
        self.add(p01), self.wait(2)
        self.remove(p01), self.add(p02), self.wait(2)
        self.remove(p02), self.add(p03), self.wait(2)
        self.remove(p03), self.add(p04), self.wait(2)
        self.remove(p04), self.add(p05), self.wait(2)
        self.remove(p05), self.add(p06), self.wait(2)
        self.remove(p06), self.add(p07), self.wait(2)
        self.remove(p07), self.add(p08), self.wait(2)
        self.remove(p08), self.add(p09), self.wait(2)
        self.remove(p09), self.add(p10), self.play(FadeOut(p10))


class Scene006(Scene):  # 实际应用（划掉）
    def construct(self):
        grid = NumberPlane()
        self.play(Create(grid))
        pea1 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea1.shift(5 * LEFT + 1.65 * UP)
        pea2 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea2.shift(5 * LEFT + 0.65 * UP)
        pea3 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea3.shift(5 * LEFT + 0.35 * DOWN)
        pea4 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea4.shift(5 * LEFT + 1.35 * DOWN)
        pea5 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea5.shift(5 * LEFT + 2.35 * DOWN)
        self.play(LaggedStart(FadeIn(pea1), FadeIn(pea2), FadeIn(pea3), FadeIn(pea4), FadeIn(pea5), lag_ratio=0.5))
        cir = Circle(radius=2, color=YELLOW).shift(2 * RIGHT)
        self.play(Create(cir))
        zombie = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\zombie.gif").shift(
            2 * RIGHT + 2 * DOWN)
        freezer = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\Freezer.gif").scale(0.5)
        frecir = Circle(color=BLUE, fill_color=BLUE, fill_opacity=0.4, radius=11.2)
        frerec = Rectangle(color=BLUE, height=2, width=1, fill_color=BLUE, fill_opacity=0.4).move_to(
            zombie.get_center())
        self.play(FadeIn(zombie, shift=UP))
        self.play(FadeIn(freezer, shift=DOWN, run_time=0.5))
        self.play(GrowFromCenter(frecir, run_time=1), FadeOut(freezer, scale=0.5, run_time=1, rate_func=rush_into))
        self.play(FadeOut(frecir), FadeIn(frerec))


class Scene009(Scene):  # 实际应用2（划掉）
    def construct(self):
        grid = NumberPlane()
        pea1 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea1.shift(5 * LEFT + 1.65 * UP)
        pea2 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea2.shift(5 * LEFT + 0.65 * UP)
        pea3 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea3.shift(5 * LEFT + 0.35 * DOWN)
        pea4 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea4.shift(5 * LEFT + 1.35 * DOWN)
        pea5 = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\wd.gif").scale(0.5)
        pea5.shift(5 * LEFT + 2.35 * DOWN)
        cir = Circle(radius=2, color=YELLOW).shift(2 * RIGHT)
        zombie = ImageMobject(r"D:\Program Files\manim20210621\manim-master\media\images\PVZ\zombie.gif").shift(
            2 * RIGHT + 2 * DOWN)
        frerec = Rectangle(color=BLUE, height=2, width=1, fill_color=BLUE, fill_opacity=0.4).move_to(
            zombie.get_center())
        self.add(grid, pea1, pea2, pea3, pea4, pea5, cir, zombie, frerec)
        awsl = Text("啊我死了", font="KaiTi", color=RED).next_to(frerec, DOWN)
        awslrec = Rectangle(color=RED, height=1, fill_color=BLACK, fill_opacity=1).surround(awsl)
        self.wait(1)
        self.play(FadeIn(awslrec))
        self.play(Write(awsl))
        self.wait(1)
        self.play(FadeOut(awsl), FadeOut(awslrec), LaggedStart(zombie.animate.stretch(0, 1, about_edge=DOWN),
                                                               frerec.animate.stretch(0, 1, about_edge=DOWN),
                                                               lag_ratio=0.4))
        self.remove(zombie, frerec)
        self.play(Transform(pea1, pea5), Transform(pea2, pea5), Transform(pea3, pea5), Transform(pea4, pea5))
        finish = Text("打完收工", font="KaiTi", color=GREEN).next_to(pea5, RIGHT)
        finrec = Rectangle(color=GREEN, fill_color=BLACK, fill_opacity=1, height=1).surround(finish)
        self.play(Create(finrec)), self.play(DrawBorderThenFill(finish))
        self.wait(2)
        faderectangle = Rectangle(color=BLACK, width=14.4, height=8, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(faderectangle))


class Scene010(Scene):  # 结尾
    def construct(self):
        word1 = Text("磁发散", font="SimSun").shift(np.array([-3, 1, 0]))
        word2 = Text("点进平出", font="SimSun").shift(np.array([-3, -1, 0]))
        word3 = Text("磁聚焦", font="SimSun").shift(np.array([3, 1, 0]))
        word4 = Text("平进点出", font="SimSun").shift(np.array([3, -1, 0]))
        self.play(Write(word1))
        self.play(FadeIn(word2, shift=DOWN))
        self.play(Write(word3))
        self.play(FadeIn(word4, shift=DOWN))
        self.wait(5)
        x1 = Text("谢", font="KaiTi", color=RED).shift(np.array([-2, 2, 0]))
        x1.scale(2)
        x2 = Text("谢", font="KaiTi", color=BLUE).shift(np.array([2, 2, 0]))
        x2.scale(2)
        x3 = Text("观", font="KaiTi", color=YELLOW).shift(np.array([-2, -2, 0]))
        x3.scale(2)
        x4 = Text("看", font="KaiTi", color=GREEN).shift(np.array([2, -2, 0]))
        x4.scale(2)
        self.play(LaggedStart(Transform(word1, x1), Transform(word3, x2),
                              Transform(word2, x3), Transform(word4, x4), lag_ratio=0.5, run_time=1.5))
        self.play(word1.animate.shift(DR), word3.animate.shift(DL), word2.animate.shift(UR), word4.animate.shift(UL))
        cir = Circle(color=WHITE, radius=3)
        self.play(FadeIn(cir, scale=0.8))
        self.wait(2)