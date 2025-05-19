def valid_anagram( A : str, S : str) -> bool:
    a, s = "".join(sorted(A)), "".join(sorted(S))
    return a==s


