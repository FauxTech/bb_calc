class BloodBowlCalculator:

    def __init__(self):
        pass

    def prob_calc(self, rolls, reroll_skill, reroll=1, repeat=1):
        if not rolls:
            return 1
        roll = rolls[0]['result']
        num_dice = rolls[0]['num_dice']
        roll_type = rolls[0]['type']

        # successful roll calculation
        if roll_type == 'armour_break':
            probability = (self.armour_pen(roll)
                           * self.prob_calc(rolls[1:], reroll_skill, reroll,
                                            repeat=1))
        else:
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
        elif reroll == 1 and repeat == 1 and roll_type != 'armour_break':
            probability += (self.roll_fail(roll, num_dice, roll_type)
                            * self.prob_calc(rolls, reroll_skill, reroll=0,
                                             repeat=0))
        return probability

    @staticmethod
    def roll_success(success, num_dice, roll_type):
        # -2d/3d block variant
        if roll_type == 'minus_block':
            return pow(success / 6, num_dice)
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
        # armour_pen_pill_on = ((sum(combinations[:13-success])/36)
        #                       + (sum(combinations[13-success:])/36)
        #                       * (sum(combinations[:13-success])/36))
        # armour_no_pen = sum(combinations[13-success:]) / 36
        # return armour_pen * 100, armour_no_pen * 100, armour_pen_pill_on * 100
        return armour_pen

    @staticmethod
    def injury_roll():
        # skills like thick head etc. can be defined as var
        # that will move the index during slicking
        combination = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
        stun = sum(combination[:6]) / 36
        ko = sum(combination[6:8]) / 36
        cas = sum(combination[8:]) / 36
        stun_pile_on = (ko + cas) * stun + stun
        ko_pile_on = (stun + cas) * ko + ko
        cas_pile_on = (stun + ko) * cas + cas

        print(f"stun: {round(stun * 100, 2)}% "
              f"stun_pile_on:  {round(stun_pile_on * 100, 2)}%")
        print(f"KO: {round(ko * 100, 2)}% "
              f"KO_pile_on:  {round(ko_pile_on * 100, 2)}%")
        print(f"CAS: {round(cas * 100, 2)}% "
              f"CAS_pile_on:  {round(cas_pile_on * 100, 2)}%")


if __name__ == '__main__':
    # reroll\throw test
    moves1 = [{'result': 5, 'num_dice': 1, 'type': 'dodge'},
              {'result': 2, 'num_dice': 1, 'type': 'dodge'},
              {'result': 2, 'num_dice': 1, 'type': 'dodge'}]
    skills1 = {'catch': 0, 'dodge': 0, 'pass_skill': 0, 'sure_feet': 0,
               'sure_hands': 0}
    # skill reroll test
    moves2 = [{'result': 5, 'num_dice': 1, 'type': 'dodge'},
              {'result': 2, 'num_dice': 1, 'type': 'dodge'},
              {'result': 2, 'num_dice': 1, 'type': 'dodge'}]
    skills2 = {'catch': 0, 'dodge': 1, 'pass_skill': 0, 'sure_feet': 0,
               'sure_hands': 0}
    moves3 = [{'result': 5, 'num_dice': 1, 'type': 'dodge'},
              {'result': 3, 'num_dice': 1, 'type': 'dodge'},
              {'result': 3, 'num_dice': 1, 'type': 'dodge'},
              {'result': 6, 'num_dice': 1, 'type': 'catch'},
              {'result': 4, 'num_dice': 1, 'type': 'sure_hands'}]
    skills3 = {'catch': 1, 'dodge': 1, 'pass_skill': 0, 'sure_feet': 0,
               'sure_hands': 1}
    # block test
    moves4 = [{'result': 5, 'num_dice': -2, 'type': 'block'}]
    moves5 = [{'result': 4, 'num_dice': -2, 'type': 'block'}]
    moves6 = [{'result': 4, 'num_dice': 1, 'type': 'block'}]
    moves7 = [{'result': 2, 'num_dice': 2, 'type': 'block'}]
    moves8 = [{'result': 1, 'num_dice': 3, 'type': 'block'}]
    moves9 = [{'result': 5, 'num_dice': 2, 'type': 'block'},
              {'result': 2, 'num_dice': 3, 'type': 'block'},
              {'result': 2, 'num_dice': 1, 'type': 'block'},
              {'result': 1, 'num_dice': 2, 'type': 'minus_block'},
              {'result': 3, 'num_dice': 3, 'type': 'minus_block'}]
    # armour pen test
    moves10 = [{'result': 8, 'num_dice': 2, 'type': 'armour_break'}]
    moves11 = [{'result': 8, 'num_dice': 2, 'type': 'armour_break'},
               {'result': 4, 'num_dice': 2, 'type': 'armour_break'}]
    # all rolls test
    moves = [{'result': 5, 'num_dice': 1, 'type': 'dodge'},
             {'result': 2, 'num_dice': 1, 'type': 'dodge'},
             {'result': 5, 'num_dice': 2, 'type': 'block'},
             {'result': 3, 'num_dice': 3, 'type': 'block'},
             {'result': 4, 'num_dice': 1, 'type': 'block'},
             {'result': 5, 'num_dice': 2, 'type': 'minus_block'},
             {'result': 5, 'num_dice': 3, 'type': 'minus_block'},
             {'result': 3, 'num_dice': 1, 'type': 'dodge'},
             {'result': 5, 'num_dice': 1, 'type': 'catch'},
             {'result': 4, 'num_dice': 1, 'type': 'sure_hands'},
             {'result': 8, 'num_dice': 2, 'type': 'armour_break'}]
    skills = {'catch': 1, 'dodge': 1, 'pass_skill': 1, 'sure_feet': 1,
              'sure_hands': 1}

    calculator = BloodBowlCalculator()
    print(round(calculator.prob_calc(moves, skills) * 100, 3),
          round(calculator.prob_calc(moves, skills, reroll=0) * 100, 3))
    print(round(calculator.prob_calc(moves1, skills1) * 100, 3),
          round(calculator.prob_calc(moves1, skills1, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves2, skills2) * 100, 3),
    #       round(calculator.prob_calc(moves2, skills2, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves2, skills2) * 100, 3),
    #       round(calculator.prob_calc(moves2, skills2, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves3, skills3) * 100, 3),
    #       round(calculator.prob_calc(moves3, skills3, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves4, skills) * 100, 3),
    #       round(calculator.prob_calc(moves4, skills, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves5, skills) * 100, 3),
    #       round(calculator.prob_calc(moves5, skills, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves6, skills) * 100, 3),
    #       round(calculator.prob_calc(moves6, skills, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves7, skills) * 100, 3),
    #       round(calculator.prob_calc(moves7, skills, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves8, skills) * 100, 3),
    #       round(calculator.prob_calc(moves8, skills, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves9, skills) * 100, 3),
    #       round(calculator.prob_calc(moves9, skills, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves10, skills) * 100, 3),
    #       round(calculator.prob_calc(moves10, skills, reroll=0) * 100, 3))
    # print(round(calculator.prob_calc(moves11, skills) * 100, 3),
    #       round(calculator.prob_calc(moves11, skills, reroll=0) * 100, 3))

    # calculator.injury_roll()
