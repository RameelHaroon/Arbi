import sys
import json
import requests


def read_file(filePath):

    drivers = {}
    with open(filePath,'r') as inFile:
        lines = inFile.readlines()
        for line in lines:
            input = line.split(',')
            month = int(input[1].strip().split('/')[0])
            drivers[input[0]] = {
                                'id':int(input[0].strip()),
                                'joiningMonth': month,
                                }
            
    return drivers


def calculate_commission(driver, ridesDetails):
    
    totalCommission = 0
    monthsDifference = 0
    for ride in ridesDetails:
        
        if ride['driver_id'] == driver['id']:
            # If driver id is found, add the commission to the total

            rideMonth = int(ride['trip_date'].split('/')[0])
            monthsDifference = rideMonth - driver['joiningMonth']

            if monthsDifference == 0:
                # Its the first month of the driver so 0 commission
                continue
            elif monthsDifference == 1:
                # Its the next month of the driver so 10% commission
                totalCommission += ride['trip_details']['fare']*0.10
            else:
                # 20% commission for later months
                totalCommission += ride['trip_details']['fare']*0.20
   
    return totalCommission


def calculate_paid_commission(driver, paymentDetails):

    totalCommissionPaid = 0

    for payment in paymentDetails:
        
        if payment['driver_id'] == driver['id']:
            # If driver id is found, add their payment to the total
            totalCommissionPaid += payment['amount']
    
    return totalCommissionPaid

def main():
    
    filePath = 'input.txt '#sys.argv[1]
    drivers = read_file(filePath)
   
    ridesURL = 'https://www.jsonkeeper.com/b/DM5F'
    paymentsURL = 'https://www.jsonkeeper.com/b/9QRZ'

    ridesDetails = json.loads((requests.get(ridesURL)).text)
    paymentDetails = json.loads((requests.get(paymentsURL)).text)

    # Calculate commission for each driver along with how much commission each driver has paid until now, and then calculate due commission
    for driver in drivers.values():
        commission = calculate_commission(driver, ridesDetails)
        commissionPaid = calculate_paid_commission(driver, paymentDetails)
        commissionDue = commission-commissionPaid
        print(f'Driver with id {driver["id"]} is due {commissionDue} commission')

    
if __name__ == '__main__':
    main()