import random #Импортируем библиотеку для случайных элементов
import math #Импортируем библиотеку для работы с математическими функциями
n = 3 #количество переменных
a = [-100,-100,-100] #Ограничение переменных слева
b = [100,100,100] #Ограничение переменных справа

def fitnessF(x,y,z): #целевая функция, приспособленность
    return math.sqrt(x**2 + y**2) + math.fabs(z)

popSize = 1000 #размер начальной популяции
currentPop = [] #создаем список с особями
addSpecies = []
genNum = 100 #количество поколений

while len(currentPop) < popSize:
    addSpecies.clear()
    for j in range(n):
        addSpecies.append(random.random()*(b[j]-a[j]) + a[j])

    currentPop.append(addSpecies.copy())

print(currentPop)

def flat_crossover(population): #плоский кроссовер
    parents = []
    for first_parent_index in range(len(population)):
        second_parent_index = random.randint(0,len(population)-1)
        if first_parent_index != second_parent_index:
            parents.append([population[first_parent_index],population[second_parent_index]])

    newSpecies = []
    for pair in parents:
        newSpecies.clear()
        for i in range(len(pair[1])):
            newSpecies.append(random.random()*(max(pair[1][i],pair[0][i])-min(pair[1][i],pair[0][i])) + min(pair[1][i],pair[0][i]))
        population.append(newSpecies.copy())

    return population

def mutation(population):
    for species in population:
        for i in range(len(species)):
            if random.randint(0,100) < 20:
                if random.randint(0,100) < 50:
                    delta = (b[i]-species[i]) / 100
                    species[i] = species[i] + delta
                else:
                    delta = (species[i]-a[i]) / 100
                    species[i] = species[i] - delta

    return population

def proportionalSelection(population, q):
    fitPopulation = []
    newPopulation = []
    for species in population:
        fitPopulation.append(fitnessF(species[0],species[1],species[2])) #Необходимо изменять при другом количестве переменных
    fitAverage = sum(fitPopulation)/len(fitPopulation)
    newPopulation.clear()
    for species in population:
        if len(newPopulation) < q:
            if fitnessF(species[0],species[1],species[2]) <= fitAverage: #Необходимо изменять при другом количестве переменных
                newPopulation.append(species)
        else:
            break

    return newPopulation.copy()

currentPopFit = []
genMin = []
genMinFit = []
currentMinFit = fitnessF(currentPop[0][0],currentPop[0][1],currentPop[0][2]) #Необходимо изменять при другом количестве переменных
currentMin = currentPop[0]
for gen in range(0,genNum):
    currentPopFit.clear()
    currentPop = flat_crossover(currentPop)
    currentPop = mutation(currentPop)
    currentPop = proportionalSelection(currentPop,5000)

    for item in currentPop:
        if currentMinFit > fitnessF(item[0],item[1],item[2]): #Необходимо изменять при другом количестве переменных
            currentMinFit = fitnessF(item[0],item[1],item[2]) #Необходимо изменять при другом количестве переменных
            currentMin = item.copy()

print("\nLast population list: " + str(currentPop))
print("Number of generations: " + str(genNum) + "\nMIN = " + str(currentMinFit) + " in " + str(currentMin))