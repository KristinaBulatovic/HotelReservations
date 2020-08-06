import rooms


def create_hotel(rooms_num=0):
    days = 365
    no_of_rooms = rooms_num
    if no_of_rooms == 0:
        no_of_rooms = int(input('Number of rooms: '))
    if no_of_rooms > 1000:
        print('The number of rooms cannot exceed 1000!')
        return create_hotel()

    hotel = [[0 for j in range(days)] for i in range(no_of_rooms)]
    return hotel


def booking_room(all_rooms, start_date, end_date):
    if start_date < 0 or end_date > 365:
        # print('Start date and end date must be between 0 and 365!')
        return 'Declined'

    free_rooms = rooms.find_free_rooms(all_rooms, start_date, end_date)

    if len(free_rooms) == 0:
        # print('There are currently no rooms available.')
        return 'Declined'

    if len(free_rooms) > 0:
        best_room = rooms.find_best_room(free_rooms, start_date)
        for i in range(start_date, end_date + 1):
            best_room[i] = 'X'
        # print('Reservation is accepted!')
        return 'Accepted'


def main():
    hotel = create_hotel()

    while True:
        print(
            """
            Options:
            1 - Booking
            2 - Show all bookings
            0 - Exit
            """
        )
        option = int(input('option: '))

        if option == 0:
            break

        if option == 1:
            start = int(input('start date: '))
            end = int(input('end date: '))

            status = booking_room(hotel, start, end)
            print('\n', status)

        if option == 2:
            for i in hotel:
                print(i)


if __name__ == "__main__":
    main()
