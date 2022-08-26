#opening the file
def get_data(data_file:str)->list:
    """takes a file name and returns a list of strings containing data from the file"""
    data_file=open(data_file,"r")
    data_lines=data_file.readlines()
    data_file.close()
    return data_lines
#parsing the file         
def parse_data(data_lines:list)->list:
    """Takes a list of strings and removes the newline character from each string
       separate each string into separate data properties"""
    data_length=len(data_lines)
    for index in range(data_length):
        data_lines[index]=data_lines[index].strip() #removing newline character
        data_lines[index]=data_lines[index].split(',')#separate each string 
    return data_lines  
#extracting the population from the CSV
def get_populations(data_lines:list)->list:
    """takes a list of list of strings and extracts the second item on each internal list to get
    the population"""
    population=[]
    for row_index in range(len(data_lines)):
        population=population+[data_lines[row_index][2]]
    return population
#finding the leading digits
def leading_digits(population:list)->None:
    """takes a list of numbers and finds their first digit then calculates their frequency
    and prints it"""
    count=[0,0,0,0,0,0,0,0,0,0]   #setting an accumulator for count of each digit
    frequency=[0,0,0,0,0,0,0,0,0,0]#setting an accumulator for frequency of each digit
    for leading_index in range(len(population)):
        first_digit=int(population[leading_index][0])
        count[first_digit]+=1 #increasing the count for each first digit in the corresponding place on accumulator
    for num in range(1,10):
        frequency[num]=count[num]/len(population) #finding frequency by dividing with total data number
        print("Frequency of "+str(num)+" :  "+str(frequency[num]))
       
#stating the frequency if the three data tables    
print("for data1.csv the frequency is :")
leading_digits(get_populations(parse_data(get_data("data1.csv"))))
print("or data2.csv the frequency is ")
leading_digits(get_populations(parse_data(get_data("data2.csv"))))
print("for data3.csv the frequency is :")
leading_digits(get_populations(parse_data(get_data("data3.csv"))))
                       
                       
            


import turtle

turtle.tracer(0,0)
turtle.setworldcoordinates(-179, 19, -59, 70)
wn=turtle.Screen()
my_turtle = turtle.Turtle()



for data in parse_data(get_data("data3.csv")):
    latitude = float(data[0])
    longitude = float(data[1])
    radius = (float(data[2]) ** 0.5) * 0.0003

    x_cordinate = -longitude
    y_cordinate = latitude

    my_turtle.up()
    my_turtle.goto(x_cordinate, y_cordinate)
    my_turtle.down()

    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()
