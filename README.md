# RNA Folding Project Documentation

## **Project Overview**

This project predicts the secondary structure of an RNA sequence by using **dynamic programming**. It computes the most stable configuration of base pairs by maximizing a scoring function that includes:
1. **Base Pairing**: Valid base pairs (e.g., \( G-C \), \( A-U \)) contribute to the overall stability.
2. **Stacking**: Consecutive base pairs (e.g., \( i, j \) and \( i+1, j-1 \)) add extra stability through stacking interactions.
3. **Bifurcations**: Handles splits in the RNA sequence where it branches into multiple substructures.

---

## **Key Components**

### **1. Base Pairing**
Base pairs are identified using a scoring function (`util.get_pair_score`) that assigns a positive score for valid pairs. For any two bases \( i \) and \( j \):
- If \( i \) and \( j \) can pair, a score is added.
- Otherwise, they remain unpaired, and no score is added for that pair.

### **2. Stacking**
If two consecutive base pairs \( i, j \) and \( i+1, j-1 \) are formed, they contribute an additional **stacking bonus** to the score. This reflects the enhanced stability of stacked helices.

### **3. Bifurcations**
The algorithm considers splits within subsequences, allowing the RNA structure to branch. This is critical for capturing complex secondary structures.

---

## **Recurrence Relations**

The dynamic programming table \( S[i][j] \) stores the maximum score for the subsequence from \( i \) to \( j \).

### **1. Base Pairing**
If \( i, j \) form a valid pair:
$$
S[i][j] = S[i+1][j-1] + \text{pair_score}(i, j)
$$

### **2. Stacking**
If \( i, j \) and \( i+1, j-1 \) form valid pairs:
$$
S[i][j] = S[i+1][j-1] + \text{pair_score}(i, j) + \text{stacking_bonus}
$$

### **3. Unpaired Cases**
To skip pairing \( i \) or \( j \):
$$
S[i][j] = \max(S[i+1][j], S[i][j-1])
$$

### **4. Bifurcation**
For all \( k \) such that \( i ≤ k < j \):
$$
S[i][j] = \max(S[i][k] + S[k+1][j])
$$

### **5. Initialization**
If \( |i - j| < 4 \) (minimum distance for a valid pair):
$$
S[i][j] = 0
$$

---

## **High-Level Workflow**

1. **Dynamic Programming Table**:
   - The algorithm iterates over all subsequences of increasing lengths to compute the maximum score for each pair \( i, j \).

2. **Base Pair Checks**:
   - Evaluate if \( i \) and \( j \) can pair.
   - Add stacking bonus if consecutive pairs are detected.

3. **Bifurcation Handling**:
   - Split subsequences at various points to handle branches.

4. **Traceback**:
   - Reconstruct the optimal structure from the `trace` table, outputting a parenthesized representation of the RNA folding.

---

## **Output**

Given an RNA sequence (e.g., `GCCGAGCG`), the program outputs:
1. The dynamic programming table (`S`) with maximum scores for subsequences.
2. The optimal folding structure as a parenthesized string (e.g., `((...)).`).

---

## **Applications**

This project simulates RNA secondary structure prediction, useful in:
- Understanding RNA stability.
- Modeling RNA behavior in biological systems.
- Designing RNA-based therapeutics.

---

## **How to Run**
1. Clone the repository:
2. ```bash
   main.py
   ```
