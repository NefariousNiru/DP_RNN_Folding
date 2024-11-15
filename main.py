import util
from rna_folding import rna_folding

if __name__ == "__main__":
    print("Enter RNA Sequence, {A, C, G, U}")
    rna_seq = str(input())
    if util.is_valid_rna(rna_seq):
        rna_folding(rna_seq, len(rna_seq))
    else:
        print(f"\033[91mInvalid RNA Sequence {rna_seq}\nRNA Sequence should only consist of 'A', 'C', 'G', 'U'\033[0m")
        exit(-1)