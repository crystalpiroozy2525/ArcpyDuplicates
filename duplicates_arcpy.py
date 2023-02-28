import arcpy
import pandas as pd
import json
Path = "PATH"
rows = arcpy.SearchCursor(Path,
fields="FIELD")
fid = []
for row in rows:
    fid.append(row.getValue("FIELD"))
rows = arcpy.SearchCursor(Path,
fields="FIELD")
fid_dict = {}
for row in rows:
    value = row.getValue("FIELD")
    count = fid.count(value)
    if(count>1 and value!=' '):
        fid_dict[value] = count
    
with open('FIDDUPLCIATES.txt', 'w') as fid_file:
     fid_file.write(json.dumps(fid_dict))
