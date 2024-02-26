def canCross(sx, sy, tx, ty, t):
    x_dist = abs(sx - tx)
    y_dist = abs(sy - ty)

    if x_dist == 0 and y_dist == 0:
        return t != 1

    return x_dist <= t and y_dist <= t

if __name__ == '__main__':
    # Test Cases
    sx1, sy1, tx1, ty1, t1 = 2, 4, 7, 7, 6
    result1 = canCross(sx1, sy1, tx1, ty1, t1)
    print("Result 1:", result1)

    sx2, sy2, tx2, ty2, t2 = 6, 3, 1, 7, 3
    result2 = canCross(sx2, sy2, tx2, ty2, t2)
    print("Result 2:", result2)

    sx3, sy3, tx3, ty3, t3 = 3, 3, 3, 3, 1
    result3 = canCross(sx3, sy3, tx3, ty3, t3)
    print("Result 3:", result3)
