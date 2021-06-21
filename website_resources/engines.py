

class estes_rocket_def:
    def __init__(self, name, total_impulse, time_delay, max_lift_weight, total_mass, propellant_mass, thrust_duration):
        self.name = name
        self.total_impulse = total_impulse #N*s = kg m/s^2 * s , divide my rocket mass to get accel?
        self.time_delay = time_delay #s
        self.max_lift_weight = max_lift_weight #kg
        self.total_mass = total_mass #kg
        self.propellant_mass = propellant_mass #kg
        self.thrust_duration = thrust_duration #

class rocket:
    def __init__(self, launch_engine, land_engine, body_properties):
        self.launch_engine = launch_engine
        self.land_engine = land_engine
        self.body_properties = body_properties #this should be the shape, dimensions, CG, CP
        self.position = [0, 0]
        self.rocket_total_mass = launch_engine.total_mass + land_engine.total_mass + body_properties.mass
        self.current_mass = self.rocket_total_mass

class body_properties: #2 dimensional, x, y
    def __init__(self, width, heigth, cg, cp, mass):
        self.width = width #meters
        self.heigth = heigth #meters
        self.cg = cg #on the centerline, in meters from the base
        self.cp = cp #on the centerline, in meters from the base
        self.mass = mass #kg

estes_b4_2 = estes_rocket_def(name="B4-2",total_impulse=5.0,time_delay=2.0,max_lift_weight=0.113,total_mass=0.0198,propellant_mass=0.00833,thrust_duration=1.1)

estes_d12_0 = estes_rocket_def(name="D12-0",total_impulse=20.0,time_delay=-1,max_lift_weight=0.396,total_mass=(0.0422),propellant_mass=0.02493,thrust_duration=1.6)

estes_d12_3 = estes_rocket_def(name="D12-3",total_impulse=20.0,time_delay=3,max_lift_weight=0.396,total_mass=(0.0422),propellant_mass=0.02493,thrust_duration=1.6)

rocket_body = body_properties(width=0.005,heigth=0.060,cg=0.030,cp=0.010,mass=0.1)

rocket_sample = rocket(launch_engine=estes_d12_0,land_engine=estes_b4_2,body_properties=rocket_body)
 