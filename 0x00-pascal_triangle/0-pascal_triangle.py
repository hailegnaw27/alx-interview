def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    
    # Initialize the list for Pascal's triangle with the first row
    triangle = [[1]]
    
    # Generate each row of the triangle
    for i in range(1, n):
        # Start the current row with 1
        row = [1]
        
        # Calculate the interior values of the current row
        for j in range(1, i):
            # The value at position j in the current row is the sum of the values at
            # positions j-1 and j in the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # End the current row with 1
        row.append(1)
        
        # Add the current row to the triangle list
        triangle.append(row)
    
    return triangle

def print_triangle(triangle):
    """
    Prints the Pascal's triangle in the required format.
    """
    for row in triangle:
        print(f"{row}")

if __name__ == "__main__":
    # Define the main function to test the pascal_triangle function
    def main():
        # Define the input value for n (number of rows in Pascal's triangle)
        n = 5
        
        # Call the pascal_triangle function to generate the triangle
        triangle = pascal_triangle(n)
        
        # Call the print_triangle function to print the triangle in the required format
        print_triangle(triangle)
    
    # Call the main function to execute the script
    main()

