

DATABASE = "profile_database.txt"

# function to check if username is available
def username_availability(username: str) -> bool:
    """Function checks if username is available in text file aka database.

    Args:
        username (str): username

    Returns:
        bool: username availability.
    """

    # starting file management
    try:
        # opening file
        database_file = open(DATABASE, 'r')

        # extracting lines
        lines = database_file.readlines()

        # looping through lines from database
        for line in lines:
            name = line.split(' : ')[0] # spliting line and extracting username

            # if username already exists
            if name == username:
                return False

    finally:
        database_file.close()

    return True

# function to write details in database file