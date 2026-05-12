from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Admin_Details,User_Details,Location_Details,Feedback_details,TrainingData,LandData
import datetime
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def home(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'home.html', {})

def ChangePassword(request):
    if request.method == 'POST':
        CurrentPassword = request.POST['CurrentPassword']
        NewPassword = request.POST['NewPassword']
        ConfirmPassword = request.POST['ConfirmPassword']

        uid = request.session['User_id']
        CurrUser = User_Details.objects.all().filter(id=uid)
        if CurrUser[0].Password == CurrentPassword:
            if NewPassword == ConfirmPassword:
                User_Details.objects.filter(id=uid).update(Password=NewPassword)
                messages.info(request,'Passwords Changed Successfully')
                return render(request, 'ChangePassword.html', {})
            else:
                messages.info(request,'New Passwords doesnt match')
                return render(request, 'ChangePassword.html', {})
        else:
            messages.info(request,'Current Password doesnt match')
            return render(request, 'ChangePassword.html', {})
        
    else:
        return render(request, 'ChangePassword.html', {})


def logout(request):
    Session.objects.all().delete()
    messages.info(request,'Account logout')
    return redirect('/')


def Admin_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if Admin_Details.objects.filter(Username=Username, Password=password).exists():
                user = Admin_Details.objects.get(Username=Username, Password=password)
                request.session['type_id'] = 'Admin'
                request.session['username'] = Username
                request.session['login'] = 'Yes'
                return redirect('/AddTrainingData/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/Admin_login/')
    else:
        return render(request, 'Admin_login.html', {})


def User_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if User_Details.objects.filter(Username=Username, Password=password).exists():
            user = User_Details.objects.get(Username=Username, Password=password)
            request.session['User_id'] = str(user.id)
            request.session['Gender'] = str(user.Gender)
            request.session['type_id'] = 'User'
            request.session['username'] = Username
            request.session['login'] = 'Yes'
            return redirect('/Analyze/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/User_login/')
    else:
        return render(request, 'User_login.html', {})


def Register(request):
    if request.method == 'POST':           
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Username = request.POST['Username']
        Dob = request.POST['Dob']
        Gender = request.POST['Gender']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        Password = request.POST['Password']
        final_address = request.POST['Address']
        City = request.POST['City']
        State = request.POST['State']
        register = User_Details( First_name=First_name, Last_name=Last_name, Dob=Dob, Gender=Gender ,Phone= Phone,Email= Email,Username= Username,Password=Password,Address=final_address,City=City,State=State)
        register.save()
        messages.info(request,'User Register Successfully')
        return redirect('/User_login/')
    else:
        return render(request, 'Register.html', {})



def Analyze(request):
    return render(request, 'Analyze.html', {})

