import csv
import constants

class Station:
    def __init__(self, station):
        self.name = station[0]
        self.region = station[1]
        self.resource = station[2]
        self.size = int(station[3])
        self.level = 0
        self.completion = 0
        self.label = self.label_me()

    def label_me(self):
        """
        if(self.region in LOCKED_REGIONS):
            return "lock"
        """
        if(self.completion < constants.size_data[self.size][0] or self.level < 3):
            return "curr"
        return "complete"
  
# reading csv file 
def getStations():
    filename = "TinyRailsStations.csv"

    # initializing the titles and rows list 
    rows = [] 
    stations = dict()

    with open(filename, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        
        #skip blank first line
        next(csvreader)

        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 

        #print(len(rows))

    for station in rows:
        stat = Station(station)
        name = stat.name
        if(name in stations):
           name = name + "_" + stat.region
        stations[name] = stat

    
    return stations