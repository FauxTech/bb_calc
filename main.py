
class BloodBowlCalculator:

    def __init__(self):
        self.probability = 1

    def prob_calc_reroll(self, rolls, rerolls=1):
        if not rolls:
            return 1
        probability = (7 - rolls[0]) / 6 * self.prob_calc_reroll(rolls[1:], rerolls)
        if rerolls == 1:
            probability += (rolls[0] - 1) / 6 * self.prob_calc_reroll(rolls, 0)
        return probability


if __name__ == '__main__':
    calculator = BloodBowlCalculator()
    print(83.333, calculator.prob_calc_reroll([2], 0))
    print(97.222, calculator.prob_calc_reroll([2]))
    print(41.667, calculator.prob_calc_reroll([2, 4], 0))
    print(69.444, calculator.prob_calc_reroll([2, 4]))
    print(6.944, calculator.prob_calc_reroll([2, 4, 6], 0))
    print(17.361, calculator.prob_calc_reroll([2, 4, 6]))
    print(1.543, calculator.prob_calc_reroll([2, 4, 6, 5, 3], 0))
    print(5.401, calculator.prob_calc_reroll([2, 4, 6, 5, 3]))
