import argparse
from openai import OpenAI

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

# create the parameters for the GPT prompt
str1 = str(args.water_avail)
str2 = str(args.atmosphere)
str3 = str(args.temp_range)
str4 = str(args.geo_activity)
str5 = str(args.magnetic_field)
str6 = str(args.star_stab)
str7 = str(args.orbital_stab)
para = str1 + " " + str2 + " " + str3 + " " + str4 + " " + str5 + " " + str6 + " " + str7
run(para)

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
run(para)
print(float(f"{survivability_index:.2f}"))


def run(para):
    client = OpenAI(api_key="sk-UfkCimKnd9lWjo-B7CtfiWWKSPEUeJvjQULuvJjSpwT3BlbkFJLAGZjP3fPX51LR1JmJl2uhrwm2lT2I_K3W1tchnpEA")
    water_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": para},
            {"role": "user",
                "content": "Output a habitation guide based on the following 7 inputs from the system content,\
                    1. water availability, 2. atmospheric conditions,\
                        3.temperature range, 4.geological activity, 5.magnetic field, 6.star stability,\
                            7.orbital stability with. use the score from 0-3 by the weight in order and give explanation of survivability and how to survive in a paragraph format\
                            parse the numbers in corresponding order. for example, the first number inputted is the water availility score, and the 4th input system would be the geological activity score\
                                explanations of scores are defined as following \
                                    if the value is -1 disregard the category and make sure to mention the summary may be less accuracy due to the missing data \
                                water availability: 0, no water or potential; 1, solid or water vapor; 2, limited liquid water; 3, abundant liquid water\
                                atmospheric conditions: 0, no atmosphere or harmful gas; 1, thin atmosphere; 2, good atmosphere but not earthlike; 3, earthlike atmosphere\
                                'Temperature Range': 0, Extreme temperatures, uninhabitable; 1, Marginally habitable with significant temperature fluctuations; 2, Generally suitable but with some temperature variations; 3, Optimal, stable temperature range \
                                'Geological Activity': 0, No geological activity, stagnant surface; 1, Minimal geological activity, limited surface dynamics; 2, Moderate geological activity, some surface renewal; 3, High geological activity, dynamic surface with nutrient recycling \
                                'Magnetic Field': 0, No magnetic field, no protection from radiation; 1, Weak magnetic field, limited protection; 2, Moderate magnetic field, partial protection; 3, Strong magnetic field, robust protection from radiation \
                                'Star Stability': 0, Highly unstable star with severe variability; 1, Unstable star with significant variations; 2, Stable star with minor luminosity fluctuations; 3, Stable star with optimal luminosity and energy output \
                                Orbital Stability': 0, Highly eccentric or unstable orbit, extreme temperature variations; 1, Highly eccentric orbit with significant temperature fluctuations; 2, Stable orbit with minor temperature variations; 3, Circular orbit within the habitable zone with stable conditions \  "}
        ],
    )
    
    water_completion.choices[0].message

