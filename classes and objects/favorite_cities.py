class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

Toronto = City("Toronto", "Canada", 3000000, ["CN Tower", "Casa Loma", "Harbourfont Centre"])
NYC = City("NYC", "USA", 8000000, ["Empire State Building", "Statue of Liberty", ""])
LA = City("LA", "USA", 3000000, ["Hollywood Sign", "Walt Disney Concert Hall", "Griffith Observatory"])

print(vars(Toronto))
print(vars(NYC))
print(vars(LA))
