
class BloodBowlCalculator:

    def __init__(self):
        pass

    def prob_calc(self, rolls, reroll_skill, reroll=1, repeat=1):
        if not rolls:
            return 1

        # successful rolls
        # put calculations into functions and create variations for different situations like -2d
        probability = self.roll_success(rolls[0][0], rolls[0][1]) *\
            self.prob_calc(rolls[1:], reroll_skill, reroll, repeat=1)

        # failed rolls being repeated with team/skill reroll
        if reroll_skill[rolls[0][2]] == 1 and repeat == 1:
            new_reroll_skill = dict(reroll_skill)
            new_reroll_skill[rolls[0][2]] = 0
            probability += self.roll_fail(rolls[0][0], rolls[0][1]) * \
                self.prob_calc(rolls, new_reroll_skill, reroll, repeat=0)
        elif reroll == 1 and repeat == 1:
            # -2/3 dice need to subtract prob instead of adding
            probability += self.roll_fail(rolls[0][0], rolls[0][1]) * \
                self.prob_calc(rolls, reroll_skill, 0, repeat=0)

        return probability

    @staticmethod
    def roll_success(success, num_dice):
        return 1 - pow(1 - success / 6, num_dice)

    @staticmethod
    def roll_fail(fail, num_dice):
        return pow(1 - fail / 6, num_dice)


if __name__ == '__main__':
    skills = {'catch': 0, 'dodge': 1, 'pass_skill': 1, 'sure_feet': 1, 'sure_hands': 1, 'block': 0}
    roll = [[5, 1, 'dodge'], [4, 1, 'catch'], [5, 1, 'dodge']]
    # roll = [[5, 1, 'dodge'], [5, 1, 'catch'], [5, 1, 'dodge'], [5, 2, 'block'],
    #         [5, 1, 'pass_skill'], [5, 1, 'sure_feet'], [5, 1, 'sure_hands']]
    # roll = [[1, 3, 'block']]
    # block = [[2, 2]]
    calculator = BloodBowlCalculator()
    print(calculator.prob_calc(roll, skills, reroll=1) * 100)
