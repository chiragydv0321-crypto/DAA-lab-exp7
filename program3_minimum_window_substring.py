"""
Experiment 7: Hashing and Strings
Program 3: Minimum Window Substring
Aim: Find the smallest substring containing all characters of the pattern.
"""

def min_window(s, t):
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    left = 0
    missing = len(t)
    start = end = 0
    for right, ch in enumerate(s, 1):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1
        if missing == 0:
            while left < right and need.get(s[left], 0) < 0:
                need[s[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

print(min_window("ADOBECODEBANC", "ABC"))
