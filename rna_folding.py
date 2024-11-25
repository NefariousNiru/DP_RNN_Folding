import util

def rna_folding(rna_seq, N):
    S = util.get_table(N, 0)
    trace = util.get_table(N, None)
    stacking_bonus = 1

    for length in range(4, N + 1):  # Minimum distance is 4
        for i in range(N - length + 1):
            j = i + length - 1

            # During the loop if distance is less than 4 skip
            if abs(i - j) < 4:
                trace[i][j] = ('SKIP_I', i)
                continue

            max_score = S[i][j - 1]  # Case where j is unpaired
            trace[i][j] = ('SKIP_J', j)

            if max_score < S[i + 1][j]:
                max_score = S[i + 1][j]# case where i is unpaired
                trace[i][j] = ('SKIP_I', i)

            # Check if i and j can pair
            pair_score = util.get_pair_score(rna_seq[i], rna_seq[j])
            if pair_score > 0:
                if i + 1 <= j - 1:
                    inner_pair_score = util.get_pair_score(rna_seq[i + 1], rna_seq[j - 1])
                    score = S[i + 1][j - 1] + pair_score
                    if inner_pair_score > 0:
                        score += stacking_bonus
                else:
                    score = pair_score  # No inner subsequence
                if score > max_score:
                    max_score = score
                    trace[i][j] = ('PAIR', i, j)

            # Check for possible bifurcations
            for k in range(i, j):
                score = S[i][k] + S[k + 1][j]
                if score > max_score:
                    max_score = score
                    trace[i][j] = ('BIFURCATE', k)

            S[i][j] = max_score  # Update DP table with the maximum score

    # Traceback to compute the parenthesis
    parenthesis = ['.' for _ in range(N)]
    util.traceback(0, N - 1, trace, parenthesis)

    # Print Output
    util.print_output(S, rna_seq, parenthesis, N)


# Example usage
seq = "GCCGAGCG"
rna_folding(seq, len(seq))
