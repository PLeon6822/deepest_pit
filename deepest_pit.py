# Coding challenge solution by Pablo Leon Pacheco

import argparse

def solution(A):

    sol = -1
    p, q, r = None, None, None

    for n in range(len(A)):
        if p is None or (r is None and q is None and A[n] >= A[p]):
            p = n
        elif p is not None and r is None and ((q is None and A[n] < A[p]) or (q is not None and A[n] < A[q])):
            q = n
        elif q is not None and ((r is None and A[n] > A[q]) or (r is not None and A[n] > A[r])):
            r = n
            partial = min(A[p] - A[q], A[r] - A[q])
            if partial > sol:
                sol = partial
        else:
            p = r
            q, r = None, None
    return sol

def main():
    parser = argparse.ArgumentParser(description="Find the deepest pit in a given integer sequence in the range [-1000000,1000000].")
    parser.add_argument('integers',action='append',nargs='*',type=int,help='The integer sequence. Must be [0,100000] in length.')
    A = vars(parser.parse_args())['integers']
    print(solution(A[0]))

if __name__ == '__main__':
    main()