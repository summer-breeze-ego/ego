import time
import os
from datetime import date
from MorningRoutineSS import morningRoutine

# time TITLE
def time2title():
    today = date.today()
    D = today.strftime("%d ")
    M = (today.strftime("%B ")).upper()
    Y = today.strftime("%Y")

    title = D + M + Y

    return title

# |------------------------------------|
# |----------< MAIN PROGRAM >----------|
# |------------------------------------|

# import time for file name
timestr = time.strftime("%Y%m%d")
filename = timestr + ".txt"

# writing data to file
try:
    f = open(filename, mode = 'w', encoding = 'utf-8')
    todayDate = time2title()

    # write date to file
    f.write("|----------< " + todayDate + " >----------|\n\n") 

    totalScore = morningRoutine(f)

    # write TOTAL SCORE to file
    f.write("\nTOTAL SCORE: " + str(totalScore))

    # moving daily score file into the daily scores folder
    os.system(f"mv {filename} Daily_Scores")
finally:
    f.close()