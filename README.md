# CAN_Extractor
Simple Extractor for CAN data formatted .blf and .asc. 

## Input 
Configuration.cfg<br>
first row: data file path. ex. C:\work\data\testdata.blf<br>
<br>
## Output
CAN_Data.pkl<br>
<br>
This pickle file contains class as below:<br><br>
self.DataCount : the number of the contents.<br>
self.StartTime : The start time of the data.<br>
self.EndTime   : The end time of the data.<br>
self.Contents  : list of the row data of CAN.

