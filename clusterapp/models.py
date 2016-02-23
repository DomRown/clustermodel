from __future__ import unicode_literals
from django.db import models
from math import sqrt
import random, json

#Each class is linked to the SQL database via MySQL-Python
class Movies(models.Model):
	id=models.IntegerField(primary_key=True)
	imid=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	type=models.CharField(max_length=50)
	year=models.IntegerField()
	series_id=models.CharField(max_length=30)
	series_name=models.CharField(max_length=300)
	series_episode=models.IntegerField()
	series_season=models.IntegerField()
	rating=models.DecimalField(max_digits=11,decimal_places=10)
	rating_count=models.IntegerField()
	release_date=models.CharField(max_length=30)
	plot=models.CharField(max_length=1000)

class Director(models.Model):
	id=models.IntegerField(primary_key=True)
	fullname=models.CharField(max_length=200)
	movie_id=models.IntegerField()

class Genres(models.Model):
	id=models.IntegerField(primary_key=True)
	genre=models.CharField(max_length=30)
	movie_id=models.ForeignKey(Movies)

class Actors(models.Model):		
	id=models.IntegerField(primary_key=True)
	fullname=models.CharField(max_length=200)
	movie_id=models.IntegerField()

class Iris(models.Model):
    sepal_length=models.IntegerField()
    sepal_width=models.FloatField()
    pet_length=models.FloatField()
    pet_width=models.FloatField()
    species=models.CharField(max_length=15)

#Get all objects & store
Moviesall=Movies.objects.all()
Directorsall=Director.objects.all()
Actorsall=Actors.objects.all()
Genresall=Genres.objects.all()
Irisall=Iris.objects.all()   

#Euclidean distance metric for Kmeans
#Input: Two "points" 
#Output: Distance between two input points
def euclidean(p,q):
    #Differences - (x2-x1) (y2-y1)
    diffv1=q[0]-p[0]
    diffv2=q[1]-p[1]
    #Squares - differences square
    sqdiff1=diffv1**2
    sqdiff2=diffv2**2
    #Sum of sq diffs
    sum=sqdiff1+sqdiff2
    #Square root of sum
    sqsum=sqrt(sum)
    return sqsum

#Normalize function
def norm(d):
    #Normalize values
        minX=min(d)
        maxX=max(d)
        newvals=[]
        for i,val in enumerate(d):
            #Xi-min(x)
            top=float(val-minX)
            bottom=float(maxX-minX)
            normalized=float(top/bottom)
            newvals.append(normalized)
        return newvals

#Kmeans is a model function, as it is grouping objects from the database based on attributes
#Kmeans 3 params - data, a function to aquire distance metric&number of clusters
def kmeans(data,distance=euclidean,k=4):
    print data
    rows=[]
    for i in data:
        rows.append(i[:2])
    #euclidrange creates list of min/max pairs 
    euclidrange=[(min([row[i] for row in rows]),max([row[i] for row in rows]))

    for i in range(len(rows[0]))] 

    #create k randomly placed centroids within len of 'data'
    centroids=[[random.random()*(euclidrange[i][1]-euclidrange[i][0])+euclidrange[i][0]
    
    for i in range(len(rows[0]))] for j in range(k)]   
    lastmatches=None
    for t in range(5):
       #print 'Iteration %d' % t
        #A list of k lists
        groups=[[] for i in range(k)]

        #find which centroid is the closts to each row
        #for the count of rows.length
        for j in range(len(rows)):
            
            #var row stores rows[j]
            row=rows[j]
            #counter is set to 0
            bestmatch=0
            for i in range(k):
                #euclidean distance between centroid and row coordinate aquired
                d=distance(centroids[i],row)
                #if d is further away from 
                if d<distance(centroids[bestmatch],row):
                    bestmatch=i
            #add index j to groups list    
            groups[bestmatch].append(j)

            
        if groups==lastmatches: break
        lastmatches=groups
        
        #move centroids to the avg of memebers
        for i in range(k):
            avgs=[0.0]*len(rows[0])
            if len(groups[i])>0:
                #print(len(bestmatches[i]))
                for rowid in groups[i]:
                    for m in range(len(rows[rowid])):
                        avgs[m]+=rows[rowid][m]
                    for j in range(len(avgs)):
                        avgs[j]/=len(groups[i])
                    centroids[i]=avgs
        coordinates = [[data[index] for index in bestmatch] for bestmatch in groups]
 
        return coordinates


