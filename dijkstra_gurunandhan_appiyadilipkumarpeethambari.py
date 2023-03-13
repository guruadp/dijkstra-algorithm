import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue
import time

obstacle_points = []

def create_obstacle_map():
    X_SIZE = 600
    Y_SIZE = 250

    plt.xlim([0,X_SIZE])
    plt.ylim([0,Y_SIZE])

    # first rectangle
    for xp in range(100,150):
        for yp in range(0,100):
            # plt.scatter(xp, yp, c="red")
            obstacle_points.append((xp,yp))
    
    # second rectangle
    for xp in range(100,150):
        for yp in range(150,250):
            # plt.scatter(xp, yp, c="red")
            obstacle_points.append((xp,yp))

    # triangle above half
    for xp in range(460,510):
        for yp in range(125,225):
            if 2*xp+yp <= 1145:
                # plt.scatter(xp, yp, c= "red")
                obstacle_points.append((xp,yp))

    # triangle below half
    for xp in range(460,600):
        for yp in range(25,125):
            if 2*xp - yp <= 895:
                # plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))

    # rectangle part of hexagon
    for xp in range(235,365):
        for yp in range(85,160):
            # plt.scatter(xp,yp, c="red")
            obstacle_points.append((xp,yp))

    # left of upper triangle
    for xp in range(235,300):
        for yp in range(160,198):
            if 38*xp - 65*yp >= -1470:
                # plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))
    
    # right of upper triangle
    for xp in range(300,365):
        for yp in range(160,198):
            if 38*xp + 65*yp <= 24270:
                # plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))

    # left of lower triangle
    for xp in range(235,300):
        for yp in range(58,85):
            if 27*xp + 65*yp >= 11870:
                # plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))

    # right of lower triangle
    for xp in range(300,365):
        for yp in range(58,85):
            if 27*xp - 65*yp <= 4330:
                # plt.scatter(xp,yp, c="red")
                obstacle_points.append((xp,yp))

    # plt.show()
    return obstacle_points

def get_input():
    accept_start_node, accept_goal_node = True, True
    while accept_start_node:
        start_x = int(input("Enter start x: "))
        start_y = int(input("Enter start y: "))
        start_node = (start_x, start_y)
        if start_node not in obstacle_points:
            accept_start_node = False
            # print("Valid nodes")
        else:
            print("You have entered invalid start node. Please enter a valid note...")
            # continue

    while accept_goal_node:    
        goal_x = int(input("Enter goal x: "))
        goal_y = int(input("Enter goal y: "))        
        goal_node = (goal_x, goal_y)
        if goal_node not in obstacle_points:
            accept_goal_node = False
            print("Valid nodes")
        else:
            print("You have entered invalid goal node. Please enter a valid note...")
    return start_node, goal_node

def move_up_right(curr_node):
    current_point = curr_node[1]
    next_point = (current_point[0] + 1, current_point[1] + 1)     

    if next_point not in visited_nodes and next_point not in obstacle_points:
        cost = 1.4
        updated_cost = curr_node[0] + cost         
        next_node = (updated_cost, next_point)
        for i in range(map_queue.qsize()):
            if map_queue.queue[i][1] == next_point:
                if map_queue.queue[i][0] > updated_cost:
                    map_queue.queue[i] = next_node 
                    parent_child_info[next_point] = current_point
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

def move_up_left(curr_node):
    current_point = curr_node[1]
    next_point = (current_point[0] - 1, current_point[1] + 1)     

    if next_point not in visited_nodes and next_point not in obstacle_points:
        cost = 1.4
        updated_cost = curr_node[0] + cost         
        next_node = (updated_cost, next_point)
        for i in range(map_queue.qsize()):
            if map_queue.queue[i][1] == next_point:
                if map_queue.queue[i][0] > updated_cost:
                    map_queue.queue[i] = next_node 
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

