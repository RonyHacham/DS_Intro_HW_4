#Get the longitude and latitude of the location
def get_lng_lat(address):
    import requests
    api_key=""
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, api_key)
    try:
        response= requests.get(url)
        if not response.status_code==200:
            print("HTTP Error", response.status_code)
        else:
            try:
                response_data=response.json()
                return(response_data)
            except:
                print("Response not in valid JSON format")
    except:
        print("Something went wrong with requests.get")  


#Get the distance from Jerusalem to the other locations
def get_dis(end):
    import requests
    start="Jerusalem,Israel"
    api_key=""
    url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" % (start, end, api_key)
    try:
        response = requests.get(url)
        if not response.status_code == 200:
            print("HTTP Errror", response.status_code)
        else:
            try:
                response_data=response.json()
            except:
                print("Response not in valid JSON format")
    except:
        print("Something went wrong with requests.get")
    return(response_data)

#Main Code
dic=dict()
file="C:/Users/ronyh/Desktop/BD Python/dests.txt"
try:
    fhand=open(file)
except: 
    print("file not found")
for city in fhand:
    lat_lng= get_lng_lat(city)  
    dis=get_dis(city)
    data= (dis['rows'][0]['elements'][0]['distance']['text'],
           dis['rows'][0]['elements'][0]['duration']['text'],
           lat_lng['results'][0]['geometry']['location']['lng'],
           lat_lng['results'][0]['geometry']['location']['lat'] )
    dic[city]=data
for k,v in dic.items():
    print("The city: "+k)
    print("The distance between Jerusalem and the city is "+v[0])
    print("The time it takes to reach the city is "+v[1])
    print("The longitude of the destination is:",v[2])
    print("The latitude  of the destination is:",v[3],"\n")
    print("***")

#Farest destinatoin
dic_des=dict()
far=[0,0,0]
cit=["","",""]
for k,v in dic.items():
    space=v[0].find(" ")
    dat=v[0][ :space]
    dat=dat.replace(",","")
    dic_des[k]=dat
for k,v in dic_des.items():
    v=int(v)
    if(v>far[2]):
        far[0]=far[1]
        cit[0]=cit[1]
        far[1]=far[2]
        cit[1]=cit[2]
        far[2]=v
        cit[2]=k
    else:
        if(v>far[1]):
            far[0]=far[1]
            cit[0]=cit[1]
            far[1]=v
            cit[1]=k
        else:
            if(v>far[0]):
                far[0]=v
                cit[0]=k
print()
print("*****************")
print()
print("The farest cities from Jerusalen are:")
print(cit[0]+"distance: ",far[0],"km","\n")
print(cit[1]+"distance: ",far[1],"km","\n")
print(cit[2]+"distance: ",far[2],"km","\n")       
        
    
    













    

   
    


        

















    













