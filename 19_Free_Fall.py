# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
# due to gravity is 9.8m/s2. You can use the formula vf = vi2 + 2ad to compute the
# final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known.

height = int(input("Enter the  height (in meters) from which the object is dropped: "))
gravity = 9.8
initial_speed = 0
final_speed = (initial_speed**2 + 2 * gravity * height) ** 0.5
print(f"The object hits the ground at a speed of {final_speed} m/s")