Some coding challenges either practicing or requested by 

## Day of the week

Having the days of the week in the form of  "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" given a string s indicating a day of the week and a number k return what day of the week will be k days example s="Sat" k = 9 should return "Mon" example s="Mon" k = 3 should return "Thu"
see [solution](./day_of_the_week.py)

## Max value in a string data
Given a table in the form of headers and data lines separated by **\n** and values are separated by **,** return the max value given a column name example:  
given  S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7"   
C = "age"  
it should return 68  

To help ilustrate the example above here is a formatted version of the data 

| id | name  | age | room | dep |
|----|-------|-----|------|-----|
| 1  | Jack  | 68  | T    | 8   |
| 17 | Betty | 28  | F    | 7   |

as you can see, the maximum value in the column **age** is 68  
see [solution](./max_value_string_table.py)  

## Minimum missing integer
Given a list of integers return the minimum postive integer missing from the list
example:
|            list            | missing vlaue |
|:--------------------------:|:-------------:|
|          [1, 2, 3]         |       4       |
|        [-1, -2, -3]        |       1       |
|          [1, 1, 1]         |       2       |
|          [0, 0, 0]         |       1       |
| [-2,-1,1,2,3,4, 9, 10, 19] | 5             |

see [solution](./min_integer_in_array.py)

## Timesheet
Given a string where each line resprest a day of work and each day is represented by an interval of working hours calculate the total number of hours in the timesheet. The intervals can be in 24 hours format or not example: one day (like shown in the example below) can be  
```10-14, 17:30-21:30```  
and other day can be represented in 12 hours format like:  
 ```11-1, 2:30-4```  
 see [solution](./time_sheet.py)  
