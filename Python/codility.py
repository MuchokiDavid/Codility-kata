def solution(A, B):
    # Initialize the result, low, and high
    result = 0
    low, high = 1, min(A, B)

    # Binary Search Loop
    while low <= high:
        # Calculate the midpoint
        mid = low + (high - low) // 2
        
        # Calculate the number of pieces from each stick
        piecesA = A // mid
        piecesB = B // mid
        
        # Calculate the total number of pieces
        totalPieces = piecesA + piecesB
        
        #print(high, low)

        # Decision Making
        if totalPieces >= 4:
            # If we can construct a square, update result and search in the right half
            result = mid
            low = mid + 1
        else:
            # If not, search in the left half
            high = mid - 1

    # Return the final result, representing the side length of the largest square
    #print(high, low)
    
    return result

print (solution(10,21))