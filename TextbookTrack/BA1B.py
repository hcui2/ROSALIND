def bm_preproces_bad_char_rule(p):
    """
    The preprocessing function for Boyer Moore's bad character heuristic
    p: the pattern string, here it stands for the PAM string
    """

    # Initialize all occurrence
    chars = ['A', 'G', 'C', 'T', 'N']
    bad_char = {}

    # Fill the actual value of last occurrence
    size = len(p)
    for i in range(size):
        bad_char[p[i]] = i

    for c in chars:
        if c not in bad_char:
            bad_char[c] = len(p)

    # return initialized dictionary
    return bad_char


def find_guide_seq_bm(s, l, p):
    """
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    """

    m = len(p)
    n = len(s)

    # create the bad character dictionary by calling
    # the pre-processing function for given pattern
    bad_char = bm_preproces_bad_char_rule(p)

    offset = l  # offset is shift of the pattern with respect to text
    occurrences = []

    while offset <= n - m:
        j = m - 1
        # Keep reducing index j of pattern while
        # characters of pattern and text are matching at this shift s
        while j >= 0:
            if p[j] == 'N' or p[j] == s[offset + j]:
                j -= 1
            else:
                break

        # If the pattern is present at current offset,
        # then index j will become -1 after the above loop
        if j < 0:
            occurrences.append(s[offset - l: offset])
            #############################################################
            # if no such char in the pattern.
            # shift the pattern such that last 'N' in the pattern matches the next char
            # or shift the pattern past the last matched char.

            # case 1:
            # AGGCTTAGCTTTAA
            #       AGC
            # since next T is not in the pattern, AGC moves past T
            # AGGCTTAGCTTTAA
            #           AGC

            # case 2:
            # AGGCTTAGCTTTAA
            #       NGC
            # even next T is not in the pattern, but we have a 'N' in pattern
            # so match N against T
            # AGGCTTAGCTTTAA
            #          NGC
            #############################################################
            if offset + m < n and bad_char[s[offset + m]] == m:
                if bad_char['N'] == m: # if we dont have 'N' in pattern
                    offset += m + 1 # past the next
                else: # we have a 'N'
                    offset += m - bad_char['N']
                continue
            #############################################################
            # Shift the pattern so that the next character in text
            # aligns with the last occurrence of it in pattern.
            # however, if there is 'N' in the pattern, shift the pattern to where the 'N' matches next character.

            # case 3:
            # AGGCTTAGCATTAA
            #       AGC
            # since next T is not in the pattern, AGC moves past T
            # AGGCTTAGCATTAA
            #          AGC

            # case 4:
            # AGGCTTAGCATTAA
            #       ANC
            # even next T is not in the pattern, but we have a 'N' in pattern
            # so match N against T
            # AGGCTTAGCATTAA
            #         ANC
            #############################################################
            offset += min(m - bad_char[s[offset + m]], m - bad_char['N']) if offset + m < n else 1


        # if the pattern is not the current offset
        # j would be larger or equal to 0.
        else:
            # if the mismatched char is not in the pattern.
            # shift the pattern past the mismatched char
            # or shift the pattern that the last occurring N is agaist the mismatched

            # case 1:
            # AGTCTTAGCTTTAA
            # AGGC
            # since T is not in the pattern, AGGC shift 3 steps
            # AGTCTTAGCTTTAA
            #    AGGC

            # case 2:
            # AGTCTTAGCTTTAA
            # ANGC
            # even T is not in the pattern, but we have a 'N' in pattern
            # so match N against T
            # AGTCTTAGCTTTAA
            #  ANGC

            offset += max(1, min(j - bad_char[s[offset + j]], j - bad_char['N']))

    return occurrences


# Driver program to test above function
def main():
    s = 'TGATCTACTAGAGACTACTAACGGGGATACATAG'
    l = 20
    p = 'NGG'
    ret = find_guide_seq_bm(s, l, p)
    print(ret)

if __name__ == '__main__':
    main()
