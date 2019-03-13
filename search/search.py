# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

import time

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
#        util.raiseNotDefined()
        print "start state from search.py"

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    "util.raiseNotDefined()"
    #Question Number 1
    from util import Stack
    #Start time of DFS
    startTime = time.time()
    cur = problem.getStartState()
    previous = None
    explored = [(cur)]
    
    
        #Initilising nodes , list of dictonary
   
    nodes = []
    nodes.append({'Cur': cur, 'Prev': None, 'Act': None, 'Travel': False})
    #initilising stack
    stack = Stack()
    #pushing cuurent state to stack
    stack.push(cur)
    #while stack is not empty
    while not stack.isEmpty():
        #poping  current state
        cur = stack.pop()
        explored.append((cur))
        #adding current state to explored node list
        curNode = []
        #going through all node in nodes
        for node in nodes:
            #if current node in node is cur then add it to curNode
            if node['Cur'] == cur:
                curNode.append(node)
    #if length of current node is greater than 1 then for all nodes curNode make them as previous node and traveled true.
        if len(curNode) > 1:
            for node in curNode:
                if node['Prev'] == previous:
                    node['Travel'] = True
        else:
            curNode[0]['Travel'] = True

        previous = cur
#check if the current state is the goal state then we reached our destination and program ends
        if problem.isGoalState(cur):
            break
#check for the successors( getting successor of current state
        successors = problem.getSuccessors(cur)
        for succ in successors:
            # if successor is not explored then add it to get explored (Traveled false)
            if succ[0] not in explored:
                nodes.append({'Cur': succ[0], 'Prev': cur, 'Act': succ[1], 'Travel': False})
                stack.push(succ[0])
    #initilising final path for the result
    finalPath = []
    pathCur1 = nodes[-1]
    #track path from end to start
    while pathCur1:
        #print "curPath = ", curPath
        if not pathCur1['Prev']:
            break
    #creating path
        finalPath.insert(0, pathCur1['Act'])
        pathCur1 = next((item for item in nodes if item['Cur'] == pathCur1['Prev'] and item['Travel'] ), None)
    print("<<< Time taken: %s seconds >>>" % (time.time() - startTime))
    return finalPath

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    #Question 2
    from util import Queue
    startTime = time.time()
    cur = problem.getStartState()
    explored = []
    
    #initilising node for keeping states
   
    nodes = []
    #appending current state, previous as null , action as null and travel state as false
    nodes.append({'Cur': cur, 'Prev': None, 'Act': None, 'Travel': False})
    #initilising queue
    stack = Queue()
    #pusing current state into stack created (queue)
    stack.push(cur)

    #cuurent node for tracking is in curPath
    curPath = None
    #checking is statck is empty or not and while it is not empty loop continues
    while not stack.isEmpty():
        # pop the current state
        cur = stack.pop()
        #if current state is already in explored then continue
        if cur in explored:
            continue
        #else add the current state into explored
        explored.append((cur))
        #travel all the nodes in the current depth then go to then depth.
        currNode = next((item for item in nodes if item['Cur'] == cur), None)
        currNode['Travel'] = True

        #check is the current state is the goal state . if yes then break else continue
        if problem.isGoalState(cur):
            curPath = currNode
            break
                #getting the successor of the current state
        successors = problem.getSuccessors(cur)
        #for all successor check if it is explored or not
        for succ in successors:
            #check if the successor is explored or not , if not explored then add it to stack
            if succ[0] not in explored:
                nodes.append({'Cur': succ[0], 'Prev': cur, 'Act': succ[1], 'Travel': False})
                stack.push(succ[0])
    #initilizing finalpath
    Finalpath = []
    #geting the path from start to end using previous state by back tracking
    while curPath:
        if not curPath['Prev']:
            break
        Finalpath.insert(0, curPath['Act'])
        curPath = next((item for item in nodes if item['Cur'] == curPath['Prev'] and item['Travel'] ), None)
        #calculating the total time taken in this process
    print("<<< Time taken: %s seconds >>>" % (time.time() - startTime))
    return Finalpath

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Question 3
    #util.raiseNotDefined()
    #initilising start time
    startTime = time.time()
    from util import PriorityQueue
    #we will be using priority queue for UCS
    cur = problem.getStartState()
    #initilising explored for keeping track of explored nodes
    explored = []

    #intilising node , for keeping current state , previous and action , cost and travel status.
    nodes = []
    #appending current , previous , action, travel status and cost for travelling
    nodes.append({'Cur': cur, 'Prev': None, 'Act': None, 'Travel': False, 'Cost': 0})
    #initilisng stack as a priority queue
    stack = PriorityQueue()
    #pushing current state into the stack
    stack.push(cur,0)
    #for tracking the path we will beusing curPath
    curPath = None
    #while stack is not empty check all the states in the stack
    while not stack.isEmpty():
        cur = stack.pop()
        #check if the current state is explored or not, if yes then continue
        if cur in explored:
            continue
        #else insert the cur state into the explored
        explored.append((cur))
        #initilising expectedResults array for keeping expected nodes
        expectedResults = []
        for node in nodes:
            #if it is the current node then append it into expectedResults
            if node['Cur'] == cur:
                expectedResults.append(node)
                    #AS UCS always travel with respect to the cost
                    #check the length of potential nodes
        if len(expectedResults) > 1:
            #current node has the smallest cost that is at expectedResults [0]
            smallestNode = expectedResults[0]
            #checking for the node with least cost and making the current state as the one having least cost
            for node in expectedResults:
                if smallestNode['Cost'] > node['Cost']:
                    smallestNode = node
            currNode = smallestNode
        else:
            #if there is only one node in the expected Result then make it the current node
            currNode = expectedResults[0]
            #update the status of currNode as true for travel
        currNode['Travel'] = True

