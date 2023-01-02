from manim import *
class Particle(Circle):
    CONFIG={
        'color':YELLOW,
        'texto':'proton',
        'value':0
    }
    def __init__(self,**kwargs):
        super().__init__(
            fill_color=self.CONFIG['color'],
            fill_opacity=1,
            radius=.3,
            stroke_width=0,
            stroke_opacity=0,
        )
        self.angle=TAU*np.random.random()
        self.fase=(RIGHT*config['frame_height']/2)*np.random.random()
        self.move_to(rotate_vector(self.fase,self.angle))
        self.center=self.get_center()
        self.add_updater(lambda m,dt: m.update_particle(dt))
        texto=self.get_tex(self.CONFIG['texto'])
        coordinate=self.coord_mob()
        self.add(texto,coordinate)
    def update_particle(self,dt):
        self.center[0]+=dt
        self.angle+=dt
        self.move_to(rotate_vector(self.fase,self.angle))
    def get_tex(self,texto):
        return MathTex(texto).move_to(self.get_center())
    def coord_mob(self):
        self.x_num=DecimalNumber(self.center[0],num_decimal_places=0)
        self.y_num=DecimalNumber(self.center[1],num_decimal_places=0)
        coordinate=VGroup(
            Tex('('),
            self.x_num,
            Tex(','),
            self.y_num,
            Tex(')'),
        ).arrange(RIGHT)
        coordinate.scale_to_fit_width(self.get_width())
        # coordinate.add_updater(lambda t: t.next_to(self.get_center(),DOWN,buff=0.3))
        self.add_updater(lambda m: m.update_coord())
        return coordinate
    def update_coord(self):
        self.x_num.add_updater(lambda t: t.set_value(self.center[0]))
        # self.y_num.add_updater(lambda t: t.set_value(self.center[1]))
class ProtonParticle(Particle):
    CONFIG={
        'color':BLUE_B,
        'texto':'+'
    }
class ElectronParticle(Particle):
    CONFIG={
        'color':RED_D,
        'texto':'-'
    }
class VectorFieldScene(Scene):
    def construct(self):
        for _ in range(3):
            electron=ElectronParticle()
            proton=ProtonParticle()
            self.add(electron,proton)
        self.wait(14)