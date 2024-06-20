class Star_Cinema():
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
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


    def book_seats(self, id, seat_info):

        if id in self.seats:
            seat = self.seats[id]
            row, col = seat_info
            if 0 <= row <= self.rows and 0 <= col <= self.cols:
                if seat[row][col] == 0:
                    seat[row][col] = 1
                    print(f'\n\tSeat {seat_info} booked Successfully..!')
                else:
                    print(f'\n\tSeat {seat_info} is already booked !')
            else:
                print(f'\n\tSorry! {seat_info} Seat is out of boundary !')
        else:

            print(f'\n\tShow Id: {id} is not found !')

    def view_show_list(self):
        for show in self.show_list:
            (id, movie_name, time) = show
           
            print(f'\n\t Show Id: {id}, Movie Name: {movie_name}, Time: {time} ')

hall = Hall(5, 4, 1)
hall.entry_show(101, 'Jawan Maji', '10/06/2024 11:00 AM')
hall.entry_show(102, 'Sujon Maji', '10/06/2014 3:00 PM')
hall.entry_show(103, 'Mon Majhi', '10/06/2024 6:00 PM')

hall.view_show_list()