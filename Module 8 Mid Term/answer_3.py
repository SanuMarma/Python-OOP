class Star_Cinema():
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        seats_arr = [[0 for i in range(self.cols)] for j in range(self.rows)]

        self.seats[id] = seats_arr

        for row in seats_arr:
            print(row)


hall = Hall(5, 4, 1)
hall.entry_show(101, 'Jawan Maji', '10/06/2024 11:00 AM')