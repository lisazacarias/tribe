import csv
import pandas as pd

def parking():
  data = pd.read_csv('Parking_meters.csv')
  umeter_ids = data.POST_ID.unique()
  
  print "unique meters: ", len(umeter_ids)
  
  smart = data.SMART_METE.value_counts()['Y']
  print "number of smart meters: ", smart

        
if __name__ == '__main__':
  parking()