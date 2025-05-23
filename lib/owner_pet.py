class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return list of pets that belong to this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Check if pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet")
        # Set this owner as the pet's owner
        pet.owner = self

    def get_sorted_pets(self):
        # Return pets sorted by their names
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Initialize owner as None first
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of Owner")
            self.owner = owner

        # Add this pet instance to the class-level list
        Pet.all.append(self)
