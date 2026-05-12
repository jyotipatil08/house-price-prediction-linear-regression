from django.db import models

class Admin_Details(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Admin_Details'  

class User_Details(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Dob = models.CharField(max_length=50,default=None)
    Gender = models.CharField(max_length=10)
    Phone = models.IntegerField(default=None)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
      
    class Meta:
        db_table = 'User_Details'




class Location_Details(models.Model):
    Name =models.CharField(max_length=100,default=None)
    address = models.CharField(max_length=500,default=None)
    bedroomes = models.CharField(max_length=100,default=None)
    BuiltupArea = models.CharField(max_length=100,default=None)
    Possession = models.CharField(max_length=100,default=None)
    FurnishingStatus = models.CharField(max_length=100,default=None)
    Parking = models.CharField(max_length=100,default=None)
    Flooring = models.CharField(max_length=100,default=None)
    Facing = models.CharField(max_length=100,default=None)
    WaterSupply = models.CharField(max_length=100,default=None)
    SwimmingPool = models.CharField(max_length=100,default=None)
    Security =models.CharField(max_length=100,default=None)
    Clubhouse = models.CharField(max_length=100,default=None)
    ChildrenPlayarea   = models.CharField(max_length=100,default=None)
    FireSafety = models.CharField(max_length=100,default=None)
    GasPipeline = models.CharField(max_length=100,default=None)
    Lift = models.CharField(max_length=100,default=None)
    NearestRailwaystation = models.CharField(max_length=100,default=None)
    Stationdistance = models.CharField(max_length=100,default=None)
    Description = models.CharField(max_length=500,default=None)
    PropertyValue = models.CharField(max_length=100,default=None)
    City = models.CharField(max_length=100,default=None)
    State = models.CharField(max_length=100,default=None)


    class Meta:
        db_table = 'Location_Details'


class Feedback_details (models.Model):
    Feedback = models.CharField(max_length=100,default=None)
    Uid = models.CharField(max_length=500,default=None)
          
    class Meta:
        db_table = 'Feedback_details'



class TrainingData(models.Model):
    Bedroomes = models.IntegerField(default=None)
    BuiltupArea = models.IntegerField(default=None)
    Furnished = models.IntegerField(default=None)
    Parking = models.IntegerField(default=None)
    WaterTiming = models.IntegerField(default=None)
    Swimmingpool = models.IntegerField(default=None)
    Security = models.IntegerField(default=None)
    Club = models.IntegerField(default=None)
    Playarea = models.IntegerField(default=None)
    Fire = models.IntegerField(default=None)
    Gas = models.IntegerField(default=None)
    Lift = models.IntegerField(default=None)
    StationDistance = models.IntegerField(default=None)
    SchoolDistance = models.IntegerField(default=None)
    Location = models.IntegerField(default = None)
    Result = models.IntegerField(default=None)


    class Meta:
        db_table = 'TrainingData'


class LandData(models.Model):
    Land_area =  models.IntegerField(default=None)
    Facing =  models.IntegerField(default=None)
    Boundary_wall =  models.IntegerField(default=None)
    Open_sides = models.IntegerField(default=None)
    Condition = models.IntegerField(default=None)
    Land_type = models.IntegerField(default=None)
    Transaction = models.IntegerField(default=None)
    road_facing = models.IntegerField(default=None)
    Stationdistance = models.IntegerField(default=None)
    Availability = models.IntegerField(default=None)
    Fertility = models.IntegerField(default=None)
    Location = models.IntegerField(default=None)
    Amount = models.IntegerField(default=None)

    class Meta:
        db_table = 'LandData'
