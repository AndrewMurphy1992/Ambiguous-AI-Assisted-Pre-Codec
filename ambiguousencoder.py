

def count_characters(data):
    # Create an empty dictionary to store character counts
    char_count = {}

    # Iterate through each character in the string
    for char in data:
        # Skip newline characters
        if char == '\n':
            continue
        
        # Check if the character is already in the dictionary
        if char in char_count:
            # If yes, increment its count by 1
            char_count[char] += 1
        else:
            # If no, add it to the dictionary with a count of 1
            char_count[char] = 1

    # Sort characters by their counts in ascending order
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1])

    # Pair the least common letter with the most common, the second least common with the second most common, and so on
    compound_characters = {}
    while sorted_chars:
        least_common = sorted_chars.pop(0)
        most_common = sorted_chars.pop()
        
        compound_characters[most_common[0] + least_common[0]] = (most_common[1], least_common[1])

    # Rewrite the data by replacing low occurrence characters with high occurrence characters
    for compound_char, counts in compound_characters.items():
        high_occurrence_char = compound_char[0]
        low_occurrence_char = compound_char[1]

        # Replace all occurrences of low occurrence char with high occurrence char in data
        data = data.replace(low_occurrence_char, high_occurrence_char)

    # Print the modified data
    print(data)
   
# Example usage:
with open("AskPython.txt") as f:
    data = f.read()

count_characters(data)

#apply huffman function to data


import heapq
from collections import defaultdict

# Define the Huffman encoding function
def huffman_encoding(data):
    # Count frequency of each character
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    # Create a priority queue to hold the nodes
    min_heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(min_heap)

    # Build Huffman tree
    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(min_heap, merged)

    # Generate codes from the tree
    codes = {}
    def generate_codes(node, code):
        if node:
            if node.char:
                codes[node.char] = code
            generate_codes(node.left, code + '0')
            generate_codes(node.right, code + '1')
    generate_codes(min_heap[0], '')

    # Encode the data using generated Huffman codes
    encoded_data = ''.join(codes[char] for char in data)

    return encoded_data, codes

# Define Node class for Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Example usage:
with open("AskPython.txt") as f:
    data = f.read()

# Modify data by replacing low occurrence characters with high occurrence characters
modified_data = count_characters(data)

# Apply Huffman encoding to modified data
encoded_data, huffman_codes = huffman_encoding(data)

# Print encoded data and Huffman codes
print("Encoded Data:", encoded_data)
print("Huffman Codes:", huffman_codes)



