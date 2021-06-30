from manimlib import *
import random


class ThreeBodiesMotion(Scene):
    def construct(self):
        def disab(a, b):
            return float(np.sqrt((b.get_x() - a.get_x()) ** 2 + (b.get_y() - a.get_y()) ** 2))

        random.seed()
        grid = NumberPlane()
        self.add(grid)
        m1 = Dot(color=RED, point=np.array([random.uniform(-4, 4), random.uniform(-2.5, 2.5), 0]))
        m2 = Dot(color=BLUE, point=np.array([random.uniform(-4, 4), random.uniform(-2.5, 2.5), 0]))
        m3 = Dot(color=GREEN, point=np.array([random.uniform(-4, 4), random.uniform(-2.5, 2.5), 0]))
        v1 = Arrow(start=m1.get_center(), fill_color=RED, buff=0,
                   end=m1.get_center() + np.array([random.uniform(-4, 4), random.uniform(-4, 4), 0]))
        v2 = Arrow(start=m2.get_center(), fill_color=BLUE, buff=0,
                   end=m2.get_center() + np.array([random.uniform(-4, 4), random.uniform(-4, 4), 0]))
        v3 = Arrow(start=m3.get_center(), fill_color=GREEN, buff=0,
                   end=m3.get_center() + np.array([random.uniform(-4, 4), random.uniform(-4, 4), 0]))
        f1 = Arrow(start=m1.get_center(), fill_color=YELLOW, buff=0,
                   end=m1.get_center() + np.array(
                       [((m2.get_x() - m1.get_x()) / (disab(m1, m2) ** 3)+(m3.get_x() - m1.get_x()) / (disab(m1, m3) ** 3)) * 5,
                        ((m2.get_y() - m1.get_y()) / (disab(m1, m2) ** 3)+(m3.get_y() - m1.get_y()) / (disab(m1, m3) ** 3)) * 5,
                        0]))
        f2 = Arrow(start=m2.get_center(), fill_color=YELLOW, buff=0,
                   end=m2.get_center() + np.array(
                       [((m3.get_x() - m2.get_x()) / (disab(m2, m3) ** 3) + (m1.get_x() - m2.get_x()) / (disab(m1, m2) ** 3)) * 5,
                        ((m3.get_y() - m2.get_y()) / (disab(m2, m3) ** 3) + (m1.get_y() - m2.get_y()) / (disab(m1, m2) ** 3)) * 5,
                        0]))
        f3 = Arrow(start=m3.get_center(), fill_color=YELLOW, buff=0,
                   end=m3.get_center() + np.array(
                       [((m1.get_x() - m3.get_x()) / (disab(m1, m3) ** 3) + (m2.get_x() - m3.get_x()) / (disab(m2, m3) ** 3)) * 5,
                        ((m1.get_y() - m3.get_y()) / (disab(m1, m3) ** 3) + (m2.get_y() - m3.get_y()) / (disab(m2, m3) ** 3)) * 5,
                        0]))
        self.play(FadeIn(m1, scale=2), FadeIn(m2, scale=2), FadeIn(m3, scale=2))
        self.play(GrowArrow(v1), GrowArrow(v2), GrowArrow(v3), GrowArrow(f1), GrowArrow(f2), GrowArrow(f3))
        m1.add_updater(lambda m, dt: m.shift((v1.get_end() - v1.get_start()) * dt))
        m2.add_updater(lambda m, dt: m.shift((v2.get_end() - v2.get_start()) * dt))
        m3.add_updater(lambda m, dt: m.shift((v3.get_end() - v3.get_start()) * dt))
        v1.add_updater(lambda m, dt: m.become(Arrow(start=m1.get_center(), fill_color=RED, buff=0,
                                                    end=v1.get_end() + (f1.get_end() - f1.get_start()) * dt)))
        v2.add_updater(lambda m, dt: m.become(Arrow(start=m2.get_center(), fill_color=BLUE, buff=0,
                                                    end=v2.get_end() + (f2.get_end() - f2.get_start()) * dt)))
        v3.add_updater(lambda m, dt: m.become(Arrow(start=m3.get_center(), fill_color=GREEN, buff=0,
                                                    end=v3.get_end() + (f3.get_end() - f3.get_start()) * dt)))
        f1.add_updater(lambda m, dt: m.become(Arrow(start=m1.get_center(), fill_color=YELLOW, buff=0,
                   end=m1.get_center() + np.array(
                       [((m2.get_x() - m1.get_x()) / (disab(m1, m2) ** 3)+(m3.get_x() - m1.get_x()) / (disab(m1, m3) ** 3)) * 5,
                        ((m2.get_y() - m1.get_y()) / (disab(m1, m2) ** 3)+(m3.get_y() - m1.get_y()) / (disab(m1, m3) ** 3)) * 5,
                        0]))))
        f2.add_updater(lambda m, dt: m.become(Arrow(start=m2.get_center(), fill_color=YELLOW, buff=0,
                   end=m2.get_center() + np.array(
                       [((m3.get_x() - m2.get_x()) / (disab(m2, m3) ** 3) + (m1.get_x() - m2.get_x()) / (disab(m1, m2) ** 3)) * 5,
                        ((m3.get_y() - m2.get_y()) / (disab(m2, m3) ** 3) + (m1.get_y() - m2.get_y()) / (disab(m1, m2) ** 3)) * 5,
                        0]))))
        f3.add_updater(lambda m, dt: m.become(Arrow(start=m3.get_center(), fill_color=YELLOW, buff=0,
                   end=m3.get_center() + np.array(
                       [((m1.get_x() - m3.get_x()) / (disab(m1, m3) ** 3) + (m2.get_x() - m3.get_x()) / (disab(m2, m3) ** 3)) * 5,
                        ((m1.get_y() - m3.get_y()) / (disab(m1, m3) ** 3) + (m2.get_y() - m3.get_y()) / (disab(m2, m3) ** 3)) * 5,
                        0]))))

        self.add(v1, v2, v3, f1, f2, f3, m1, m2, m3)
        self.wait(10)

