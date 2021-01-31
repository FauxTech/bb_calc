
class BloodBowlCalculator:

    def __init__(self):
        pass

    def prob_calc(self, rolls, reroll_skill, reroll=1, repeat=1):
        if not rolls:
            return 1

        # successful rolls
        probability = (1 - pow(1 - rolls[0][0] / 6, rolls[0][1])) * \
            self.prob_calc(rolls[1:], reroll_skill, reroll, repeat=1)

        # failed rolls being repeated with team/skill reroll
        if reroll_skill[rolls[0][2]] == 1 and repeat == 1:
            new_reroll_skill = dict(reroll_skill)
            new_reroll_skill[rolls[0][2]] = 0
            probability += (pow(1 - rolls[0][0] / 6, rolls[0][1])) * \
                self.prob_calc(rolls, new_reroll_skill, reroll, repeat=0)
        elif reroll == 1 and repeat == 1:
            probability += (pow(1 - rolls[0][0] / 6, rolls[0][1])) * \
                self.prob_calc(rolls, reroll_skill, 0, repeat=0)

        return probability


if __name__ == '__main__':
    skills = {'catch': 1, 'dodge': 1, 'pass_skill': 1, 'sure_feet': 1, 'sure_hands': 1, 'block': 0}
    # roll = [[5, 1, 'dodge'], [4, 1, 'catch'], [5, 1, 'dodge'], [2, 3, 'block']]
    roll = [[5, 1, 'dodge'], [5, 1, 'catch'], [5, 1, 'dodge'], [5, 2, 'block'],
            [5, 1, 'pass_skill'], [5, 1, 'sure_feet'], [5, 1, 'sure_hands']]

    block = [[2, 2]]
    calculator = BloodBowlCalculator()
    print(calculator.prob_calc(roll, skills, reroll=1))
