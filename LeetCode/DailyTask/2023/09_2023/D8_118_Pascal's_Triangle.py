def generate_pascals_triangle(numRows):
    res = [[1]]

    for _ in range(numRows - 1):
        dummy_row = [0] + res[-1] + [0]
        row = []

        for i in range(len(res[-1]) + 1):
            row.append(dummy_row[i] + dummy_row[i+1])
        res.append(row)

    return res

def main():
    numRows = 5
    result = generate_pascals_triangle(numRows)

    # Print Pascal's Triangle
    print("Test Case 1")
    for row in result:
        print(row)


    numRows = 1
    result = generate_pascals_triangle(numRows)
    print("\nTest Case 2")
    # Print Pascal's Triangle
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
