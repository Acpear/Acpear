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
        subtitle = Text("力学题不常见方法", font="SimSun").scale(1.4)
        self.play(Write(subtitle), run_time=2)
        self.wait(0.5)
        self.play(subtitle.animate.scale(2 / 3))
        maintitle = Text("拆拼向量", font="KaiTi").scale(2.5)
        self.play(FadeIn(maintitle, shift=2 * UP, rate_func=rush_from), subtitle.animate.to_edge(UP))
        need = Text("需要：尺、规、量角器……", font="SimSun").to_edge(DOWN)
        self.play(DrawBorderThenFill(need))
        self.wait(1)


class Scene003(Scene):

    def construct(self):
        obj = Rectangle(width=2, height=1.6, fill_color=GRAY)
        obj.set_sheen(factor=0.5, direction=UL)
        self.play(SpinInFromNothing(obj))
        gravity = Arrow(start=obj.get_center(), end=obj.get_center() + DOWN, color=RED, buff=0)
        support = Arrow(start=obj.get_center(), end=obj.get_center() + UP, color=BLUE, buff=0)
        external = Arrow(start=obj.get_center(), end=obj.get_center() + 2 * LEFT, color=YELLOW, buff=0)
        friction = Arrow(start=obj.get_center(), end=obj.get_center() + 2 * RIGHT, color=WHITE, buff=0)
        self.play(GrowArrow(gravity), GrowArrow(support), GrowArrow(external), GrowArrow(friction))
        self.play(obj.animate.scale(1.1), gravity.animate.stretch(factor=2, dim=1, about_edge=UP),
                  support.animate.stretch(factor=2, dim=1, about_edge=DOWN), rate_func=there_and_back, run_time=2)
        self.play(external.animate.stretch(factor=0.5, dim=0, about_edge=RIGHT),
                  friction.animate.stretch(factor=0.5, dim=0, about_edge=LEFT), rate_func=there_and_back, run_time=2)
        disband = Text("拆向量", font="KaiTi").to_edge(RIGHT, buff=1)
        self.play(Write(disband)), self.play(Indicate(disband))
        self.play(gravity.animate.shift(DOWN), support.animate.shift(UP),
                  external.animate.shift(2 * LEFT), friction.animate.shift(2 * RIGHT))
        combine = Text("拼向量", font="KaiTi").to_edge(RIGHT, buff=1)
        self.play(ReplacementTransform(disband, combine)), self.play(Indicate(combine))
        self.play(obj.animate.shift(4 * LEFT))
        self.play(gravity.animate.move_to(point_or_mobject=(-1, 0, 0)),
                  support.animate.move_to(point_or_mobject=(1, 0, 0)),
                  external.animate.move_to(point_or_mobject=(0, 0.5, 0)),
                  friction.animate.move_to(point_or_mobject=(0, -0.5, 0)))
        self.wait(0.5)
        group_force = VGroup(gravity, support, external, friction)
        self.play(group_force.animate.stretch(factor=2, dim=1), rate_func=there_and_back)
        self.play(group_force.animate.stretch(factor=2, dim=0), rate_func=there_and_back)
        finish = Text("基本操作演示完毕...", font="SimSun").to_edge(DOWN)
        self.play(FadeOut(combine), FadeIn(finish))
        self.wait(0.3)
        self.play(FadeOut(finish), FadeOut(group_force), FadeOut(obj))


class Scene004(Scene):
    def construct(self):
        quiz = Text("托盘盛放木块做匀速圆周运动", font="SimSun").shift(2 * LEFT)
        obj = Square(side_length=0.5, fill_color=GOLD_D, fill_opacity=1).move_to((6.5, 0, 0))
        pallets = Brace(obj, DOWN, buff=0)
        tracecir = Circle(radius=1.5, color=WHITE).shift(5 * RIGHT)
        masscenter = VectorizedPoint(location=np.array([6.5, 0, 0]))
        self.play(Write(quiz), Create(obj), FadeIn(pallets, shift=UP))
        obj.add_updater(lambda m, dt: m.move_to(masscenter))
        pallets.add_updater(lambda m, dt: m.next_to(obj, DOWN, buff=0))
        self.add(obj, pallets)
        self.play(quiz.animate.to_edge(UP), Create(tracecir, run_time=5, rate_func=linear),
                  Rotating(masscenter, OUT, TAU, about_point=np.array([5, 0, 0]), run_time=5, rate_func=linear))
        obj.clear_updaters()
        pallets.clear_updaters()
        know = Text("已知：加速度，半径，角速度", font="SimSun").next_to(quiz, DOWN)
        knowsign = MathTex(r"g,R,\omega").next_to(know, DOWN)
        question = Text("问保持稳定的动摩擦因数至少为？", font="SimSun").next_to(knowsign, DOWN)
        condition = Text("设最大静摩擦力为滑动摩擦力").scale(0.5).next_to(question, DOWN, aligned_edge=RIGHT)
        tryit = Text("试一试！", font="SimSun").next_to(question, DOWN, aligned_edge=LEFT)
        self.play(LaggedStart(FadeIn(know, shift=LEFT), FadeIn(knowsign, shift=UP),
                              FadeIn(question, scale=2), FadeIn(condition, shift=DOWN),
                              FadeIn(tryit, shift=LEFT), lag_ratio=0.8))
        self.wait(2)
        wecandothis = Text("我们可以这样...", font="SimSun").next_to(tryit, DOWN, aligned_edge=LEFT)
        self.play(FadeOut(tryit, shift=LEFT), FadeIn(wecandothis, shift=LEFT))
        self.wait()
        fadetodark = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1, width=15, height=8)
        self.play(FadeIn(fadetodark))


