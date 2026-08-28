# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

def count_categories(categories):
    # TODO: Write your logic here
    result = {}
    for cat in categories:
        if result.get(cat, ''):
            result[cat] += 1
        else:
            result[cat] = 1
    return result

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))