
import matplotlib.pyplot as plt
import math

def is_inside_polygon(edges, xp, yp):
    cnt = 0
    for edge in edges:
        (x1, y1), (x2, y2) = edge
        if (yp <= y1) != (yp <= y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            cnt += 1

        # Check if point is on edge
        if min(x1, x2) <= xp <= max(x1, x2) and min(y1, y2) <= yp <= max(y1, y2):
            # Equation of the line for the edge
            if y2 - y1 == 0:  # Edge is horizontal
                if yp == y1:
                    return True
            else:  # Edge is not horizontal
                slope = (y2 - y1) / (x2 - x1)
                y_intercept = y1 - slope * x1
                if yp == slope * xp + y_intercept:  # Point lies on the line
                    return True
    return cnt % 2 == 1


def is_inside_convexQuadilateral(edges, xp, yp):
    return is_inside_polygon(edges, xp, yp)

def is_inside_nonConvexQuadilateral(edges, xp, yp):
    return is_inside_polygon(edges, xp, yp)

def is_inside_semiCircle(xp, yp, center=(1,1), radius=math.sqrt(2)):
    h, k = center
    r = radius

    # check if the point lies within the circle
    if ((xp - h) ** 2 + (yp - k) ** 2) > r ** 2:
        return False

    # check if the point lies in the upper half plane
    if yp < k:
        return False

    return True

countA = 0
countB = 0
countC = 0
countNone = 0

def main():

    polygonA = [(-2, -0.5), (-2.5, -2.5), (0.5, -2), (0,0)]
    polygonB = [(-2.5, 1.4), (-1,1), (0.5, 1.4), (-1, -1)]
    polygonA.append(polygonA[0])
    polygonB.append(polygonB[0])
    edgesA = list(zip(polygonA, polygonA[1:] + polygonA[:1]))
    edgesB = list(zip(polygonB, polygonB[1:] + polygonB[:1]))
        
    f = open("points.txt")
    for line in f:
        x, y = map(float, line.split())
        if is_inside_convexQuadilateral(edgesA, x, y):
            global countA
            countA += 1
        elif is_inside_nonConvexQuadilateral(edgesB, x, y):
            global countB
            countB += 1
        elif is_inside_semiCircle(x, y):
            global countC
            countC += 1
        else:
            global countNone
            countNone += 1
            
    f.close()

    print("~~~~~~ Sequential ~~~~~~")
    print("countA: ", countA)
    print("countB: ", countB)
    print("countC: ", countC)
    print("countNone: ", countNone)


main()

    
   
