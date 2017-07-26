# Tower of Hanoi implementation in Python

# This function will recursively show all the moves of the solution
def TowerOfHanoi(count, source, aux, destination):
    # When there is only single disk move it from 'source' to 'destination'
    if count == 1:
        print("Move disk 1 from: {source} to: {destination}".format(source=source,destination=destination))
        return

    # Move 'n-1' disks from 'source' to 'aux'
    TowerOfHanoi(count - 1, source, destination, aux)

    # Move n-th disk from 'source' to 'detination'
    print("Move disk {disk} from: {source} to: {destination}".format(disk=count,source=source,destination=destination))

    # Move (n-1) disks from 'aux' to 'destination'
    TowerOfHanoi(count - 1, aux, source, destination);



# Testing Tower of Hanoi code
TowerOfHanoi(3, 'A', 'B', 'C');
