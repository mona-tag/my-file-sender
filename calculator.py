import math

def calculate_circle_area(n_slices):
    R = 1.0
    dr = R / n_slices

    precise_area = math.pi * R**2
    trapezoid_sum = 0
    rectangle_sum = 0

    for i in range(n_slices):
        r = i * dr

        s_trapezoid = (2 * math.pi * r +2 * math.pi * (r + dr)) * dr / 2
        trapezoid_sum += s_trapezoid

        s_rectangle = (2 * math.pi * r) * dr
        rectangle_sum += s_rectangle

        print(f"切割份数: {n_slices}")
        print(f"真实圆面积(pi): {precise_area:.10f}")
        print(f"梯形之和(精确): {trapezoid_sum:.10f}")
        print(f"长方形之和(近似): {rectangle_sum:.10f}")
        print(f"近似误差: {abs(precise_area-rectangle_sum):.10f}")
        print("-" * 20)

calculate_circle_area(10)
calculate_circle_area(100)
calculate_circle_area(10000)

