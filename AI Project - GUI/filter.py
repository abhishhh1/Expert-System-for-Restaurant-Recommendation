import collections
from knn_from_scratch import knn, euclidean_distance

def getSecs(time):
    a=time.split(":")
    ans=int(a[0])*60+int(a[1])
    return ans

def filterbyTime(time,dataset):
    newdata=[]
    time=getSecs(time)
    for data in dataset:
        openTime=getSecs(data['opening_time'])
        closeTime=getSecs(data['closing_time'])
        if openTime<=time and time<=closeTime:
            newdata.append(data)
    return newdata

def filterbyCuisine(cuisine,dataset):
    newdata=[]
    for data in dataset:
        if data[cuisine]=='1':
            newdata.append(data)
    return newdata

def filterbyBudget(budget,dataset):
    newdata=[]
    for data in dataset:
        restaurantCost=int(data['price'])
        if restaurantCost<=budget:
            newdata.append(data)
    return newdata

def filterbyDistance(distance,dataset):
    newdata=[]
    for data in dataset:
        distData=float(data['distance'])
        if distData<=distance:
            newdata.append(data)
    return newdata

def filterbyParking(dataset):
    newdata=[]
    for data in dataset:
        if data['parking']=='1':
            newdata.append(data)
    return newdata

def filterbyWifi(dataset):
    newdata=[]
    for data in dataset:
        if data['wi-fi']=='1':
            newdata.append(data)
    return newdata

def sortbyScore(dataset,money,travel):
    newdata={}
    for data in dataset:
        rating=float(data['rating'])
        budget=float(data['price'])
        distance=float(data['distance'])
        score=10*rating+3*(money/budget)+1*(travel/distance)
        newdata[-score]=data
    sorted_data=[]
    for score in sorted(newdata):
        sorted_data.append(newdata[score])
    return sorted_data
    
def FindBestwithKNN(restaurant_query,k_recommendations,dataset):
    recommendation_indices, _ = knn(
        dataset, restaurant_query, k=k_recommendations,
        distance_fn=euclidean_distance, choice_fn=lambda x: None
    )
    restaurant_recommendations = []
    for _, index in recommendation_indices:
        restaurant_recommendations.append(dataset[index])

    return restaurant_recommendations