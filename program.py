import time

class Cardio:
	def __init__(self, name, minutes, intensity):
		self.name = name
		self.seconds = minutes * 60
		self.intensity = intensity

	def print(self):

		name = f'{self.name}'.ljust(45, "-")
		intensity = f'Int:{self.intensity}'.ljust(47, "-")
		total = time.strftime("%H:%M:%S", time.gmtime(self.seconds))
		
		print(f'{name}{intensity}{total}')

crun = Cardio("Run", 15, "Moderate")
cbike = Cardio("Bike", 15, "Moderate")
cwalk = Cardio("Walk", 25, "Low")
chiit = Cardio("Bike", 15, "HIIT")
crest = Cardio("Rest", 0, "Rest")

class Stretch:
	def __init__(self, group, name, hold, unilateral=False, rest=5):
		self.group = group
		self.name = name
		self.hold = hold
		self.unilateral = unilateral
		self.rest = rest

	@property
	def time(self):
		if self.unilateral:
			return (self.hold + self.rest) * 2
		else:
			return self.hold + self.rest

	def print(self):

		group = f'{self.group}'.lower().ljust(10)
		name = f'{self.name}'.ljust(35, ".")
		hold = f'Hold:{self.hold}'.ljust(10)
		unilateral = f'Unilateral:{"Yes" if self.unilateral else "No"}'.ljust(30)
		rest = f'Rest:{self.rest}'.ljust(10)
		total = time.strftime("%M:%S", time.gmtime(self.time))

		print(f'{group}{name}{hold}{rest}{unilateral}{total}')


class StretchingRoutine:
	def __init__(self, name, stretches, repeat=1):
		self.name = name
		self.stretches = stretches
		self.repeat = repeat

	@property
	def time(self):
		total = 0

		for stretch in self.stretches:
			total += stretch.time
		
		return total * self.repeat
	
	def print(self):
		self.printDetails()
		for stretch in self.stretches:
			stretch.print()
		print(f'Repeat x{self.repeat}'.center(100, "-"))

	def printDetails(self):
		print(f'{self.name}'.ljust(92, "-") + f'{time.strftime("%H:%M:%S", time.gmtime(self.time))}')

s1 = StretchingRoutine("Full Body Stretch A", [
	Stretch("calf", "Gastrocnemius stretch", 30, True),
	Stretch("calf", "Shin stretch", 30),
	Stretch("biceps", "Standing biceps stretch", 30),
	Stretch("shoulders", "Cross body shoulder stretch", 30, True),
	Stretch("back", "Cobra stretch", 30),
	Stretch("chest", "Wall chest stretch", 30, True),
	Stretch("hips", "Pigeon stretch", 30, True),
	Stretch("quads", "Standing quad stretch", 30, True),
	Stretch("hamstring", "Strap assisted lying ham", 30, True),
], 2)

s2 = StretchingRoutine("Full Body Stretch B", [
	Stretch("calf", "Soleus stretch", 30, True),
	Stretch("triceps", "OH triceps", 30, True),
	Stretch("biceps", "Standing biceps stretch", 30),
	Stretch("hamstring", "Standing hamstring", 30),
	Stretch("shoulders", "Cross body shoulder stretch", 30, True),
	Stretch("back", "Child's pose", 30),
	Stretch("glutes", "Supine figure 4 glute stretch", 30, True),
	Stretch("quads", "Standing quad stretch", 30, True),
	Stretch("hips", "Standing hip stretch", 30, True),
], 2)

class Exercise:
	def __init__(self, group, name, sets, reps, rest=120, intensity=7.5, tempo=[3, 1, 2]):
		self.group = group
		self.name = name
		self.sets = sets
		self.reps = reps
		self.rest = rest
		# Value 1 to 10
		self.intensity = intensity
		# [eccentric phase, squeeze, concentric phase] in seconds
		self.tempo = tempo
	
	@property
	def tut(self):
		return self.reps * sum(self.tempo)

	@property
	def time(self):
		return self.tut * self.sets + self.sets * self.rest
	
	def printExercise(self):
		group = f'{self.group}'.lower().ljust(10)
		name = f'{self.name}'.ljust(35, ".")
		vol = f'{self.sets}x{self.reps}'.ljust(6)
		rest = f'Rest:{self.rest}'.ljust(10)
		tut = f'TUT:{self.tut}'.ljust(9)
		intensity = f'Int:{self.intensity}'.ljust(15)
		tempo = f'Tempo:{self.tempo}'.ljust(20)

		print(f'{group}{name}{vol}{rest}{tut}{intensity}{tempo}')
	
class Workout:
	def __init__(self, name, exercises):
		self.name = name
		self.exercises = exercises
	
	@property
	def time(self):
		total = 0

		for exercise in self.exercises:
			total += exercise.time
		
		return total
	
	def printWorkout(self):
		self.printDetails()
		for exercise in self.exercises:
			exercise.printExercise()
	
	def printDetails(self):
		print(f'{self.name}'.ljust(92, "-") + f'{time.strftime("%H:%M:%S", time.gmtime(self.time))}')

