from math import sqrt, acos, degrees

class Circle():
    def __init__(self, radius):
        self.__radius = radius
        self.__center = [0, 0]
        self.__color = "black"
        self.name = "circle"

    def set_color(self, color):
        self.__color = color

    def set_center(self, center):
        if len(center) == 2:
            self.__center = center

    def area(self):
        return  3.14159 * (self.__radius ** 2)

    def intersection(self, c_bis):
        distance = sqrt(((self.__center[0] - c_bis.__center[0]) ** 2) + ((self.__center[1] - c_bis.__center[0]) ** 2))
        return distance < self.__radius + c_bis.__radius

    def intersection_percentage(self, c_bis):
        d = sqrt((self.__center[0] - c_bis.__center[0])**2 + (self.__center[1] - c_bis.__center[1])**2)
        r = float(c_bis.__radius)
        R = float(self.__radius)
        k = ((d ** 2) + (r ** 2) - (R ** 2))
        l = ((d ** 2) + (R ** 2) - (r ** 2))
        y =  (2 * d * r)
        z = (2 * d * R)
        t = (-d + r + R)(d + r - R)(d - r + R)(d + r +R)
        print "d: %f\nr: %f\nt: %f\nk: %f\nl: %f\n" % (d, r, t, k, l)
        overlap = ((r ** 2) * degrees(acos(k/y)) + ((R ** 2) * degrees(acos(l/z))) - (sqrt(t) / 2))
        return overlap / self.area()

        if __name__ == "__main__":
            c = Circle(4)
            c.set_center([0, 0])
            c.set_color("Yellow")
            c.name = "Sun"
            print "Area of %s is %f" % (c.name, c.area())

            c1 = Circle(4)
            c1.set_center([0, 0])
            c1.name = "Sun"

            c2 = Circle(4)
            c2.set_center([1, 1])
            c2.name = "Earth"

            if c1.intersection(c2):
                print "Intersection between %s and %s" % (c1.name, c2.name)
            else:
                print "No intersection between %s and %s" % (c1.name, c2.name)

                print "%s is %f%% inside %s" % (c2.name, c1.intersection_percentage(c2), c1.name)
