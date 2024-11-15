import re


def is_valid_rna(rna_seq: str) -> bool:
    rna_pattern = re.compile(r'^[ACGU]+$')
    if rna_pattern.match(rna_seq):
        return True
    return False

def get_pair_score(base1: str, base2: str) -> int:
    pair = base1 + base2
    pair_scores = {
        # Watson-Crick pair C-G gains 3 points
        "CG": 3,
        "GC": 3,
        # Watson-Crick pair A-U gains 2 points
        "AU": 2,
        "UA": 2,
        # Wobble pair G-U gains 1 point
        "GU": 1,
        "UG": 1
    }
    try:
        return pair_scores[pair]
    except KeyError:
        return 0

def traceback(i, j, trace, parenthesis):
    if i > j:
        return
    if trace[i][j] is None:
        return
    action = trace[i][j]
    if action[0] == 'PAIR':
        _, i_paired, j_paired = action
        parenthesis[i_paired] = '('
        parenthesis[j_paired] = ')'
        traceback(i + 1, j - 1, trace, parenthesis)
    elif action[0] == 'SKIP_J':
        traceback(i, j - 1, trace, parenthesis)
    elif action[0] == 'BIFURCATE':
        _, k = action
        traceback(i, k, trace, parenthesis)
        traceback(k + 1, j, trace, parenthesis)

def get_table(n: int, val: int|None):
    return [[val] * n for i in range(n)]

def print_output(table: list[list[int]], rna_seq: str, parenthesis: list[str], N: int):
    print('RNA Sequence:  ' + rna_seq)
    print('Structure:     ' + ''.join(parenthesis))
    print('Maximum Score: ' + str(table[0][N - 1]))
    print("DP Table:")
    for row in table:
        print(row)