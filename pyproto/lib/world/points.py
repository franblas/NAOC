import math

HEADING_TO_RADIAN = (360.0/4096.0) * (math.pi/180.0)

# Cartesian grid:
#        90
#         |
# 180 --------- 0
#         |
#        270
#
# Heading grid:
#       2048
#         |
# 1024 ------- 3072
#         |
#         0

def new_coordinates_from_heading(x, y, heading, distance):
    angle = float(heading) * HEADING_TO_RADIAN
    target_x = float(x) - math.sin(angle) * distance
    target_y = float(y) + math.cos(angle) * distance
    res_x = target_x if (target_x > 0) else 0
    res_y = target_y if (target_y > 0) else 0
    return int(res_x), int(res_y)

def opposite_heading(heading):
    if heading >= 2048:
        return heading - 2048
    else:
        return heading + 2048

def left_heading(heading):
    if heading >= 3072:
        return heading - 3072
    else:
        return heading + 1024
