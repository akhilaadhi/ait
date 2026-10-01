# Monkey Banana Problem - Goal Stack Planning
# Application: Robot Traversal to Fetch a Tool

# Initial state
state = {
    "robot": "A",
    "tool": "C",
    "has_tool": False
}

# Goal
goal = {
    "robot": "A",
    "has_tool": True
}

# Goal stack
stack = ["HAS_TOOL"]

print("Initial State:")
print(state)

while stack:
    current_goal = stack.pop()

    if current_goal == "HAS_TOOL":
        if not state["has_tool"]:
            # To get the tool, robot must go to the tool location
            stack.append("PICK_TOOL")
            stack.append("GO_TO_TOOL")

    elif current_goal == "GO_TO_TOOL":
        if state["robot"] != state["tool"]:
            print("\nAction: Robot moves from", state["robot"],
                  "to", state["tool"])
            state["robot"] = state["tool"]

    elif current_goal == "PICK_TOOL":
        if state["robot"] == state["tool"]:
            print("Action: Robot picks up the tool")
            state["has_tool"] = True

print("\nFinal State:")
print(state)

if state["has_tool"]:
    print("\nGoal Achieved: Robot successfully fetched the tool.")