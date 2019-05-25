class Pokemon(object):

    def __init__(self, name, max_hp=None, strength=None, types=None):
        if not isinstance(name, str):
            raise ValueError('name must be a string')
        if not name:
            raise ValueError('name must not be empty')
        if max_hp is None:
            raise ValueError('max_hp must not be None')
        if strength is None:
            raise ValueError('max_hp must not be None')
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.strength = strength
        self.types = types
        return

    def __repr__(self):
        return '{}(HP={}/{}, STR={}, TYPES={})'.format(
            self.name,
            self.current_hp,
            self.max_hp,
            self.strength,
            self.types,
        )
