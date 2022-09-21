from multiprocessing.dummy import active_children
from gameoflife import width, height, stage, print_stage, count_neighbors

def init_stage(stage):
    for v_pos in range(0, height):
      for h_pos in range(0, width):
        if h_pos == 1:
          stage[v_pos][h_pos] = True
        else:
          stage[v_pos][h_pos] = False

# Generation Rules:
# 1. Any live cell with < 2 neighbors dies
# 2. Any live cell with 2-3 neighbors lives
# 3. Any live cell with > 3 neighbors dies
# 4. Any dead cell with 3 neighbors comes alive
# neighbor means live cells
# y: v_pos; x: h_pos



def one_generation(stage):
    # build logic on the the original stage
    # active - make changes to this copy
    # !!! shallow copy
    # make a shallow copy, makes a new list, new outer list, but inner list is the same
    # means inner list is pointing to the same memory as original
    # active_stage = stage.copy()  
    
    # make new copy, immutable ???

    # primitive type: copy value; non-p type: copy reference; use less storage
    active_stage = []
    for i in range(height):
        active_stage.append(stage[i].copy())

    for v_pos in range(len(stage)):
        for h_pos in range(len(stage[v_pos])):
            neighbors = count_neighbors(stage, v_pos, h_pos)
            # 4. Any dead cell with 3 neighbors comes alive
            if not stage[v_pos][h_pos] and neighbors == 3:
                active_stage[v_pos][h_pos] = True
            # 1. Any live cell with < 2 neighbors die
            elif stage[v_pos][h_pos] and neighbors < 2:
                active_stage[v_pos][h_pos] = False
            # 2. Any live cell with 2-3 neighbors lives
            elif stage[v_pos][h_pos] and (neighbors == 2 or neighbors == 3):
                active_stage[v_pos][h_pos] = True
            # 3. Any live cell with > 3 neighbors dies
            elif stage[v_pos][h_pos] and neighbors > 3:
                active_stage[v_pos][h_pos] = False
    #print(active_stage) 

    # overwrite everything from active stage   
    # we want to modify the stage - ok with side effect
           
    for v_pos in range(len(stage)):
        for h_pos in range(len(stage[v_pos])):
            stage[v_pos][h_pos] = active_stage[v_pos][h_pos]

init_stage(stage)
print("First Generation:")
print_stage(stage)
one_generation(stage)
print("Second Generation:")
print_stage(stage)
one_generation(stage)
print("Third Generation:")
print_stage(stage)
one_generation(stage)
print("Forth Generation:")
print_stage(stage)
one_generation(stage)
print("Fifth Generation:")
print_stage(stage)

