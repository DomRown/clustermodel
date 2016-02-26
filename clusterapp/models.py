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
	movie_ref=models.ForeignKey(Movies, db_column='movie_ref')

class Genres(models.Model):
	id=models.IntegerField(primary_key=True)
	genre=models.CharField("genre type",max_length=200, db_column='genre')
	movie_ref=models.ForeignKey(Movies, db_column='movie_ref')

class Actors(models.Model):		
	id=models.IntegerField(primary_key=True)
	fullname=models.CharField("actors full name",max_length=200)
	movie_ref=models.ForeignKey(Movies, db_column='movie_ref')

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
    #print data
    rows=[]
    for i in data:
        rows.append(i[:2])
    #print rows
    
    #euclidrange creates list of min/max pairs 
    euclidrange=[(min([row[i] for row in rows]),max([row[i] for row in rows]))
    #[min(rows, key=lambda item: (item[0], -item[1])),max(rows, key=lambda item: (item[0], -item[1]))]
    
                for i in range(len(rows[0]))] 

    #euclidrange=[(12,5),(67,8.4)]
    #print euclidrange
    #create k randomly placed centroids within len of 'data'
   
    centroids=[[random.random()*(euclidrange[i][1]-euclidrange[i][0])+euclidrange[i][0]
    
    for i in range(len(rows[0]))] for j in range(k)] 
    #centroids=[(51,7),(22,6.5),(89,6)]
    # print 'centroids'
    # print centroids
    # print 'centroids'
    lastmatches=None
    for t in range(2):
        print 'Iteration %d' % t
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
            #print groups
            
        if groups==lastmatches: break
        lastmatches=groups
        
        #no of clusters x
        for i in range(k):
            #create var avgs @ 0.0
            avgs=[0.0]*len(rows[0])

            #if number of elements in each cluster is > 0
            if len(groups[i])>0:
                #for each element in cluster
                for rowid in groups[i]:
                    # for count 2
                    for m in range(len(rows[rowid])):
                        avgs[m]+=rows[rowid][m]
                        #for count 2
                        mean=len(groups[i])
                for j in range(len(avgs)):
                        #avgs[0,1] 
                    avgs[j]/=mean
                       # print avgs[j]
                        #print (len(groups[i]))
                        #print 'en'
                    #print i
                centroids[i]=avgs
                    #print centroids
        coordinates = [[data[index] for index in bestmatch] for bestmatch in groups]
   # print centroids
    return coordinates


