from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt

def parking():
  data = pd.read_csv('Parking_meters.csv')
  print "unique meters: ", len(data)
  
  smart_filter = data['SMART_METE'].map(lambda x: x == 'Y')
  smart = data[smart_filter]
  
  print "number of smart meters: ", len(smart)
  
  geary_filter = smart['STREETNAME'].map(lambda x: x == "GEARY BLVD")
  geary = smart[geary_filter]
  
  print "number of smart meters on geary blvd: ", len(geary)

  ustreets = data['STREETNAME'].value_counts()
  num_streets = len(ustreets)
  print "number of distinct streets with meters: ", num_streets
  
  print "top five streets with the most meters:"
  for i in xrange(0,5):
    print "    " + str(ustreets.index[i]) + ": " + str(ustreets[i]) + " meters"
    
  meter_types = data['METER_TYPE'].value_counts()
  
  percents = []
  labels = ["Single-space", "Multi-space"]
  
  for i in xrange(0,2):
    percents.append((meter_types[i]/len(data))*100)
    
  plt.pie(percents, labels = labels, autopct = "%1.1f%%", 
    colors = ['cornflowerblue', 'c'], shadow=True, explode = (0,0.1))
    
  plt.axis('equal')
  plt.title("Breakdown of Meter Types")
  plt.savefig("MeterType.png")
  
  total = 0
  for count in ustreets:
    total += count
    
  print "street summary statistics:"
  
  print "    " + "mean: " + str(round(total/num_streets, 2)) + " meters"
  print "    " + "median: " + str(ustreets[num_streets//2]) + " meters" 
  print "    " + "minimum: " + str(ustreets[-1]) + " meter"
  print "    " + "maximum: " + str(ustreets[0]) + " meters"
        
if __name__ == '__main__':
  parking()