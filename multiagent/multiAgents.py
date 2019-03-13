# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
import time
from game import Agent

class ReflexAgent(Agent):
	"""
	  A reflex agent chooses an action at each choice point by examining
	  its alternatives via a state evaluation function.

	  The code below is provided as a guide.  You are welcome to change
	  it in any way you see fit, so long as you don't touch our method
	  headers.
	"""


	def getAction(self, gameState):
		"""
		You do not need to change this method, but you're welcome to.

		getAction chooses among the best options according to the evaluation function.

		Just like in the previous project, getAction takes a GameState and returns
		some Directions.X for some X in the set {North, South, West, East, Stop}
		"""
		# Collect legal moves and successor states
		legalMoves = gameState.getLegalActions()

		# Choose one of the best actions
		scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
		bestScore = max(scores)
		bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
		chosenIndex = random.choice(bestIndices) # Pick randomly among the best

		"Add more of your code here if you want to"

		return legalMoves[chosenIndex]

	def evaluationFunction(self, currentGameState, action):
		"""
		Design a better evaluation function here.

		The evaluation function takes in the current and proposed successor
		GameStates (pacman.py) and returns a number, where higher numbers are better.

		The code below extracts some useful information from the state, like the
		remaining food (newFood) and Pacman position after moving (newPos).
		newScaredTimes holds the number of moves that each ghost will remain
		scared because of Pacman having eaten a power pellet.

		Print out these variables to see what you're getting, then combine them
		to create a masterful evaluation function.
		"""
		# Useful information you can extract from a GameState (pacman.py)
		successorGameState = currentGameState.generatePacmanSuccessor(action)
		newPos = successorGameState.getPacmanPosition()
		newFood = successorGameState.getFood()
		newGhostStates = successorGameState.getGhostStates()
		newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
		#question number 1
		"*** YOUR CODE HERE ***"
		#using manhathan algorithm
		#initilising food distance martix
		fDis = []
		#initilising ghost distance martix
		gDis = []
		#initilising food list getting from current game
		fList = currentGameState.getFood().asList()
		#getting packman position
		pacmanPos = list(successorGameState.getPacmanPosition())
		#generating gost distance using manhattan distance formula
		gDis = [manhattanDistance(ghost.getPosition(),pacmanPos)\
						for ghost in newGhostStates if ghostState.scaredTimer == 0]
			#for each gost distance check if distance is less than 2 then return turn
		for ghostDis in gDis:
			if ghostDis < 2:
				return float('-inf')
	#calculating manhattan distance between food and pacman postion for each food in food list
		fDis = [ -1 * manhattanDistance(food,pacmanPos) for food in fList]
		#return the max food distance
		return max(fDis)

def scoreEvaluationFunction(currentGameState):
	"""
	  This default evaluation function just returns the score of the state.
	  The score is the same one displayed in the Pacman GUI.

	  This evaluation function is meant for use with adversarial search agents
	  (not reflex agents).
	"""
	return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
	"""
	  This class provides some common elements to all of your
	  multi-agent searchers.  Any methods defined here will be available
	  to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

	  You *do not* need to make any changes here, but you can if you want to
	  add functionality to all your adversarial search agents.	Please do not
	  remove anything, however.

	  Note: this is an abstract class: one that should not be instantiated.  It's
	  only partially specified, and designed to be extended.  Agent (game.py)
	  is another abstract class.
	"""

	def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
		self.index = 0 # Pacman is always agent index 0
		self.evaluationFunction = util.lookup(evalFn, globals())
		self.depth = int(depth)
		self.startTime1 = time.time()
		self.node=0
	def __del__(self):
		print('Destructor called, MultiAgentSearchAgent deleted.')
		print("<<<total time taken: %s seconds >>>" % (time.time() - self.startTime1))
		print("<<< Node Count: %s  >>>" % (self.node))


class MinimaxAgent(MultiAgentSearchAgent):
	"""
	  Your minimax agent (question 2)
	"""
	
	def getAction(self, gameState):
		"""
		  Returns the minimax action from the current gameState using self.depth
		  and self.evaluationFunction.

		  Here are some method calls that might be useful when implementing minimax.

		  gameState.getLegalActions(agentIndex):
			Returns a list of legal actions for an agent
			agentIndex=0 means Pacman, ghosts are >= 1

		  gameState.generateSuccessor(agentIndex, action):
			Returns the successor game state after an agent takes an action

		  gameState.getNumAgents():
			Returns the total number of agents in the game
		"""
		"*** YOUR CODE HERE ***"
		"util.raiseNotDefined()"
		#Question Number 2
		#Start time of Mini Max
		startTime = time.time()
		
		#initilising mini max values
		minimaxValues = []
		#initilising legal action set
		legalActionSet = gameState.getLegalActions(0)
		#for each legal action calculate minimax and append it to minimax values with the legal action
		for lAction in legalActionSet:
			p = self.minimax(gameState.generateSuccessor(0,lAction), 1, 0)
			minimaxValues.append((p, lAction))
		
		print("<<< time taken: %s seconds >>>" % (time.time() - startTime))
		
		return max(minimaxValues)[1]

	def minimax(self, gameState, agent, mdepth):
		if agent >= gameState.getNumAgents():
			agent = 0
			mdepth += 1
		#if max depth is equal to the self depth return self evaluated gamestate
		if mdepth == self.depth:
			return self.evaluationFunction(gameState)
		#getting legal actions from gamestate
		legalActions = gameState.getLegalActions(agent)
		#if it not a legal action then return the self evaluation
		if not legalActions:
			return self.evaluationFunction(gameState)
			#initilising minimaxvalues
		minimaxValues = []
		#if agent is equal to zero then return max of minimax value
		if agent == 0:
			for lAction in legalActions:
				p = self.minimax(gameState.generateSuccessor(agent,lAction), agent+1, mdepth)
				minimaxValues.append((p, lAction))
			self.node=self.node+1
			return max(minimaxValues)[0]
				#else return max of minimax value
		else:
			for lAction in legalActions:
				p = self.minimax(gameState.generateSuccessor(agent,lAction), agent+1, mdepth)
				minimaxValues.append((p, lAction))
			self.node=self.node+1
			return min(minimaxValues)[0]

