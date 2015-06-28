from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt

def parking():
  data = pd.read_csv('Parking_meters.csv')
  # umeter_ids = data['POST_ID'].nunique()
  
  # print "unique meters: ", umeter_ids
  print "unique meters: ", len(data)
  
  smart_filter = data['SMART_METE'].map(lambda x: x == 'Y')
  smart = data[smart_filter]
  
  print "number of smart meters: ", len(smart)
  
  geary_filter = smart['STREETNAME'].map(lambda x: x == "GEARY BLVD")
  geary = smart[geary_filter]
  
  print "number of smart meters on geary blvd: ", len(geary)

  ustreets = data['STREETNAME'].value_counts()
  print "number of distinct streets with meters: ", len(ustreets)
  
  print "top five streets with the most meters:"
  for i in xrange(0,5):
    print "\t" + str(ustreets.index[i]) + ": " + str(ustreets[i]) + " meters"
    
  meter_types = data['METER_TYPE'].value_counts()
  
  percents = []
  labels = ["Single-space", "Multi-space"]
  
  for i in xrange(0,2):
    # labels.append(meter_types.index[i])
    percents.append((meter_types[i]/len(data))*100)
  
  # counts = meter_types.index.values.pop()
#
#   for idx in meter_types.index:
#     print str(idx) + ": " + str(meter_types[idx])
#   percents = []
#   for count in meter_types:
#     percents.append((count/len(data))*100)
    
  
  plt.pie(percents, labels = labels, autopct = "%1.1f%%", 
    colors = ['cornflowerblue', 'c'], shadow=True, explode = (0,0.1))
    
  plt.axis('equal')
  plt.show()
        
if __name__ == '__main__':
  parking()