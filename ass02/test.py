
import matplotlib.pyplot as plt
import math
import time
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
            print(f"Point [{x}, {y}] is inside A")
        elif is_inside_nonConvexQuadilateral(edgesB, x, y):
            print(f"Point [{x}, {y}] is inside B")
        elif is_inside_semiCircle(x, y):
            print(f"Point [{x}, {y}] is inside C")
        else:
            print(f"Point [{x}, {y}] is outside all")


if __name__ == '__main__':

   

# polygon = random_polygon(num_points=4)
# polygon = [(-2, -0.5), (-2.5, -2.5), (0.5, -2), (0,0)]
# polygon = [(-2.5, 1.4), (-1,1), (0.5, 1.4), (-1, -1)]
# polygon.append(polygon[0])
# edges = list(zip(polygon, polygon[1:] + polygon[:1]))
# plt.figure(figsize=(10, 10))
# plt.gca().set_aspect("equal")
# xs, ys = zip(*polygon)
# plt.gcf().canvas.mpl_connect('button_press_event', onclick)
# plt.plot(xs, ys, "b-", linewidth=0.8)
# plt.show()