def AddLocation(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Addesss =  request.POST['Addesss']
        Bedroomes = request.POST['Bedroomes']
        BuiltupArea = request.POST['BuiltupArea']
        Possession = request.POST['Possession']
        Furnished = request.POST['Furnished']
        Parking = request.POST['Parking']
        Flooring = request.POST['Flooring']
        Facing = request.POST['Facing']
        WaterTiming = request.POST['WaterTiming']
        Swimmingpool = request.POST['Swimmingpool']
        Security = request.POST['Security']
        Club = request.POST['Club']
        Playarea = request.POST['Playarea']
        Fire = request.POST['Fire']
        Gas = request.POST['Gas']
        Lift = request.POST['Lift']
        Railwaystation = request.POST['Railwaystation']
        StationDistance = request.POST['StationDistance']
        City = request.POST['City']
        State = request.POST['State']
        Description = request.POST['Description']
        PropertyValue = request.POST['PropertyValue']
        register = Location_Details(Name = Name,address = Addesss,bedroomes = Bedroomes,BuiltupArea = BuiltupArea,Possession = Possession,FurnishingStatus = Furnished,Parking = Parking,Flooring =Flooring,Facing = Facing,WaterSupply = WaterTiming,SwimmingPool = Swimmingpool,Security =Security,Clubhouse =Club,ChildrenPlayarea   = Playarea,FireSafety = Fire,GasPipeline =Gas,Lift = Lift,NearestRailwaystation = Railwaystation,Stationdistance = StationDistance,Description = Description,PropertyValue =PropertyValue,City = City,State = State)
        register.save()
        messages.info(request,'Location Added Successfully')
        return redirect('/AddLocation/')
    else:
        return render(request, 'AddLocation.html', {})




def AddDensity(request):
    if request.method == 'POST':
        pass    
    else:
        return render(request, 'AddLocation.html', {})



  
def ViewLocation(request):
    if request.method == 'POST':
        pass
    else:
        Location = Location_Details.objects.all()
        return render(request, 'ViewLocation.html', {'Location':Location})


def ViewFeedback(request):
    if request.method == 'POST':
        pass
    else:
        Feedb_det = Feedback_details.objects.all()
        return render(request, 'ViewFeedback.html', {'Feedb_det':Feedb_det})


def WriteFeedback(request):
    if request.method == 'POST':
        Feedbck = request.POST['Feedback']
        did = request.POST['hfuid']
        Feed = Feedback_details(Feedback=Feedbck, Uid=did)
        Feed.save()
        messages.info(request,'Feedback Saved')
        return redirect('/WriteFeedback/')

    else:
        did = request.session['User_id']
        return render(request, 'WriteFeedback.html', {'did':did})


def ViewUser(request):
    if request.method == 'POST':
        pass
    else:
        Users = User_Details.objects.all()
        return render(request, 'ViewUser.html', {'Users':Users})


def AddTrainingData(request):
    if request.method == 'POST':
        Bedroomes =  request.POST['Bedroomes']
        BuiltupArea = request.POST['BuiltupArea']
        Furnished = request.POST['Furnished']
        Parking = request.POST['Parking']
        WaterTiming = request.POST['WaterTiming']
        Swimmingpool = request.POST['Swimmingpool']
        Security = request.POST['Security']
        Club = request.POST['Club']
        Playarea = request.POST['Playarea']
        Fire = request.POST['Fire']
        Gas = request.POST['Gas']
        Lift = request.POST['Lift']
        Location = request.POST['Location']
        StationDistance = request.POST['StationDistance']
        SchoolDistance = request.POST['SchoolDistance']
        Value = request.POST['Result']
        register = TrainingData(Bedroomes = Bedroomes,BuiltupArea = BuiltupArea,Furnished = Furnished,Parking = Parking,WaterTiming = WaterTiming,Swimmingpool = Swimmingpool,Security =Security,Club =Club,Playarea   = Playarea,Fire = Fire,Gas =Gas,Lift = Lift,Location = Location,StationDistance =StationDistance,SchoolDistance= SchoolDistance,Result =Value)
        register.save()
        messages.info(request,'Data Added Successfully')
        return redirect('/AddTrainingData/')

    else:
        return render(request, 'AddTrainingData.html', {})



def test(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'test.html', {})





def get_response(request):
    Bedroomes = request.POST.get('Bedroomes')
    BuiltupArea = request.POST.get('BuiltupArea')
    Furnished = request.POST.get('Furnished')
    Parking = request.POST.get('Parking')
    WaterTiming = request.POST.get('WaterTiming')
    Swimmingpool = request.POST.get('Swimmingpool')
    Security = request.POST.get('Security')
    Club = request.POST.get('Club')
    Playarea = request.POST.get('Playarea')
    Fire = request.POST.get('Fire')
    Gas = request.POST.get('Gas')
    Lift = request.POST.get('Lift')
    Location = request.POST.get('Location')
    StationDistance = request.POST.get('StationDistance')
    SchoolDistance = request.POST.get('SchoolDistance')


    count = TrainingData.objects.all().count()

    if count > 0:
        Packages = TrainingData.objects.all()
        
        ArrBedroomes = []
        ArrBuiltupArea = []
        ArrFurnished = []
        ArrParking = []
        ArrWaterTiming = []
        ArrSwimmingpool = []
        ArrSecurity = []
        ArrClub = []
        ArrPlayarea = []
        ArrFire = []
        ArrGas = []
        ArrLift = []
        ArrLocation = []
        ArrStationDistance = []
        ArrSchoolDistance = []
        ArrResult = []


        for line in Packages:
            ArrBedroomes.append(line.Bedroomes)
            ArrBuiltupArea.append(line.BuiltupArea)
            ArrFurnished.append(line.Furnished)
            ArrParking.append(line.Parking)
            ArrWaterTiming.append(line.WaterTiming)
            ArrSwimmingpool.append(line.Swimmingpool)
            ArrSecurity.append(line.Security)
            ArrClub.append(line.Club)
            ArrPlayarea.append(line.Playarea)
            ArrFire.append(line.Fire)
            ArrGas.append(line.Gas)
            ArrLift.append(line.Lift)
            ArrLocation.append(line.Location)
            ArrStationDistance.append(line.StationDistance)
            ArrSchoolDistance.append(line.SchoolDistance)
            ArrResult.append(line.Result)


        '''ArrBedroomes.append(Bedroomes)
        ArrBuiltupArea.append(BuiltupArea)
        ArrFurnished.append(Furnished)
        ArrParking.append(Parking)
        ArrWaterTiming.append(WaterTiming)
        ArrSwimmingpool.append(Swimmingpool)
        ArrSecurity.append(Security)
        ArrClub.append(Club)
        ArrPlayarea.append(Playarea)
        ArrFire.append(Fire)
        ArrGas.append(Gas)
        ArrLift.append(Lift)
        ArrStationDistance.append(StationDistance)
        ArrSchoolDistance.append(SchoolDistance)

        #le = preprocessing.LabelEncoder()




        Bedroomes_encoded=ArrBedroomes
        last_Bedroomes = Bedroomes_encoded[-1]
        Bedroomes_encoded = Bedroomes_encoded[:-1]

        BuiltupArea_encoded=ArrBuiltupArea
        last_BuiltupArea = BuiltupArea_encoded[-1]
        BuiltupArea_encoded = BuiltupArea_encoded[:-1]

        Furnished_encoded=ArrFurnished
        last_Furnished = Furnished_encoded[-1]
        Furnished_encoded = Furnished_encoded[:-1]

        Parking_encoded=ArrParking
        last_Parking = Parking_encoded[-1]
        Parking_encoded = Parking_encoded[:-1]

        WaterTiming_encoded=ArrWaterTiming
        last_WaterTiming = WaterTiming_encoded[-1]
        WaterTiming_encoded = WaterTiming_encoded[:-1]

        Swimmingpool_encoded=ArrSwimmingpool
        last_Swimmingpool = Swimmingpool_encoded[-1]
        Swimmingpool_encoded = Swimmingpool_encoded[:-1]

        Security_encoded=ArrSecurity
        last_Security = Security_encoded[-1]
        Security_encoded = Security_encoded[:-1]

        Club_encoded=ArrClub
        last_Club = Club_encoded[-1]
        Club_encoded = Club_encoded[:-1]

        Playarea_encoded=ArrPlayarea
        last_Playarea = Playarea_encoded[-1]
        Playarea_encoded = Playarea_encoded[:-1]

        Fire_encoded=ArrFire
        last_Fire = Fire_encoded[-1]
        Fire_encoded = Fire_encoded[:-1]

        Gas_encoded=ArrGas
        last_Gas = Gas_encoded[-1]
        Gas_encoded = Gas_encoded[:-1]

        Lift_encoded=ArrLift
        last_Lift = Lift_encoded[-1]
        Lift_encoded = Lift_encoded[:-1]

        StationDistance_encoded=ArrStationDistance
        last_StationDistance = StationDistance_encoded[-1]
        StationDistance_encoded = StationDistance_encoded[:-1]

        SchoolDistance_encoded=ArrSchoolDistance
        last_SchoolDistance = SchoolDistance_encoded[-1]
        SchoolDistance_encoded = SchoolDistance_encoded[:-1]'''


        Bedroomes_encoded=ArrBedroomes
        BuiltupArea_encoded=ArrBuiltupArea
        Furnished_encoded=ArrFurnished
        Parking_encoded=ArrParking
        WaterTiming_encoded=ArrWaterTiming
        Swimmingpool_encoded=ArrSwimmingpool
        Security_encoded=ArrSecurity
        Club_encoded=ArrClub
        Playarea_encoded=ArrPlayarea
        Fire_encoded=ArrFire
        Gas_encoded=ArrGas
        Lift_encoded=ArrLift
        Location_encoded = ArrLocation
        StationDistance_encoded=ArrStationDistance
        SchoolDistance_encoded=ArrSchoolDistance

 

    


        temp1 = list(zip(Bedroomes_encoded,BuiltupArea_encoded,Furnished_encoded,Parking_encoded,WaterTiming_encoded,Swimmingpool_encoded,Security_encoded,Club_encoded,Playarea_encoded,Fire_encoded,Gas_encoded,Lift_encoded,Location_encoded,StationDistance_encoded,SchoolDistance_encoded))
        model = LinearRegression()
        model.fit(temp1,ArrResult)
        #score = model.evaluate(temp1,ArrResult, verbose=0)
        #print(score[1])
        
        #predicted= model.predict([[int(last_Bedroomes),int(last_BuiltupArea),int(last_Furnished),int(last_Parking),int(last_WaterTiming),int(last_Swimmingpool),int(last_Security),int(last_Club),int(last_Playarea),int(last_Fire),int(last_Gas),int(last_Lift),int(last_SchoolDistance)]])

        predicted= model.predict([[int(Bedroomes),int(BuiltupArea),int(Furnished),int(Parking),int(WaterTiming),int(Swimmingpool),int(Security),int(Club),int(Playarea),int(Fire),int(Gas),int(Lift),int(Location),int(StationDistance),int(SchoolDistance)]])
        
        print("Result :",predicted)

        answer = predicted
        print("before",answer)
        answer = str(answer)[1:-1]
        print("answer",answer)

        answer = int(float(answer))

              

        #register = TrainingData(Bedroomes = Bedroomes,BuiltupArea = BuiltupArea,Furnished = Furnished,Parking = Parking,WaterTiming = WaterTiming,Swimmingpool = Swimmingpool,Security =Security,Club =Club,Playarea   = Playarea,Fire = Fire,Gas =Gas,Lift = Lift,StationDistance =StationDistance,SchoolDistance= SchoolDistance,Result =Value,City = City)
        #register.save()

        data = {
        'respond': answer
        }
        return JsonResponse(data)


def AddLandData(request):
    if request.method == 'POST':
        Land_area = request.POST['LandArea']
        Facing = request.POST['Facing']
        Boundary_wall = request.POST['Boundary_wall']
        Open_sides = request.POST['Open']
        Condition = request.POST['Condition']
        Land_type = request.POST['LandType']
        Transaction = request.POST['Transaction']
        road_facing = request.POST['roadfacing']
        Stationdistance = request.POST['StationDistance']
        Availability = request.POST['Availability']
        Fertility = request.POST['Fertility']
        Amount = request.POST['price']
        Location = request.POST['Location']
        land = LandData(Land_area =  Land_area, Facing =  Facing,Boundary_wall =  Boundary_wall,Open_sides = Open_sides,Condition = Condition,Land_type = Land_type,Transaction = Transaction,road_facing = road_facing,Location = Location ,Stationdistance = Stationdistance,Amount = Amount,Availability = Availability, Fertility = Fertility )
        land.save()
        return render(request,'AddLandData.html',{})
    else:
        return render(request,'AddLandData.html',{})


def AnalyseLandPrice(request):
     return render(request,'AnalyseLandPrice.html',{})



def get_response1(request):
        Land_area = request.POST.get('LandArea')
        print("Land_area :"+str(Land_area))
        Facing = request.POST.get('Facing')
        print("Facing :"+str(Facing))
        Boundary_wall = request.POST.get('Boundary_wall')
        print("Boundary_wall :"+str(Boundary_wall))
        Open_sides = request.POST.get('Open')
        Condition = request.POST.get('Condition')
        Land_type = request.POST.get('LandType')
        Transaction = request.POST.get('Transaction')
        road_facing = request.POST.get('roadfacing')
        Location = request.POST.get('Location')
        Stationdistance = request.POST.get('StationDistance')
        Availability = request.POST.get('Availability')
        Fertility = request.POST.get('Fertility')
        print("Open_sides"+str(Open_sides))
        print("Condition"+str(Condition))
        print("Land_type"+str(Land_type))
        print("Transaction"+str(Transaction))
        print("road_facing"+str(road_facing))
        print("Location"+str(Location))
        print("Stationdistance"+str(Stationdistance))
        print("Availability"+str(Availability))
        print("Fertility"+str(Fertility))


        count = LandData.objects.all().count()


        if count > 0:
            Packages = LandData.objects.all()

            ArrLand_area = []
            ArrFacing = []
            ArrBoundary_wall = []
            ArrOpen_sides = []
            ArrCondition = []
            ArrLand_type = []
            ArrTransaction = []
            Arrroad_facing = []
            ArrLocation = []
            ArrStationdistance = []
            ArrAmount = []
            ArrAvailability = []
            ArrFertility = []


            for line1 in Packages:
                ArrLand_area.append(line1.Land_area)
                ArrLand_area.append(line1.Facing)
                ArrBoundary_wall.append(line1.Boundary_wall)
                ArrOpen_sides.append(line1.Open_sides)
                ArrCondition.append(line1.Condition)
                ArrLand_type.append(line1.Land_type)
                ArrTransaction.append(line1.Transaction)
                Arrroad_facing.append(line1.road_facing)
                ArrLocation.append(line1.Location)
                ArrStationdistance.append(line1.Stationdistance)
                ArrAmount.append(line1.Amount)
                ArrAvailability.append(line1.Availability)
                ArrFertility.append(line1.Fertility)

        
        Land_area_encoded=ArrLand_area
        Facing_encoded=ArrLand_area
        Boundary_wall_encoded=ArrBoundary_wall
        Open_sides_encoded=ArrOpen_sides
        Condition_encoded=ArrCondition
        Land_type_encoded=ArrLand_type
        Transaction_encoded=ArrTransaction
        road_facing_encoded=Arrroad_facing
        Location_encoded=ArrLocation
        Stationdistance_encoded=ArrStationdistance
        Availability_encoded = ArrAvailability
        Fertility_encoded = ArrFertility


        temp2 = list(zip(Land_area_encoded,Facing_encoded,Boundary_wall_encoded,Open_sides_encoded,Condition_encoded,Land_type_encoded,Transaction_encoded,road_facing_encoded,Location_encoded,Stationdistance_encoded,Availability_encoded,Fertility_encoded))
        model = LinearRegression()
        model.fit(temp2,ArrAmount)
        
        #predicted= model.predict([[int(last_Bedroomes),int(last_BuiltupArea),int(last_Furnished),int(last_Parking),int(last_WaterTiming),int(last_Swimmingpool),int(last_Security),int(last_Club),int(last_Playarea),int(last_Fire),int(last_Gas),int(last_Lift),int(last_SchoolDistance)]])

        predicted1= model.predict([[int(Land_area),int(Facing),int(Boundary_wall),int(Open_sides),int(Condition),int(Land_type),int(Transaction),int(road_facing),int(Location),int(Stationdistance),int(Availability),int(Fertility)]])
        

        print("Result :",predicted1)
        
        answer1 = predicted1
        print("before",answer1)
        answer1 = str(answer1)[1:-1]
        print("answer",answer1)

        answer1 = int(float(answer1))
       
        data1 = {
        'respond': answer1
        }
        return JsonResponse(data1)

    
        
              

        #register = TrainingData(Bedroomes = Bedroomes,BuiltupArea = BuiltupArea,Furnished = Furnished,Parking = Parking,WaterTiming = WaterTiming,Swimmingpool = Swimmingpool,Security =Security,Club =Club,Playarea   = Playarea,Fire = Fire,Gas =Gas,Lift = Lift,StationDistance =StationDistance,SchoolDistance= SchoolDistance,Result =Value,City = City)
        #register.save()
        
        

