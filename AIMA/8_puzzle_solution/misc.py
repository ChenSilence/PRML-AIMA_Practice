

# getInvCount
def getInvCount(state):
    state = state.flatten()
    int_count = 0
    for i in range(8):
        for j in range(i+1, 9):
            if state[j] and state[i] and state[i] > state[j]:
                int_count += 1
    return int_count
# judge
def isSolvable(state):
    invCount = getInvCount(state)
    if invCount % 2 == 0:
        return True
    else:
        return False