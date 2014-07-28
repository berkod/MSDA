__author__ = 'dberko'

import sqlite3

def createTables(cursor):
    sql = (
        '''CREATE TABLE IF NOT EXISTS colors ("id"  INTEGER PRIMARY KEY AUTOINCREMENT, "name", "pantone");''',
        '''CREATE TABLE IF NOT EXISTS paintstock ("id"  INTEGER PRIMARY KEY AUTOINCREMENT, "pantone", "finish", "size");''',
    )
    for s in sql:
        cursor.execute(s)
    inserts = (
        ''' INSERT INTO colors (name, pantone) VALUES ('Radiant Orchid', '18-3224'),
         ('Emerald', '17-5641'),
         ('Tangerine Tango', '17-1463'),
         ('Honeysuckle', '18-2120'),
         ('Turquoise', '15-5519'),
         ('Mimosa', '14-0848'),
         ('Blue Iris', '18-3943'),
         ('Chili Pepper', '19-1557'),
         ('Sand Dollar', '13-1106'),
         ('Blue Turquoise', '15-5217'),
         ('Tigerlily', '17-1456'),
         ('Aqua Sky', '14-4811'),
         ('True Red', '19-1664'),
         ('Fuchsia Rose', '17-2031'),
         ('Cerulean', '15-4020');''',
        '''INSERT INTO paintstock (pantone, finish, size) VALUES  ('17-1456', 'eggshell', 'quart'),
                ('14-4811', 'eggshell', 'quart'),
                ('19-1664', 'eggshell', 'quart'),
                ('17-2031', 'eggshell', 'quart'),
                ('17-1456', 'flat', '1 gallon'),
                ('14-4811', 'flat', '1 gallon'),
                ('19-1664', 'flat', '1 gallon'),
                ('17-2031', 'flat', '1 gallon'),
                ('17-1456', 'glossy', '1 gallon'),
                ('14-4811', 'glossy', '1 gallon'),
                ('19-1664', 'glossy', '1 gallon'),
                ('17-2031', 'glossy', '1 gallon'),
                ('17-1456', 'glossy', '5 gallon'),
                ('14-4811', 'glossy', '5 gallon'),
                ('19-1664', 'glossy', '5 gallon'),
                ('17-2031', 'glossy', '5 gallon');'''
    )
    for s in inserts:
        cursor.execute(s)

def retrieveData( cursor ):
    one_gallons = cursor.execute('''SELECT colors.name, paintstock.finish from colors join paintstock on colors.pantone=paintstock.pantone where size='1 gallon' order by colors.name, paintstock.finish;''')
    print("COLOR NAME\t|\tFINISH\n")
    for gallon in one_gallons:
        print("%s\t|\t%s\n" % gallon)

if __name__ == '__main__':
    conn = sqlite3.connect('week8.db')
    cursor = conn.cursor()
    # Comment out the next two lines to not duplicate rows.
    # Better would obviously be to validate data on inserts.
    createTables(cursor)
    conn.commit()

    retrieveData(cursor)