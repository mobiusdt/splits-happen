class Bowling_Scorer():
	# Calculates the score from the points in each frame. Allows for
	# iteration through each roll, and sends a string to be calculated 
	# independently based on the value of the roll.
	def __init__(self):
		self.score = 0
		self.sub_score = 0

	def iterate_through_rolls(self, roll_string):
		#iterates through each roll provided and passes the appropriate
		#substring based on the value to the calc_substring method.
		for iterate, roll in enumerate(roll_string):
			if roll == "X":
				#make sure we are not on a bonus roll in the last frame
				if iterate < len(roll_string) - 3:
					self.calc_substring(
							roll_string[iterate:iterate + 3])
				#we are on a bonus roll, do not modify substring
				else:
					self.calc_substring(roll)
			elif roll == "/":
				#make sure we are not on a bonus roll in the last frame
				if iterate < len(roll_string) - 2:
					self.calc_substring(
							roll_string[iterate:iterate + 2])
				#we are on a bonus roll, do not modify substring
				else:
					self.calc_substring(roll)	
			else:
				self.calc_substring(roll)
		self.score += self.sub_score
		print("")
				
	def calc_substring(self, substring):
		#calculates the values for the substring provided by the
		#iterate_through_rolls method.
		for iterate, roll in enumerate(substring):
			if roll == "X":
				#add the score from previous roll's score, add ten,
				#reset previous roll score to 0
				self.score += self.sub_score + 10
				self.sub_score = 0
			elif roll == "/":
				#add ten to the score and reset previous roll score to 0
				self.score += 10
				self.sub_score = 0
			elif roll.isnumeric():
				#check if the substring is singular, add to score with
				#previous roll and replace previous roll score with
				#value from roll variable
				if len(substring) == 1:
					self.score += self.sub_score
					self.sub_score = int(roll)
				#check if we are before the end of the substring,
				#insert roll variable into previous roll variable
				elif iterate < len(substring) - 1:
					self.subscore = int(roll)
				#we are at end of substring, add roll variable to score
				#reset previous roll score to 0
				else:
					self.score += int(roll)
					self.sub_score = 0
			elif roll == "-":
				#add previous roll value to total score and reset to 0
				self.score += self.sub_score
				self.sub_score = 0
