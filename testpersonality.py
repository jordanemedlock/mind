import unittest
from personality import *


class TestPersonality(unittest.TestCase):
    def test_default(self):
        p = Personality()
        self.assertEqual(p.value, 0.5)

    def test_add_traits(self):
        p = Personality()
        p.add_trait('confidence', 0.25)
        self.assertEqual(p.value, 0.25)
        self.assertEqual(p['confidence'], 0.25)

        p.add_trait('happiness', 0.75)
        self.assertEqual(p.value, 0.5)
        self.assertEqual(p['happiness'], 0.75)

    def test_add_trait_to(self):
        p = Personality()
        p.add_trait('loyalty', 0.5)
        p.add_trait_to('loyalty','family', 0.25)
        self.assertEqual(p['loyalty.family'], 0.25)
        self.assertEqual(p['loyalty'], 0.25)

        p.add_trait_to('loyalty', 'friends', 0.75)
        self.assertEqual(p['loyalty.friends'], 0.75)
        self.assertEqual(p['loyalty.family'], 0.25)
        self.assertEqual(p['loyalty'], 0.5)

    def test_equals(self):
        p = Personality()
        self.assertEqual(p, 0.5)





if __name__ == '__main__':
    unittest.main()
