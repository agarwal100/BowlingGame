class BowlingGame(object):

	def __init__(self):
		self.score = 0
		self.rolls = []
		self.inProgress = False
		self.gameOver = False

	def __str__(self):
		stringRep = ""
		for roll in self.rolls:
			stringRep = stringRep + "| "+ str(roll[0]) +" "
			if len(roll) == 2:
				stringRep = stringRep + str(roll[1]) 		
		return stringRep + " | "		

	def getScore(self):
		return self.score

	def startOver(self):
		#if user wants to play another game
		self.score = 0
		self.rolls = []
		self.inProgress = False
		self.gameOver = False

	def addRoll(self,pinsDown):
		# NOTE: pinsDown is the number of pins that have been knocked down on the current ROLL 
		# thus, if this is the second roll in the frame and the first roll knocked down 7 pins,
		# the max value of pinsDown is 3 because 10 is the total number of pins in a frame (3+7=10)
		
		#Only play 10 frames unless you need fill ball(s)
		
		# if self.gameOver:
		# 	raise IndexError#("Can't add roll after game is over. Try '.startOver'")		

		if (self.inProgress == True) and (self.gameOver == False): #second roll
			if self.rolls[-1][0] + pinsDown == 10:
				
				self.rolls[-1].append('/')
			else: #open frame
				
				self.rolls[-1].append(pinsDown)

			self.inProgress = False	
		else: 
			if pinsDown == 10:
				self.rolls.append(['X'])
			else:  #first roll
				
				self.inProgress = True
				self.rolls.append([pinsDown])

		if len(self.rolls) >= 12 or (len(self.rolls) == 11 and self.rolls[9][0] != 'X') or (len(self.rolls) == 10 and (self.rolls[9][0] != 'X' and self.rolls[9][0] != '/')):
			self.gameOver = True




#old version
		# if pinsDown == 10:
		# 	if self.inProgress == True: #spare not strike
		# 		self.rolls[-1].append('/')
				
		# 	else: #strike
		# 		self.rolls.append(['X'])
		# 	self.inProgress = False	

		# else:	
		# 	if self.inProgress == True: #second roll
		# 		lastRoll = self.rolls[-1][0]
		# 		rollToAdd = pinsDown - lastRoll
		# 		self.rolls[-1].append(rollToAdd)
		# 	else: #first roll
		# 		self.rolls.append([pinsDown])
		
		# 	self.inProgress = not self.inProgress 

		BowlingGame.updateScore(self)

	def updateScore(self):
		# NOTE: spares are only scored when a roll after the spare has been completed and 
		# stikes are only scored when 2 rolls after the strike are completed.
		# this was an intended feature, not a bug
		newScore = 0
		for i in range(len(self.rolls)):
			frame = self.rolls[i]
			

			if frame[0] == 'X': #strike
				#print "strike"
				if i < len(self.rolls)-1:
					nextFrame = self.rolls[i+1]
					if nextFrame[0] == 'X': #consecutive strikes
						if i < len(self.rolls)-2:
							secondNextFrame = self.rolls[i+2]
							if secondNextFrame[0] == 'X': #3 consecutive strikes
								newScore += 30
							else:	
								
								newScore += 20 + secondNextFrame[0] #2 consecutive strikes with normal 3rd roll
						
					elif len(nextFrame) == 2:	
						if nextFrame[1] == '/':
							newScore += 20 #10 for strike, 10 for spare
						else:
					
							newScore += 10 + sum(nextFrame)	# 10 for strike plus sum of next frame
							
		
			elif len(frame) > 1 and frame[1] == '/': #spare
				#print "spare"
				if i < len(self.rolls)-1:
					#print "enter"
					nextFrame = self.rolls[i+1]
					if nextFrame[0] == 'X':
						#print "enter if"
						newScore += 20
					else:	
						#print "enter else"
						newScore += 10 + nextFrame[0] 
						#print "newScore in loop", newScore
						

			else:
				# print 'self.score',self.score
				# #print "normal frame"
				# print 'frame', frame
				# sumVal  = sum(frame)
				# print 'sumVal', sumVal
				newScore += sum(frame)
		#print "newScore", newScore
		self.score = newScore		


##################
#######TESTS
##################

########
#addRoll
########
# myScore = BowlingGame()

# myScore.addRoll(4)
# print myScore.getScore()
# myScore.addRoll(7)
# myScore.addRoll(5)
# myScore.addRoll(10)


		