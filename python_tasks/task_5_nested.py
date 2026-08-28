# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # TODO: Write your logic here safely
    if data.get('specs', None):
        if data['specs']['model_info']:
            if data['specs']['model_info']['year']:
                return data['specs']['model_info']['year']
    
    return 'Unkown'

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))