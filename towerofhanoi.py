def tower(n, source = 'A',aux = 'B', destination = 'C'):
    if n == 1:
        print('Move Disk', n, 'from', source, 'to', destination)
        return
    tower(n-1,source, destination, aux)
    print('Move Disk', n, 'from', source, 'to', destination)
    tower(n-1, aux, source, destination)

tower(2)
tower(3, 'x', 'y', 'z')