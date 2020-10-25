

class estes_rocket_def:
    def __init__(self, name, total_impulse, time_delay, max_lift_weight, total_mass, propellant_mass, thrust_duration):
        self.name = name
        self.total_impulse = total_impulse #N*s
        self.time_delay = time_delay #s
        self.max_lift_weight = max_lift_weight #kg
        self.total_mass = total_mass #kg
        self.propellant_mass = propellant_mass #kg
        self.thrust_duration = thrust_duration #s

class rocket:
    def __init__(self, name, launch_engine, land_engine, body_properties):
        self.name = name
        self.launch_engine = launch_engine
        self.land_engine = land_engine
        self.body_properties = body_properties #this should be the shape, dimensions, CG, CP

class body_properties: #2 dimensional, x, y
    def __init__(self, width, heigth, cg, cp):
        self.width = width #meters
        self.heigth = heigth #meters
        self.cg = cg #on the centerline, in meters from the base
        self.cp = cp #on the centerline, in meters from the base

estes_b4_2 = estes_rocket_def("B4-2",5.0,2.0,0.113,0.0198,0.00833,1.1)

estes_d12_0 = estes_rocket_def("D12-0",20.0,-1,0.396,0.0409,0.02493,1.6)

rocket_body = body_properties(0.005,0.060,0.030,0.010)

rocket_sample = rocket("try1",estes_d12_0,estes_b4_2,rocket_body)