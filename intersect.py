def simple_intersect(s1, s2):
    assert ('z' not in s1 and 'z' not in s2), 'one of s1, s2 contains z'
    # assert (len(s1) > 0 and len(s2) > 0), 'one of s1, s2 is empty'

    n1 = len(s1)
    n2 = len(s2)

    if (n1 == 0):
        return [s2]

    if (n2 == 0):
        return [s1]

    if (n2 > n1):
        s1, s2 = s2, s1
        n1, n2 = n2, n1

    # now s1 is the longest

    s = []
    for i in range(n2):
        if (s1[i] != s2[i]):
            return []
    return [s1]


def intersect1(seq_with_z, usual_seq, z_index):
    seq_before_z = seq_with_z[: z_index]
    seq_after_z = seq_with_z[z_index + 1:]

    s = simple_intersect(seq_before_z, usual_seq)

    if (len(s) == 0):  # this means that prefixes do not match => sequences do not intersect
        return []

    if (len(usual_seq) <= z_index):  # this means prefixes match but seq_with_z belongs to set represented by usual_seq
        return [seq_with_z]

    t = seq_after_z[0]
    k = 0
    res = []

    for j in range(z_index, len(usual_seq)):   # check suffixes
        if (usual_seq[j] != 0):                    # usual_seq does not end with zeros
            if (usual_seq[j] == t):          # usual_seq ends with correct terminator and some more
                return [usual_seq]                     # which means in belongs to set represented by seq_with_z
            else:
                return []                              # usual_seq does not have the terminator after zero
        else:                                          # which means intersection is empty
            pass

    # if we reach this point, we know that usual_seq matches the prefix and ends with zeros

    if(len(seq_before_z) == 0):  # usual_seq consists of zeros
        return [seq_with_z]      # so (z)t belongs to its pattern
    else:                        # otherwise...
        return [usual_seq + seq_after_z]


def intersect2(s1, s2, k1, k2):
    if (k1 > k2):
        s1, s2 = s2, s1
        k1, k2 = k2, k1

    n1 = len(s1)
    n2 = len(s2)

    # s1 has 'z' in earlier position

    a = []
    s1_before_z = s1[: k1]
    zeros = []
    s1_after_z = s1[k1 + 1:]

    for n_zeros in range(k2 - k1):
        a += intersect1(usual_seq=(s1_before_z + zeros + s1_after_z), seq_with_z=s2, z_index=k2)
        zeros += [0]

    if (s1[k1 + 1] == s2[k2 + 1]):
        if (s1[: k1] + zeros == s2[: k2]):
            a += [s2]

    return a


def intersect(s1, s2):
    k1 = -1
    k2 = -1

    for i in range(len(s1)):
        if (s1[i] == 'z'):
            k1 = i

    for i in range(len(s2)):
        if (s2[i] == 'z'):
            k2 = i

    if (k1 == -1 and k2 == -1):
        return simple_intersect(s1, s2)

    if (k1 == -1 and k2 != -1):
        return intersect1(seq_with_z=s2, usual_seq=s1, z_index=k2)

    if (k1 != -1 and k2 == -1):
        return intersect1(seq_with_z=s1, usual_seq=s2, z_index=k1)

    if (k1 != -1 and k2 != -1):
        return intersect2(s1, s2, k1, k2)