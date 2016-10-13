import unittest
from bowling_scorer import Bowling_Scorer

class Test_Bowling(unittest.TestCase):
	
	def test1(self):
		#Simulation of a perfect game
		string_to_test = "XXXXXXXXXXXX"
		act_score = 300
		bowler = "test1"
		
		test = Bowling_Scorer()
		test.iterate_through_rolls(string_to_test)
		self.assertEqual(act_score, test.score)
		print(bowler + " got a score of " + str(test.score))


	def test2(self):
		#Simulation of a game where bowler only gets 9 pins per frame
		string_to_test = "9-9-9-9-9-9-9-9-9-9-"
		act_score = 90
		bowler = "test2"
		
		test = Bowling_Scorer()
		test.iterate_through_rolls(string_to_test)
		self.assertEqual(act_score, test.score)
		print(bowler + " got a score of " + str(test.score))

		
	def test3(self):
		#Simulation of game where bowler gets 5 pins per roll
		string_to_test = "5/5/5/5/5/5/5/5/5/5/5"
		act_score = 150
		bowler = "test3"
		
		test = Bowling_Scorer()
		test.iterate_through_rolls(string_to_test)
		self.assertEqual(act_score, test.score)
		print(bowler + " got a score of " + str(test.score))
		
	def test4(self):
		#Simulation of a game where bolwer gets a mix of strikes,
		#spares, partials, and misses
		string_to_test = "X7/9-X-88/-6XXX81"
		act_score = 167
		bowler = "test4"
		
		test = Bowling_Scorer()
		test.iterate_through_rolls(string_to_test)
		self.assertEqual(act_score, test.score)
		print(bowler + " got a score of " + str(test.score))

unittest.main()
