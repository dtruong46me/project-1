
class State:
    def __init__(self, x, y, step) -> None:
        self.x = x
        self.y = y
        self.step = step

class WaterJugs:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.visited = []
        self.queue = []

    # Check Problem is solved    
    def is_solved(self, state: State):
        if state.x == self.c or state.y == self.c:
            return True
        return False
    
    # Add State to Queue
    def add_queue(self, state: State):
        if (state.x, state.y) not in self.visited:
            self.queue.append(state)
            self.visited.append((state.x, state.y))

    # Fill Jug
    def fill_jug(self, state: State, jug_a=False, jug_b=False) -> State:
        if jug_a==True and jug_b==False:
            new_state = State(x=self.a, y=state.y, step=state.step+1)
        
        if jug_a==False and jug_b==True:
            new_state = State(x=state.x, y=self.b, step=state.step+1)
        
        return new_state
        # self.add_queue(new_state)

    # Empty Jug
    def empty_jug(self, state: State, jug_a=False, jug_b=False) -> State:
        if jug_a==True and jug_b==False:
            new_state = State(x=0, y=state.y, step=state.step+1)
        
        if jug_a==False and jug_b==True:
            new_state = State(x=state.x, y=0, step=state.step+1)
        
        return new_state
        # self.add_queue(new_state)

    # Pour Jug_m to Jug_n
    def pour_jug(self, state: State, jug_a=False, jug_b=False) -> State:
        if jug_a==True and jug_b == False:
            if state.x + state.y < self.b:
                new_state = State(x=0, y=state.x+state.y, step=state.step+1)
            else:
                new_state = State(x=state.x+state.y-self.b, y=self.b, step=state.step+1)

        if jug_a==False and jug_b==True:
            if state.x + state.y < self.a:
                new_state = State(x=state.x+state.y, y=0, step=state.step+1)
            else:
                new_state = State(x=self.a, y=state.x+state.y-self.a, step=state.step+1)

        return new_state

    # Solve Water Jugs
    def solve(self) -> State:

        s0 = State(x=0, y=0, step=0)
        self.queue.append(s0)
        self.visited.append(s0)

        while len(self.queue) != 0:
            cur_state = self.queue.pop(0)

            assert isinstance(cur_state, State)

            # Fill Jug_a
            new_state = self.fill_jug(state=cur_state, jug_a=True, jug_b=False)
            if self.is_solved(new_state):
                return new_state
            self.add_queue(new_state)

            # Fill Jug_b
            new_state = self.fill_jug(state=cur_state, jug_a=False, jug_b=True)
            if self.is_solved(new_state):
                return new_state
            self.add_queue(new_state)

            # Empty Jug_a
            new_state = self.empty_jug(state=cur_state, jug_a=True, jug_b=False)
            if self.is_solved(new_state):
                return new_state
            self.add_queue(new_state)

            # Empty Jug_b
            new_state = self.empty_jug(state=cur_state, jug_a=False, jug_b=True)
            if self.is_solved(new_state):
                return new_state
            self.add_queue(new_state)

            # Pour Jug_a to Jug_b
            new_state = self.pour_jug(state=cur_state, jug_a=True, jug_b=False)
            if self.is_solved(new_state):
                return new_state
            self.add_queue(new_state)

            # Pour Jug_b to Jug_a
            new_state = self.pour_jug(state=cur_state, jug_a=False, jug_b=True)
            if self.is_solved(new_state):
                return new_state
            self.add_queue(new_state)

        return None

def main():
    a, b, c = [int(x) for x in input().split()]

    water_jugs = WaterJugs(a, b, c)

    solution = water_jugs.solve()

    if solution is not None:
        print(solution.step)
    else:
        print(-1)

if __name__ == '__main__':
    main()