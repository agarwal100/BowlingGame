import BowlingGame
import unittest

class TestBowlingGame(unittest.TestCase):

	def setUp(self):
		self.myScore = BowlingGame.BowlingGame()
		self.myScore2 = BowlingGame.BowlingGame()
		self.myScore3 = BowlingGame.BowlingGame()
		# self.myScore4 = BowlingGame.BowlingGame()

	def test_scoreRolls(self):
		self.myScore.addRoll(4)
		self.assertEquals(self.myScore.getScore(),4)
		self.myScore.addRoll(3)
		self.assertEquals(self.myScore.getScore(),7)
		self.myScore.addRoll(6)
		self.myScore.addRoll(0)
		self.assertEquals(self.myScore.getScore(),13)

	def test_scoreSpare(self):
		"""This function tests interactions of spares"""
		#spare and then one roll inProgress
		self.myScore.addRoll(4)
		self.myScore.addRoll(6)
		self.assertEquals(self.myScore.getScore(),0) #cannot score spare until next roll
		self.myScore.addRoll(3)
		self.assertEquals(self.myScore.getScore(),16)

		#spare and then one complete frame
		self.myScore.addRoll(6)
		self.assertEquals(self.myScore.getScore(),22)

		#spare and then more than one frame, last frame is inProgress
		
		self.myScore.addRoll(3)
		self.myScore.addRoll(3)
		self.myScore.addRoll(6)

		self.assertEquals(self.myScore.getScore(),34)

		#spare and then more than one frame, last frame is not inProgress(complete)
		self.myScore.addRoll(7)
		self.assertEquals(self.myScore.getScore(),41)


		#normal frames and then spare and then one roll inProgress
		self.myScore2.addRoll(4)
		self.myScore2.addRoll(5) 
		self.myScore2.addRoll(3)
		self.myScore2.addRoll(7)
		self.assertEquals(self.myScore2.getScore(),9)
		self.myScore2.addRoll(3)
		self.assertEquals(self.myScore2.getScore(),25)

		#normal frames and then spare and then normal frame
		self.myScore2.addRoll(0)
		self.assertEquals(self.myScore2.getScore(),25)

	def test_scoreStrike(self):
		"""This function tests interactions strikes"""
		#strike and then one roll inProgress
		self.myScore.addRoll(10)
		self.assertEquals(self.myScore.getScore(),0) #cannot score strike until next 2 rolls
		self.myScore.addRoll(3)
		self.assertEquals(self.myScore.getScore(),3) #cannot score strike until next roll
		
		#strike and then one complete frame
		self.myScore.addRoll(3)
		self.assertEquals(self.myScore.getScore(),22)

		#strike and then more than one frame, last frame is inProgress
		self.myScore.addRoll(3)
		self.myScore.addRoll(3)
		self.myScore.addRoll(6)

		self.assertEquals(self.myScore.getScore(),34)

		#strike and then more than one frame, last frame is not inProgress(complete)
		self.myScore.addRoll(1)
		self.assertEquals(self.myScore.getScore(),35)	

		#normal frames and then spare and then one roll inProgress
		self.myScore2.addRoll(4)
		self.myScore2.addRoll(5) 
		self.myScore2.addRoll(10)
		self.assertEquals(self.myScore2.getScore(),9)
		self.myScore2.addRoll(3)
		self.assertEquals(self.myScore2.getScore(),12)

		#normal frames and then spare and then normal frame
		self.myScore2.addRoll(1)
		self.assertEquals(self.myScore2.getScore(),27)

	def test_scoreSpareNStrike(self):
		"""This function tests interactions of spares and strikes"""

		#strike and then spare
		self.myScore.addRoll(10)
		self.myScore.addRoll(3)
		self.myScore.addRoll(7)
		self.assertEquals(self.myScore.getScore(),20) #cannot score spare until next roll
		self.myScore.addRoll(3)
		self.assertEquals(self.myScore.getScore(),36)
		
		#spare and then strike
		self.myScore2.addRoll(6)
		self.myScore2.addRoll(4)
		self.myScore2.addRoll(10)
		self.assertEquals(self.myScore2.getScore(),20)
		self.myScore2.addRoll(6)
		self.myScore2.addRoll(1)
		self.assertEquals(self.myScore2.getScore(),44)

		#strike, strike, stike
		self.myScore3.addRoll(10)
		self.myScore3.addRoll(10)
		self.myScore3.addRoll(10)
		self.assertEquals(self.myScore3.getScore(),30)
		self.myScore3.addRoll(3)
		self.assertEquals(self.myScore3.getScore(),56)
		self.myScore3.addRoll(3)
		self.assertEquals(self.myScore3.getScore(),75)
	
	def test_gameLength(self):
		"""This function tests that the game ends properly"""
		#frame 10 is strike, so accepts 2 more rolls
		self.myScore.addRoll(10)#frame #1
		self.myScore.addRoll(10)#2
		self.myScore.addRoll(10)#3
		self.myScore.addRoll(10)#4
		self.myScore.addRoll(10)#5
		self.myScore.addRoll(10)#6
		self.myScore.addRoll(10)#7
		self.myScore.addRoll(10)#8
		self.myScore.addRoll(10)#9
		self.myScore.addRoll(10)#10
		self.myScore.addRoll(10)# fill ball 1
		self.myScore.addRoll(10)# fill ball 2
		self.assertEquals(self.myScore.getScore(),300)#make sure this is 300, the max possible score

		self.myScore.addRoll(10)# should not actually add, game is over
		self.assertEquals(self.myScore.getScore(),300)#make sure this does not change 
		self.assertEquals(len(self.myScore.rolls),12)#make sure this does not change 
		

		#frame 10 is spare, so accepts 1 more roll
		self.myScore2.addRoll(10)#frame #1
		self.myScore2.addRoll(10)#2
		self.myScore2.addRoll(10)#3
		self.myScore2.addRoll(10)#4
		self.myScore2.addRoll(10)#5
		self.myScore2.addRoll(10)#6
		self.myScore2.addRoll(10)#7
		self.myScore2.addRoll(10)#8
		self.myScore2.addRoll(10)#9
		self.myScore2.addRoll(5)#10a
		self.myScore2.addRoll(5)#10b
		self.myScore2.addRoll(4)# fill ball 1
		self.assertEquals(self.myScore2.getScore(),269)

		self.myScore2.addRoll(2)# should not actually add, game is over
		self.assertEquals(self.myScore2.getScore(),269)#make sure this does not change 
		self.assertEquals(len(self.myScore2.rolls),11)#make sure this does not change
		
	
		#frame 10 is an open frame, so does not accept another roll
		self.myScore3.addRoll(10)#frame #1
		self.myScore3.addRoll(10)#2
		self.myScore3.addRoll(10)#3
		self.myScore3.addRoll(10)#4
		self.myScore3.addRoll(10)#5
		self.myScore3.addRoll(10)#6
		self.myScore3.addRoll(10)#7
		self.myScore3.addRoll(10)#8
		self.myScore3.addRoll(10)#9
		self.myScore3.addRoll(5)#10a
		self.myScore3.addRoll(4)#10b
		self.assertEquals(self.myScore3.getScore(),263)

		self.myScore3.addRoll(2)# should not actually add, game is over
		self.assertEquals(self.myScore3.getScore(),263)#make sure this does not change 
		self.assertEquals(len(self.myScore3.rolls),10)#make sure this does not change
		
	
		#self.assertRaises(IndexError,self.myScore2.addRoll,[10])
if __name__ == '__main__':
	unittest.main()