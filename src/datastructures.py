from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {"id": 1, "first_name": "John", "last_name": "Jackson", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "last_name": "Jackson", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "last_name": "Jackson", "age": 5, "lucky_numbers": [1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name  # Asegura que siempre sea "Jackson"
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return True
        return False

    def update_member(self, id, updated_member):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members[i].update(updated_member)
                self._members[i]["last_name"] = self.last_name  # Asegura que siempre sea "Jackson"
                return self._members[i]
        return None

    def get_member(self, id):
        return next((m for m in self._members if m["id"] == id), None)

    def get_all_members(self):
        return self._members