class Routine:
	def __init__(self, name, workouts, stretches, cardios):
		self.name = name
		self.workouts = workouts
		self.stretches = stretches
		self.cardios = cardios
	
	def details(self):
		for i in range(7):
			print(f'Day {i+1}'.upper().center(100, "-"))

			self.workouts[i].printWorkout()
			self.stretches[i].print()
			self.cardios[i].print()
	
	def printDay(self, day):
		if day in range(1, 8):
			self.workouts[day-1].printWorkout()
			self.stretches[day-1].print()
			self.cardios[day-1].print()
		else:
			print("Day does not exist")
			
	@property
	def volume(self):
		vol = {
			"chest": {"sets": 0, "reps": 0},
			"shoulders": {"sets": 0, "reps": 0},
			"triceps": {"sets": 0, "reps": 0},
			"back": {"sets": 0, "reps": 0},
			"biceps": {"sets": 0, "reps": 0},
			"calves": {"sets": 0, "reps": 0},
			"abs": {"sets": 0, "reps": 0},
			"legs": {"sets": 0, "reps": 0},
		}

		for workout in self.workouts:
			for exercise in workout.exercises:
				vol[exercise.group]["sets"] += exercise.sets
				vol[exercise.group]["reps"] += exercise.sets * exercise.reps
		
		return vol

	def printVolume(self):
		for key, value in self.volume.items():
			name = f'{key.lower()}'.ljust(20)
			sets = f'sets:{value["sets"]}'.ljust(20)
			reps = f'reps:{value["reps"]}'
			print(f'{name}{sets}{reps}')
	
	def printSchema(self):
		for i in range(7):
			print(f'Day {i+1}'.upper())

			self.workouts[i].printDetails()
			self.stretches[i].printDetails()
			self.cardios[i].print()

			totalTime = self.workouts[i].time + self.stretches[i].time + self.cardios[i].seconds

			print(f'Total Time: {time.strftime("%H:%M:%S", time.gmtime(totalTime))}'.rjust(100))

push = Workout("Push", [
		Exercise("chest", "bench press", 3, 12),
		Exercise("abs", "decline situp", 3, 12),
		Exercise("chest", "incline dumbbell press", 3, 12),
		Exercise("triceps", "triceps rope pushdown", 3, 12),
		Exercise("chest", "chest fly", 2, 12),
		Exercise("triceps", "triceps cable extension", 2, 12),
		Exercise("abs", "machine crunch", 2, 12),
	])

pull = Workout("Pull", [
		Exercise("back", "pull up", 4, 12),
		Exercise("shoulders", "rear delt fly", 2, 12),
		Exercise("back", "bent over row", 3, 12),
		Exercise("biceps", "incline curl", 3, 12),
		Exercise("back", "lat pulldown", 2, 12),
		Exercise("biceps", "cable curl", 2, 12),
		Exercise("shoulders", "reverse fly single arm cable", 2, 12),
	])
	
legs = Workout("Legs", [
		Exercise("legs", "squat", 3, 12),
		Exercise("calves", "Calf press", 3, 12),
		Exercise("legs", "leg press", 3, 12),
		Exercise("calves", "seated calf raise", 2, 10),
		Exercise("shoulders", "dumbbell shoulder press", 3, 12),
		Exercise("legs", "leg curl", 2, 12),
		Exercise("shoulders", "lateral dumbbell raise", 2, 12),
	])

rest = Workout("Rest", [])


r = Routine("Push/Pull/Shoulders/Legs", [
	push, pull, legs, rest, push, pull, legs
], [
	s1, s2, s1, s2, s1, s2, s1
], [
	crun, cbike, cwalk, crest, chiit, crun, cwalk
])

def helpMenu():
	print("Commands")
	print(f'\thelp'.ljust(20) + "Display help menu")
	print(f'\texit'.ljust(20) + "Exit program")
	print(f'\tday [1-7]'.ljust(20) + "Display plan for given day")
	print(f'\tvolume'.ljust(20) + "Display total weekly volume")
	print(f'\tschema'.ljust(20) + "Show schedule for week")
	print(f'\tweek'.ljust(20) + "Show schedule for whole week")
	print("Vocab")
	print(f'\tTUT'.ljust(20) + "Time under tension")
	print(f'\tTempo'.ljust(20) + "[eccentric phase, squeeze, concentric phase]")
	print(f'\tUnilateral'.ljust(20) + "One side of body at a time")
	print(f'\tInt'.ljust(20) + "Short for intensity")

def main():
	while True:
		command = input("> ").lower().strip()
		if command == "exit":
			break
		elif command == "help":
			helpMenu()
		elif command == "":
			print("command not recognized, try help")
		elif command.split()[0] == "day":
			if len(command.split()) == 2:
				arg = command.split()[1]
				if command.split()[1].isnumeric():
					arg = int(arg)
					if (arg in range(1, 8)):
						r.printDay(arg)
					else:
						print(f'invalid argument {arg}')
				else:
					print(f'invalid argument {arg}')
			else:
				print("no argument given")
		elif command == "volume":
			r.printVolume()
		elif command == "schema":
			r.printSchema()
		elif command == "week":
			r.details()
		else:
			print("command not recognized, try help")

if __name__ == "__main__":
	main()