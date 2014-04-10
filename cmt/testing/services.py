import numpy as np


def get_port(name):
    return _SERVICES[name]


def get_port_names():
    return _SERVICES.keys()


class EmptyPort(object):
    def __init__(self):
        self._shape = (4, 5)
        self._spacing = (1., 2.)
        self._origin = (0., 1.)
        self._values = {}
        self._time = self.start_time

    def initialize(self):
        for array in self._values.values():
            array.fill(0.)

    def run(self, time):
        self._time = time
        for array in self._values.values():
            array.fill(self.current_time)

    def finalize(self):
        for array in self._values.values():
            array.fill(0.)

    def get_grid_shape(self, var_name):
        return self._shape

    def get_grid_spacing(self, var_name):
        return self._spacing

    def get_grid_origin(self, var_name):
        return self._origin

    def get_grid_values(self, var_name):
        return self._values[var_name]

    @property
    def start_time(self):
        return 0.

    @property
    def current_time(self):
        return self._time

    @property
    def end_time(self):
        return 100.

    @property
    def time_step(self):
        return 1.


class WaterPort(EmptyPort):
    def __init__(self):
        EmptyPort.__init__(self)
        self._values = {
            'ocean_surface__temperature': np.empty(self._shape),
            'ocean_surface__density': np.empty(self._shape),
        }


class AirPort(EmptyPort):
    def __init__(self):
        EmptyPort.__init__(self)
        self._values = {
            'air__temperature': np.empty(self._shape),
            'air__density': np.empty(self._shape),
        }


class EarthPort(EmptyPort):
    def __init__(self):
        EmptyPort.__init__(self)
        self._values = {
            'earth_surface__temperature': np.empty(self._shape),
            'earth_surface__density': np.empty(self._shape),
            'glacier_top_surface__slope': np.empty(self._shape),
        }


_SERVICES = {
    'air_port': AirPort(),
    'water_port': WaterPort(),
    'earth_port': EarthPort(),
}
