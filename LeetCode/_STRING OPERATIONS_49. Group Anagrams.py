# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from tokenize import group


def groupAnagrams(strs):
    grouped = {}

    for str in strs:
        sorted_str = sorted(str)

        if sorted_str not in grouped.keys():
            grouped[sorted_str] = []
            grouped[sorted_str].append(str)

        else:
            grouped[sorted_str].append(str)

    return grouped.values()

def groupAnagrams_2(strs):
    grouped = {}

    for str in strs:
        sorted_str = ''.join(sorted(str))      

        if sorted_str not in grouped.keys():
            grouped[sorted_str] = []
            grouped[sorted_str].append(str)

        else:
            grouped[sorted_str].append(str)

    return grouped.values()

strs1 = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs1))