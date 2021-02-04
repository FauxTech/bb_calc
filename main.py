
class BloodBowlCalculator:

    def __init__(self):
        pass

    def prob_calc(self, rolls, reroll_skill, reroll=1, repeat=1):
        if not rolls:
            return 1

        # successful roll calculation
        probability = self.roll_success(rolls[0][0], rolls[0][1]) *\
            self.prob_calc(rolls[1:], reroll_skill, reroll, repeat=1)

        # skill reroll calculation
        if reroll_skill[rolls[0][2]] == 1 and repeat == 1:
            new_reroll_skill = dict(reroll_skill)
            new_reroll_skill[rolls[0][2]] = 0
            probability += self.roll_fail(rolls[0][0], rolls[0][1]) * \
                self.prob_calc(rolls, new_reroll_skill, reroll, repeat=0)
        # team reroll calculation
        elif reroll == 1 and repeat == 1:
            probability += self.roll_fail(rolls[0][0], rolls[0][1]) * \
                self.prob_calc(rolls, reroll_skill, 0, repeat=0)

        return probability

    @staticmethod
    def roll_success(success, num_dice):
        # -2d/3d block variant
        if num_dice < 0:
            return pow(success / 6, abs(num_dice))

        return 1 - pow(1 - success / 6, num_dice)

    @staticmethod
    def roll_fail(success, num_dice):
        # -2d/3d block variant
        if num_dice < 0:
            return 1 - pow(success / 6, abs(num_dice))

        return pow(1 - success / 6, num_dice)

    # @staticmethod
    # def minus_block(success, num_dice):
    #     prob_no_reroll = pow(success / 6, num_dice)
    #     prob_reroll = pow(success / 6, num_dice) + \
    #         (1 - pow(success / 6, num_dice)) * pow(success / 6, num_dice)
    #     return prob_no_reroll * 100, prob_reroll * 100

    @staticmethod
    def armour_pen(success):
        combinations = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
        armour_pen = sum(combinations[:13 - success]) / 36
        armour_pen_pill_on = (sum(combinations[:13 - success]) / 36) + \
            (sum(combinations[13 - success:]) / 36) * (sum(combinations[:13 - success]) / 36)
        armour_no_pen = sum(combinations[13 - success:]) / 36
        return armour_pen * 100, armour_no_pen * 100, armour_pen_pill_on * 100

    @staticmethod
    def injury_roll():
        # skills like thick head etc. can be defined as var that will move the index during slicking
        combination = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
        stun = sum(combination[:6]) / 36
        ko = sum(combination[6:8]) / 36
        cas = sum(combination[8:]) / 36
        stun_pile_on = (ko + cas) * stun + stun
        ko_pile_on = (stun + cas) * ko + ko
        cas_pile_on = (stun + ko) * cas + cas

        print(f"stun: {round(stun * 100, 2)}% stun_pile_on:  {round(stun_pile_on * 100, 2)}%")
        print(f"KO: {round(ko * 100, 2)}% KO_pile_on:  {round(ko_pile_on * 100, 2)}%")
        print(f"CAS: {round(cas * 100, 2)}% CAS_pile_on:  {round(cas_pile_on * 100, 2)}%")


if __name__ == '__main__':
    skills = {'catch': 1, 'dodge': 1, 'pass_skill': 0, 'sure_feet': 0, 'sure_hands': 0, 'block': 0}
    # roll = [[5, 1, 'dodge'], [4, 1, 'catch'], [5, 1, 'dodge']]
    # roll = [[5, 1, 'dodge'], [5, 1, 'catch'], [5, 1, 'dodge'], [5, 2, 'block'],
    #         [5, 1, 'pass_skill'], [5, 1, 'sure_feet'], [5, 1, 'sure_hands']]
    # roll = [[1, -2, 'block'], [5, 1, 'dodge'], [2, 1, 'dodge'], [3, 1, 'catch']]
    roll = [[5, -2, 'block'], [5, 1, 'dodge'], [5, 1, 'dodge'], [5, 1, 'dodge'], [4, 1, 'dodge']]
    calculator = BloodBowlCalculator()
    # print(calculator.prob_calc(roll, skills, reroll=1) * 100)
    # print(calculator.armour_pen(4))
    calculator.injury_roll()
