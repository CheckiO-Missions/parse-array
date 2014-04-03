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
    ],
    "Extra": [
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
    ]
}
