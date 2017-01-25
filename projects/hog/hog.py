"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################



def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    roll = 1
    ones = 0
    total = 0
    while roll <= num_rolls:
        value = dice()
        if value == 1:
            ones = ones + 1
        if value != 1:
            total = total + value
        roll +=1
    if ones != 0:
        return ones
    else:
        return total
    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    first_digit = opponent_score // 10
    second_digit = opponent_score % 10
    return 1 + max(first_digit, second_digit)
    # END PROBLEM 2


def factor_a(n, k):
    if n % k == 0:
        return True
def is_prime(n):
    k = 2
    while k < n:
        if factor_a(n,k):
            return False
        k +=1
    if factor_a(n,k):
        return True
    if n == 1:
        return False

def prime(round_score):
    """"If a number is not prime, then that number is returned. If the number is prime, the consecutive prime number is returned.

    >>> prime (31)
    37
    >>> prime (151)
    157
    >>> prime (347)
    349"""
    if is_prime(round_score) == False:
        new_score = round_score
    else:
        new_score = round_score + 1
        while is_prime(new_score) == False:
            new_score +=1
    return new_score



def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if num_rolls == 0:
        return prime(free_bacon(opponent_score))
    elif num_rolls !=0:
        score = roll_dice(num_rolls, dice)
        return min(prime(score), 25-num_rolls)
    # END PROBLEM 2


def reroll(dice):
    """Return dice that return even outcomes and re-roll odd outcomes of DICE."""
    def rerolled():
        # BEGIN PROBLEM 3
        value = dice()
        if value % 2 == 0:
            return value
        else:
            value = dice()
            return value
        # END PROBLEM 3
    return rerolled


def select_dice(score, opponent_score, dice_swapped):
    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    swapped for four-sided dice (Pork Chop).

    DICE_SWAPPED is True if and only if four-sided dice are being used.
    """
    # BEGIN PROBLEM 4
    if dice_swapped:
        dice = four_sided
    else:
        dice = six_sided
    # END PROBLEM 4
    if (score + opponent_score) % 7 == 0:
        dice = reroll(dice)
    return dice


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False  # Whether 4-sided dice have been swapped for 6-sided
    dice = six_sided

    while score0 < goal and score1 < goal:
        if player == 0:
            num_rolls = strategy0(score0, score1)
            dice = select_dice(score1, score0, dice_swapped)
            if num_rolls == -1:
                if dice_swapped:
                    dice_swapped = False
                else:
                    dice_swapped = True
                score0 = score0 + 1
            else:
                a = take_turn(num_rolls, score1, dice)
                score0 = score0 + a
            player = other(0)
        elif player == 1:
            num_rolls = strategy1(score1, score0)
            dice = select_dice(score1, score0, dice_swapped)
            if num_rolls == -1:
                if dice_swapped:
                    dice_swapped = False
                else:
                    dice_swapped = True
                score1 = score1 + 1
            else:
                b = take_turn(num_rolls, score0, dice)
                score1 = score1 + b
            player = other(1)
        if (score1 == 2 * score0) or (score0 == 2 * score1):
            score0, score1 = score1, score0
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert -1 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    score = 0
    opponent_score = 0

    while check_strategy_roll(score, opponent_score, strategy(score, opponent_score)) == None:
        score = score + 1
        #print(score)
        #print(opponent_score)
        if score == goal:
            score = 0
            opponent_score = opponent_score + 1
            if opponent_score == goal:
                break
    return None

    # END PROBLEM 6


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75"""

    # BEGIN PROBLEM 7
    def avg(*args):
        avgtotal = 0
        counter = 0
        while counter < num_samples:
            avgtotal = avgtotal + fn(*args)
            counter = counter + 1
        return avgtotal/counter
    return avg

    # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8

    count = 1
    highnum = 0
    greatest_dice = 1
    while count <= 10:
        k =(make_averaged(roll_dice)(count, dice))
        if k > highnum:
            highnum = k
            greatest_dice = count
        count = count + 1
    return greatest_dice

    # END PROBLpEM 8


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        rerolled_max = max_scoring_num_rolls(reroll(six_sided))
        print('Max scoring num rolls for re-rolled dice:', rerolled_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    if prime(free_bacon(opponent_score)) >= margin:
        return 0
    else:
        return num_rolls
    # END PROBLEM 9
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    output1 = prime(free_bacon(opponent_score))
    output2 = take_turn(num_rolls, opponent_score, dice = six_sided)
    if output1 >= margin:
        return 0
    elif score + output2 == .5 * opponent_score:
        return 0
    else:
        return num_rolls
    # END PROBLEM 10
check_strategy(swap_strategy)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 11
    k = 0
    m = 0
    l = 0
    s = 0
    num_rolls = 5
    if score == 0 and opponent_score == 0:
        return -1
    if opponent_score % 10 == 9:
        return 0
    if score < opponent_score:
        while s <= 10:
            if opponent_score % 10 == s:
                if prime(s) > (opponent_score // 10):
                    if prime(s) + score == .5 * opponent_score:
                        return 0
            if opponent_score // 10 == s:
                if prime(s) > (opponent_score % 10):
                    if prime(s) + score == .5 * opponent_score:
                        return 0
            s += 1
        if abs(score - opponent_score) < 10:
            return swap_strategy(score, opponent_score, 6, 5)
        if score + 1 == .5 * opponent_score:
            return -1
        while k <= 10:
            if ((score + take_turn(k, opponent_score)) == 0.5 * opponent_score):
                return k
            k += 1
        if 10 < abs(score - opponent_score) < 20:
            while l <= 10:
                if opponent_score + take_turn(l, score) == 100:
                    return 2
                l += 1
    if score > opponent_score:
        while m <= 10:
            if (score + take_turn(k, opponent_score) != 2 * opponent_score):
                return m
            m += 1
            if take_turn(k, opponent_score) % 5 == 0 and score + take_turn(k, opponent_score) == 2 * opponent_score:
                return -1
            if take_turn(k, opponent_score) % 6 == 0 and score + take_turn(k, opponent_score) == 2 * opponent_score:
                return -1

    return swap_strategy(score, opponent_score, 6, 5)

    # END PROBLEM 11
#check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()