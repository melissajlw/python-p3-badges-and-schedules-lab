def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    rooms = []
    for i in range(len(names)):
        rooms.append(f"Hello, {names[i]}! You'll be assigned to room {i + 1}!")
    return rooms

def printer(names):
    rooms = assign_rooms(names)
    for name in names:
        print(f"Hello, my name is {name}.")
    for room in rooms:
        print(room)
