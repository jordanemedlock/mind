# TODO: Add testing
# this would actually be a good case for unit testing
# TODO: Add docset
class Personality(object):
    def __init__(self, traits=None, value=None):
        """
        So this is a representation of a recursive tree shaped personality trait
        which is just a glorified dict.
        """
        self._traits = traits or {}
        self._value = value or 0.5
        self._parent = None

    def add_trait(self, name, value=None):
        trait = Personality(value=value)
        trait._parent = self
        self._traits[name] = trait
        trait._value = value or self._value
        self._recalculate_value()

    def add_trait_to(self, parent, name, value=None):
        self.parse_list(parent).add_trait(name, value)
        self._recalculate_value()

    def _recalculate_value(self):
        values = map(lambda v: v._recalculate_value(), self._traits.itervalues())
        nv = sum(values)
        if nv > 0:
            self._value = nv / float(len(values))
            return self._value
        else:
            return self._value

    @property
    def value(self):
        return self._value

    def add_value(self, n):
        if self._value + n >= 1 or self._value + n <= 0:
            # assert that you cant go over 1 or under 0
            return
        if len(self._traits) == 0:
            self._value += n
        else:
            dn = n / float(len(self._traits))
            for k, v in self._traits.iteritems():
                v.add_value(dn)

    def __getitem__(self, key=None):
        return self.parse_list(key)

    def parse_list(self, key):
        keys = key.split('.')
        last = self
        for k in keys:
            last = last._traits[k]
        return last

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return 'Personality({},{})'.format(self._traits, self._value)

    def __eq__(self, other):
        return self is other or self.value == other

    def __ne__(self, other):
        return not self == other








