def convert_rect(x, y, w, h):
    return (x, x + w), (y, y + h)


rect1 = convert_rect(*map(int, input().split()))
rect2 = convert_rect(*map(int, input().split()))

if rect1[0][1] - rect1[0][0] < rect2[0][1] - rect2[0][0] and \
    rect1[1][1] - rect1[1][0] < rect2[1][1] - rect2[1][0]:
    rect1, rect2 = rect2, rect1

if (rect1[0][0] <= rect2[0][0] <= rect1[0][1] or
    rect1[0][0] <= rect2[0][1] <= rect1[0][1]) and \
    (rect1[1][0] <= rect2[1][0] <= rect1[1][1] or
     rect1[1][0] <= rect2[1][1] <= rect1[1][1]):
    print("YES")
else:
    print("NO")