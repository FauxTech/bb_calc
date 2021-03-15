class BloodBowlCalculator:

    def __init__(self):
        pass

    def prob_calc(self, rolls, reroll_skill, reroll=1, repeat=1):
        if not rolls:
            return 1
        roll = rolls[0]['result']
        num_dice = rolls[0]['num_dice']
        roll_type = rolls[0]['type']

        # base probability (every roll is success)
        probability = (self.roll_success(roll, num_dice, roll_type)
                       * self.prob_calc(rolls[1:], reroll_skill, reroll,
                                        repeat=1))

        # skill reroll calculation
        if reroll_skill.get(roll_type, 0) == 1 and repeat == 1:
            new_reroll_skill = dict(reroll_skill)
            new_reroll_skill[roll_type] = 0
            probability += (self.roll_fail(roll, num_dice, roll_type)
                            * self.prob_calc(rolls, new_reroll_skill, reroll,
                                             repeat=0))
        # team reroll calculation
        elif (reroll == 1 and repeat == 1 and
              roll_type not in ['armour_pen', 'injury']):
            probability += (self.roll_fail(roll, num_dice, roll_type)
                            * self.prob_calc(rolls, reroll_skill, reroll=0,
                                             repeat=0))
        return probability

    def roll_success(self, success, num_dice, roll_type):
        # -2d/3d block variant
        if roll_type == 'minus_block':
            return pow(success / 6, num_dice)
        elif roll_type == 'armour_pen':
            return self.armour_pen(success)
        elif roll_type == 'injury':
            return self.injury_roll(success)
        return 1 - pow(1 - success / 6, num_dice)

    @staticmethod
    def roll_fail(success, num_dice, roll_type):
        # -2d/3d block variant
        if roll_type == 'minus_block':
            return 1 - pow(success/6, num_dice)
        return pow(1 - success/6, num_dice)

    ''' function that calculates armour penetration
        base mechanic is already done
        add mighty blow (+1 to threshold)
        add pilling on (reroll) <- it might get changed with bb_2021 '''
    @staticmethod
    def armour_pen(armour_value):
        combinations = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
        armour_pen = sum(combinations[armour_value - 1:]) / 36
        return armour_pen

    @staticmethod
    def injury_roll(success):
        # skills like thick head etc. can be defined as var
        # that will move the index during slicking
        combination = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
        stun = sum(combination[:6]) / 36
        ko = sum(combination[6:8]) / 36
        cas = sum(combination[8:]) / 36
        injury_rolls = {'stun': stun, 'ko': ko, 'cas': cas}

        return sum(injury_rolls.get(option, 1) for option in success)


if __name__ == '__main__':
    pass
