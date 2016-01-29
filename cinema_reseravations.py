import sqlite3


class Cinema_Reservation_System:

    def __init__(self):
        self.con = sqlite3.connect("cinema_data.db")
        self.c = self.con.cursor()

    def create_table(self):

        try:
            self.c.execute('''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY,
                                                  name TEXT,
                                                  rating REAL)''')

            movie_data = [(1, 'The Hunger Games: Catching Fire', 7.9),
                          (2, 'Wreck-It Ralph', 7.8),
                          (3, 'Her', 8.3), ]

            self.c.executemany('INSERT INTO movies VALUES (?, ?, ?)',
                               movie_data)

        except:
            None

        try:
            self.c.execute('''CREATE TABLE IF NOT EXISTS projections(id INTEGER,
                                                       movie_id INTEGER,
                                                       type TEXT,
                                                       date TEXT,
                                                       time TEXT,
                                                       FOREIGN KEY(movie_id) REFERENCES movies(id))''')

            projection_data = [(1, 1, '3D', '2014-04-01', '19:10'),
                               (2, 1, '2D', '2014-04-01', '19:00'),
                               (3, 1, '4DX', '2014-04-02', '21:00'),
                               (4, 3, '2D', '2014-04-05', '20:20'),
                               (5, 2, '3D', '2014-04-02', '22:00'),
                               (6, 2, '2D', '2014-04-02', '19:30'), ]

            self.c.executemany(
                'INSERT INTO projections VALUES (?, ?, ?, ?, ?)',
                projection_data)

        except:
            None

        try:
            self.c.execute('''CREATE TABLE IF NOT EXISTS reservations(id INTEGER PRIMARY KEY,
                                                        username TEXT,
                                                        projection_id INTEGER,
                                                        row INTEGER,
                                                        colomn INTEGER,
                                                        FOREIGN KEY(projection_id) REFERENCES projections(id))''')

            reservation_data = [(1, "RadoRado", 1, 2, 1),
                                (2, "RadoRado", 1, 3, 5),
                                (3, "RadoRado", 1, 7, 8),
                                (4, "Ivo", 3, 1, 1),
                                (5, "Ivo", 3, 1, 2),
                                (6, "Mysterious", 5, 2, 3),
                                (7, "Mysterious", 5, 2, 4), ]

            self.c.executemany(
                'INSERT INTO reservations VALUES (?, ?, ?, ?, ?)',
                reservation_data)

        except:
            None

    def show_movies(self):
        cursor = self.con.execute(
            "SELECT id, name, rating FROM movies ORDER BY rating ASC")

        print("Current movies:")

        for row in cursor:
            print("[{}] - {} ({})".format(row[0], row[1], row[2]))

    def show_movie_projections(self, i):  # mine
        cursor_m = self.con.execute(
            "SELECT id, name FROM movies WHERE id = ?", (i, ))

        cursor = self.con.execute(
            "SELECT id, movie_id, type, date, time FROM projections WHERE movie_id = ?", (i, ))

        for row in cursor_m:
            print("{} {}".format(row[0], row[1]))

        for row in cursor:
            print("{} {} {} {}".format(row[0], row[1], row[2], row[3]))

    def make_reservation(self):
        n = input("Choose name> ")
        if n != "":
            ticket = input("Choose number of tickets> ")
            if int(ticket) > 0:
                self.show_movies()
                ID = input("Choose a movie> ")
                self.show_movie_projections(int(ID))
                proj = input("Choose a projection> ")
                self.show_movie_projections(int(proj))
                row = input("Choose a row>")
                column = input("Choose the number of the seat you want> ")
                self.matrix(int(row), int(column))

    def matrix(self, row, column):
        new_matrix = []

        result = []

        count = 0
        matrix = (" 0 1 2 3 4 5 6 7 8 9 10\
                1  . . . . . . . . . .\
                2  . . . . . . . . . .\
                3  . . . . . . . . . .\
                4  . . . . . . . . . .\
                5  . . . . . . . . . .\
                6  . . . . . . . . . .\
                7  . . . . . . . . . .\
                8  . . . . . . . . . .\
                9  . . . . . . . . . .\
                10 . . . . . . . . . .")

        for elem in matrix.split():
            count += 1
            new_matrix += [elem]
            if count == 11:
                result += [new_matrix]
                new_matrix = []
                count = 0

        r = result[row][column] = "X"
        print(result)
        return r

    def exit(self):
        self.con.close()


f = Cinema_Reservation_System()
f.create_table()
# f.show_movies()
# f.show_movie_projections(2)
f.make_reservation()
# f.matrix(1, 2)
