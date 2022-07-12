def trap(height: list) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters
            # print(top, stack[-1], height[i], height[stack[-1]], height[top])
            # print(distance, waters, volume)

        stack.append(i)
    return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))