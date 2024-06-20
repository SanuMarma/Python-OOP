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

    def __repr__(self) -> str:
        return f'rows: {self.rows}, cols: {self.cols}, hall_no: {self.hall_no}'

hall = Hall(5, 4, 1)

print(hall.hall_list)