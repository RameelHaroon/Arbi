import json
import requests
import sys


def read_file(filename):

    noOfCleints = 0
    clients = []
    with open(filename, 'r') as infile:

        noOfCleints = int(infile.readline())
        tempClients = infile.readlines() 

        for each in tempClients:
            line = each.strip().split(',')
            clients.append([line[0],int(line[1])])

    return noOfCleints, clients


def rescheduled_more_than_twice(copyOfClients, clientNumber, noOfCleints):

    for client in range(clientNumber, noOfCleints):
        
        if copyOfClients[clientNumber][2] == 2:
            # Client has been rescheduled 2 time
            return True, clientNumber
        
    return False, None


def rearrange(copyOfClients, scheduleClientIndex, clientNumber):
    for rearragne in range(scheduleClientIndex, clientNumber, -1):
        copyOfClients[rearragne] = copyOfClients[rearragne-1]
        copyOfClients[rearragne][2] += 1 
    return copyOfClients            

def schedule(noOfCleints, clients):

    copyOfClients = clients[:]
    potentialHighValueClientFound = False
    for clientNumber in range(noOfCleints):
        # We will append another variable to each list which will count the number of reschedules of each client
        copyOfClients[clientNumber].append(0)

    finalResult = []
    for clientNumber in range(noOfCleints):
        # Client who came first in order is our priority right now
        scheduleClient = copyOfClients[clientNumber]
        scheduleClientIndex = clientNumber
        # Here we will check if any other client has higher priority than the client in order
        # First we will check if any of the client has been rescheduled more than 2 times
        isRescheduled, clientIndex = rescheduled_more_than_twice(copyOfClients, clientNumber, noOfCleints)
        if isRescheduled:
            # If we find such case, we will give them priority
            scheduleClient = copyOfClients[clientIndex]
            scheduleClientIndex = clientIndex

            copyOfClients = rearrange(copyOfClients, scheduleClientIndex, clientNumber)
            copyOfClients[clientNumber] = scheduleClient

            clientName = copyOfClients[clientNumber][0]
            delay = 2
            finalResult.append([clientName, delay])
        else:
            # Otherwise we will find client with highest business value
            for potentialHighValueClient in range(clientNumber+1, noOfCleints):

                if  scheduleClient[1] < copyOfClients[potentialHighValueClient][1]:
                    # If we find someone else with more business value, make them our priority
                    scheduleClient = copyOfClients[potentialHighValueClient]
                    scheduleClientIndex = potentialHighValueClient
                    potentialHighValueClientFound = True
            
            if potentialHighValueClientFound:
            # Now we will rearrange the order
                
                copyOfClients = rearrange(copyOfClients, scheduleClientIndex, clientNumber)
                copyOfClients[clientNumber] = scheduleClient

            # Now we will match the scheduled client with their original order and find out their actual delay
                
            clientName = copyOfClients[clientNumber][0]

            finalOrder = clientNumber
            for clientnum in range(noOfCleints):
                if clientName == clients[clientnum][0]:

                    if finalOrder <= clientnum:
                        delay = 0
                    else:
                        delay = copyOfClients[clientNumber][2]

            finalResult.append([clientName, delay])
            
    
    return finalResult
                


def main():

    filepath = 'input.txt' # sys.argv[1]
    try:
        noOfCleints, clients = read_file(filepath)
    except:
        print("Error")
    else:
        appoinmentList = schedule(noOfCleints, clients)
        print(appoinmentList)
        

if __name__ == '__main__':
    main()