"""Building a File Zipper 
Difficulty level: Medium
This project focuses on building a file compression tool using a Greedy Huffman encoder or Run-Length Encoding. This File Zipper tool compresses a large file or directory into a single compressed file that saves your memory storage. These compressed files are usually of smaller sizes and are easy to transfer from one machine to another.
Learning outcomes:
    • Knowledge of algorithms like Huffman coding, RLE (Run-Length Encoding), or LZW (Lempel-Ziv-Welch), required for compressing and decompressing files
    • Understanding binary trees and the Tries data structures particularly used in Huffman coding to efficiently encode and decode your data
    • Gain experience with handling bits and bytes for file compression 
    • Knowledge of designing user interfaces for users to interact with the system 
"""
#Run-Length Encoding (RLE)
def rle_encode(data):
    if not data: return ""
    encoding = ""
    prev_char = data[0]
    count = 0
    
    for char in data:
        if char == prev_char:
            count += 1
        else:
            encoding += str(count) + prev_char
            prev_char = char
            count = 1
    encoding += str(count) + prev_char
    return encoding

def rle_decode(data):
    decode = ""
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ""
    return decode

# Test
text = "AAAAAABBBCCCCCDDE"
compressed = rle_encode(text)
print(f"RLE Compressed: {compressed}") 
print(f"RLE Decoded: {rle_decode(compressed)}")
#Huffman Coding (Simplified)
import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char, self.freq = char, freq
        self.left = self.right = None
    
    # Required for heapq to compare nodes
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # 1. Count frequencies
    counts = Counter(text)
    # 2. Put nodes in a priority queue (Min-Heap)
    heap = [Node(char, freq) for char, freq in counts.items()]
    heapq.heapify(heap)
    
    # 3. Build the tree by merging two smallest nodes
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged = Node(None, n1.freq + n2.freq)
        merged.left, merged.right = n1, n2
        heapq.heappush(heap, merged)
    return heap[0]

def generate_codes(node, current_code="", codes={}):
    if node:
        if node.char is not None: # It's a leaf node
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(text):
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, root

def huffman_decode(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root
    return decoded_text

# Test
msg = "huffman coding is fun"
encoded, tree = huffman_encode(msg)
print(f"Huffman Bits: {encoded}")
print(f"Huffman Decoded: {huffman_decode(encoded, tree)}")
