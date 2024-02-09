#a hellow function 

def hello():
    print("hello from the hello function")



#another function 
def funtion_with_parameter(fname,sname):

    print(fname +" " + sname)



#calculate of area of square

def area(height , base):

    area_of_object  = (0.5*base) * height

    return area_of_object

 


base_of_triangle = float(input("enter the base "))
height_of_triangle = float(input("enter the height "))

print( "the area of a triangle is ")
print(area(base_of_triangle, height_of_triangle))