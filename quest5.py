def circle(r):
    radius = r
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if x*x + y*y <= radius*radius:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

circle(100)