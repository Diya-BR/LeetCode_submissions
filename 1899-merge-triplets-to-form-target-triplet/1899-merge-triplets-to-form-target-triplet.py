from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        
        for triplet in triplets:
            # Simply skip the invalid triplets instead of removing them
            if (triplet[0] > target[0] or 
                triplet[1] > target[1] or 
                triplet[2] > target[2]):
                continue
            
            # Record matching positions
            if triplet[0] == target[0]: found[0] = True
            if triplet[1] == target[1]: found[1] = True
            if triplet[2] == target[2]: found[2] = True
            
            # Early exit if we have found all three matches
            if all(found):
                return True
                
        return all(found)
