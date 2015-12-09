class Particle:
	'Class defining what a particle is by mass, x_pos and y_pos'
	
	def __init__(self, mass, x, y):
		self.mass = mass
		self.x = x
		self.y = y

	def displayInfo(self):
		print("Mass: {} X-Pos: {} Y-Pos: {}".format(\
 str(self.mass), str(self.x), str(self.y)))


""" partDefine() defines a particle based on mass, x, and y position."""
def partDefine():
	while True:
		part_in = str(input("Please input a set of three\
 numbers. The first should be mass, 2nd is x-position,\
  3rd is y-position: "))
		part_process = part_in.split()
		particle = Particle(int(part_process[0]), \
int(part_process[1]), int(part_process[2]))
		print("Particle: ")
		particle.displayInfo()
		
		if str(input("Is this information correct? (y/n)")) == "y":
			break
	return particle

""" distance(part1, part2) consumes two particles and produces a number
corresponds to the distance between those two particles."""
def distance(part1, part2):
	return ((((part2.x - part1.x)**2) + ((part2.y - part1.y) ** 2))\
**(1/2))

""" main() consumes two inputs in row form. Each row must have three
	numbers. The first represents a particle's mass, second represents
	particle x-position, and third represents particle y-position.
	The repulsion is determined by a formula represented as such:
	repul = (mass of 1 * mass of 2) / (distance ^ 2) """
def main():
	while True:
		particle1 = partDefine()
		particle2 = partDefine()

		print("Repulsion force is...")
		print(str(((particle1.mass * particle2.mass) / \
distance(particle1, particle2))))

		if (input("Do you wish to continue? (y/n)")) == "n":
			break
		
main()
