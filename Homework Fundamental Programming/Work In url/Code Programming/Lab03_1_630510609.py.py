#630510609
#นายกฤตเมธ ไทยเจริญ
#003
#Lab03_1
import math#import math
def find_r_from_surface_area(a):#define function find_r_from_surface_area(a) and a = surface_area
    radius = math.sqrt(a/(4*math.pi))#calculate radius from math.sqrt(a/(4*math.pi))
    return radius#restore the radius

def sphere_volume(r):#define function find_r_from_surface_area(a) and a = surface_area
    volume = (4/3)*math.pi*(r**3)#calculate volume from (4/3)*math.pi*(r**3)
    return volume#restore the volume

def main()::#define function main
    surface_area = float(input("input surface area: "))#set surface_area to float and input by user 
    radius = find_r_from_surface_area(surface_area)#calculate radius from function find_r_from_surface_area(surface_area)
    volume = sphere_volume(radius)#calculate volume from function sphere_volume(radius)
    print("volume = {0:.2f}".format(volume))#show volume

if __name__ =='__main__':
    main()


