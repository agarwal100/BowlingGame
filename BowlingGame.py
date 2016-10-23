class BowlingGame(object):

	def __init__(self):
		self.score = 0
		self.rolls = []
		self.inProgress = False

	def __str__(self):
		stringRep = ""
		for roll in self.rolls:
			stringRep = stringRep + str(roll[0]) 
			if len(roll) == 2:
				stringRep = stringRep + str(roll[1]) 
		return stringRep		

	def getScore(self):
		return self.score

	def startOver(self):
		#if user wants to play another game
		self.score = 0
		self.rolls = []
		self.inProgress = False

	def addRoll(self,pinsDown):
		if pinsDown == 10:
			if self.inProgress == True: #spare not strike
				self.rolls[-1].append('/')
				self.inProgress = not self.inProgress
			else: #strike
				self.rolls.append(['X'])

		else:	
			if self.inProgress == True: #second roll
				lastRoll = self.rolls[-1][0]
				rollToAdd = pinsDown - lastRoll
				self.rolls[-1].append(rollToAdd)
			else: #first roll
				self.rolls.append([pinsDown])
		
			self.inProgress = not self.inProgress 

		BowlingGame.updateScore(self)

	def updateScore(self):
		for i in range(len(self.rolls)):
			frame = self.rolls[i]
			newScore = 0

			if frame[0] == 'X': #strike
				if i < len(self.rolls-1):
					nextFrame = self.rolls[i+1]
					if nextFrame[1] == 'X':
						newScore += 20
					else:	
						newScore += 10 + nextFrame[0] 
				if i < len(self.rolls-2):
					nextFrame = self.rolls[i+2]
					if secondNextFrame[2] == 'X':
						newScore += 10
					else:	
						newScore += secondNextFrame[0] 		
			elif len(frame) > 1 and frame[1] == '/': #spare
				if i < len(self.rolls-1):
					nextFrame = self.rolls[i+1]
					if nextFrame[1] == 'X':
						newScore += 20
					else:	
						newScore += 10 + nextFrame[0] 

			else:
				newScore += sum(frame)

		self.score = newScore		


##################
#######TESTS
##################
import unittest
########
#addRoll
########
myScore = BowlingGame()
myScore.addRoll(4)
assertEqual(myScore,4)

		