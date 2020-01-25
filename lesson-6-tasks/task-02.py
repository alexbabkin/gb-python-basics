#
# Task 2
#


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def _calc_asphalt_mass(self, coating_thickness, specific_gravity):
        return self._length * self._width * coating_thickness * specific_gravity

    def get_asphalt_mass_in_tons(self, coating_thickness, specific_gravity):
        return self._calc_asphalt_mass(coating_thickness, specific_gravity) / 1000


road = Road(5000, 20)
print(f'asphalt mass in tons is {road.get_asphalt_mass_in_tons(5, 25)}')
