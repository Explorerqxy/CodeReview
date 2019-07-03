def VerifySequenceOfBST(sequence, length):
    if sequence == [] or length == 0:
        return False
    root = sequence[length - 1]

    for i in range(0,length):
        if sequence[i] > root:
            break

    for j in range(i, length):
        if sequence[j] < root:
            return False

    left = True
    if i > 0 :
        left = VerifySequenceOfBST(sequence, i)
    right = True
    if j < length - 1:
        right = VerifySequenceOfBST(sequence[j:], length-i+1)
    return left and right


