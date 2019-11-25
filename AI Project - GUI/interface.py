import tkinter as tk
from tkinter import *
import main

def askDetails():
    top=Toplevel()
    top.geometry("805x488")
    top.configure(background='#bfbf9d')
    label=Label(top,text="Please answer the following questions to get better food recommendation:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
    label.grid(row=0,column=0,columnspan=5, ipadx=150)

    label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
    label1.grid(row=1,column=0,columnspan=4, ipadx=100)

    budget_amount=Entry(top,width=30, font=200)
    budget_amount.grid(row=2,column=4)
    visit_time=Entry(top,width=30, font=200)
    visit_time.grid(row=3,column=4)
    travel=Entry(top,width=30, font=200)
    travel.grid(row=4,column=4)
    parking=Entry(top,width=30, font=200)
    parking.grid(row=5,column=4)
    wifi=Entry(top,width=30, font=200)
    wifi.grid(row=6,column=4)

    budget_label=Label(top,text="Enter your budget per person:(in Rupees) ", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
    budget_label.grid(row=2,column=0,columnspan=4,ipadx=100)
    visit_label=Label(top,text="Enter your time to visit restaurant:(HH:MM) ", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
    visit_label.grid(row=3,column=0,columnspan=4, ipadx=100)
    travel_label=Label(top,text="Enter Maximum distance you can travel:(in Km) ", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
    travel_label.grid(row=4,column=0,columnspan=4, ipadx=100)
    parking_label=Label(top,text="Do you need parking area there?(Y/N) : ", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
    parking_label.grid(row=5,column=0,columnspan=4, ipadx=100)
    wifi_label=Label(top,text="Do you need free wifi there?(Y/N) ", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
    wifi_label.grid(row=6,column=0,columnspan=4, ipadx=100)

    label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
    label1.grid(row=7,column=0,columnspan=4, ipadx=100)
    label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
    label1.grid(row=8,column=0,columnspan=4, ipadx=100)

    button1 = Button(top,text='Save', font=70, padx=10, pady=10, fg='red', bg='#fac370', command=lambda: main.details_submitted(visit_time.get(),int(budget_amount.get()),float(travel.get()),parking.get(),wifi.get()))
    button1.grid(row=9,column=0,columnspan=5, ipadx=385)
    button2 = Button(top,text='Next', padx=10, pady=10, font=70, fg='red', bg='#fac370', command=askCuisine)
    button2.grid(row=10,column=0,columnspan=5, ipadx=385)


def askCuisine():
    top=Toplevel()
    top.geometry("800x488")
    label=tk.Label(top,text="Which of the following cuisine for food you want to eat?", font=200, fg='red', bg='#fac370', padx=10, pady=10)
    label.pack(anchor=W, fill=BOTH, expand=True)
    label1=tk.Label(top,text=" ", bg='#bfbf9d')
    label1.pack(anchor=W, fill=BOTH, expand=True)
    cuisines = [
        ('North Indian', 'north_indian'),
        ('South Indian', 'south_indian'),
        ('Chinese', 'chinese'),
        ('Italian', 'italian'),
        ('Mughlai', 'mughlai')
    ]
    cuisine_radio=StringVar()
    cuisine_radio.set('italian')
    for name,key in cuisines:
        Radiobutton(top,text=name,variable=cuisine_radio,value=key,font=70, fg='green', bg='#bfbf9d').pack(anchor=W,fill=BOTH)
        label1=tk.Label(top,text=" ", bg='#bfbf9d')
        label1.pack(anchor=W, fill=BOTH, expand=True)

    button1 = Button(top,text='Save', font=70, padx=10, pady=10, command=lambda: main.cuisine_clicked(cuisine_radio.get()), fg='red', bg='#fac370')
    button1.pack(anchor=W, fill=BOTH, expand=True)
    button2 = Button(top,text='Submit', padx=10, pady=10, font=70, fg='red', bg='#fac370', command=lambda : main.recommend(main.time,main.budget,main.cuisine,main.distance,main.parking,main.wifi,main.dataset))
    button2.pack(anchor=W, fill=BOTH, expand=True)

def getRecommendation(dataset):
    top=Toplevel()
    top.geometry("805x488")
    top.configure(background='#bfbf9d')
    if len(dataset)==0:
        label=Label(top,text="Sorry, No Restaurant found in database which fulfilling your requirement :-(", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=200)
    else:
        label=Label(top,text="Best suited restaurant as per your requirements are following:", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=0,column=0,columnspan=5, ipadx=190)
        label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
        label1.grid(row=1,column=0,columnspan=5, ipadx=100)

        rank=Label(top,text="Rank", font=200, fg='red', padx=10, pady=10, bg='white')
        rank.grid(row=2,column=0)
        name=Label(top,text="Name", font=200, fg='red', padx=10, pady=10, bg='white')
        name.grid(row=2,column=1, ipadx=120)
        rating=Label(top,text="Rating", font=200, fg='red', padx=10, pady=10, bg='white')
        rating.grid(row=2,column=2)
        price=Label(top,text="Price", font=200, fg='red', padx=10, pady=10, bg='white')
        price.grid(row=2,column=3)
        distance=Label(top,text="Distance", font=200, fg='red', padx=10, pady=10, bg='white')
        distance.grid(row=2,column=4)

        cnt=5
        j=3
        for data in dataset:
            if cnt==0:
                break
            rank=Label(top,text=str(5-cnt+1), font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            rank.grid(row=j,column=0)
            name=Label(top,text=data['name'], font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            name.grid(row=j,column=1, ipadx=120)
            rating=Label(top,text=str(data['rating']), font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            rating.grid(row=j,column=2)
            price=Label(top,text=str(data['price']), font=200, padx=10, pady=10, bg='#bfbf9d', fg='green')
            price.grid(row=j,column=3)
            distance=Label(top,text=str(data['distance']), font=200,  padx=10, pady=10, bg='#bfbf9d', fg='green')
            distance.grid(row=j,column=4)

            cnt-=1
            j+=1
        
        while j<8:
            label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
            label1.grid(row=j,column=0,columnspan=5, ipadx=100)
            j+=1

        label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
        label1.grid(row=8,column=0,columnspan=5, ipadx=100)
        label1=Label(top,text="", font=200, fg='red', padx=10, pady=10, bg='#bfbf9d')
        label1.grid(row=9,column=0,columnspan=5, ipadx=100)
        label=tk.Label(top,text="Thank you for using! Hope you have great food today.", font=200, fg='red', bg='#fac370', padx=10, pady=10)
        label.grid(row=10,column=0,columnspan=5, ipadx=220)

