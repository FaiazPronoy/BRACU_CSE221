input = open("input8.txt")
output = open("output8.txt", "w")

def main():
    size = 20005
    tc = int(input.readline())
    t = 0
    while t < tc:
        n = int(input.readline())
        color = [0] * size
        adj = [[] for _ in range(size)]

        for i in range(n):
            x, y = map(int, input.readline().split())
            adj[x].append(y)
            adj[y].append(x)

        mx = 0
        for i in range(size):
            if adj[i] and color[i] == 0:
                black, red = 0, 0
                q = [i]
                color[i] = 1
                black += 1

                while q:
                    node = q.pop(0)
                    for neighbor in adj[node]:
                        if color[neighbor] == 0:
                            q.append(neighbor)
                            if color[node] == 1:
                                color[neighbor] = 2
                                red += 1
                            else:
                                color[neighbor] = 1
                                black += 1

                mx += max(red, black)

        output.write(f"Case {t+1}: {mx}\n")
        t += 1

main()
output.close()