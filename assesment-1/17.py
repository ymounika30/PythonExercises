##In the given Class DateFormatter, implement the method format() such that it accepts the date (date month year), separated by comma / space or both and return the date in the format of YYYY-MM-DD. 
##Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012 
##Output : 2012-05-21 
## 
##Note the following: 
##1.	The input can have comma, space or both. No other separator is allowed 
##2.	The month can be given in full form (January, February etc) or in short 3-Letter form (Jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) . This program should accept both types. 
##3.	Output month should always be a number. 
##4.	Validate for invalid values. 
##5.	Return null for error in input. 
##

import datetime

x = datetime.datetime(2018, 9, 5)

print(x.strftime("%Y-%b-%d"))

