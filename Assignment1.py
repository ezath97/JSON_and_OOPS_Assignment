
# Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
# Each employee information consists of Name, DOB, Height, City, State. 
# Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. 
# Finally print the list of the Employee objects.
# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
 
# Solution 1

import json
class Employee:
    def __init__(self,Name,DOB,Height,City,State):
        self.Name = Name
        self.DOB = DOB
        self.Height = Height
        self.City = City
        self.State = State

E1=Employee('Harish','20/05/1998','165cm','Chennai','Tamil Nadu')
E2=Employee('Ramesh','20/06/1987','168cm','Chennai','Tamil Nadu')
E3=Employee('Suresh','30/05/1990','174cm','Chennai','Tamil Nadu')
E4=Employee('Vijay','24/05/1998','178cm','Chennai','Tamil Nadu')
E5=Employee('Ajith','14/04/1999','160cm','Chennai','Tamil Nadu')
Employee_Dict = {'Employee_1':E1.__dict__,'Employee_2':E2.__dict__,'Employee_3':E3.__dict__,'Employee_4':E4.__dict__,'Employee_5':E5.__dict__}
#print(Employee_Dict)
with open('employee.json','w') as f:
    json.dump(Employee_Dict,f,indent=4)
    print('Json file is created')
    
    
with open('employee.json','r') as h:
    E=json.load(h)
    print('Json file is readed')
Emp = list(E.keys())
Emp_1 = list(E['Employee_1'].items())
Emp_2 = list(E['Employee_2'].items())
Emp_3 = list(E['Employee_3'].items())
Emp_4 = list(E['Employee_4'].items())
Emp_5 = list(E['Employee_5'].items())
print('List of Employee: ',Emp)
print('Count: ',len(Emp))
print('Employee 1: ',Emp_1)
print('Employee 2: ',Emp_2)
print('Employee 3: ',Emp_3)
print('Employee 4: ',Emp_4)
print('Employee 5: ',Emp_5)
    
print('***************************************************************************************************************')
    
# Solution 2
Indian_states = {'Tamil Nadu':'Chennai','Kerala':'Thiruvananthapuram','Telangana':'Hydrabad','Karnataka':'Bengaluru','Goa':'Panaji','Bihar':'Patna','Assam':'Dispur'}
print('Dictionary created: ',Indian_states)
with open('indianstates.json','w') as p:
    json.dump(Indian_states,p)
    print('Indian states Json file is writen')


    
 