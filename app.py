import sys
from config import DB_DETAILS

<<<<<<< HEAD
=======
from util import get_tables

>>>>>>> Added to read table list that needs to be loaded from a file

def main():
    """Program take atleast one argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
<<<<<<< HEAD
    print(db_details)
=======
    tables = get_tables('table_list')
    for table in tables['table_name']:
        print(table)
>>>>>>> Added to read table list that needs to be loaded from a file


if __name__=='__main__':
    main()