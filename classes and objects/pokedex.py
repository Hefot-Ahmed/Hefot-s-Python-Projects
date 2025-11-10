class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name + self.name)

  def display_details(self):
    print('Entry Number: ' + str (self.entry))
    print('Name: ' + (self.name)) 

pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)
charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)

pikachu.speak()
charizard.speak()
