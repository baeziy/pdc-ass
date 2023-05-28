import math

def is_inside_semiCircle(center, radius, xp, yp):
    h, k = center
    r = radius

    # check if the point lies within the circle
    if ((xp - h) ** 2 + (yp - k) ** 2) > r ** 2:
        return False

    # check if the point lies in the upper half plane
    if yp < k:
        return False

    return True

# Usage:
center = (1,1)
radius = math.sqrt(2)
xp, yp = 2.3, 1 # Example point
print(is_inside_semiCircle(center, radius, xp, yp))
