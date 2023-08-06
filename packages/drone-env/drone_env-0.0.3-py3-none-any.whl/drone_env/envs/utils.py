import numpy as np


def offtrack(p1, p2, p):
    line = tuple((p2[i]-p1[i])*1. for i in (0, 1))
    pos_r = tuple(p[i]-p1[i]*1. for i in (0, 1))

    proj = (line[0]*pos_r[0] + line[1]*pos_r[1])/separation(p1, p2)
    return separation(p1, p) if proj < 0 else separation(p2, p) if proj > 1 else np.sqrt(abs(separation(p1, p)**2 - proj**2))


def separation(p1, p2):
    d = (p1[0] - p2[0], p1[1] - p2[1])
    return np.sqrt(d[0] ** 2 + d[1] ** 2)


def projection(p1, p2, d):
    track = (p2[0] - p1[0], p2[1] - p1[1])
    track_length = np.sqrt(track[0] ** 2 + track[1] ** 2)
    track_dir = [t / track_length for t in track]

    return track_dir[0] * d[0] + track_dir[1] * d[1]


def on_segment(p, q, r):
    if ((q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and
            (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
        return True
    else:
        return False


def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    if (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1])) > 0:
        # Clockwise orientation
        return 1
    else:
        # Counterclockwise orientation
        return 2


def intersect(p1, q1, p2, q2):
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if (o1 != o2) and (o3 != o4):
        return True
    else:
        return False


def rpy2rot(euler):
    theta1 = euler[2]
    theta2 = euler[1]
    theta3 = euler[0]

    c1 = np.cos(theta1 * np.pi / 180)
    s1 = np.sin(theta1 * np.pi / 180)
    c2 = np.cos(theta2 * np.pi / 180)
    s2 = np.sin(theta2 * np.pi / 180)
    c3 = np.cos(theta3 * np.pi / 180)
    s3 = np.sin(theta3 * np.pi / 180)

    matrix = np.array([[c2 * c3, -c2 * s3, s2],
                       [c1 * s3 + c3 * s1 * s2, c1 * c3 - s1 * s2 * s3, -c2 * s1],
                       [s1 * s3 - c1 * c3 * s2, c3 * s1 + c1 * s2 * s3, c1 * c2]])

    return matrix.flatten()

