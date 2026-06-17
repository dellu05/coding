"""D. Goods on the Shelf

Time limit: 2 seconds Memory limit: 512 megabytes

In a supermarket, goods of the same type are usually placed next to each other
so that the shelf looks neat and it is easier for customers to find what they
need.

The shelf is described by an array a of n elements, where a_i is the type of the
good at position i.

We will say that the shelf is arranged correctly if for every two positions i
and j such that 1 \le i < j \le n and a_i = a_j, the following condition holds:
for each k from i to j, it is true that a_k = a_i. In other words, goods of each
type on the shelf must form one contiguous block.

You are allowed to choose two different positions at most once and swap the
goods at these positions. You may also choose not to perform any swap.

Determine whether it is possible to make the shelf arranged correctly after
that.

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 10^4). The description of the test cases follows.

The first line of each test case contains an integer n
(2 \le n \le 2 \cdot 10^5) — the number of goods on the shelf.

The second line of each test case contains n integers a_i (1 \le a_i \le 10^9),
where a_i denotes the type of the good at position i.

Additional input constraints:

  - The sum of n over all test cases does not exceed 2 \cdot 10^5.

Output

For each test case, output one of the following:

  - NO, if it is impossible to arrange the shelf correctly;
  - YES, if it is possible to make the shelf arranged correctly with at most one
    swap of two goods.

You may output the answer in any case (for example, yes, YES, No, no will also
be accepted).

Example

Input:

7
3
1 2 1
2
7 7
6
1 2 3 1 2 3
6
1 1 2 3 2 3
7
1 2 3 1 2 3 4
6
1 2 1 2 1 1
6
1 2 2 3 3 1

Output:

YES
YES
NO
YES
NO
YES
NO

Note

1.  In the first example, you can swap the goods at positions 1 and 2, after
    which the shelf will look like this: [2, 1, 1].
2.  In the second example, the shelf is already arranged correctly.
3.  In the third example, it is impossible to arrange the shelf correctly with
    one swap.
4.  In the sixth example, you can swap the goods at positions 1 and 4, after
    which the shelf will be arranged correctly.
"""

def solve():
    # Fast I/O
    input_data = input().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    output = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        a = list(map(int, input_data[ptr : ptr + n]))
        ptr += n
        
        if n <= 1:
            output.append("YES")
            continue
            
        # 1. Identify segments (contiguous blocks)
        segments = [] 
        curr_val = a[0]
        curr_start = 0
        for i in range(1, n):
            if a[i] != curr_val:
                segments.append((curr_val, curr_start, i - 1))
                curr_val = a[i]
                curr_start = i
        segments.append((curr_val, curr_start, n - 1))
        
        b_orig = len(segments)
        val_block_count = {}
        for s in segments:
            val_block_count[s[0]] = val_block_count.get(s[0], 0) + 1
        
        d = len(val_block_count)
        
        # Already correct
        if b_orig == d:
            output.append("YES")
            continue
        
        # Heuristic: 1 swap can only reduce block count by a small constant.
        if b_orig > d + 10:
            output.append("NO")
            continue
            
        # 2. Select candidate indices for swapping
        split_vals = {v for v, count in val_block_count.items() if count > 1}
        relevant_seg_indices = set()
        for i in range(b_orig):
            if segments[i][0] in split_vals:
                relevant_seg_indices.add(i)
                if i > 0: relevant_seg_indices.add(i - 1)
                if i < b_orig - 1: relevant_seg_indices.add(i + 1)
        
        candidate_indices = set()
        for idx in relevant_seg_indices:
            candidate_indices.add(segments[idx][1]) 
            candidate_indices.add(segments[idx][2])
        
        cand_list = sorted(list(candidate_indices))
        found = False
        
        # O(1) check to see if swap results in B == D
        def check_swap(i, j):
            if a[i] == a[j]: return False
            
            check_pos = set()
            for p in [i, i + 1, j, j + 1]:
                if 0 < p < n: check_pos.add(p)
            
            diff_before = 0
            for p in check_pos:
                if a[p] != a[p-1]: diff_before += 1
            
            a[i], a[j] = a[j], a[i] # Swap
            
            diff_after = 0
            for p in check_pos:
                if a[p] != a[p-1]: diff_after += 1
            
            is_ok = (b_orig - diff_before + diff_after == d)
            a[i], a[j] = a[j], a[i] # Restore
            return is_ok

        for idx_i in range(len(cand_list)):
            for idx_j in range(idx_i + 1, len(cand_list)):
                if check_swap(cand_list[idx_i], cand_list[idx_j]):
                    found = True
                    break
            if found: break
        
        output.append("YES" if found else "NO")
        
    print("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()
