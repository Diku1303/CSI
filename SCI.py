def calculate_taxi_fare(distance):
    if distance == 0:
        return 0
    if distance < 0:
        return(f"Distance cannot be negative")
    fare = 0
    if distance <=1:
        fare = 15000
    if distance > 1:
        km_2_to_10 = min(distance - 1, 9)
        fare += km_2_to_10 * 13500
    if distance > 10:
        km_11_onward = distance - 10
        fare += km_11_onward * 11000
    if distance > 120:
        fare *= 0.9
    if distance > 200:
        print(f"Value exceeded")
    return int(fare)

distance_traveled = float(input("Enter distance traveled (km): "))
total_fare = calculate_taxi_fare(distance_traveled)
print(f"Total taxi fare: {total_fare:} VND")