class Scene005(Scene):
    def construct(self):
        tracecir = Circle(radius=2, color=WHITE)
        massdot = Dot(point=(2, 0, 0))
        gravity = Arrow(start=massdot.get_center(), end=massdot.get_center() + 2.5 * DOWN,
                        color=RED, buff=0)
        support = Arrow(start=massdot.get_center(), end=massdot.get_center() + (2.5 - massdot.get_y()) * UP,
                        color=BLUE, buff=0)
        friction = Arrow(start=massdot.get_center(), end=massdot.get_center() - massdot.get_x() * RIGHT,
                         color=YELLOW, buff=0)
        slxysyz=Text("三力下匀速圆周",font="SimSun").shift(4.6*LEFT)
        self.play(Write(slxysyz),FadeIn(tracecir), FadeIn(massdot), FadeIn(gravity), FadeIn(support), FadeIn(friction))
        massdot.add_updater(lambda m, dt: m.rotate(dt, about_point=ORIGIN))
        gravity.add_updater(lambda m, dt: m.become(
            Arrow(start=massdot.get_center(), end=massdot.get_center() + 2.5 * DOWN,
                  color=RED, buff=0)))
        support.add_updater(lambda m, dt: m.become(
            Arrow(start=massdot.get_center(), end=massdot.get_center() + (2.5 - massdot.get_y()) * UP,
                  color=BLUE, buff=0)))
        friction.add_updater(lambda m, dt: m.become(
            Arrow(start=massdot.get_center(), end=massdot.get_center() - massdot.get_x() * RIGHT,
                  color=YELLOW, buff=0)))
        self.wait(5)
        szfxlhz=Text("竖直方向力合成",font="SimSun").shift(4.6*LEFT)
        self.play(ReplacementTransform(slxysyz,szfxlhz))
        massdot.clear_updaters()
        gravity.clear_updaters()
        support.clear_updaters()
        verticalcombine = Arrow(start=massdot.get_center(), end=massdot.get_center() - massdot.get_y() * UP,
                                color=PURPLE, buff=0)
        self.play(Transform(gravity,verticalcombine),ReplacementTransform(support,verticalcombine))
        elxysyz = Text("二力下匀速圆周", font="SimSun").shift(4.6 * LEFT)
        self.remove(gravity),self.play(ReplacementTransform(szfxlhz,elxysyz))
        verticalcombine.add_updater(lambda m:m.become(
            Arrow(start=massdot.get_center(), end=massdot.get_center() - massdot.get_y() * UP,
                  color=PURPLE, buff=0)
        ))
        massdot.add_updater(lambda m, dt: m.rotate(dt, about_point=ORIGIN))
        self.wait(5)
        elhc = Text("二力合成", font="SimSun").shift(4.6 * LEFT)
        self.play(ReplacementTransform(elxysyz,elhc))
        massdot.clear_updaters()
        verticalcombine.clear_updaters()
        friction.clear_updaters()
        combine = Arrow(start=massdot.get_center(), end=ORIGIN, color=WHITE, buff=0)
        self.play(Transform(verticalcombine,combine),ReplacementTransform(friction,combine))
        self.remove(verticalcombine)
        xxl=Text("向心力", font="SimSun").shift(4.6 * LEFT)
        self.play(ReplacementTransform(elhc,xxl))
        combine.add_updater(lambda m:m.become(
            Arrow(start=massdot.get_center(), end=ORIGIN, color=WHITE, buff=0)
        ))
        massdot.add_updater(lambda m, dt: m.rotate(dt, about_point=ORIGIN))
        self.wait(5)
        self.play(Unwrite(xxl))
        massdot.clear_updaters()
        gravity.clear_updaters()
        support.clear_updaters()
        friction.clear_updaters()
        gravity = Arrow(start=massdot.get_center(), end=massdot.get_center() + 2.5 * DOWN,
                        color=RED, buff=0)
        support = Arrow(start=massdot.get_center(), end=massdot.get_center() + (2.5 - massdot.get_y()) * UP,
                        color=BLUE, buff=0)
        friction = Arrow(start=massdot.get_center(), end=massdot.get_center() - massdot.get_x() * RIGHT,
                         color=YELLOW, buff=0)
        self.play(FadeIn(gravity),FadeIn(support),FadeIn(friction))
        massdot.add_updater(lambda m, dt: m.rotate(dt, about_point=ORIGIN))
        gravity.add_updater(lambda m, dt: m.become(
            Arrow(start=massdot.get_center(), end=massdot.get_center() + 2.5 * DOWN,
                  color=RED, buff=0)))
        support.add_updater(lambda m, dt: m.become(
            Arrow(start=massdot.get_center(), end=massdot.get_center() + (2.5 - massdot.get_y()) * UP,
                  color=BLUE, buff=0)))
        friction.add_updater(lambda m, dt: m.become(
            Arrow(start=massdot.get_center(), end=massdot.get_center() - massdot.get_x() * RIGHT,
                  color=YELLOW, buff=0)))
        self.wait(3.25)
        disbandandcombine = Text("拆拼向量", font="KaiTi").to_edge(RIGHT, buff=1)
        self.play(Write(disbandandcombine)),self.play(Indicate(disbandandcombine))
        massdot.clear_updaters()
        gravity.clear_updaters()
        support.clear_updaters()
        friction.clear_updaters()
        combine.clear_updaters()
        self.play(gravity.animate.become(Arrow(start=ORIGIN, end= 2.5 * DOWN, color=RED, buff=0)))
        self.play(support.animate.shift((2.5+massdot.get_y())*DOWN))
        self.play(friction.animate.shift((massdot.get_y()+2.5)*DOWN),FadeOut(disbandandcombine))
        friction.add_updater(lambda m,dt:m.become(Arrow(end=np.array([0,-2.5,0]),color=YELLOW,buff=0,
                                                        start=np.array([0,-2.5,0])+massdot.get_x()*RIGHT)))
        support.add_updater(lambda m,dt:m.become(Arrow(start=friction.get_start(),end=(massdot.get_x(),-massdot.get_y(),0),
                                                       color=BLUE,buff=0)))
        combine.add_updater(lambda m:m.become(Arrow(start=massdot.get_center(), end=ORIGIN, color=WHITE, buff=0)))
        massdot.add_updater(lambda m, dt: m.rotate(dt, about_point=ORIGIN))
        self.wait(5)
        suppose=Text("假设每一时刻都刚要滑动，可得", font="SimSun").to_edge(UP)
        word1=MathTex(r"f=\mu {F_{N}} ").shift(4*LEFT)
        word2=MathTex(r"\mu ={f \over F_{N}}").shift(4*LEFT)
        word2.move_to(word1)
        fshow=MathTex("f").set_color(YELLOW)
        fshow.move_to(word2[0][2])
        FN=MathTex("F_{N}").set_color(BLUE)
        FN.move_to(word2[0][4])
        self.play(FadeIn(suppose,shift=UP))
        self.play(Write(word1)),self.wait(0.8)
        self.play(TransformMatchingShapes(word1,word2)),self.wait(0.8)
        self.add(fshow,FN)
        self.play(fshow.animate.move_to(friction),FN.animate.move_to(support.tip),run_time=0.25)
        self.play(fshow.animate.next_to(friction,DOWN),FN.animate.next_to(support.tip,RIGHT),run_time=0.25)
        fshow.add_updater(lambda m:m.next_to(friction.tip,DOWN))
        FN.add_updater(lambda m:m.next_to(support.tip,RIGHT))
        self.wait(2)
        auxiliaryline=DashedLine(start=friction.get_end(),end=support.get_end())
        self.add(auxiliaryline)
        auxiliaryline.add_updater(lambda m:m.become(
            DashedLine(start=friction.get_end(), end=support.get_end(),stroke_width=0.5,color=PURPLE)
        ))
        self.wait(1)
        linegroup=VGroup()
        def copy(obj):
            obj.add(auxiliaryline.copy().clear_updaters())
        linegroup.add_updater(copy)
        self.add(linegroup)
        self.wait(TAU-0.005)
        auxiliarylinecopy = Line(start=friction.get_end(), end=support.get_end(),color=WHITE)
        self.add(auxiliarylinecopy)
        auxiliarylinecopy.add_updater(lambda m: m.become(
            Line(start=friction.get_end(), end=support.get_end(),color=WHITE)
        ))
        word3=Text("不难发现μ为\n支持力与辅助\n线之间夹角", font="SimSun").shift(5*RIGHT)
        self.play(Write(word3))
        self.wait(3)
        word4 = Text("夹角的最大值\n在相切时取得", font="SimSun").shift(5 * RIGHT)
        self.play(ReplacementTransform(word3,word4))
        self.wait(2)
        word5 = Text("即μ的临界值\n在相切时取得", font="SimSun").shift(5 * RIGHT)
        self.play(ReplacementTransform(word4, word5))
        self.wait(2)
        fadetodark = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1, width=15, height=8)
        Group(*self.mobjects).clear_updaters()
        self.play(FadeIn(fadetodark))
        self.remove(Group(*self.mobjects))
        tangentline=Line(start=(0,-2.5,0),end=(1.2,-1.6,0))
        radiusline=Line(start=ORIGIN,end=(1.2,-1.6,0))
        self.play(LaggedStart(FadeIn(tracecir),GrowArrow(gravity),Create(tangentline),Create(radiusline),lag_ratio=0.5))
        mg=MathTex("mg").next_to(gravity,LEFT,buff=0.25)
        mrw2=MathTex(r"mR \omega ^{2}").next_to(radiusline,UR,buff=0.1)
        msqrt1=MathTex(r"\sqrt{(mg)^{2}-(mR{\omega}^{2})^{2}}").next_to(tangentline,DR,buff=0.1)
        msqrt2=MathTex(r"\sqrt{m^{2}(g^2-r^2\omega^4)}").next_to(tangentline,DR,buff=0.1)
        msqrt3=MathTex(r"m\sqrt{g^2-r^2\omega^4}").next_to(tangentline,DR,buff=0.1)
        newfriction=Arrow(start=(0,-2.5,0),end=(1.2,-2.5,0),color=YELLOW,buff=0)
        newsupport=Arrow(start=(1.2,-2.5,0),end=(1.2,-1.6,0),color=BLUE,buff=0)
        self.play(FadeIn(mg,shift=UP),FadeIn(mrw2,shift=DL))
        self.play(FadeIn(msqrt1,shift=UL)),self.wait(0.5)
        self.play(ReplacementTransform(msqrt1,msqrt2)),self.wait(0.5)
        self.play(ReplacementTransform(msqrt2,msqrt3)),self.wait(0.5)
        self.play(GrowArrow(newfriction))
        self.play(GrowArrow(newsupport))
        arc1=Arc(radius=0.4,arc_center=(1.2,-1.6,0),start_angle=217*DEGREES,angle=53*DEGREES)
        arc2=Arc(radius=0.4,arc_center=(0,-2.5,0),start_angle=37*DEGREES,angle=53*DEGREES)
        self.play(Create(arc1),Create(arc2)),self.wait()
        conclusion1 = MathTex(r"\mu = \frac{\qquad}{\qquad}").to_edge(LEFT)
        conclusion2=MathTex(r"\mu=\tan \angle( \quad )").to_edge(LEFT)
        conclusion3 = MathTex(r"\mu = \frac{\qquad}{\qquad}").to_edge(LEFT)
        self.play(Write(conclusion1))
        self.play(newfriction.animate.move_to((-5.1,0.5,0)),newsupport.animate.move_to((-5.1,-0.5,0)))
        self.wait(0.5)
        self.play(FadeOut(newfriction),FadeOut(newsupport),ReplacementTransform(conclusion1,conclusion2))
        self.play(Indicate(arc1,scale_factor=2)),self.play(arc1.animate.move_to((-4,0,0))), self.wait(0.5)
        self.play(Indicate(arc2,scale_factor=2)),self.play(arc2.animate.move_to((-4,0,0)).rotate(PI)), self.wait(0.5)
        self.play(FadeOut(arc1),FadeOut(arc2),ReplacementTransform(conclusion2,conclusion3))
        self.play(mrw2.animate.move_to((-5.1,0.6,0)),msqrt3.animate.move_to((-5.1,-0.5,0))),self.wait(0.5)
        conclusion4=MathTex(r"{\mu}=\frac{R\omega^2}{\sqrt{g^2-R^2\omega^4}}").to_edge(LEFT)
        self.play(FadeOut(mrw2),FadeOut(msqrt3),ReplacementTransform(conclusion3,conclusion4))
        self.wait(2)


