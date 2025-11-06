# You are given the results of a sequence of matches played by India in ODIs.
#  A win is represented by 'W' and a loss is represented by 'L'. 
# A winning streak is a string of consecutive wins. 
# For example, if India has played five matches with the following results - 'WLWWWL' - then it has a three-match streak. 
# Write a code to accept the result-sequence as input and find the longest streak in it.

# Accept input
results = input("Enter the match results (W for win, L for loss): ")

max_streak = 0 
current_streak = 0  

for result in results:
    if result == 'W':
        current_streak += 1  
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0  
print("Longest winning streak:", max_streak)


# Input: WLWWWL
# Output: Longest winning streak: 3

# Input: WWLWLWWWLW
# Output: Longest winning streak: 3