#check if the current state and goal state are same or not , if same then break the while loop
        if problem.isGoalState(cur):
            curPath = currNode
            break
#getting all the successor node for the solution
        successors = problem.getSuccessors(cur)
#for each successor check whether it is explored or not
        for succ in successors:
            if succ[0] not in explored:
                # if the successor is not explored then add the cost of travelling into total cost
                TotalCost = succ[2] + currNode['Cost']
                nodes.append({'Cur': succ[0], 'Prev': cur, 'Act': succ[1], 'Travel': False, 'Cost': TotalCost })
                #add successor and the travelling cost to the priority queue
                stack.push(succ[0],TotalCost)
                    #initilising the final path
    FinalPath = []
    #path is the path from the start state to final goal state
    while curPath:
        #back tracking using previous state
        if not curPath['Prev']:
            break
        #add the action of previous state into the final path
        FinalPath.insert(0, curPath['Act'])
        #initilizing expectedResult ARRAY
        expectedResult = []
        #for each node check whether the current state is the action of prev path and travel status is true or not , if yes then add it to expected result
        for node in nodes:
            if node['Cur'] == curPath['Prev'] and node['Travel']:
                expectedResult.append(node)
                    #if expected result is of length >1 then tack bak all the nodes in that
        if len(expectedResult) > 1:
            curPath = expectedResult[0]
            for FinalPath in expectedResult:
                if curPath['Cost'] > path['Cost']:
                    curPath = FinalPath
        else:
            #if the expected result length is of length 1 then make it the cur path
            curPath = expectedResult[0]
    print("<<< Time taken: %s seconds >>>" % (time.time() - startTime))
    #returing the final path
    return FinalPath

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    #Question 4
    #using prioriy quene
    from util import PriorityQueue
    #initilising start time of the process for time calculation
    startTime = time.time()
    #getting the current state
    cur = problem.getStartState()
    #initilising the explored array for keeping explored states
    explored = []
    #initilising the nodes for keeping the states , current previous , action and travelled status and cost
    nodes = []
    nodes.append({'Cur': cur, 'Prev': None, 'Act': None, 'Travel': False, 'Cost': 0})
    #initilising the priority queue
    stack = PriorityQueue()
    #pushing the current state into the priority queue
    stack.push(cur,0)

    #keeping a track of search we will be using curPath for track back
    curPath = None
    #check if the stack is empty or not , continue untill the stack is empty
    while not stack.isEmpty():
        #take current state from stack
        cur = stack.pop()
        #check if the current state is explored or not
        if cur in explored:
            continue
        #if explored then continue or else append to the explored
        explored.append(cur)
        #initilising the expected results array
        expectedResults = []
        #add the current node to the expected results
        for node in nodes:
            if node['Cur'] == cur:
                expectedResults.append(node)

                    #if the length of expected results is >1 then get the smallestest node having least cost and make the current node as the cheapest node
        if len(expectedResults) > 1:
            smallestNode = expectedResults[0]
            for node in expectedResults:
                if smallestNode['Cost'] > node['Cost']:
                    smallestNode = node
            currNode = smallestNode
#making the smallest node as the current node
        else:
            #else make the first node as the current node
            currNode = expectedResults[0]
#make the current node status as travel true

        currNode['Travel'] = True

#check if the current state is the final goal state , yes then break the while loop
        if problem.isGoalState(cur):
            #make current path as the current node
            curPath = currNode
            break
#getting the successors of the path current
        successors = problem.getSuccessors(cur)
#for each successor in successor list check if it is sxplored or not
        for succ in successors:
            if succ[0] not in explored:
                #if the successor is not explore then calculate the total cost for travelling
                TotalCost = succ[2] + currNode['Cost']
                #calculate the cost along with heuristic cost
                TotalcostWithHeur = TotalCost + heuristic(succ[0],problem)
                #appending the current node
                nodes.append({'Cur': succ[0], 'Prev': cur, 'Act': succ[1], 'Travel': False, 'Cost': TotalCost })
                #push the successor into the stack
                stack.push(succ[0],TotalcostWithHeur)

                    #initilising the finalPath for keeping a track of nodes from start to end node
    finalPath = []
    #for all nodes in current path
    while curPath:
        #if the current path is not in previous then break else add it to final path
        if not curPath['Prev']:
            break
        finalPath.insert(0, curPath['Act'])
        #initilising final expected result array for result.
        expectedResult = []
        #for each node check if the node is current path previous and travel is true, if yes then add it to expected result
        for node in nodes:
            if node['Cur'] == curPath['Prev'] and node['Travel']:
                expectedResult.append(node)
                    #if length of expected result is >1 then add it to cur path the first node of expected path
        if len(expectedResult) > 1:
            curPath = expectedResult[0]
            #get the path with the least cost and make it the expected final path
            for finalPath in expectedResult:
                if curPath['Cost'] > path['Cost']:
                    curPath = finalPath
#if the expected path length is 1 then thats the final curpath and add it to current path
        else:
            curPath = expectedResult[0]
                #calculating the total time taken
    print("<<< Time taken: %s seconds >>>" % (time.time() - startTime))

    return finalPath
   

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