class Scene006(MovingCameraScene):
    def construct(self):
        # 图像
        grid=NumberPlane(x_range=[-7,15])
        example2=Text("例2",font="KaiTi").scale(3)
        self.play(Write(example2)),self.wait(),self.play(FadeOut(example2,scale=2))
        obj1=Square(side_length=1,fill_color=DARKER_GRAY,fill_opacity=1).shift(1.5*DL).set_sheen(factor=0.7,direction=UL)
        obj2=Square(side_length=1,fill_color=DARKER_GRAY,fill_opacity=1).shift(1.5*DR).set_sheen(factor=0.7,direction=UL)
        pulley=Annulus(0.125,0.25,0.5,2,RED).shift(np.array([0.5,2*np.sqrt(3)-0.5,0]))
        point1=Dot(point=np.array([-1.5,0,0]))
        point2=Dot(point=np.array([1.5,np.sqrt(3),0]))
        bracket=Line(start=point1.get_center(),end=point2.get_center(),stroke_width=10,stroke_color=GOLD)
        lineUL=Line(start=np.array([0.5-0.125*np.sqrt(3),2*np.sqrt(3)-0.375,0]),
                    end=point1.get_center(),stroke_color=RED,stroke_width=2)
        lineUR=Line(start=np.array([0.5+0.125*np.sqrt(3),2*np.sqrt(3)-0.375,0]),
                    end=point2.get_center(),stroke_color=RED,stroke_width=2)
        lineDL=Line(start=point1.get_center(),end=np.array([-1.5,-1,0]),stroke_color=BLUE,stroke_width=2)
        lineDR = Line(start=point2.get_center(), end=np.array([1.5, -1, 0]), stroke_color=BLUE, stroke_width=2)
        auxiliary_line=DashedLine(start=point1.get_center(),end=ORIGIN,stroke_color=WHITE)
        clamping_angle=Arc(radius=0.7,start_angle=0,angle=PI/6,arc_center=point1.get_center(),stroke_color=WHITE)
        point1copy=Dot(point=np.array([5,1,0]))
        point2copy=Dot(point=np.array([9,1,0]))
        obj1_gravity=Arrow(start=point1copy.get_center(),end=point1copy.get_center()+DOWN,color=BLUE,buff=0)
        obj2_gravity = Arrow(start=point2copy.get_center(), end=point2copy.get_center() + 2*DOWN, color=BLUE, buff=0)
        obj1_support=Arrow(start=point1copy.get_center(),end=point1copy.get_center()+np.array([-np.sqrt(3)/2,-0.5,0]),color=GOLD,buff=0)
        obj2_support = Arrow(start=point2copy.get_center(), end=point2copy.get_center() + np.array([np.sqrt(3) / 2, 0.5, 0]), color=GOLD, buff=0)
        obj1_pull=Arrow(start=point1copy.get_center(),end=point1copy.get_center()+np.array([np.sqrt(3)/2,1.5,0]),color=RED,buff=0)
        obj2_pull = Arrow(start=point2copy.get_center(),end=point2copy.get_center() + np.array([-np.sqrt(3) / 2, 1.5, 0]), color=RED, buff=0)
        symmetrical_axis=DashedLine(start=[0.5,4,0],end=[0.5,2,0],stroke_width=2,color=WHITE)
        line_m1g=Line(start=np.array([5-np.sqrt(3)/2,0.5,0]),end=np.array([5-np.sqrt(3)/2,-0.5,0]),color=BLUE)
        line_m2g = Line(start=np.array([5,1, 0]), end=np.array([5,-1, 0]),color=BLUE)
        line_support=Line(start=np.array([5-np.sqrt(3)/2,0.5,0]),end=np.array([5,1,0]),color=GOLD)
        line_pull1=Line(start=np.array([5-np.sqrt(3)/2,-0.5,0]),end=np.array([5,1,0]),color=RED)
        line_pull2 = Line(start=np.array([5,-1, 0]), end=np.array([5-np.sqrt(3)/2,0.5,0]), color=RED)
        fadetodark = Rectangle(color=BLACK, fill_color=BLACK, fill_opacity=1, width=15, height=8).shift((5-np.sqrt(3)/2)*RIGHT)
        # 文字
        pulley_text=Text("滑轮",color=RED,font="KaiTi").next_to(pulley,LEFT)
        bracket_text=Text("轻杆",color=GOLD,font="KaiTi").next_to(bracket,0.5*UR)
        clamping_angle_text=MathTex(r"\theta").next_to(clamping_angle)
        clamping_angle_30 = MathTex(r"\theta =30^{\circ} ").next_to(clamping_angle)
        obj1_weigh_text=MathTex(r"m_{1}=1").next_to(obj1,DOWN)
        obj2_weigh_text=MathTex(r"m_{2}=?").next_to(obj2,DOWN)
        m1g=MathTex(r"m_{1}g").next_to(obj1_gravity.tip,0.5*DL)
        m2g=MathTex(r"m_{2}g").next_to(obj2_gravity.tip,RIGHT)
        fn1=MathTex(r"F_{N1}").next_to(obj1_support.tip,0.5*UL)
        fn2=MathTex(r"F_{N2}").next_to(obj2_support.tip,0.5*UL)
        fp1=MathTex(r"F_{p1}").next_to(obj1_pull.tip,0.5*DR)
        fp2=MathTex(r"F_{p2}").next_to(obj2_pull.tip,0.5*DL)
        theme=Text("拆拼向量",font="SimSun").shift(np.array([7,-2.5,0]))
        symmetry=Text("对称",font="SimSun").shift(0.5*RIGHT+UP)
        bigsamedirectionopposite=Text("等大反向",font="SimSun",color=GOLD).shift((5-(np.sqrt(3)/4))*RIGHT+2.75*UP)
        m1g_new = MathTex(r"1").next_to(line_m1g, 0.5*LEFT)
        m2g_new = MathTex(r"2").next_to(line_m2g, 0.5*RIGHT)
        fn1_new = MathTex(r"1").next_to(line_support.get_center(), 0.3*UL)
        fn2_new = MathTex(r"1").next_to(line_support.get_center(), 0.3 * UL)
        fp1_new = MathTex(r"\sqrt{3}").next_to(line_pull1.get_center(), 0.25 * DR)
        fp2_new = MathTex(r"\sqrt{3}").next_to(line_pull2.get_center(), 0.3 * DL)
        obj1_weigh_text_anwser=MathTex(r"m_{1}=1").next_to(obj1,DOWN)
        obj2_weigh_text_anwser=MathTex(r"m_{2}=2").next_to(obj2,DOWN)
        # 动画
        self.play(LaggedStart(FadeIn(pulley),Create(lineUL),Create(lineUR),FadeIn(point1,scale=2),FadeIn(point2,scale=2),
                              Create(bracket),Create(lineDL),Create(lineDR),
                              DrawBorderThenFill(obj1),DrawBorderThenFill(obj2),
                              Create(auxiliary_line),Create(clamping_angle),lag_ratio=0.4))
        self.play(FadeIn(pulley_text,shift=LEFT),FadeIn(clamping_angle_text,target_position=point1.get_center(),scale=0))
        self.wait()
        self.play(ReplacementTransform(pulley_text,bracket_text),ReplacementTransform(clamping_angle_text,clamping_angle_30))
        self.play(Write(obj1_weigh_text),Write(obj2_weigh_text))
        self.play(Indicate(obj1_weigh_text,scale_factor=2),Indicate(obj2_weigh_text,scale_factor=2))
        self.wait(3)
        self.play(self.camera.frame.animate.shift(4.5 * RIGHT),FadeOut(bracket_text))
        self.play(TransformFromCopy(point1,point1copy),TransformFromCopy(point2,point2copy)),self.wait(0.5)
        self.play(LaggedStart(GrowArrow(obj1_gravity),GrowArrow(obj1_support),GrowArrow(obj1_pull),lag_ratio=0.4)),self.wait()
        self.play(ReplacementTransform(obj1_weigh_text,m1g),Write(fn1),Write(fp1))
        self.play(LaggedStart(GrowArrow(obj2_gravity),GrowArrow(obj2_support),GrowArrow(obj2_pull),lag_ratio=0.4)),self.wait()
        self.play(ReplacementTransform(obj2_weigh_text,m2g), Write(fn2), Write(fp2))
        self.wait()
        m1g.add_updater(lambda m:m.next_to(obj1_gravity.tip,0.5*DL))
        m2g.add_updater(lambda m:m.next_to(obj2_gravity.tip,RIGHT))
        fn1.add_updater(lambda m:m.next_to(obj1_support.tip,0.5*UL))
        fn2.add_updater(lambda m:m.next_to(obj2_support.tip,0.5*UL))
        fp1.add_updater(lambda m:m.next_to(obj1_pull.tip,0.5*DR))
        fp2.add_updater(lambda m:m.next_to(obj2_pull.tip,0.5*DL))
        self.play(obj2_gravity.animate.stretch(factor=2,dim=1,about_edge=UP),rate_func=there_and_back,run_time=2)
        self.play(Write(theme)),self.play(ApplyWave(theme,run_time=1,rate_func=smooth)),self.wait(0.5)
        self.play(LaggedStart(FadeOut(point1copy,run_time=0.5),
                              obj1_gravity.animate.shift(np.array([-np.sqrt(3)/2,-0.5,0])),
                              obj1_pull.animate.shift(np.array([-np.sqrt(3)/2,-1.5,0])),
                              lag_ratio=0.6))
        self.play(LaggedStart(FadeOut(point2copy,run_time=0.5),
                              obj2_pull.animate.shift(2*DOWN),
                              obj2_support.animate.shift(np.array([-np.sqrt(3) / 2, -0.5, 0])),
                              lag_ratio=0.6))
        m1g.clear_updaters()
        m2g.clear_updaters()
        fn1.clear_updaters()
        fn2.clear_updaters()
        fp1.clear_updaters()
        fp2.clear_updaters()
        self.wait(2)
        self.play(FadeOut(m1g),FadeOut(m2g),FadeOut(fn1),FadeOut(fn2),FadeOut(fp1),FadeOut(fp2),FadeOut(theme))
        self.play(obj2_gravity.animate.shift(4*LEFT),obj2_support.animate.shift(4*LEFT),obj2_pull.animate.shift(4*LEFT))
        self.play(self.camera.frame.animate.scale(0.5)),self.wait()
        self.play(self.camera.frame.animate.shift(4*LEFT+1.5*UP)),self.wait(0.25)
        self.play(Create(symmetrical_axis),Write(symmetry)),self.wait()
        self.play(self.camera.frame.animate.shift(4 * RIGHT + 1.5 * DOWN),
                  symmetrical_axis.animate.shift(4 * RIGHT + 1.5 * DOWN),
                  symmetry.animate.shift(4 * RIGHT + 1.5 * DOWN)), self.wait(0.25)
        self.play(FadeOut(obj1_gravity),FadeOut(obj2_gravity),FadeOut(obj1_support),FadeOut(obj2_support))
        obj1_pull.save_state()
        obj2_pull.save_state()
        self.play(obj1_pull.animate.move_to([3.5,0,0]),obj2_pull.animate.move_to([5.5,0,0])),self.wait(0.5)
        self.play(obj2_pull.animate.flip(UP,about_point=[4.5,0,0]).set_color(YELLOW)),self.wait(0.5)
        self.play(obj2_pull.animate.flip(UP, about_point=[4.5, 0, 0]).set_color(RED)), self.wait(0.5)
        self.play(Restore(obj1_pull),Restore(obj2_pull),FadeOut(symmetry),FadeOut(symmetrical_axis))
        self.play(FadeIn(obj1_gravity),FadeIn(obj2_gravity),FadeIn(obj1_support),FadeIn(obj2_support))
        self.play(self.camera.frame.animate.shift(2.5*UP),obj1_support.animate.shift(UP),obj2_support.animate.shift(3*UP))
        self.play(Write(bigsamedirectionopposite)),self.wait(0.5)
        self.play(Rotating(obj2_support,OUT,radians=PI,about_point=np.array([5-np.sqrt(3)/4,2.75,0]),run_time=0.5)),self.wait(0.7)
        self.play(Rotating(obj2_support, OUT, radians=PI, about_point=np.array([5-np.sqrt(3)/4, 2.75, 0]), run_time=0.5)), self.wait(0.7)
        self.play(self.camera.frame.animate.shift(2.5 * DOWN), FadeOut(bigsamedirectionopposite),
                  obj1_support.animate.shift(DOWN),obj2_support.animate.shift(3 * DOWN))
        self.wait(0.5)
        self.play(LaggedStart(Uncreate(obj1_gravity),Uncreate(obj1_support),Uncreate(obj1_pull),
                  Uncreate(obj2_gravity),Uncreate(obj2_support),Uncreate(obj2_pull),lag_ratio=0.4))
        self.play(LaggedStart(Create(line_m1g),Create(line_m2g),Create(line_support),Create(line_pull1),Create(line_pull2),lag_ratio=0.4))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(0.5*UP)),self.wait(0.5)
        self.play(Wiggle(clamping_angle,n_wiggles=3,rotation_angle=PI/12,run_time=1),Indicate(clamping_angle_30,scale_factor=1.4,run_time=1))
        self.play(Restore(self.camera.frame))
        self.play(line_m1g.animate.set_color(YELLOW),line_support.animate.set_color(YELLOW),line_pull1.animate.set_color(YELLOW))
        self.play(Write(m1g),Write(fn1),Write(fp1)),self.wait(0.5)
        self.play(LaggedStart(ReplacementTransform(m1g,m1g_new),ReplacementTransform(fn1,fn1_new),ReplacementTransform(fp1,fp1_new)))
        self.play(line_m1g.animate.set_color(BLUE),line_support.animate.set_color(GOLD),line_pull1.animate.set_color(RED),
                  FadeOut(m1g_new),fp1_new.animate.shift(2*LEFT),fn1_new.animate.shift(0.5*UP))
        self.play(line_m2g.animate.set_color(YELLOW),line_support.animate.set_color(YELLOW),line_pull2.animate.set_color(YELLOW))
        m1g.next_to(line_m1g, 0.5 * LEFT)
        m2g.next_to(line_m2g, 0.5 * RIGHT)
        fn1.next_to(line_support.get_center(), 0.3 * UL)
        fn2.next_to(line_support.get_center(), 0.3 * UL)
        fp1.next_to(line_pull1.get_center(), 0.25 * DR)
        fp2.next_to(line_pull2.get_center(), 0.3 * DL)
        self.play(Write(m2g), Write(fn2), Write(fp2)),self.wait(0.5)
        self.play(LaggedStart(FadeOut(fp2),ReplacementTransform(fp1_new,fp2_new),FadeOut(fn2),ReplacementTransform(fn1_new,fn2_new)))
        self.wait(1)
        self.play(ReplacementTransform(m2g,m2g_new)),self.wait(1)
        self.play(self.camera.frame.animate.scale(2),line_m2g.animate.set_color(BLUE),
                  line_support.animate.set_color(GOLD),line_pull2.animate.set_color(RED))
        self.play(self.camera.frame.animate.shift(2*LEFT),FadeOut(fp2_new),FadeOut(fn2_new),FadeIn(m1g_new)),self.wait()
        self.play(TransformFromCopy(m1g_new,obj1_weigh_text_anwser),TransformFromCopy(m2g_new,obj2_weigh_text_anwser))
        self.wait(2)
        self.play(FadeIn(fadetodark))


