
    # Create sample array
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])

    # Shuffle rows in-place (modifies original array)
    np.random.shuffle(arr)
    print(arr)
    # Output: randomly shuffled rows