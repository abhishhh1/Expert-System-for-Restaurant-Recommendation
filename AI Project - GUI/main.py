from experta import *
import csv
import pandas as pd
import collections 
import fileHandler
import filter
import interface
from knn_from_scratch import knn, euclidean_distance
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

dataset=[]
time='00:00'
budget=0
cuisine='italian'
distance=0
parking=0
wifi=0
dataset=dataset=fileHandler.readDataFromCSVFile("dataset.csv")

class Restaurant(Fact):
  rating = Field(float, mandatory=True)
  name = Field(str, mandatory=True)
  opening_time = Field(str, mandatory=True)
  closing_time = Field(str, mandatory=True)
  budget = Field(int, mandatory=True)
  cuisine = Field(int, mandatory=True)
  distance = Field(float, mandatory=True)
  parking = Field(int, mandatory=True)
  wifi = Field(int, mandatory=True)

class Recommender(KnowledgeEngine):
  @Rule(Fact(time=MATCH.time,data=MATCH.data))
  def timeFilter(self,time,data):
    data=filter.filterbyTime(time,data)

  @Rule(Fact(budget=MATCH.budget,data=MATCH.data))
  def BudgetFilter(self,budget,data):
    data=filter.filterbyBudget(budget,data)

  @Rule(Fact(cuisine=MATCH.cuisine,data=MATCH.data))
  def CuisineFilter(self,cuisine,data):
    data=filter.filterbyCuisine(cuisine,data)

  @Rule(Fact(distance=MATCH.distance,data=MATCH.data))
  def DistanceFilter(self,distance,data):
    data=filter.filterbyDistance(distance,data)
  
  @Rule(Fact(parking=MATCH.parking,data=MATCH.data))
  def ParkingFilter(self,parking,data):
    if(parking=='Y'):
      data=filter.filterbyParking(data)
  
  @Rule(Fact(wifi=MATCH.wifi,data=MATCH.data))
  def WifiFilter(self,wifi,data):
    if(wifi=='Y'):
      data=filter.filterbyWifi(data)

  @Rule(Fact(distance=MATCH.distance,budget=MATCH.budget,data=MATCH.data))
  def FindBest(self,budget,distance,data):
    data=filter.sortbyScore(data,budget,distance)

  @Rule(Fact(data=MATCH.data))
  def print_output(self,data):
    dataset=fileHandler.createDataframe(data)
    print()
    print(dataset)
    print()
    interface.getRecommendation(data)

def details_submitted(value_time,value_budget,value_distance,value_parking,value_wifi):
  global dataset
  global time
  time=value_time
  dataset=filter.filterbyTime(time,dataset)
  global distance
  distance=value_distance
  dataset=filter.filterbyDistance(distance,dataset)
  global budget
  budget=value_budget
  dataset=filter.filterbyBudget(budget,dataset)
  global parking
  parking=value_parking
  if parking=='Y':
    dataset=filter.filterbyParking(dataset)
  global wifi
  wifi=value_wifi
  if wifi=='Y':
    dataset=filter.filterbyWifi(dataset)
  
def cuisine_clicked(response):
  global  cuisine
  cuisine=response
  global dataset
  dataset=filter.filterbyCuisine(cuisine,dataset)

def recommend(time,budget,cuisine,distance,parking,wifi,dataset):
  dataset=filter.sortbyScore(dataset,budget,distance)
  engine=Recommender()
  engine.reset()
  engine.declare(Fact(time=time,
                      budget=budget,
                      cuisine=cuisine,
                      distance=distance,
                      parking=parking,
                      wifi=wifi,
                      data=dataset))
  engine.run()

def main():
  root=tk.Tk()
  root.title('Expert Restaurant Recommendation System')
  background_image = ImageTk.PhotoImage(Image.open('home.png'))

  label=tk.Label(image=background_image)
  label.pack()
  button = Button(root,text="Start", bg='#fac370', fg='red', padx=10, pady=10, font=200, command=interface.askDetails)
  button.pack(side=BOTTOM,fill = BOTH, expand=True)
  root.mainloop()

if __name__=='__main__':
  main()