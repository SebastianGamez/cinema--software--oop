class Film:

    def __init__(self, name):
        self._name = name
        self._projections = []

    @property
    def name(self):
        return self._name

    @property
    def projections(self):
        return self._projections

    @projections.setter
    def projections(self, projections):
        self._projections = projections

    def add_projections(self, projection):
        self.projections.append(projection)
