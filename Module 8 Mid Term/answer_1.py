
class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def __repr__(self) -> str:
        return f'rows: {self.rows}, cols: {self.cols}, hall_no: {self.hall_no}'


hallCinema = Star_Cinema()
hall = Hall(5, 4, 1)
hallCinema.entry_hall(hall)

print(hallCinema.hall_list)
