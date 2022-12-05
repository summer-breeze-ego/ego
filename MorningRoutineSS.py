# DSS: Morning Routine Score System
# imports
from msilib.schema import File
from traitlets import Bool
from diffVar import yes, no

# yes or no question
def ynQ(str: str) -> Bool:
    """Returns bool value from yes or no string

    Args:
        str (str): yes or no

    Returns:
        Bool: result.
    """
    if str in yes:
        res = True
    elif str in no:
        res = False
    else:
        exit("the fuck is you doin' fam")

    return res

# wake up time score
def wakeUp(wakeUpTime: int) -> int:
    """Function that calculates score based on wake up time.

    Args:
        wakeUpTime ([integer]): wake up time.

    Returns:
        [integer]: score.
    """
    if (wakeUpTime < 6) :
        return 30
    elif (wakeUpTime < 7):
        return 20
    elif (wakeUpTime < 9):
        return 10
    # if you woke up between 9 and 12 there's no points
    elif (wakeUpTime < 12): 
        return 0 
        
    # -5 productivity points for waking up after noon
    return -5

# morning exercise score
def exMorning() -> int:
    """Returns score based on morning exercise.

    Returns:
        int: [description]
    """
    EMscore = 0
    YoN = input("So, did you do any? (y for yes; n for no)\n")

    if ynQ(YoN) == False:
        return 0 # no exercise -> 0 score
    else:
        exSpec = input("Ok, good! What exactly did you do? (s for stretch; r for running; sr for both)\n")
        if 's' in list(exSpec):
            EMscore += 5
        if 'r' in list(exSpec):
            EMscore += 30
        
    return EMscore

# mindfull activities score
def mindMorning() -> int:
    """Returns score based on morning mindfulness.

    Returns:
        int: score.
    """
    MMscore = 0
    YoN = input("So, did you practice any? (y for yes; n for no)\n")

    if ynQ(YoN) == False:
        return 0 # no mindfulness -> 0 score
    else:
        mindSpec = input("Ok, good! What exactly did you do? (j for journaling; m for meditation, jm for both)\n")
        if 'j' in list(mindSpec):
            MMscore += 20
        if 'm' in list(mindSpec):
            MMscore += 20
        
    return MMscore

# hygiene score
def hygiMorning() -> int:
    """Score based on morning hygiene.

    Returns:
        int: score.
    """
    HMscore = 0

    # brush teeth
    teeth = input('Did you brush your teeth? Be honest! (y for yes; n for no)')
    if ynQ(teeth) == True:
        HMscore += 10
    elif ynQ(teeth) == False:
        print("Wow! Disappointing...\n")
        HMscore -= 10
    
    # shower
    shower = input('Did you shower this morning? (y for yes; n for no)')
    if ynQ(shower) == True:
        typeS = input('how about the heat of the shower? (h - hot; c - cold; n - normal)\n')
        if typeS == 'h':
            HMscore += 15
        elif typeS == 'c':
            HMscore += 25
        elif typeS == 'n':
            HMscore += 10
    
    # shave
    shave = input('Did you shave? (y for yes; n for no)')
    if ynQ(shave) == True:
        HMscore += 25
    elif ynQ(teeth) == False:
        print("Well, that's not that bad.\n")

    return HMscore

# weight if weighed
def weightDaily():
    weight = 0
    w = input('Did you weigh yourself this morning? (y for yes; n for no)')
    if ynQ(w) == True:
        weight = float(input('How much do you weigh?\n'))

    return weight


# morning routine main program
def morningRoutine(f) -> int:
    """Call necessary functions to calculate total morning routine score.

    Args:
        f ([type]): file

    Returns:
        int: total score.
    """
    # wake up time score
    wakeUpTime = float(input('\nAt what time did you wake up today?\nTime: '))
    wakeUpScore = wakeUp(int(wakeUpTime))

    # hygiene
    print("Let's start with the hygiene.\n")
    HMscore = hygiMorning()

    # morning exercise score
    print("\nLet's talk about exercise... in the morning.")
    EMscore = exMorning()

    # mindfull activities score
    print("Mindfulness is extremely important as well.\n")
    MMscore = mindMorning()

    # weight update
    print("Let's talk about the weight...\n")
    weight = weightDaily()

    # write to file score for each activity
    f.write('You got ' + str(wakeUpScore) + ' points for waking up at ' + str(int(wakeUpTime)) + ':00.\n\n')
    f.write('You got ' + str(HMscore) + ' points for the hygiene.\n')
    f.write('You got ' + str(EMscore) + ' points for the exercise you did.\n')
    f.write('You got ' + str(MMscore) + ' points for the mindfulness you practiced.\n')
    if weight == 0:
        f.write('You didn\' yourself this morning.')
    else:
        f.write('Your weight: ' + str(weight) + '.\n')
    
    TotalMR = wakeUpScore + HMscore + EMscore + MMscore
    
    return TotalMR