class AlphaBetaAgent(MultiAgentSearchAgent):
	"""
	Your minimax agent with alpha-beta pruning (question 3)
	"""

	def getAction(self, gameState):
		
		"""
		  Returns the minimax action using self.depth and self.evaluationFunction
		"""
		"*** YOUR CODE HERE ***"
		#util.raiseNotDefined()
		#question number 3
		#Start time of Alpha beta
		startTime = time.time()
		p = (float("-inf"), 'None')
		alpha = float('-inf')
		beta = float('inf')
		lActions = gameState.getLegalActions(0)
		#for each legal action in action set return min action using self depth and self evaluation
		for lAction in lActions:
			p = max(p, (self.alphabeta(gameState.generateSuccessor(0, lAction), 1, 0, alpha, beta), lAction))
			if p[0] > beta:
				print("<<< Time taken: %s seconds >>>" % (time.time() - startTime))
				return p[1]
			alpha = max(alpha, p[0])
		print("<<< Time taken: %s seconds >>>" % (time.time() - startTime))
		return p[1]

	def alphabeta(self, gameState, agent, mdepth, alpha, beta):
		if agent >= gameState.getNumAgents():
			agent = 0
			mdepth += 1

		if mdepth == self.depth or gameState.isWin() or gameState.isLose():
			return self.evaluationFunction(gameState)

		legalActions = gameState.getLegalActions(agent)
		#if agent is equal to zero then return max of alpha or p value
		if agent == 0:
			p = float("-inf")
			for lAction in legalActions:
				p = max(p, self.alphabeta(gameState.generateSuccessor(agent, lAction), agent + 1,mdepth, alpha, beta))
				if p > beta:
					self.node=self.node+1
					return p
				alpha = max(alpha, p)
			self.node=self.node+1
			return p
						#if agent is equal to zero then return min of beta or p value
		else:
			p = float("inf")
			for lAction in legalActions:
				p = min(p, self.alphabeta(gameState.generateSuccessor(agent, lAction), agent + 1,mdepth, alpha, beta))
				if p < alpha:
					self.node=self.node+1
					return p
				beta = min(beta, p)
			self.node=self.node+1
			return p

class ExpectimaxAgent(MultiAgentSearchAgent):
	"""
	  Your expectimax agent (question 4)
	"""

	def getAction(self, gameState):
		"""
		  Returns the expectimax action using self.depth and self.evaluationFunction

		  All ghosts should be modeled as choosing uniformly at random from their
		  legal moves.
		"""
		"*** YOUR CODE HERE ***"
		util.raiseNotDefined()
		



def betterEvaluationFunction(currentGameState):
	"""
	  Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
	  evaluation function (question 5).

	  DESCRIPTION: <write something here so we know what you did>
	"""
	"*** YOUR CODE HERE ***"
	util.raiseNotDefined()
	
	#question number 5 attempted
	"""newPos = currentGameState.getPacmanPosition()
	newFood = currentGameState.getFood()
	newGhostStates = currentGameState.getGhostStates()
	newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
	newCapsules = currentGameState.getCapsules()

	fDis = []
	gDis = []
	fList = currentGameState.getFood().asList()
	pacmanPos = list(currentGameState.getPacmanPosition())
	
	score = currentGameState.getScore()
	score -= len(fList)
	score -= len(newCapsules)
	for gState in newGhostStates:
		dist = manhattanDistance(gState.getPosition(),pacmanPos)
		if gState.scaredTimer > 0:
			if gState.scaredTimer > dist:
				score += 2 * dist
			else:
				score += 1.5 * dist
		else:
			score -= 1.5 * dist

	for food in foodList:
		score -= 0.5 * manhattanDistance(food,pacmanPos)

	
	for capsule in newCapsules:
		score -= 2 * manhattanDistance(capsule,pacmanPos)
	
	return score"""


# Abbreviation
better = betterEvaluationFunction

