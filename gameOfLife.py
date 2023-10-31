{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ae83aa39-7481-4ac2-9fba-17d1c184e507",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Matrix:\n",
    "    \n",
    "    def __init__(self,size):\n",
    "        board = []\n",
    "        for i in range(size):\n",
    "            tempArr = []\n",
    "            for j in range(size):\n",
    "                tempArr.append(False)\n",
    "            board.append(tempArr)\n",
    "        self.board = board\n",
    "        \n",
    "    def nextGeneration(self):\n",
    "        x = nextGeneration(self)\n",
    "        self.board = x.board\n",
    "        \n",
    "    def getNum(self):\n",
    "        result = \"\"\n",
    "        for i in range(size):\n",
    "            for j in range(size):\n",
    "                result += \"1\" if self.board[i][j] else \"0\"        \n",
    "\n",
    "                \n",
    "def getNum(matrix):\n",
    "    result = \"\"\n",
    "    for i in range(size):\n",
    "        for j in range(size):\n",
    "            result += \"1\" if matrix.board[i][j] else \"0\"       \n",
    "    return result\n",
    "# check if i,j inside the bounds of matrix\n",
    "def inBounds(self,i,j):\n",
    "    return i > 0 and i < len(self.board) and j > 0 and j < len(self.board)\n",
    "\n",
    "# return if a cell live in the next generation\n",
    "def amIAlive(self,i,j):\n",
    "    countNeighbers = 0\n",
    "    willLive = 3\n",
    "    mayLive = 2\n",
    "    # check each neighbor\n",
    "    for a in range(i-1,i+2):\n",
    "        for b in range(j-1,j+2):\n",
    "            # don't count yourself\n",
    "            if a==i and b==j:\n",
    "                continue\n",
    "            if inBounds(self,a,b) and self.board[a][b] == True:\n",
    "                countNeighbers += 1\n",
    "    if countNeighbers == willLive:\n",
    "        return True\n",
    "    if countNeighbers == mayLive and self.board[i][j] == True:\n",
    "        return True\n",
    "    return False\n",
    "\n",
    "# compare two boards\n",
    "def equals(matrix1,matrix2):\n",
    "    m1 = getNum(matrix1)\n",
    "    m2 = getNum(matrix2)\n",
    "    return m1 == m2\n",
    "\n",
    "# return a copy of a board\n",
    "def copyBoard(self):\n",
    "    m = Matrix(size)\n",
    "    for i in range(len(self.board)):\n",
    "        for j in range(len(self.board)):\n",
    "            m.board[i][j] = self.board[i][j]\n",
    "    return m\n",
    "\n",
    "# calc how the matrix looks in the next generation\n",
    "def nextGeneration(self):\n",
    "    n = len(self.board)\n",
    "    newMatrix = Matrix(n);\n",
    "    for i in range(n):\n",
    "        for j in range(n):\n",
    "            newMatrix.board[i][j] = amIAlive(self,i,j)\n",
    "    return newMatrix\n",
    "\n",
    "# return if a configuration is new\n",
    "def isNew(self,history):\n",
    "    s = set()\n",
    "    for step in history:\n",
    "        if step.getNum() in s:\n",
    "            return False\n",
    "        s.add(step.getNum())\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c481f95a-f580-489b-b7c8-16c9f6a11a80",
   "metadata": {},
   "outputs": [],
   "source": [
    "# population\n",
    "\n",
    "# update the population after one generation\n",
    "def updatePopulation(pop,popByGrade):\n",
    "    newPop = []\n",
    "    for i in range(len(pop)):\n",
    "        newPop.append(match(pop,popByGrade))\n",
    "    return newPop\n",
    "\n",
    "# create arr with all the population appear according to their grade\n",
    "def popultionByGrade(population):\n",
    "    r = []\n",
    "    for i in population:\n",
    "        if grade(i) == 0:\n",
    "            r.append(i)\n",
    "        for j in range(grade(i)):\n",
    "            r.append(i)\n",
    "    return r\n",
    "\n",
    "# create initial population\n",
    "def initializePopulation():\n",
    "    population = []\n",
    "    for i in range(numOfPopulation):\n",
    "        m = setPopulation()\n",
    "        population.append(m)\n",
    "    return population\n",
    "\n",
    "# returns a random matrix\n",
    "def setPopulation():\n",
    "    m = Matrix(size)\n",
    "    numOfAliveCells = random.randint(minStart,maxStart)\n",
    "    lim = 0\n",
    "    while lim == 0:\n",
    "        lim = random.randint(0,size - 1 - offset)\n",
    "    while(numOfAliveCells > 0):\n",
    "        row = random.randint(lim,lim+offset)\n",
    "        col = random.randint(lim,lim+offset)\n",
    "        if m.board[row][col] == False:\n",
    "            m.board[row][col] = True\n",
    "            numOfAliveCells -= 1        \n",
    "    return m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aec97ece-191c-420e-88f5-7604dea6ab7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# evaluate solutions\n",
    "\n",
    "# returns how many cells alive in a matrix\n",
    "def howManyAlive(matrix):\n",
    "    res = 0\n",
    "    for i in range(size):\n",
    "        for j in range(size):\n",
    "             if matrix.board[i][j]:\n",
    "                    res +=1\n",
    "    return res\n",
    "\n",
    "# get arr of matrixes and returns their grades as an arr\n",
    "def lsOfGrades(pop):\n",
    "    grades = []\n",
    "    for i in pop:\n",
    "        if grade(i) == 1:\n",
    "            grades.append(0)\n",
    "        else:\n",
    "            grades.append(grade(i))\n",
    "    return grades \n",
    "\n",
    "# calc biggest difference between the amount of alive cells in the best configuration in the next generation\n",
    "# to the initial amout of alive cells\n",
    "def grade(self):\n",
    "    m = copyBoard(self)\n",
    "    initialSize = howManyAlive(m)\n",
    "    n = numOfGenerationUntilBiggest(m)\n",
    "    for i in range(n):\n",
    "        m = nextGeneration(m)\n",
    "    return max(howManyAlive(m)-initialSize,1);\n",
    "\n",
    "\n",
    "# returns in how many generations the configuration is the largest and the size of it\n",
    "def numOfGenerationUntilBiggest(self):\n",
    "    m = copyBoard(self)\n",
    "    num = 0\n",
    "    numOfGen = 0\n",
    "    biggestSize = 0\n",
    "    for i in range(numOfNewGenerations(m)):\n",
    "        num = howManyAlive(m)\n",
    "        if num > biggestSize:\n",
    "            biggestSize = num\n",
    "            numOfGen = i\n",
    "        m = nextGeneration(m)\n",
    "    return numOfGen\n",
    "\n",
    "# calc how many generation takes until a configuration appears twice\n",
    "def numOfNewGenerations(self):\n",
    "    m = copyBoard(self)\n",
    "    num = getNum(m)\n",
    "    s = set()\n",
    "    while True:\n",
    "        if num in s:\n",
    "            break;\n",
    "        else:\n",
    "            s.add(num)\n",
    "        m = nextGeneration(m)\n",
    "        num = getNum(m)\n",
    "        #print(getNum(m) + \"this is suppose to be a string represent matrix\")\n",
    "    return len(s)-1\n",
    "\n",
    "# returns the size of a matrix in his last new configuration\n",
    "def sizeInTheEnd(matrix):\n",
    "    m = copyBoard(matrix)\n",
    "    num = numOfNewGenerations(matrix)\n",
    "    for i in range(num):\n",
    "        m = nextGeneration(m)\n",
    "    return howManyAlive(m)\n",
    "\n",
    "# returns the size of a matrix in his last new configuration\n",
    "def sizeInTheBiggest(matrix):\n",
    "    m = copyBoard(matrix)\n",
    "    num = numOfGenerationUntilBiggest(matrix)\n",
    "    for i in range(num):\n",
    "        m = nextGeneration(m)\n",
    "    return howManyAlive(m)     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "012dcb22-de17-4571-90fe-e9f16fbc12a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# evolution\n",
    "\n",
    "# chose parents from population by grades\n",
    "def choseParent(population):\n",
    "    flip = random.randint(0,len(population) - 1)\n",
    "    return population[flip]\n",
    "\n",
    "# choose two parents and return their son\n",
    "def match(pop,popByGrade):\n",
    "    \n",
    "    # choose parents\n",
    "    flip = random.randint(0,len(popByGrade)-1)\n",
    "    dad = choseParent(popByGrade)\n",
    "    mom = choseParent(popByGrade)\n",
    "    while equals(dad,mom):\n",
    "        dad = choseParent(population)\n",
    "    # get birth\n",
    "    return birth(mom,dad)\n",
    "\n",
    "# return the son of two parents\n",
    "def birth(mom,dad):\n",
    "    son = Matrix(size)\n",
    "    for i in range(size):\n",
    "        for j in range(size):\n",
    "            \n",
    "            # recombination \n",
    "            whichParent = random.randint(0,1)\n",
    "            if whichParent == 0:\n",
    "                son.board[i][j] = mom.board[i][j]\n",
    "            else:\n",
    "                son.board[i][j] = dad.board[i][j]\n",
    "                \n",
    "            # mutation\n",
    "            chance = random.randint(0,chanceToMutation)\n",
    "            if chance == chanceToMutation:\n",
    "                if son.board[i][j]:\n",
    "                    son.board[i][j] = False\n",
    "                else:\n",
    "                    son.board[i][j] = True\n",
    "    return son"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e387a680-bf95-4521-aa02-adc5d33acb47",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import math\n",
    "import random\n",
    "\n",
    "# variables\n",
    "size = 10\n",
    "chanceToMutation = 1000\n",
    "numOfPopulation = 15\n",
    "numOfGenertions = 30\n",
    "cell_size = 20\n",
    "minStart = 6\n",
    "maxStart = 15\n",
    "offset = 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7006c6c3-963f-410d-8763-b0afadbc14cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# gui\n",
    "def drawGrid(matrix):\n",
    "    \n",
    "    # intialize variables\n",
    "    root = Tk()\n",
    "    root.geometry(\"600x680\")\n",
    "    root.title(\"Game Of Life\")\n",
    "    my_canvas = Canvas(root,width = 600, height = 650,bg = \"white\")\n",
    "    my_canvas.pack(pady = 0)\n",
    "    next_button = Button(root, text=\"Next\", command=lambda : run_and_canvas(my_canvas))\n",
    "    next_button.pack()\n",
    "    print(\"num of alive cells:\" + str(howManyAlive(matrix)))\n",
    "       \n",
    "    emptyBoard(my_canvas)\n",
    "    fillBoard(my_canvas,matrix)\n",
    "\n",
    "    # btn func\n",
    "    def run_and_canvas(my_canvas): \n",
    "        matrix.nextGeneration()\n",
    "        emptyBoard(my_canvas)\n",
    "        fillBoard(my_canvas,matrix)\n",
    "        print(\"num of alive cells:\" + str(howManyAlive(matrix)))\n",
    "        \n",
    "    root.mainloop()\n",
    "    \n",
    "def emptyBoard(my_canvas):\n",
    "    for j in range(size):\n",
    "        for k in range(size):\n",
    "            my_canvas.create_rectangle(j*cell_size,k*cell_size,(j+1)*cell_size,(k+1)*cell_size,fill = \"white\")\n",
    "            \n",
    "def fillBoard(my_canvas,matrix): \n",
    "    for j in range(size):\n",
    "        for k in range(size):\n",
    "            if matrix.board[j][k]:\n",
    "                my_canvas.create_rectangle(j*cell_size,k*cell_size,(j+1)*cell_size,(k+1)*cell_size,fill = \"black\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "27bf1399-cbfa-4b17-a4f6-0bbe29982a13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generation: 0\n",
      "[3, 17, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 8]\n",
      "Generation: 3\n",
      "[0, 19, 10, 0, 4, 22, 9, 20, 20, 0, 3, 6, 2, 0, 14]\n",
      "Generation: 6\n",
      "[4, 8, 20, 13, 0, 2, 4, 7, 4, 11, 11, 8, 2, 0, 19]\n",
      "Generation: 9\n",
      "[0, 2, 6, 18, 0, 3, 8, 0, 2, 3, 0, 11, 7, 4, 11]\n",
      "Generation: 12\n",
      "[7, 6, 13, 14, 4, 0, 2, 8, 16, 0, 6, 0, 12, 5, 19]\n",
      "Generation: 15\n",
      "[11, 2, 13, 32, 12, 13, 6, 17, 9, 8, 10, 13, 21, 11, 13]\n",
      "Generation: 18\n",
      "[16, 16, 10, 12, 8, 20, 20, 10, 17, 7, 15, 7, 11, 21, 15]\n",
      "Generation: 21\n",
      "[21, 21, 3, 4, 20, 7, 3, 8, 12, 10, 21, 17, 17, 20, 11]\n",
      "Generation: 24\n",
      "[17, 12, 17, 13, 17, 19, 7, 22, 17, 11, 12, 9, 12, 12, 17]\n",
      "Generation: 27\n",
      "[12, 17, 17, 17, 17, 21, 17, 17, 13, 17, 8, 12, 11, 16, 17]\n",
      "Generation: 30\n",
      "[17, 10, 10, 13, 17, 21, 20, 17, 13, 17, 12, 16, 17, 21, 21]\n",
      "-------------------------------------------------------------------------------\n",
      "Biggest size - initial size: 32\n",
      "Get biggest in 47 generations\n",
      "Stabalize in 51 genertions\n",
      "Final size: 10\n",
      "Biggest size: 46\n",
      "[2.2, 8.6, 7.533333333333333, 5.0, 7.466666666666667, 12.733333333333333, 13.666666666666666, 13.0, 14.266666666666667, 15.266666666666667, 16.133333333333333]\n",
      "-------------------------------------------------------------------------------\n",
      "num of alive cells:14\n",
      "num of alive cells:16\n",
      "num of alive cells:19\n",
      "num of alive cells:15\n",
      "num of alive cells:15\n",
      "num of alive cells:14\n",
      "num of alive cells:13\n",
      "num of alive cells:15\n",
      "num of alive cells:19\n",
      "num of alive cells:18\n",
      "num of alive cells:17\n",
      "num of alive cells:16\n",
      "num of alive cells:13\n",
      "num of alive cells:11\n",
      "num of alive cells:11\n",
      "num of alive cells:14\n",
      "num of alive cells:16\n",
      "num of alive cells:17\n",
      "num of alive cells:17\n",
      "num of alive cells:15\n",
      "num of alive cells:19\n",
      "num of alive cells:14\n",
      "num of alive cells:21\n",
      "num of alive cells:14\n",
      "num of alive cells:14\n",
      "num of alive cells:10\n",
      "num of alive cells:9\n",
      "num of alive cells:9\n",
      "num of alive cells:9\n",
      "num of alive cells:11\n",
      "num of alive cells:12\n",
      "num of alive cells:14\n",
      "num of alive cells:17\n",
      "num of alive cells:16\n",
      "num of alive cells:19\n",
      "num of alive cells:21\n",
      "num of alive cells:25\n",
      "num of alive cells:25\n",
      "num of alive cells:30\n",
      "num of alive cells:34\n",
      "num of alive cells:34\n",
      "num of alive cells:30\n",
      "num of alive cells:32\n",
      "num of alive cells:36\n",
      "num of alive cells:36\n",
      "num of alive cells:35\n",
      "num of alive cells:37\n",
      "num of alive cells:46\n",
      "num of alive cells:26\n",
      "num of alive cells:18\n",
      "num of alive cells:14\n",
      "num of alive cells:10\n",
      "num of alive cells:10\n",
      "num of alive cells:10\n",
      "num of alive cells:10\n"
     ]
    }
   ],
   "source": [
    "# main\n",
    "\n",
    "# set population\n",
    "\n",
    "population = initializePopulation()\n",
    "popByGrades = popultionByGrade(population)\n",
    "biggest = 0\n",
    "\n",
    "# initialize variables\n",
    "bestMatrix = Matrix(size)\n",
    "midBestMatrix = Matrix(size)\n",
    "avgPerGen = []\n",
    "\n",
    "for i in range(numOfGenertions+1):\n",
    "    \n",
    "    population = updatePopulation(population,popByGrades)\n",
    "    popByGrades = popultionByGrade(population)\n",
    "       \n",
    "    # print grades for a generation each 5 generations\n",
    "    if i % math.floor(numOfGenertions / 10) == 0:\n",
    "        #print(\"hello2!\")\n",
    "        print(\"Generation: \" + str(i))\n",
    "        ls = lsOfGrades(population)\n",
    "        print(ls)\n",
    "        avgPerGen.append(sum(ls)/len(ls))\n",
    "    j = 0\n",
    "    \n",
    "    # check each solution in the current population\n",
    "    for p in population:\n",
    "        num = grade(p)\n",
    "        # update best solutions\n",
    "        if j == math.floor(numOfGenertions / 2):\n",
    "            midBestMatrix = bestBoard\n",
    "            \n",
    "        if num > biggest:\n",
    "            biggest = num\n",
    "            bestBoard = copyBoard(p)\n",
    "        j += 1\n",
    "        \n",
    "print(\"-------------------------------------------------------------------------------\")       \n",
    "print(\"Biggest size - initial size: \" + str(grade(bestBoard)))\n",
    "print(\"Get biggest in \" + str(numOfGenerationUntilBiggest(bestBoard))+ \" generations\")\n",
    "print(\"Stabalize in \" + str(numOfNewGenerations(bestBoard))+ \" genertions\")\n",
    "print(\"Final size: \" + str(sizeInTheEnd(bestBoard)))\n",
    "print(\"Biggest size: \" + str(sizeInTheBiggest(bestBoard)))\n",
    "print(avgPerGen)\n",
    "print(\"-------------------------------------------------------------------------------\")   \n",
    "drawGrid(bestBoard)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f693d4c-978d-4849-8caf-719d275d8e03",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc7b5377-1f34-4ff5-8330-16e979d7d1d6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "feeecdde-3989-481f-b2cc-b6972e350838",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b642d216-83bf-44d4-94ba-11b53906c339",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec070801-243c-4cfb-a944-369a4496179f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1894981-edb6-4a22-8bcc-20120548adb9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3d49465-d719-4a47-9229-41e187da7393",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccc062f4-e5ce-4719-bb89-f8939656b77d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c01a87d4-bfd2-48c9-8774-854a0b04ada6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00ef1c1d-7ba6-4a72-a7e3-eeede9b5a5cd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e7f10fc-ac84-45cc-ba17-f53e60f5953e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed57fce1-9782-49a4-8871-60495a173170",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c724753-f4c4-4eb1-b2d5-eb904d88b930",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30627676-5dca-4aee-a692-836a378781be",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9193b1ad-642c-4453-aacb-590cd6299d07",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f279732-677e-4cde-9b26-785ee6c19037",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7d27bf8-8150-4fed-bf75-bf6bb645022a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "869252b9-0b03-4a48-8da9-01036c8c5b60",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2a7f464-cf3c-41dd-a1d2-0035ae3c3711",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4ff2a8a-9c6b-4cac-837f-0a26d9c63e03",
   "metadata": {},
   "outputs": [],
   "source": [
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f594ec0-9bbc-46c6-a214-9fd4e0155f9f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21b9e433-efb1-4402-a822-a994c6915a34",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "deb0fe47-a471-442e-8855-076247567ee5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b705a8d5-c415-4ab7-9df4-c2b184272509",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c16a0f80-9a66-4ba0-aa9b-cf4da41c2a1b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78a5cc5c-c98c-4774-813f-f350820b9a2c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73035f1a-7500-45a7-aea5-ad7241bf5f71",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "118bc704-eb68-4e06-a300-0f74d9841439",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5a58241-2590-440e-a3ec-99acaee60ef6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60e407c8-1ca5-414f-847e-ebf6e7f3ed0f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "073fce43-da2d-4a58-bfd7-39d1c00a5e63",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "403e3297-e4c0-40ae-b30d-87746e6404d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c964a43-906e-4628-8697-0b2e5c2ff1c3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e62cc3ef-db6f-4165-84cf-e9cb19a62fca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae680592-1fe1-4eaf-8fdc-dca4c1f1ed79",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "660adeb1-7b17-4b0e-b2ee-cc1dab5b26f2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77349cff-e1c3-4ba1-89b4-8e132085eb63",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c20fed2e-9a19-4815-82ea-8960d0fcf324",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68e18006-1e51-4c06-bb51-73636d4097bd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89e80252-4f86-4dcb-acdf-284692dd25a3",
   "metadata": {},
   "outputs": [],
   "source": [
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "317be187-0ef1-4e50-ac75-6892cbbae707",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91bafda3-2f5b-420e-bbc6-2c60c1ad3018",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57ef8ee4-c7a9-4f2f-9253-2589a8a03aa1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b91242d-5ced-4340-882a-7245a0b32381",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "def printArr(self):\n",
    "    r = \"\"\n",
    "    for i in range(len(self.board)):\n",
    "        for j in range(len(self.board)):\n",
    "            if(self.board[i][j]):\n",
    "                r = r +\"1\\t\"\n",
    "                \n",
    "            else:\n",
    "                r = r +\"0\\t\"\n",
    "        r = r + \"\\n\"\n",
    "    print(r)\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c578b51d-accf-4662-896a-e118af41001f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7f7a236-a93f-4535-bc39-85f649684e6b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92c9b9b2-b2d1-4bfb-96eb-15a5548019df",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
