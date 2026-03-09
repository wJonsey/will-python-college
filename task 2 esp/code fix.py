import time

def get_region():
    regions = ('North Wales', 'South Wales', 'North East', 'North West', 'Yorkshire and The Humber',
               'East Midlands', 'West Midlands', 'East of England', 'London', 'South East', 
               'South West', 'Northern Ireland', 'Scotland')
   
    flag = True

    while flag:
        print("Please choose a region: ")
        for i in regions:
            print("{}: {} ".format((regions.index(i) + 1), i))
        
        userRegion = input('Enter the number of the region you wish to select: ')
        
        
        try:
            int(userRegion)
        except:
            print("Sorry, you did not enter a number")
            flag = True
        else:
            if int(userRegion) < 1 or int(userRegion) >  12:
                print("----------------")
                print("Sorry you did not enter a valid option. Please try again.")
                flag = True
            else:

                region = regions[int(userRegion) - 1]
                return region



def get_weight():
    flag = True

    while flag:
        weight = input("Weight KG:")
        try:
            float(weight)
        except:
            print("Sorry, you did not enter a number")
            flag = True
        else:
            return weight
        
def get_num_parcels():
    flag = True

    while flag:
        print("Please enter the number of parcels to be collected/delivered.")
        parcels = input("Number of parcels:")
        try:
            int(parcels)
        except:
            print("Sorry, you did not enter a number")
            flag = True
        else:
            return int(parcels)

def parcel_price(weight):

    if weight > 0 and weight <= 5:
        price = 10.50
    elif weight > 6 and weight < 10:
        price = 13.50
    else:
        price = 22.75
    return float(price)

def calc_additional_charge(collect, deliver):
    
    if collect == "Northern Ireland" or deliver != "Northern Ireland":
        additionalCharge = 0.10
    elif deliver == "Northern Ireland" or collect != "Northern Ireland":
        additionalCharge = 0.10
    else:
        additionalCharge = 0
    
    return additionalCharge

def main():
    
    parcelPrices = []
    parcelWeights = ()

    print("-------------")
    print('Where will the parcel be collected from?')
    collectRegion = get_region()

    print("-------------")
    print('Where will the parcel be delivered to?')
    deliverRegion = get_region()

    additionalChargeValue = calc_additional_charge(collectRegion, deliverRegion)

    numParcels = get_num_parcels()

    for i in range(numParcels):
        print('Please enter the weight for parcel number', i + 1)
        weight = get_weight()

        parcelWeights.append(weight)

        totalWeight = sum(parcelWeights)

        price = parcel_price(weight)
        
        parcelPrices.append(price)

        subTotal = sum(parcelPrices)
        
        additionalCharge = subTotal + additionalChargeValue
        finalTotal = subTotal + additionalCharge
    
  
    print("--------Order Summary--------")
    print("Collection Region:", collectRegion)
    print("Delivery Region:", deliverRegion)
    print("Parcel Weight Summary (KGs):", parcelWeights)
    print("Parcel Prices Summary:", parcelPrices)
    print("Subtotal: £{}".format(subTotal)) 
    print("Additional Charge: £{}".format(additionalCharge))
    print("Final Order Total: £{}".format(finalTotal))

man()
