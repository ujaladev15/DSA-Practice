class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """

        # Find the closest point on the rectangle to the circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Squared distance from circle center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        distance_squared = dx * dx + dy * dy

        # Overlap if closest point is inside/on the circle
        return distance_squared <= radius * radius
        