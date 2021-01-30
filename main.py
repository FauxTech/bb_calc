
class BloodBowlCalculator:

    def __init__(self):
        pass

    def prob_calc(self, rolls, reroll_skill, reroll=1, repeat=1):
        if not rolls:
            return 1

        # successful rolls
        probability = (7 - rolls[0][0]) / 6 * self.prob_calc(rolls[1:], reroll_skill, reroll, repeat=1)

        # failed rolls being repeated with team/skill reroll
        if reroll_skill[rolls[0][1]] == 1 and repeat == 1:
            new_reroll_skill = dict(reroll_skill)
            new_reroll_skill[rolls[0][1]] = 0
            probability += (rolls[0][0] - 1) / 6 * self.prob_calc(rolls, new_reroll_skill, reroll, repeat=0)
        elif reroll == 1 and repeat == 1:
            probability += (rolls[0][0] - 1) / 6 * self.prob_calc(rolls, reroll_skill, 0, repeat=0)

        return probability

    @staticmethod
    def block_roll(rolls, reroll=1):
        if reroll == 0:
            probability = (1 - pow((6 - rolls[0][0]) / 6, rolls[0][1]))
        else:
            probability = (1 - pow((6 - rolls[0][0]) / 6, 2 * rolls[0][1]))
        return probability


if __name__ == '__main__':
    skills = {'catch': 1, 'dodge': 1, 'pass_skill': 1, 'sure_feet': 1, 'sure_hands': 1, 'reroll': 1}
    roll = [[2, 'dodge'], [3, 'catch'], [2, 'dodge']]
    block = [[3, 2]]
    calculator = BloodBowlCalculator()
    # print(calculator.prob_calc(roll, skills, reroll=1))
    print(calculator.block_roll(block))
