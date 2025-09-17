class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        char_indices = {}
        for i, char in enumerate(s):
            if char in char_indices:
                char_indices[char].append(i)
            else:
                char_indices[char] = [i]
        
        for char in char_indices:
            char_index = char_indices[char]
            char_distance = char_index[1] - char_index[0] - 1
            if char_distance != distance[ord(char) - ord('a')]:
                return False
        return True