class Scene007(MovingCameraScene):
    def construct(self):
        ground=Line(start=np.array([-7,-1,0]),end=np.array([7,-1,0]),color=GREEN)
        triangle_base_point_1 = Dot(np.array([-3,-1,0]),color=WHITE)
        triangle_base_point_2 = Dot(np.array([2,-1,0]),color=WHITE)
        triangle_base_point_3 = Dot(np.array([0.189,1.4,0]),color=GOLD)
        triangle_base_line_1 = Line(start=triangle_base_point_1.get_center(),end=triangle_base_point_2.get_center())
        triangle_base_line_2 = Line(start=triangle_base_point_2.get_center(),end=triangle_base_point_3.get_center(),color=BLUE)
        triangle_base_line_3 = Line(start=triangle_base_point_3.get_center(),end=triangle_base_point_1.get_center(),color=RED)
        box1=Square(side_length=1,color=RED,fill_color=RED,fill_opacity=0.6).move_to(np.array([-1.833,0.505,0])).rotate(37*DEGREES)
        box2=Square(side_length=1,color=BLUE,fill_color=BLUE,fill_opacity=0.6).move_to(np.array([1.497,0.505,0])).rotate(-53*DEGREES)
        pulley=Annulus(0.1,0.25,fill_opacity=0.6,stroke_width=4,color=GOLD).move_to(np.array([0.24,1.755,0]))
        pulleysupport=Line(start=triangle_base_point_3.get_center(),end=pulley.get_center(),color=GOLD)
        pulleypoint=Dot(point=(0.24,1.755,0))
        line1=Line(start=np.array([0.088,1.953,0]),end=np.array([-1.437,0.804,0])).set_color([RED,GOLD]).set_sheen(factor=0,direction=np.array([0.8,0.6,0]))
        line2=Line(start=np.array([0.442,1.906,0]),end=np.array([1.194,0.908,0])).set_color([BLUE,GOLD]).set_sheen(factor=0,direction=np.array([-0.6,0.8,0]))
        self.play(Create(ground))
        self.play(LaggedStart(FadeIn(triangle_base_point_1,scale=2), Create(triangle_base_line_1),
                              FadeIn(triangle_base_point_2,scale=2), Create(triangle_base_line_2),
                              FadeIn(triangle_base_point_3,scale=2), Create(triangle_base_line_3),
                              lag_ratio=0.5))
        self.add(triangle_base_point_3)
        self.play(Create(pulleysupport)),self.play(FadeIn(pulleypoint)),self.play(FadeIn(pulley,scale=0))
        self.play(FadeIn(box1,shift=np.array([0.6,-0.8,0])),FadeIn(box2,shift=np.array([-0.8,-0.6,0])),
                  Create(line1),Create(line2),rate_func=rush_from)
        text_equal_mass=Text("两个质量相等的物块",font="KaiTi").move_to(2.5*DOWN)
        tex_mass_of_object1=MathTex(r"m").move_to(np.array([-1.833,0.505,0]))
        tex_mass_of_object2 = MathTex(r"m").move_to(np.array([1.497,0.505,0]))
        text_given_angle_37=Text("37 度角",font="KaiTi").move_to(2.5*DOWN)
        tex_angle_37=MathTex(r"37^{\circ} ").move_to(np.array([-2.052,-0.683,0]))
        text_given_angle_53 = Text("53 度角", font="KaiTi").move_to(2.5 * DOWN)
        tex_angle_53 = MathTex(r"53^{\circ} ").move_to(np.array([1.105,-0.554, 0]))
        text_horizontal_acceleration=Text("系统获得水平方向加速度",font="KaiTi").move_to(2.5*DOWN)
        rect_the_system=Rectangle(width=5.204,height=3,color=YELLOW,fill_color=YELLOW,fill_opacity=0.5).shift(np.array([-0.398,0.5,0]))
        tex_a=MathTex(r"a").move_to(2.5*DOWN)
        arrow_acceleration=Arrow(start=np.array([-0.398,0.5,0]),end=np.array([-2.398,0.5,0]),color=BLUE,buff=0)
        text_no_slip=Text("确保各物体无相对滑动",font="KaiTi").move_to(2.5*DOWN)
        text_smooth_surfaces=Text("所有接触面均光滑",font="KaiTi").move_to(2.5*DOWN)
        text_question=Text("问:该加速度应为多少? (已知g)",font="KaiTi").move_to(2.5*DOWN)
        brace_arrow_length=BraceText(arrow_acceleration,"?")
        self.play(Write(text_equal_mass)),self.wait(2)
        self.play(ReplacementTransform(text_equal_mass,tex_mass_of_object1),
                  TransformFromCopy(text_equal_mass,tex_mass_of_object2))
        self.play(Write(text_given_angle_37)),self.wait()
        self.play(ReplacementTransform(text_given_angle_37,tex_angle_37)),self.wait(0.5)
        self.play(Write(text_given_angle_53)),self.wait()
        self.play(ReplacementTransform(text_given_angle_53,tex_angle_53)),self.wait(0.5)
        self.play(Write(text_horizontal_acceleration)),self.wait()
        self.play(Create(rect_the_system)),self.wait(0.5)
        self.play(ReplacementTransform(text_horizontal_acceleration,tex_a)),self.wait(0.5)
        self.play(GrowArrow(arrow_acceleration)),self.play(tex_a.animate.next_to(arrow_acceleration.get_end(),DOWN))
        tex_a.add_updater(lambda m:m.next_to(arrow_acceleration.get_end(),DOWN))
        self.play(arrow_acceleration.animate.stretch(-1,0,about_point=np.array([-0.398,0.5,0])))
        self.play(arrow_acceleration.animate.stretch(-2,0,about_point=np.array([-0.398,0.5,0])))
        self.play(arrow_acceleration.animate.stretch(0.5, 0,about_point=np.array([-0.398,0.5,0])))
        tex_a.clear_updaters()
        self.play(Write(text_no_slip),FadeOut(rect_the_system),FadeOut(tex_a),FadeOut(arrow_acceleration))
        self.play(FadeIn(rect_the_system,scale=2))
        self.play(FadeIn(arrow_acceleration,run_time=0.25))
        self.play(Transform(text_no_slip,rect_the_system)),self.play(FadeOut(text_no_slip))
        self.play(Write(text_smooth_surfaces)),self.wait(),self.play(FadeOut(text_smooth_surfaces,shift=3*UP,run_time=1.5))
        self.play(Write(text_question)),self.wait(),self.play(FadeIn(brace_arrow_length))
        brace_arrow_length.add_updater(lambda m:m.become(BraceText(arrow_acceleration,"?")))
        self.play(arrow_acceleration.animate.stretch(-2, 0,about_point=np.array([-0.398,0.5,0])))
        self.play(arrow_acceleration.animate.stretch(-2, 0,about_point=np.array([-0.398,0.5,0])))
        self.play(arrow_acceleration.animate.stretch(0.25, 0,about_point=np.array([-0.398,0.5,0])))
        brace_arrow_length.clear_updaters()
        self.wait()
        self.play(self.camera.frame.animate.shift(8*DOWN))


