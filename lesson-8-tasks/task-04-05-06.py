#
# Task 4-5-6.
#

from abc import ABC, abstractmethod


class Store:
    def __init__(self, capacity):
        # in slots
        self._capacity = capacity
        # in slots
        self._used_capacity = 0
        self._facilities = {}
        self._total_count = 0
        self.__last_id = 1

    def get_free_space(self):
        """returns free slots"""
        return self._capacity - self._used_capacity

    def take(self, facility):
        if facility.slots > self.get_free_space():
            print(f'Can not take this facility: {facility}, not enough free space')
            return
        self._total_count += 1
        self._used_capacity += facility.slots
        facility.set_id(self.__last_id)
        self.__last_id += 1

        f_type = facility.get_type()
        if self._facilities.get(f_type) is None:
            self._facilities[f_type] = []
        self._facilities[f_type].append(facility)

    def request(self, f_type, model=None):
        types = self._facilities.get(f_type)
        if types is not None and len(types) > 0:
            if model is None:
                self._total_count -= 1
                return types.pop()
            else:
                found_t = None
                for t in types:
                    if t.get_model() == model:
                        found_t = t
                        break
                if found_t is not None:
                    types.remove(found_t)
                    self._total_count -= 1
                    return found_t
        return None

    @staticmethod
    def facility_can_be_stored(facility):
        if not isinstance(facility, Facility):
            return False
        if facility.get_type() is None:
            return False
        if facility.get_model() is None:
            return False
        return True


class Facility(ABC):
    def __init__(self, model):
        self._store_id = None
        self._facility_type = None
        self._model = model
        self.set_type()

    def __str__(self):
        return f'Id {self._store_id}, type: {self._facility_type}, mode: {self._model}'

    def __eq__(self, other):
        return self._store_id == other._store_id

    def set_id(self, store_id):
        self._store_id = store_id

    def get_type(self):
        return self._facility_type

    def get_model(self):
        return self._model

    @abstractmethod
    def slots(self):
        pass

    @abstractmethod
    def set_type(self):
        pass


class Printer(Facility):
    def __init__(self, model):
        super().__init__(model)

    def set_type(self):
        self._facility_type = 'Printer'

    @property
    def slots(self):
        return 1


class Copier(Facility):
    def __init__(self, model):
        super().__init__(model)

    def set_type(self):
        self._facility_type = 'Copier'

    @property
    def slots(self):
        return 2


class Scanner(Facility):
    def __init__(self, model):
        super().__init__(model)

    def set_type(self):
        self._facility_type = 'Scanner'

    @property
    def slots(self):
        return 1


store = Store(5)
facilities = [Printer('printer_model1'),
              Printer('printer_model2'),
              Copier('copier_model1'),
              Copier('copier_model2'),
              Scanner('scanner_model1'),
              Scanner('scanner_model2'),
              'Something that can not be stored']

for f in facilities:
    if Store.facility_can_be_stored(f):
        store.take(f)
    else:
        print(f'{f} can not be stored')

print(store.request('Printer'))
print(store.request('Printer'))
print(store.request('Printer'))
print(store.request('Copier', 'copier_model1'))
