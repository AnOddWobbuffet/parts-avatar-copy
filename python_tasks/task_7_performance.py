# Task: Performance Optimization
# Instructions: You have a list of 10,000 banned emails. 
# Write a function that checks if a user's email is banned in an efficient way.

def banned_list(banned):
    banned_list = {}
    for b in banned:
        banned_list[b] = 1

def is_banned(email, banned_dict):
    # TODO: Implement the search logic
    if email in banned_dict:
        return True
    return False

# Test
banned = ["user1@test.com", "user2@test.com"] # Pretend this is 10k items
banned_dict = banned_list(banned)
print(is_banned("user1@test.com", banned))
print(is_banned("user5@test.com", banned))