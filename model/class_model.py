

class Classroom:
    def __init__(self, class_id, name, room, owner_id):
        self.class_id = class_id
        self.name = name
        self.room = room
        self.owner_id = owner_id


def from_json(json):
    return Classroom(json['id'], json['name'], json['room'], json['ownerId'])
