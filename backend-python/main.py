import argparse
from openai import OpenAI
from dotenv import load_dotenv
from os import getenv


load_dotenv()

def runAI(para):
    client = OpenAI(api_key=getenv('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": para},
            {"role": "user",
                "content": """
                Output a habitation guide based on the following 7 inputs from the previous prompt,
                Argument 1: Water Availability
                Argument 2: Atmospheric Condtions
                Argument 3: Temperature Range
                Argument 4: Geological Activity
                Argument 5: Magnetic Field
                Argument 6: Star Stability
                Argument 7: Orbital Stability
                Use the score from 0-3 by the weight in order and give explanation of survivability and how to survive in a paragraph format
                Parse the arguments in accordance with the above list.
                For example, the first number inputted is the water availability score, and the fourth input is the geological activity score.
                Explanations of scores are defined as following:
                    If the value is -1 disregard the category and make sure to mention the summary may be less accuracy due to the missing data.
                        'Water availability':       0: No water available; 1: Potential for water; 2: Water in non-liquid form; 3: Liquid water available
                        'Atmospheric conditions':   0: No atmosphere or toxic to life; 1: Thin atmosphere lacking pressure or composition; 2: Atmosphere present but not Earthlike; 3: Earthlike Atmosphere 
                        'Temperature Range':        0: Extreme cold or heat (200+°C or -50°C and below); 1: Very high heat or cold (100°C to 200°C and -50°C to -25°C); 2: Marginally suitable temperature (50°C to 100°C and 0°C to -25°C; 3: Optimal temperature (0°C to 50°C)
                        'Geological Activity':      0: No geological activity; 1: Low geological activity; 2: Moderate geological activity; 3: High geological activity
                        'Magnetic Field':           0: No magnetic field; 1: Low strength magnetic field; 2: Moderate strength magnetic field; 3: Strong magnetic field
                        'Star Stability':           0: Highly variable or end-of-life star; 1: Unstable star with significance variance; 2: Stable with slight variance (may be slight off main sequence); 3: Main sequence star with stable output
                        'Orbital Stability':        0: Highly variable and unstable orbit; 1: Variable and eccentric orbit; 2: Elliptical but stable orbit; 3: Near-Circular orbit
                Output a 200-250 word paragraph
                """}
        ],
    )
    return completion.choices[0].message

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
str1 = str(args.water_avail) + " - Water Availability"
str2 = str(args.atmosphere) + " - Atmospheric Condtions"
str3 = str(args.temp_range) + " - Temperature Range"
str4 = str(args.geo_activity) + " - Geological Activity"
str5 = str(args.magnetic_field) + " - Magnetic Field"
str6 = str(args.star_stab) + " - Star Stability"
str7 = str(args.orbital_stab) + " - Orbital Stability"
para = str1 + " " + str2 + " " + str3 + " " + str4 + " " + str5 + " " + str6 + " " + str7
strats = runAI(para)

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
print(strats.content)