"""The latest gossip in the henchman breakroom is that "LAMBCHOP" stands for "Lambda's Anti-Matter Biofuel Collision Hadron Oxidating Potentiator". You're pretty sure it runs on diesel, not biofuel, but you can at least give the commander credit for trying."""
"""

Please Pass the Coded Messages
==============================

You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9).
Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3.
If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.
The same digit may appear multiple times in the list, but each element in the list may only be used once.

Languages


-- Python cases --
Input:
solution.solution([3, 1, 4, 1])
Output:
    4311

Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311
"""
def make_biggest_number(L):
    L.sort(reverse= True)
    if not L:
        return 0
    answer = ""
    for i in L:
        answer += str(i)
    return int(answer)

def get_biggest_divisible_3(L):
    residual = sum(L) % 3
    if residual == 0:
        return L
    else:
        candidate = 10
        for i in L:
            if i % 3 == residual and i < candidate:
                candidate = i
        if candidate < 10:
            L.remove(candidate)
            return L

        else:
            candidates = [10, 10]
            for i in L:
                if i % 3 != 0 and i < max(candidates):
                    candidates.remove(max(candidates))
                    candidates.append(i)
            if max(candidates) < 10:
                for candidate in candidates:
                    L.remove(candidate)
                return L
            else:
                return []

def solution(l):
    biggest_numbers = get_biggest_divisible_3(l)
    answer = make_biggest_number(biggest_numbers)
    return answer
