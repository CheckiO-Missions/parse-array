"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "[1, 2, 3]",
            "answer": [1, 2, 3],
        },
        {
            "input": "[[1], 2, 3]",
            "answer": [[1], 2, 3],
        },
        {
            "input": "[-3, [-2, 0], 10]",
            "answer": [-3, [-2, 0], 10],
        },
        {
            "input": "[100]",
            "answer": [100],
        },
        {
            "input": "[2,     3]",
            "answer": [2, 3],
        },
        {
            "input": "[[10, [11]], [[[1], 2], 3], 5]",
            "answer": [[10, [11]], [[[1], 2], 3], 5],
        },
        {
            "input": "   [3, 4]   ",
            "answer": [3, 4],
        },
        {
            "input": "[[], 0]",
            "answer": [[], 0],
        },
        {
            "input": "[[0,], 0]",
            "answer": [[0], 0],
        },


    ],
    "Error": [
        {
            "input": "[asd]",
            "answer": "raisedValueError",
        },
        {
            "input": "[2, 3]]",
            "answer": "raisedValueError",
        },
        {
            "input": "[++2, 1]",
            "answer": "raisedValueError",
        },
        {
            "input": "[10, 11, , 12]",
            "answer": "raisedValueError",
        },
        {
            "input": " 13 ",
            "answer": "raisedValueError",
        },
        {
            "input": "[[2]",
            "answer": "raisedValueError",
        },
    ],
    "Extra": [
        {
            "input": "[3 4]",
            "answer": "raisedValueError",
        },
        # Check for double separators without a space in between:
        {
            "input": "[10, 11,, 12]",
            "answer": "raisedValueError",
        },
        # Check for missing separators after []:
        {
            "input": "[[]3]",
            "answer": "raisedValueError",
        },
        # Check for missing separators before []:
        {
            "input": "[2[]]",
            "answer": "raisedValueError",
        },
        {
            "input": "[999, 0, -999, []]",
            "answer": [999, 0, -999, []]
        },
        {
            "input": "[[[[1], 2][]]]",
            "answer": "raisedValueError"
        },
        {
            "input": "[0, [0,], ,1]",
            "answer": "raisedValueError"
        },
        {
            "input": "[99, 9, [100, [13, [12], [1, 2], []], 0]]",
            "answer": [99, 9, [100, [13, [12], [1, 2], []], 0]]
        },
        {
            "input": " 0, [1, 2]",
            "answer": "raisedValueError"
        },
        {
            "input": " [999], 13]",
            "answer": "raisedValueError"
        },
        {
            "input": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]",
            "answer": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                       75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
                       99]
        },

        {
            "input": "[[0], -]",
            "answer": "raisedValueError"
        },


    ]
}
