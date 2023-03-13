from queue import PriorityQueue
import time
import pygame as pyg

obstacle_points = []

X_SIZE = 600
Y_SIZE = 250

def create_obstacle_map():

    # first rectangle
    for xp in range(100,150):
        for yp in range(0,100):
            obstacle_points.append((xp,yp))
    
    # second rectangle
    for xp in range(100,150):
        for yp in range(150,250):
            obstacle_points.append((xp,yp))

    # triangle above half
    for xp in range(460,510):
        for yp in range(125,225):
            if 2*xp+yp <= 1145:
                obstacle_points.append((xp,yp))

    # triangle below half
    for xp in range(460,600):
        for yp in range(25,125):
            if 2*xp - yp <= 895:
                obstacle_points.append((xp,yp))

    # rectangle part of hexagon
    for xp in range(235,365):
        for yp in range(85,160):
            obstacle_points.append((xp,yp))

    # left of upper triangle
    for xp in range(235,300):
        for yp in range(160,198):
            if 38*xp - 65*yp >= -1470:
                obstacle_points.append((xp,yp))
    
    # right of upper triangle
    for xp in range(300,365):
        for yp in range(160,198):
            if 38*xp + 65*yp <= 24270:
                obstacle_points.append((xp,yp))

    # left of lower triangle
    for xp in range(235,300):
        for yp in range(58,85):
            if 27*xp + 65*yp >= 11870:
                obstacle_points.append((xp,yp))

    # right of lower triangle
    for xp in range(300,365):
        for yp in range(58,85):
            if 27*xp - 65*yp <= 4330:
                obstacle_points.append((xp,yp))

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
                    parent_child_info[next_point] = current_point
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
                    parent_child_info[next_point] = current_point
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
                    parent_child_info[next_point] = current_point
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
                    parent_child_info[next_point] = current_point
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
                    parent_child_info[next_point] = current_point
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
                    parent_child_info[next_point] = current_point
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
                    parent_child_info[next_point] = current_point
                    return 
                else:
                    return
        map_queue.put(next_node)
        parent_child_info[next_point] = current_point

# function to track back from the final state to the initial state to get the shortest path
def back_tracking(path_info, initial, current):
    child = path_info.get(current)
    current_tuple = tuple(current)
    child_tuple = tuple(child)
    shortest_path.append(current_tuple)
    shortest_path.append(child_tuple)
    while child != initial:  
        child = path_info.get(child)
        child_tuple = tuple(child)
        shortest_path.append(child_tuple)
    return shortest_path

def flip_points(points, height):
    return (points[0], height - points[1])

def flip_object_points(points, height, object_height):
    return (points[0], height - points[1] - object_height)

def pygame_visualization(visited_nodes, shortest_path):

    pyg.init()
    window = pyg.display.set_mode((X_SIZE,Y_SIZE))

    obstacle_color = "red"
    clearance_color = "pink"
    condition = True
    clock = pyg.time.Clock()

    rect2_clearance = flip_object_points([95, 0], 250, 105)
    rect1_clearance = flip_object_points([95, 145], 250, 105)
    rect2_original = flip_object_points([100, 0], 250, 100)
    rect1_original = flip_object_points([100, 150], 250, 100)

    triangle1_clearance = flip_points([455, 20], 250)
    triangle2_clearance = flip_points([463, 20], 250)
    triangle3_clearance = flip_points([515.5, 125], 250)
    triangle4_clearance = flip_points([463, 230], 250)
    triangle5_clearance = flip_points([455, 230], 250)

    triangle1 = (460, 25)
    triangle2 = (460, 225)
    triangle3 = (510, 125)

    hexagon1_clearance = (300, 205.76)
    hexagon2_clearance = (230, 165.38)
    hexagon3_clearance = (230, 84.61)
    hexagon4_clearance = (300, 44.23)
    hexagon5_clearance = (370, 84.61)
    hexagon6_clearance = (370, 165.38)

    hexagon1_org = (235,87.5)
    hexagon2_org = (300,50)
    hexagon3_org = (365,87.5)
    hexagon4_org = (365,162.5)
    hexagon5_org = (300,200)
    hexagon6_org = (235,162.5)

    while condition:
        for loop in pyg.event.get():
            if loop.type == pyg.QUIT:
                condition = False

        pyg.draw.rect(window, clearance_color, pyg.Rect(rect2_clearance[0], rect2_clearance[1], 60, 105))
        pyg.draw.rect(window, clearance_color, pyg.Rect(rect1_clearance[0], rect1_clearance[1], 60, 105))
        pyg.draw.rect(window, obstacle_color, pyg.Rect(rect2_original[0], rect2_original[1], 50, 100))
        pyg.draw.rect(window, obstacle_color, pyg.Rect(rect1_original[0], rect1_original[1], 50, 100))

        pyg.draw.polygon(window, clearance_color, ((triangle1_clearance),(triangle2_clearance),(triangle3_clearance), (triangle4_clearance), (triangle5_clearance)))
        pyg.draw.polygon(window, obstacle_color, ((triangle1),(triangle2),(triangle3)))

        pyg.draw.polygon(window, clearance_color, ((hexagon1_clearance),(hexagon2_clearance),(hexagon3_clearance),(hexagon4_clearance),(hexagon5_clearance),(hexagon6_clearance)))
        pyg.draw.polygon(window, obstacle_color, ((hexagon1_org),(hexagon2_org),(hexagon3_org),(hexagon4_org),(hexagon5_org),(hexagon6_org)))

        pyg.draw.rect(window, clearance_color ,pyg.Rect(0, 0, 600, 5))
        pyg.draw.rect(window, clearance_color ,pyg.Rect(0, 245, 600, 5))
        pyg.draw.rect(window, clearance_color ,pyg.Rect(0, 0, 5, 250))
        pyg.draw.rect(window, clearance_color ,pyg.Rect(595, 0, 5, 250))

        for node in visited_nodes:
            pyg.draw.circle(window, "white", flip_points(node, 250), 1)
            pyg.display.flip()
            clock.tick(700)

        for node in shortest_path:
            pyg.draw.circle(window, "teal", flip_points(node, 250), 1)
            pyg.display.flip()
            clock.tick(10)

        pyg.display.flip()
        pyg.time.wait(3000)
        condition = False
    pyg.quit()

create_obstacle_map()
start_node, goal_node = get_input()
start = time.time()
map_queue = PriorityQueue()
map_queue.put((0, start_node))

visited_nodes = []
parent_child_info = {}
shortest_path = []

while True:
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
        shortest = back_tracking(parent_child_info, start_node, goal_node)
        shortest.reverse()     
        print(shortest)
        break

pygame_visualization(visited_nodes, shortest_path)