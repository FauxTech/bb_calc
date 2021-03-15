import unittest
from main import BloodBowlCalculator


class TestBloodBowlCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = BloodBowlCalculator()
        self.moves = {
            'catch': {
                5: {'result': 5, 'num_dice': 1, 'type': 'catch'},
                4: {'result': 4, 'num_dice': 1, 'type': 'catch'},
                3: {'result': 3, 'num_dice': 1, 'type': 'catch'},
                2: {'result': 2, 'num_dice': 1, 'type': 'catch'},
                1: {'result': 1, 'num_dice': 1, 'type': 'catch'}},
            'dodge': {
                5: {'result': 5, 'num_dice': 1, 'type': 'dodge'},
                4: {'result': 4, 'num_dice': 1, 'type': 'dodge'},
                3: {'result': 3, 'num_dice': 1, 'type': 'dodge'},
                2: {'result': 2, 'num_dice': 1, 'type': 'dodge'},
                1: {'result': 1, 'num_dice': 1, 'type': 'dodge'}},
            'pass_skill': {
                5: {'result': 5, 'num_dice': 1, 'type': 'pass_skill'},
                4: {'result': 4, 'num_dice': 1, 'type': 'pass_skill'},
                3: {'result': 3, 'num_dice': 1, 'type': 'pass_skill'},
                2: {'result': 2, 'num_dice': 1, 'type': 'pass_skill'},
                1: {'result': 1, 'num_dice': 1, 'type': 'pass_skill'}},
            'sure_feet': {
                5: {'result': 5, 'num_dice': 1, 'type': 'sure_feet'},
                4: {'result': 4, 'num_dice': 1, 'type': 'sure_feet'}},
            'sure_hands': {
                5: {'result': 5, 'num_dice': 1, 'type': 'sure_hands'},
                4: {'result': 4, 'num_dice': 1, 'type': 'sure_hands'},
                3: {'result': 3, 'num_dice': 1, 'type': 'sure_hands'},
                2: {'result': 2, 'num_dice': 1, 'type': 'sure_hands'},
                1: {'result': 1, 'num_dice': 1, 'type': 'sure_hands'}},
            'block': {
                15: {'result': 5, 'num_dice': 1, 'type': 'block'},
                14: {'result': 4, 'num_dice': 1, 'type': 'block'},
                13: {'result': 3, 'num_dice': 1, 'type': 'block'},
                12: {'result': 2, 'num_dice': 1, 'type': 'block'},
                11: {'result': 1, 'num_dice': 1, 'type': 'block'},
                25: {'result': 5, 'num_dice': 2, 'type': 'block'},
                24: {'result': 4, 'num_dice': 2, 'type': 'block'},
                23: {'result': 3, 'num_dice': 2, 'type': 'block'},
                22: {'result': 2, 'num_dice': 2, 'type': 'block'},
                21: {'result': 1, 'num_dice': 2, 'type': 'block'},
                35: {'result': 5, 'num_dice': 3, 'type': 'block'},
                34: {'result': 4, 'num_dice': 3, 'type': 'block'},
                33: {'result': 3, 'num_dice': 3, 'type': 'block'},
                32: {'result': 2, 'num_dice': 3, 'type': 'block'},
                31: {'result': 1, 'num_dice': 3, 'type': 'block'}},
            'minus_block': {
                25: {'result': 5, 'num_dice': 2, 'type': 'minus_block'},
                24: {'result': 4, 'num_dice': 2, 'type': 'minus_block'},
                23: {'result': 3, 'num_dice': 2, 'type': 'minus_block'},
                22: {'result': 2, 'num_dice': 2, 'type': 'minus_block'},
                21: {'result': 1, 'num_dice': 2, 'type': 'minus_block'},
                35: {'result': 5, 'num_dice': 3, 'type': 'minus_block'},
                34: {'result': 4, 'num_dice': 3, 'type': 'minus_block'},
                33: {'result': 3, 'num_dice': 3, 'type': 'minus_block'},
                32: {'result': 2, 'num_dice': 3, 'type': 'minus_block'},
                31: {'result': 1, 'num_dice': 3, 'type': 'minus_block'}},
            'armour_pen': {
                2: {'result': 2, 'num_dice': 2, 'type': 'armour_pen'},
                3: {'result': 3, 'num_dice': 2, 'type': 'armour_pen'},
                4: {'result': 4, 'num_dice': 2, 'type': 'armour_pen'},
                5: {'result': 5, 'num_dice': 2, 'type': 'armour_pen'},
                6: {'result': 6, 'num_dice': 2, 'type': 'armour_pen'},
                7: {'result': 7, 'num_dice': 2, 'type': 'armour_pen'},
                8: {'result': 8, 'num_dice': 2, 'type': 'armour_pen'},
                9: {'result': 9, 'num_dice': 2, 'type': 'armour_pen'},
                10: {'result': 10, 'num_dice': 2, 'type': 'armour_pen'}},
            'injury': {
                1: {'result': ['stun'], 'num_dice': 2, 'type': 'injury'},
                2: {'result': ['ko'], 'num_dice': 2, 'type': 'injury'},
                3: {'result': ['cas'], 'num_dice': 2, 'type': 'injury'},
                12: {'result': ['stun', 'ko'], 'num_dice': 2,
                     'type': 'injury'},
                23: {'result': ['ko', 'cas'], 'num_dice': 2,
                     'type': 'injury'},
                13: {'result': ['stun', 'cas'], 'num_dice': 2,
                     'type': 'injury'}}
            }
        self.skills_off = {'catch': 0, 'dodge': 0, 'pass_skill': 0,
                           'sure_feet': 0, 'sure_hands': 0}
        self.skills_on = {'catch': 1, 'dodge': 1, 'pass_skill': 1,
                          'sure_feet': 1, 'sure_hands': 1}

    def test_roll(self):
        self.assertEqual(round(
            self.calc.prob_calc([self.moves['dodge'][5]],
                                self.skills_off, reroll=0), 5), 0.83333)
        self.assertEqual(round(
            self.calc.prob_calc([self.moves['sure_feet'][4]],
                                self.skills_off, reroll=0), 5), 0.66667)
        self.assertEqual(round(
            self.calc.prob_calc([self.moves['catch'][3]],
                                self.skills_off, reroll=0), 5), 0.5)
        self.assertEqual(round(
            self.calc.prob_calc([self.moves['pass_skill'][2]],
                                self.skills_off, reroll=0), 5), 0.33333)
        self.assertEqual(round(
            self.calc.prob_calc([self.moves['sure_hands'][1]],
                                self.skills_off, reroll=0), 5), 0.16667)
        self.assertEqual(round(
            self.calc.prob_calc([self.moves['dodge'][5]],
                                self.skills_off, reroll=0), 5), 0.83333)
        self.assertEqual(round(
            self.calc.prob_calc([self.moves['dodge'][5],
                                 self.moves['dodge'][4]],
                                self.skills_off, reroll=0), 5), 0.55556)
        self.assertEqual(round(
            self.calc.prob_calc([self.moves['dodge'][5],
                                 self.moves['dodge'][4],
                                 self.moves['dodge'][3],
                                 self.moves['dodge'][2],
                                 self.moves['dodge'][1]],
                                self.skills_off, reroll=0), 5), 0.01543)

    def test_reroll(self):
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['dodge'][5]],
            self.skills_off),
            5), 0.92593)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['dodge'][4]],
            self.skills_off),
            5), 0.83333)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][3], self.moves['dodge'][2]],
            self.skills_off),
            5), 0.36111)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['dodge'][1],
             self.moves['dodge'][1]], self.skills_off),
            5), 0.06559)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][1], self.moves['dodge'][5],
             self.moves['dodge'][3]], self.skills_off),
            5), 0.17361)

    def test_skill_reroll(self):
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['dodge'][4]],
            self.skills_on, reroll=0), 5), 0.83333)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['dodge'][4]],
            self.skills_on), 5), 0.8642)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['dodge'][4],
             self.moves['dodge'][3]], self.skills_on, reroll=0), 5), 0.55556)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['dodge'][4],
             self.moves['dodge'][3]], self.skills_on), 5), 0.64043)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['dodge'][3],
             self.moves['catch'][5], self.moves['catch'][2],
             ], self.skills_on, reroll=0), 5), 0.35365)

    def test_block(self):
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][15]], self.skills_on, reroll=0), 5), 0.83333)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][15]], self.skills_on), 5), 0.97222)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][24]], self.skills_on, reroll=0), 5), 0.88889)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][24]], self.skills_on), 5), 0.98765)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][33]], self.skills_on, reroll=0), 5), 0.875)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][33]], self.skills_on), 5), 0.98438)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][25], self.moves['block'][24]],
            self.skills_on, reroll=0), 5), 0.8642)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][25], self.moves['block'][24]],
            self.skills_on), 5), 0.98422)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][15], self.moves['block'][24],
             self.moves['block'][25], self.moves['block'][33]],
            self.skills_on, reroll=0), 5), 0.63014)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['block'][15], self.moves['block'][24],
             self.moves['block'][25], self.moves['block'][33]],
            self.skills_on), 5), 0.90146)

    def test_minus_block(self):
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][25]],
            self.skills_on, reroll=0), 5), 0.69444)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][24]],
            self.skills_on), 5), 0.69136)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][25], self.moves['minus_block'][23]],
            self.skills_on, reroll=0), 5), 0.17361)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][24], self.moves['minus_block'][23]],
            self.skills_on), 5), 0.25617)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][35]],
            self.skills_on, reroll=0), 5), 0.5787)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][31]],
            self.skills_on), 5), 0.00924)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][35], self.moves['minus_block'][34]],
            self.skills_on, reroll=0), 5), 0.17147)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][35], self.moves['minus_block'][34]],
            self.skills_on), 5), 0.36437)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][24], self.moves['minus_block'][23],
             self.moves['minus_block'][35], self.moves['minus_block'][34]],
            self.skills_on, reroll=0), 5), 0.01905)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][24], self.moves['minus_block'][23],
             self.moves['minus_block'][35], self.moves['minus_block'][34]],
            self.skills_on), 5), 0.06536)

    def test_block_both(self):
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][25], self.moves['block'][25]],
            self.skills_on, reroll=0), 5), 0.67515)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][25], self.moves['block'][25]],
            self.skills_on), 5), 0.90021)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][25], self.moves['block'][25],
             self.moves['block'][35], self.moves['block'][15]],
            self.skills_on, reroll=0), 5), 0.56002)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][25], self.moves['block'][25],
             self.moves['block'][35], self.moves['block'][15]],
            self.skills_on), 5), 0.84263)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][24], self.moves['minus_block'][35],
             self.moves['block'][35], self.moves['block'][14],
             self.moves['block'][33], self.moves['block'][23]],
            self.skills_on, reroll=0), 5), 0.112)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['minus_block'][24], self.moves['minus_block'][35],
             self.moves['block'][35], self.moves['block'][14],
             self.moves['block'][33], self.moves['block'][23]],
            self.skills_on), 5), 0.30127)

    def test_armour(self):
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['armour_pen'][2]],
            self.skills_on, reroll=0), 5), 0.97222)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['armour_pen'][2]],
            self.skills_on), 5), 0.97222)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['armour_pen'][8]],
            self.skills_on), 5), 0.27778)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['armour_pen'][10]],
            self.skills_on), 5), 0.08333)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['armour_pen'][8], self.moves['armour_pen'][9]],
            self.skills_on), 5), 0.0463)

    def test_injury(self):
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['injury'][1]],
            self.skills_off, reroll=0), 5), 0.58333)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['injury'][2]], self.skills_off), 5), 0.25)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['injury'][3]], self.skills_off), 5), 0.16667)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['injury'][12]], self.skills_off, reroll=0), 5), 0.83333)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['injury'][23]], self.skills_off), 5), 0.41667)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['injury'][13]], self.skills_off), 5), 0.75)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['injury'][1], self.moves['injury'][2],
             self.moves['injury'][3], self.moves['injury'][12],
             self.moves['injury'][23], self.moves['injury'][13]],
            self.skills_off), 5), 0.00633)

    def test_general(self):
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['block'][32],
             self.moves['minus_block'][25], self.moves['armour_pen'][8]],
            self.skills_off, reroll=0), 5), 0.11312)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['block'][32],
             self.moves['minus_block'][25], self.moves['armour_pen'][8]],
            self.skills_off, reroll=1), 5), 0.20006)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['block'][35],
             self.moves['injury'][23], self.moves['armour_pen'][7]],
            self.skills_on, reroll=0), 5), 0.16801)
        self.assertEqual(round(self.calc.prob_calc(
            [self.moves['dodge'][5], self.moves['block'][35],
             self.moves['injury'][23], self.moves['armour_pen'][7]],
            self.skills_on, reroll=1), 5), 0.16878)


if __name__ == '__main__':
    unittest.main()
