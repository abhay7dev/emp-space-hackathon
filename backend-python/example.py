from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def run(para):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    water_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": para},
            {"role": "user",
                "content": """
                Output a habitation guide based on the following 7 inputs from the system content,
                1. water availability, 2. atmospheric conditions,
                3.temperature range, 4.geological activity, 5.magnetic field, 6.star stability,
                7.orbital stability with. use the score from 0-3 by the weight in order and give explanation of survivability
                and how to survive in a paragraph format parse the numbers in corresponding order. for example, the first number
                inputted is the water availility score, and the 4th input system would be the geological activity score
                explanations of scores are defined as the following enclosed by the square brackets
                [water availability: 0, no water or potential; 1, solid or water vapor; 2, limited liquid water; 3, abundant liquid water
                atmospheric conditions: 0, no atmosphere or harmful gas; 1, thin atmosphere; 2, good atmosphere but not earthlike; 3, earthlike atmosphere
                'Temperature Range': 0, Extreme temperatures, uninhabitable; 1, Marginally habitable with significant temperature fluctuations; 2, Generally suitable but with some temperature variations; 3, Optimal, stable temperature range 
                'Geological Activity': 0, No geological activity, stagnant surface; 1, Minimal geological activity, limited surface dynamics; 2, Moderate geological activity, some surface renewal; 3, High geological activity, dynamic surface with nutrient recycling
                'Magnetic Field': 0, No magnetic field, no protection from radiation; 1, Weak magnetic field, limited protection; 2, Moderate magnetic field, partial protection; 3, Strong magnetic field, robust protection from radiation
                'Star Stability': 0, Highly unstable star with severe variability; 1, Unstable star with significant variations; 2, Stable star with minor luminosity fluctuations; 3, Stable star with optimal luminosity and energy output
                Orbital Stability': 0, Highly eccentric or unstable orbit, extreme temperature variations; 1, Highly eccentric orbit with significant temperature fluctuations; 2, Stable orbit with minor temperature variations; 
                3, Circular orbit within the habitable zone with stable conditions, for any of the categories, if the score is -1, disregard the category and mention that the score may be less accurate due to missing data. Remember that a score of 0 does not mean
                the data is absent, rather, the score is just very low]
                """}
        ],
    )



    print(water_completion.choices[0].message)


#water content
#atmospheric content
#temperature range
# required data to pass to chatgpt
# Output a "habitable" score given these parameters. Return only 1 integer in the range 0 - 100. Water=Available, Temperature=70F