class Scene008(MovingCameraScene):
    def construct(self):
        self.camera.frame.shift(6*UP)
        # basic elements & Fade animations for obj1
        obj1=Square(side_length=1,color=RED,fill_color=RED,fill_opacity=0.6).rotate(37*DEGREES)
        dot1=Dot(color=WHITE)
        self.play(self.camera.frame.animate.shift(6*DOWN),FadeIn(obj1),FadeIn(dot1)),self.wait(0.5)
        self.play(FadeOut(obj1))
        # four forces applying to obj1
        obj1_gravity=Arrow(buff=0,color=RED,start=dot1.get_center(),end=dot1.get_center()+2*DOWN)
        obj1_support=Arrow(buff=0,color=BLUE,start=dot1.get_center(),end=dot1.get_center()+np.array([-0.856,1.141,0]))
        obj1_pull=Arrow(buff=0,color=GOLD,start=dot1.get_center(),end=dot1.get_center()+np.array([1.145,0.859,0]))
        obj1_accc=Arrow(buff=0,color=YELLOW,start=dot1.get_center(),end=dot1.get_center()+np.array([-0.289,0,0]))
        self.play(GrowArrow(obj1_gravity),GrowArrow(obj1_support),GrowArrow(obj1_pull),GrowArrow(obj1_accc)),self.wait()
        # four forces re-combining
        self.play(obj1_accc.animate.shift(obj1_gravity.get_end()))
        self.play(obj1_support.animate.shift(obj1_accc.get_end()))
        self.play(obj1_pull.animate.shift(obj1_support.get_end()))
        self.wait()
        # three points representing Arrow ends
        obj1_gravity_point = Point(obj1_gravity.get_end())
        obj1_accc_point = Point(obj1_accc.get_end())
        obj1_support_point=Point(obj1_support.get_end())
        # add updater for next moving around
        obj1_accc.add_updater(lambda m:m.become(Arrow(buff=0,color=YELLOW,start=obj1_gravity_point.get_end(),
                                                      end=obj1_accc_point.get_center())))
        obj1_support.add_updater(lambda m: m.become(Arrow(buff=0, color=BLUE, start=obj1_accc_point.get_center(),
                                                          end=obj1_support_point.get_center())))
        obj1_pull.add_updater(lambda m:m.become(Arrow(buff=0,color=GOLD,start=obj1_support_point.get_center(),
                                                      end=ORIGIN)))
        # show Arrow moving
        obj1_accc_point.save_state()
        obj1_support_point.save_state()
        self.play(obj1_accc_point.animate.move_to(np.array([-1.5,-2,0])),
                  obj1_support_point.animate.move_to(np.array([-1.92,-1.44,0])))
        self.wait(0.5)
        self.play(obj1_accc_point.animate.move_to(np.array([-1, -2, 0])),
                  obj1_support_point.animate.move_to(np.array([-1.6, -1.2, 0])))
        self.wait(0.5)
        self.play(obj1_accc_point.animate.move_to(np.array([0.5, -2, 0])),
                  obj1_support_point.animate.move_to(np.array([-0.64, -0.48, 0])))
        self.wait(0.5)
        self.play(Restore(obj1_accc_point),Restore(obj1_support_point))
        # clean updater
        obj1_accc.clear_updaters()
        obj1_support.clear_updaters()
        obj1_pull.clear_updaters()
        self.play(FadeOut(dot1),FadeOut(obj1_gravity),FadeOut(obj1_support),FadeOut(obj1_pull),FadeOut(obj1_accc))
        # object2
        obj2=Square(side_length=1,color=BLUE,fill_color=BLUE,fill_opacity=0.6).rotate(-53*DEGREES)
        dot2=Dot(color=WHITE)
        obj2_gravity = Arrow(buff=0, color=RED, start=dot2.get_center(), end=dot2.get_center() + 2 * DOWN)
        obj2_pull = Arrow(buff=0, color=GOLD, start=dot2.get_center(), end=dot2.get_center() + np.array([-0.856, 1.141, 0]))
        obj2_support = Arrow(buff=0, color=BLUE, start=dot2.get_center(), end=dot2.get_center() + np.array([1.145, 0.859, 0]))
        obj2_accc = Arrow(buff=0, color=YELLOW, start=dot2.get_center(), end=dot2.get_center() + np.array([-0.289, 0, 0]))
        self.play(FadeIn(dot2),FadeIn(obj2)),self.wait()
        self.play(GrowArrow(obj2_gravity), GrowArrow(obj2_support), GrowArrow(obj2_pull), GrowArrow(obj2_accc))
        self.play(FadeOut(obj2))
        # moving
        self.play(obj2_accc.animate.shift(obj2_gravity.get_end()))
        self.play(obj2_pull.animate.shift(obj2_accc.get_end()))
        self.play(obj2_support.animate.shift(obj2_pull.get_end()))
        self.wait()
        self.play(dot2.animate.shift(3*RIGHT),obj2_gravity.animate.shift(3*RIGHT),obj2_support.animate.shift(3*RIGHT),
                  obj2_pull.animate.shift(3*RIGHT),obj2_accc.animate.shift(3*RIGHT))
        # multi-blocks showing
        self.play(FadeIn(dot1),FadeIn(obj1),FadeIn(obj1_gravity),
                  FadeIn(obj1_support),FadeIn(obj1_pull),FadeIn(obj1_accc))
        self.play(FadeOut(obj1))
        self.play(self.camera.frame.animate.shift(np.array([1,-1,0])))
        # show parallel
        line37_1=Line(start=np.array([-4,-3,0]),end=np.array([4,3,0]))
        line37_2=Line(start=np.array([-1,-3,0]),end=np.array([7,3,0]))
        line53_1=Line(start=np.array([1,-3.72,0]),end=np.array([-3,1.617,0]))
        line53_2=Line(start=np.array([4,-3.72,0]),end=np.array([0,1.617,0]) )
        self.play(Create(line37_1),Create(line37_2),Indicate(obj1_pull),Indicate(obj2_support))
        self.play(Uncreate(line37_1),Uncreate(line37_2))
        self.play(Create(line53_1), Create(line53_2),Indicate(obj1_support),Indicate(obj2_pull))
        self.play(Uncreate(line53_1), Uncreate(line53_2))
        # pull forces are equal
        equal_pull=Text("同一根绳拉力相等").shift(np.array([0.8,1.5,0]))
        equal_radius=Circle(color=GOLD,radius=1.431).move_to(obj1_support_point.get_center())
        equal_radius_center=Dot(point=obj1_support_point.get_center())
        self.play(Write(equal_pull),GrowFromCenter(equal_radius),FadeIn(equal_radius_center)),self.wait()
        self.play(equal_radius.animate.move_to(obj2_pull.get_start()),
                  equal_radius_center.animate.move_to(obj2_pull.get_start()),rate_func=linear)
        self.wait(0.5),self.play(FadeOut(equal_pull),FadeOut(equal_radius),FadeOut(equal_radius_center))
        self.play(self.camera.frame.animate.scale(0.1))


