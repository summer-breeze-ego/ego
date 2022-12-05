# CREATION OF PROFILE

# NAME
print('HEAR ME OUT MOTHERFUCKER!\nI AM YOUR EGO! YOUR INNER SOUL!\nLet\'s get acquainted.')
Fname = input('What\'s your first name? ')
Lname = input('Last name? ')
username = input('What do you prefer being called?\n')
print('Hello, ' + username + '!\n')

# AGE
dateBirth = input('What\'s your date of birth? (format: ddmmyyyy)\n')
print("Damn, you're getting old...\n")

# writing data to file
try:
    f = open('./' + username + "Profile.txt", mode = 'w', encoding = 'utf-8')

    f.write('|------------------------------------|\n|------------< PROFILE >-------------|\n|------------------------------------|\n\n')
    f.write('First Name: ' + Fname + '\n')
    f.write('Last Name: ' + Lname + '\n')
    f.write('Username: ' + username + '\n')
finally:
    f.close()