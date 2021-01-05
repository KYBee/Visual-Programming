import math
sin_angle = 0

# 0 ~ 720도 까지
for i in range(48):
    sin_angle = (sin_angle + 15) % 360    
    dot_point = int(round(math.sin(math.radians(sin_angle)), 1) * 10)

    print(" " * (10 + dot_point), "*")