class Scene009(MovingCameraScene):
    def construct(self):
        grid=NumberPlane(y_range=(-5,5))
        self.play(GrowFromCenter(grid))
        line1=Line(start=np.array([2,3.5,0]),end=np.array([2,-3.5,0]),color=WHITE)
        line2 = Line(start=np.array([2, -3.5, 0]), end=np.array([1, -3.5, 0]), color=WHITE)
        line3 = Line(start=np.array([1,-3.5,0]), end=np.array([-2, 0.5, 0]), color=WHITE)
        line4 = Line(start=np.array([-2, 0.5, 0]), end=np.array([2, 3.5, 0]), color=WHITE)
        rectangle=Rectangle(width=4,height=7,color=WHITE)
        self.play(Create(line1),Create(line2),Create(line3),Create(line4))
        self.play(Create(rectangle))
        self.play(grid.animate.shift(0.5*DOWN))
        self.add(line1,line2)
        self.play(line2.animate.set_color(YELLOW),line1.animate.set_color(RED)),self.wait(2)
        anwser=MathTex(r"a=\dfrac{1}{7}g",).shift(4*RIGHT)
        self.play(Write(anwser)),self.wait(2)
        self.play(self.camera.frame.animate.shift(10*UP))


class Scene010(Scene):
    def construct(self):
        dlph=Text("多力平衡",font="KaiTi").scale(2)
        cfxl=Text("拆分向量",font="KaiTi").scale(2)
        xxgk = Text("谢谢观看", font="KaiTi").scale(2)
        self.play(Write(dlph)),self.wait()
        self.play(FadeIn(cfxl,shift=UP),FadeOut(dlph,shift=UP),rate_func=rush_from),self.wait(3)
        self.play(FadeIn(xxgk,shift=UP), FadeOut(cfxl,shift=UP), rate_func=rush_from), self.wait()
        self.play(FadeOut(xxgk)),self.wait()