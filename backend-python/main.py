import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Process some arguments.")

#Parse the seven main factors
parser.add_argument("water_avail", type=int, help="The first argument passed from the command line")
parser.add_argument("atmosphere", type=int, help="The second argument passed from the command line")
parser.add_argument("temp_range", type=int, help="The third argument passed from the command line")
parser.add_argument("geo_activity", type=int, help="The fourth argument passed from the command line")
parser.add_argument("magnetic_field", type=int, help="The fifth argument passed from the command line")
parser.add_argument("star_stab", type=int, help="The sixth argument passed from the command line")
parser.add_argument("orbital_stab", type=int, help="The seventh argument passed from the command line")

# Parse the arguments
args = parser.parse_args()

#Print out the factor scores
# print(f"Received water availability: {args.water_avail}")
# print(f"Received atmosphere: {args.atmosphere}")
# print(f"Received temperature range: {args.temp_range}")
# print(f"Received geological activity: {args.geo_activity}")
# print(f"Received magnetic field: {args.magnetic_field}")
# print(f"Received star stability: {args.star_stab}")
# print(f"Received orbital stability: {args.orbital_Stab}")

factors_entered = 7
water_weight = 50
atmos_weight = 50
temp_weight = 30
geo_weight = 10
magnet_weight = 20
star_weight = 20
orbit_weight = 20
total_weight = water_weight + atmos_weight + temp_weight + geo_weight + magnet_weight + star_weight + orbit_weight


for arg_name in vars(args):
    value = getattr(args, arg_name)
    #print(f"{arg_name}: {value}")   
    #Check if the value is -1
    # if value == -1 or value == '-1':
    #     print(f'N/A found for {arg_name}')
    #     factors_entered -= 1
        
# calculate total weight (used when user doesn't input data for all fields)
# else statement adds to the sum when the data does exist
sum = 0
if args.water_avail == -1:
    total_weight -= water_weight
else:
    sum += args.water_avail * water_weight
    
if args.atmosphere == -1:
    total_weight -= atmos_weight
else:
    sum += args.atmosphere * atmos_weight
    
if args.temp_range == -1:
    total_weight -= temp_weight
else:
    sum += args.temp_range * temp_weight
    
if args.geo_activity == -1:
    total_weight -= geo_weight
else:
    sum += args.geo_activity * geo_weight
    
if args.magnetic_field == -1:
    total_weight -= magnet_weight
else:
    sum += args.magnetic_field * magnet_weight
    
if args.star_stab == -1:
    total_weight -= star_weight
else:
    sum += args.star_stab * star_weight
    
if args.orbital_stab == -1:
    total_weight -= orbit_weight
else:
    sum += args.orbital_stab * orbit_weight
    

total_score = total_weight * 3

survivability_index = sum/total_score * 100
print(float(f"{survivability_index:.2f}"))