def move_down_right(curr_node):
    current_point = curr_node[1]
    next_point = (current_point[0] + 1, current_point[1] - 1)     

    if next_point not in visited_nodes and next_point not in obstacle_points:
        cost = 1.4
        updated_cost = curr_node[0] + cost         
        next_node = (updated_cost, next_point)
        for i in range(map_queue.qsize()):
            if map_queue.queue[i][1] == next_point:
                if map_queue.queue[i][0] > updated_cost:
                    map_queue.queue[i] = next_node 
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

def move_down_left(curr_node):
    current_point = curr_node[1]
    next_point = (current_point[0] - 1, current_point[1] - 1)     

    if next_point not in visited_nodes and next_point not in obstacle_points:
        cost = 1.4
        updated_cost = curr_node[0] + cost         
        next_node = (updated_cost, next_point)
        for i in range(map_queue.qsize()):
            if map_queue.queue[i][1] == next_point:
                if map_queue.queue[i][0] > updated_cost:
                    map_queue.queue[i] = next_node 
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

def move_up(curr_node):
    current_point = curr_node[1]
    next_point = (current_point[0], current_point[1] + 1)     

    if next_point not in visited_nodes and next_point not in obstacle_points:
        cost = 1
        updated_cost = curr_node[0] + cost         
        next_node = (updated_cost, next_point)
        for i in range(map_queue.qsize()):
            if map_queue.queue[i][1] == next_point:
                if map_queue.queue[i][0] > updated_cost:
                    map_queue.queue[i] = next_node 
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

def move_down(curr_node):
    current_point = curr_node[1]
    next_point = (current_point[0], current_point[1] - 1)     

    if next_point not in visited_nodes and next_point not in obstacle_points:
        cost = 1
        updated_cost = curr_node[0] + cost         
        next_node = (updated_cost, next_point)
        for i in range(map_queue.qsize()):
            if map_queue.queue[i][1] == next_point:
                if map_queue.queue[i][0] > updated_cost:
                    map_queue.queue[i] = next_node 
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

def move_left(curr_node):
    current_point = curr_node[1]
    next_point = (current_point[0] - 1, current_point[1])     

    if next_point not in visited_nodes and next_point not in obstacle_points:
        cost = 1
        updated_cost = curr_node[0] + cost         
        next_node = (updated_cost, next_point)
        for i in range(map_queue.qsize()):
            if map_queue.queue[i][1] == next_point:
                if map_queue.queue[i][0] > updated_cost:
                    map_queue.queue[i] = next_node 
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

def move_right(curr_node):
    current_point = curr_node[1]
    next_point = (current_point[0] + 1, current_point[1])     

    if next_point not in visited_nodes and next_point not in obstacle_points:
        cost = 1
        updated_cost = curr_node[0] + int(cost)        
        next_node = (updated_cost, next_point)
        for i in range(map_queue.qsize()):
            if map_queue.queue[i][1] == next_point:
                if map_queue.queue[i][0] > updated_cost:
                    map_queue.queue[i] = next_node 
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

create_obstacle_map()
# print(obs_points)
# obs_points = [(50, 50), (100, 100)]
start_node, goal_node = get_input()
start = time.time()
# start_node, goal_node = (6, 6), (40, 40)
map_queue = PriorityQueue()
map_queue.put((0, start_node))

visited_nodes = []
parent_child_info = {}
while True:
    # print("queue not empty")
    current_node = map_queue.get()
    visited_nodes.append(current_node[1])
    x, y = current_node[1][0], current_node[1][1]
    if current_node[1] != goal_node:
        if y+1 < 600:
            move_up(current_node)
        if y-1 >= 0:
            move_down(current_node)
        if x+1 < 250:
            move_right(current_node)
        if x-1 >= 0:
            move_left(current_node)
        if x+1 < 600 and y+1 < 250:
            move_up_right(current_node)
        if x-1 >=0 and y+1 < 250:
            move_up_left(current_node)
        if x+1 < 600 and y-1 >= 0:
            move_down_right(current_node)
        if x-1 >=0 and y-1 >= 0:
            move_down_left(current_node)
        
    else:
        print("END")
        print(current_node[1])
        stop = time.time()
        print("Time: ",stop - start)        
        break