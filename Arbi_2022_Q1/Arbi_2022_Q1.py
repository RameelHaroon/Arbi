import requests
import json


def read_json_file():
    
    with open('Inputfile.txt','r') as infile:
        id = infile.readline()

    url = 'https://www.jsonkeeper.com/' + id
    response = requests.get(url)
    data = json.loads(response.text)

    return data


def group_timelines(timeLines, masks):  
    
    tempGroupedTimelines = {}

    for index,timeLine in enumerate(timeLines):

        if masks[index] in tempGroupedTimelines:
            # if the mask exists,just append the new value with same mask
            tempGroupedTimelines[masks[index]].append(timeLine)

        else:
            # if not, then make a new entry in the tempGroupedTimelines
            tempGroupedTimelines[masks[index]] = [timeLine]
        
    return tempGroupedTimelines


def calculateMaskResult(mask,groupedTimeline,subOperations,transitionTable):

    subOperation = transitionTable[subOperations[mask]]
    
    if subOperation == 'MAX':
        return max(groupedTimeline)
    elif subOperation == 'MIN':
        return min(groupedTimeline)
    elif subOperation == 'SUM':
        return sum(groupedTimeline)
    else:
        # if sub operation is missing for a mask
        return 0


def disrupt_timeline():

    timeline_data = read_json_file()
    
    finalResult = []
    subOperationsResults = {}
    operation = timeline_data['data']['action_plan']['operation']
    subOperations = timeline_data['data']['action_plan']['sub_operations']
    transitionTable = {
        'FOO': 'SUM',
        'BAR': 'MIN',
        'FOX': 'MAX',
    }
    groupedTimelines = group_timelines(timeline_data['data']['timelines'], timeline_data['data']['masks'])

   
    for mask, groupedTimeline in zip(groupedTimelines.keys(), groupedTimelines.values()):
        subOperationsResults[mask] = calculateMaskResult(mask,groupedTimeline,subOperations,transitionTable)

    for subOperationsResult in subOperationsResults:
            finalResult.append(subOperationsResults[subOperationsResult])

    operation = transitionTable[operation]

    if operation == 'MAX':
        return max(finalResult)
    elif operation == 'MIN':
        return min(finalResult)
    else:
        return sum(finalResult)
    

def main():

    print(disrupt_timeline())

if __name__=="__main__":
    main()