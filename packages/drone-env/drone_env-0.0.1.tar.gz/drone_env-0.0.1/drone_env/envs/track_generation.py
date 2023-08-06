import numpy as np
from itertools import combinations
from utils import separation, intersect


class TrackGenerator:
    def __init__(self, size, border, collinear_threshold, separation_threshold, segment_count=0):
        self.offset = None
        self.scale = None
        if segment_count == 0:
            self.point_count = None
            self.rand_point_count = True
        else:
            self.point_count = segment_count + 1
            self.rand_point_count = False
        self.collinear_threshold = collinear_threshold
        self.separation_threshold = separation_threshold

        self.size = size
        self.border = border

    def track_generate(self):
        accept = False
        point_list = None
        trial = 0

        if not self.rand_point_count:
            self.scale = np.tile(self.size, (self.point_count, 1))
            self.offset = np.tile(self.border, (self.point_count, 1))

        while not accept:
            if self.rand_point_count:
                self.point_count = np.random.randint(2, 8)
                self.scale = np.tile(self.size, (self.point_count, 1))
                self.offset = np.tile(self.border, (self.point_count, 1))
            trial = 0

            while not (accept or trial > 10000):
                trial += 1

                # Roll the Points and Scale
                point_list = np.random.rand(self.point_count, 2)
                point_list = np.multiply(point_list, self.scale)

                # Check Collinearity
                if self.check_collinearity(point_list):
                    continue

                # Check Point Separation
                if self.check_point_separation(point_list):
                    continue

                # Arrange the Point List
                point_list = self.arrange(point_list)

                # Check Track Intersection (Not Working)
                if self.check_intersection(point_list):
                    continue

                # Accept the Points
                accept = True

        # Order Way Points
        return point_list

    def check_collinearity(self, point_list):
        flag = False

        # Calculate the Angle for each Pair of Points
        angles = [np.arctan2((point_list[i] - point_list[j])[1], (point_list[i] - point_list[j])[0])
                  for (i, j) in list(combinations(range(self.point_count), 2))]
        angles = [a if a >= 0 else a + np.pi for a in angles]

        for (i, j) in list(combinations(range(len(angles)), 2)):
            if abs(angles[i] - angles[j]) < self.collinear_threshold:
                flag = True
                break

        return flag

    def check_point_separation(self, point_list):
        flag = False

        # Check every Combination of 2 Points
        for [i, j] in list(combinations(range(self.point_count), 2)):
            d = separation(point_list[i], point_list[j])
            if d < self.separation_threshold[0] or d > self.separation_threshold[1]:
                flag = True
                break

        return flag

    def arrange(self, point_list):
        # Put the First point in
        way_points = np.ndarray((1, 2))
        way_points[0] = point_list[0]
        point_list = np.delete(point_list, 0, 0)

        # Arrange the Rest of Points except the Last
        while len(point_list) > 1:
            # Scan for Closest Next Point
            d = [separation(way_points[-1], point_list[i]) for i in range(len(point_list))]
            i = np.argmin(d)

            # Pop the Point from "point_list" to "way_points"
            way_points = np.vstack((way_points, point_list[i]))
            point_list = np.delete(point_list, i, 0)

        # Add the Last Point
        return np.add(np.vstack((way_points, point_list)), self.offset)

    def check_intersection(self, point_list):
        flag = False

        # Pick the set of Line Segments to be Checked
        lp = list(combinations(range(self.point_count - 1), 2))
        lp = [i for i in lp if abs(i[0] - i[1]) != 1]

        for i in lp:
            if intersect(point_list[i[0]], point_list[i[0] + 1], point_list[i[1]], point_list[i[1] + 1]):
                flag = True
                break

        return flag
