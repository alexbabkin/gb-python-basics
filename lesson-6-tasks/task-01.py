#
# Task 1
#

from time import sleep


class TrafficLight:
    def __init__(self):
        self._color = 'red'

    def _switch(self):
        if self._color == 'red':
            self._color = 'yellow'
        elif self._color == 'yellow':
            self._color = 'green'
        elif self._color == 'green':
            self._color = 'red'
        else:
            raise Exception('Incorrect state')

    def running(self):
        print(self._color)
        sleep(7)
        self._switch()

        print(self._color)
        sleep(2)
        self._switch()

        print(self._color)
        sleep(10)
        self._switch()

        print(self._color)


tl = TrafficLight()
tl.running()
