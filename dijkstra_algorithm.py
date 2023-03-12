import matplotlib.pyplot as plt
import numpy as np

def create_obstacle_map():
    X_SIZE = 600
    Y_SIZE = 250

    obstacle_points = [()]

    plt.xlim([0,X_SIZE])
    plt.ylim([0,Y_SIZE])

    # first rectangle
    for xp in range(100,150):
        for yp in range(0,100):
            plt.scatter(xp, yp, c="red")
            obstacle_points.append((xp,yp))
    
    # second rectangle
    for xp in range(100,150):
        for yp in range(150,250):
            plt.scatter(xp, yp, c="red")
            obstacle_points.append((xp,yp))

    # triangle above half
    for xp in range(460,510):
        for yp in range(125,225):
            if 2*xp+yp <= 1145:
                plt.scatter(xp, yp, c= "red")
                obstacle_points.append((xp,yp))

    # triangle below half
    for xp in range(460,600):
        for yp in range(25,125):
            if 2*xp - yp <= 895:
                plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))

    # rectangle part of hexagon
    for xp in range(235,365):
        for yp in range(85,160):
            plt.scatter(xp,yp, c="red")
            obstacle_points.append((xp,yp))

    # left of upper triangle
    for xp in range(235,300):
        for yp in range(160,198):
            if 38*xp - 65*yp >= -1470:
                plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))
    
    # right of upper triangle
    for xp in range(300,365):
        for yp in range(160,198):
            if 38*xp + 65*yp <= 24270:
                plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))

    # left of lower triangle
    for xp in range(235,300):
        for yp in range(58,85):
            if 27*xp + 65*yp >= 11870:
                plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))

    # right of lower triangle
    for xp in range(300,365):
        for yp in range(58,85):
            if 27*xp - 65*yp <= 4330:
                plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))

    # plt.show()
    return obstacle_points

obs_points = create_obstacle_map()
print(obs_points)