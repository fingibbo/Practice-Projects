def hanoi_solver(disks: int) -> str:
    left_tower = []
    middle_tower = []
    right_tower = []

    #start by getting the left tower with the numbers on it from largest to biggest
    for n in range(disks, 0, -1):
        left_tower.append(n)

    moves = [f"{left_tower} {middle_tower} {right_tower}"]

    def move(num_disks, start, helper, end_tower):
        if num_disks <= 0:
            return
        
        # Move n-1 disks from start to helper, so they are out of the way
        move(num_disks - 1, start, end_tower, helper)
        
        # Move the nth disk from start to end_tower
        end_tower.append(start.pop())
        
        # Record the move
        moves.append(f"{left_tower} {middle_tower} {right_tower}")

        move(num_disks - 1, helper, start, end_tower)

    move(disks, left_tower, middle_tower, right_tower)
    return '\n'.join(moves)

