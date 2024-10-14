class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, obj):
        cls.hall_list.append(obj)

class Hall (Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        super().entry_hall(self)

    def entry_show (self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))

        seat = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]

        self.__seats[id] = seat
    
    def book_seats (self, id, seat_list):
        if id not in self.__seats:
            raise ValueError('Invalid Show ID')

        for seat in seat_list:
            row, col = seat

            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                raise ValueError(f'Invalid Seat')
            if self.__seats[id][row][col] == 'Booked':
                raise ValueError(f'This Seat ({row}, {col}) is already booked')

            self.__seats[id][row][col] = 'Booked'

    def view_show_list (self):
        print('Show List:')
        for show in self.__show_list:
            print(f'Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}')

    def view_available_seats (self, id):
        if id not in self.__seats:
            raise ValueError("Invalid show ID")

        print(f'Available seats for show ID {id}:')
        for row in range(self.__rows):
            for col in range(self.__cols):
                status = self.__seats[id][row][col]
                print(f'({row}, {col}): {status}')

    def __repr__(self):
        return (f'Hall No: {self.__hall_no}, Rows: {self.__rows}, Columns: {self.__cols}, Show List: {self.__show_list}')


def cinema_system ():
    hall1 = Hall(5, 4, 1)

    hall1.entry_show('101', 'Spider Man', '5:00 PM')
    hall1.entry_show('102', 'Bat Man', '3:00 PM')
    hall1.entry_show('103', 'Iron Man', '10:00 AM')

    while True:
        print('1. VIEW ALL SHOW FOR TODAY')
        print('2. VIEW AVAILABLE SEATS')
        print('3. BOOK TICKET')
        print('4. EXIT')

        option = input('ENTER OPTION: ')

        if option == '1':
            hall1.view_show_list()
            print('----------------')

        elif option == '2':
            show_id = input('Enter the show ID: ')

            try:
                hall1.view_available_seats(show_id)
            except ValueError as e:
                print(e)

            print('----------------')

        elif option == '3':
            show_id = input('Enter the show ID: ')
            seats_to_book = []
            num_seats = int(input('Number of Ticket? : '))

            for _ in range(num_seats):
                row = int(input('Enter Seat Row: '))
                col = int(input('Enter Seat Col: '))
                seats_to_book.append((row, col))

            try:
                hall1.book_seats(show_id, seats_to_book)
                print(f'Successfully booked seat {seats_to_book} for Show ID {show_id}')
            except ValueError as e:
                print(e)

            print('----------------')

        elif option == '4':
            break

        else:
            print('Invalid Option. Please select a valid option')
            print('----------------')


cinema_system()