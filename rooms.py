def find_free_rooms(hotel, start_date, end_date):
    free_rooms = []
    for room in hotel:
        status = True
        for day in range(start_date, end_date + 1):
            # print room[day],
            if room[day] == 'X':
                status = False
                break
        if status:
            free_rooms.append(room)
        # print('')
    return free_rooms


def find_best_room(free_rooms, start_date):
    best_room = free_rooms[0]
    if start_date - 1 > 0:
        for i in free_rooms:
            if i[start_date - 1] == 'X':
                best_room = i
                break
    return best_room
