import threading
import math

# using ray casting algorithm
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

countA = 0
countB = 0
countC = 0
countNone = 0
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

def check_point(edgesA, edgesB, coordinates):
    for x, y in coordinates:
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

def main():
    polygonA = [(-2, -0.5), (-2.5, -2.5), (0.5, -2), (0,0)]
    polygonB = [(-2.5, 1.4), (-1,1), (0.5, 1.4), (-1, -1)]
    polygonA.append(polygonA[0])
    polygonB.append(polygonB[0])
    edgesA = list(zip(polygonA, polygonA[1:] + polygonA[:1]))
    edgesB = list(zip(polygonB, polygonB[1:] + polygonB[:1]))

    f = open("points.txt")

    threads = []
    pointsT1 = []
    pointsT2 = []
    pointsT3 = []
    pointsT4 = []
    pCount = 0
    for line in f:
        x, y = map(float, line.split())
        if pCount <= 2500:
            pointsT1.append((x,y))
            pCount += 1
        elif pCount <= 5000:
            pointsT2.append((x,y))
            pCount += 1
        elif pCount <= 7500:
            pointsT3.append((x,y))
            pCount += 1
        else:
            pointsT4.append((x,y))
            pCount += 1

    # each thread will check 2500 points
    for i in range(4):
        if i == 0:
            thread = threading.Thread(target=check_point, args=(edgesA, edgesB, pointsT1))
            thread.start()
            threads.append(thread)
        elif i == 1:
            thread = threading.Thread(target=check_point, args=(edgesA, edgesB, pointsT2))
            thread.start()
            threads.append(thread)
        elif i == 2:
            thread = threading.Thread(target=check_point, args=(edgesA, edgesB, pointsT3))
            thread.start()
            threads.append(thread)
        else:
            thread = threading.Thread(target=check_point, args=(edgesA, edgesB, pointsT4))
            thread.start()
            threads.append(thread)
    
    f.close()
    # wait for all threads to complete
    for thread in threads:
        thread.join()

    print("~~~~~~ Multithreaded ~~~~~~")
    print(f"Count A: {countA}")
    print(f"Count B: {countB}")
    print(f"Count C: {countC}")
    print(f"Count None: {countNone}")


main()

