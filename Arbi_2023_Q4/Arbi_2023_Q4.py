import sys


def read_input_file(fileName):
    
    tempBuildingWeights = []
    intData = []

    with open(fileName, 'r') as inFile:
        data = inFile.readlines()
    
    for row in data:
        
        if ',' in row:
            # If we are reading a list of number
            tempBuildingWeights.append([int(num) for num in row.strip().split(',')])
        else:
            # If its a single integer
            intData.append(int(row.strip()))

    return intData[0],intData[1],intData[2],tempBuildingWeights


def fill_zeros(floors, currentFloor, building):
    
    while currentFloor >= 0:
        floors[currentFloor][building] = 0
        currentFloor -= 1
    return floors



def sum_of_upper_floors(floors, currentFloor, building):
    
    sum = 0
    while currentFloor >= 0:
        sum += floors[currentFloor][building]
        currentFloor -= 1
    return sum


def merge_floors(verticalMerges, floors, floor_number, numberOfBuildings):
    
    for building in range(numberOfBuildings):
        
        numberOfMerges = verticalMerges
        currentFloor = floor_number

        while numberOfMerges > 0:
            merge = False
            sumOfUpperFloors = sum_of_upper_floors(floors, currentFloor-1, building)
            
            if floors[currentFloor][building] < sumOfUpperFloors:
                # Sum of upper floors is greater than current floors, so we merge the floors
                marge = True
                floors = fill_zeros(floors, currentFloor - 1, building)
                floors[currentFloor][building] += sumOfUpperFloors
            if not merge:
                break
            currentFloor +=1
            numberOfMerges -= 1

    return floors


def count_remaining_floors(floors, numberOfFloors, numberOfBuildings):
    
    remainingFloors = []
    

    for building in range(numberOfBuildings):
        floorCount = 0 
        floor = numberOfFloors-1
        while (floors[floor][building] > 0 
               and floor >= 0):
            floorCount += 1
            floor -= 1

        remainingFloors.append(floorCount)
    return remainingFloors


def run_simulations(simulations, verticalMerges, floors, numberOfBuildings):
    
    for floor_number in range(1,simulations+1,1):
        # Starting from first row of input e.g row 1
        if floor_number > len(floors) - 1:
            return floors
        floors = merge_floors(verticalMerges, floors, floor_number, numberOfBuildings)
    return floors


def main():

    filePath = 'input.txt' # sys.argv[1]
    simulations, verticalMerges, numberOfFloors, floors = read_input_file(filePath)
    numberOfBuildings = len(floors[0])

    floors = run_simulations(simulations, verticalMerges, floors, numberOfBuildings)
    remainingFloors = count_remaining_floors(floors, numberOfFloors, numberOfBuildings)

    print("Height of remaining floors")
    print(remainingFloors)
    
    

if __name__ == "__main__":
    main()