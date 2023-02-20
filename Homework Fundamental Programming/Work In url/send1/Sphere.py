import math
def find_r_from_surface_area(a):
    radius = math.sqrt(a/(4*math.pi))
    return radius

def sphere_volume(r):
    volume = (4/3)*math.pi*(r**3)
    return volume

def main():
    surface_area = float(input("input surface area: "))
    radius = find_r_from_surface_area(surface_area)
    volume = sphere_volume(radius)
    print("volume = {0:.2f}".format(volume))

if __name__ =='__main__':
    main()


