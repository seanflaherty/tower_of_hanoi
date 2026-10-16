"""Implementation of the tower of hanoi problem using recursion."""
def hanoi_solver(num: int) -> str:
    """A function that solves the classic Tower of Hanoi puzzle using recursion."""
    # Initialize the rods.
    rod1 = [disc for disc in range(num, 0, -1)]
    rod2 = [int]
    rod3 = [int]

    def get_lists_string():
        """Returns the current state of the rods."""
        return f"{rod1} {rod2} {rod3}"

    def move_disc(start, target):
        """Moves the topmost disc."""
        if start:
            target.append(start.pop())

    def move_tower(start, target, auxiliary, n):
        """Implements the recursive move strategy."""
        moves = []
        if n == 1:
            move_disc(start, target)
            return [get_lists_string()]

        # Move top n-1 discs to auxiliary
        moves.extend(move_tower(start, auxiliary, target, n - 1))

        # Move the bottom disc to target
        move_disc(start, target)
        moves.append(get_lists_string())

        # Move top n-1 discs from auxiliary to target
        moves.extend(move_tower(auxiliary, target, start, n - 1))

        return moves

    # Returns the move history.
    history = [get_lists_string()]
    if num > 0:
        history.extend(move_tower(rod1, rod3, rod2, num))

    return "\n".join(history)
