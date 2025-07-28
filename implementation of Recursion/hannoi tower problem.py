count = 0
def hannoi(n,source,target,temp):
    global count
    if n == 1:
        print(f"m0ve disk 1 from {source} to {target}")
        count+=1
    else:
        hannoi(n-1,source,temp,target)
        print(f"move disk {n} from {source} to {target}")
        hannoi(n-1,temp,target,source)
        count+=1

n= int(input("Enter the number of disks:"))
process = hannoi(n,"A","B","C")
print(f"count: {count}")


def hannoi(n, source, target, temp, moves):
    if n == 1:
        moves.append(f"move disk 1 from {source} to {target}")
    else:
        hannoi(n-1, source, temp, target, moves)
        moves.append(f"move disk {n} from {source} to {target}")
        hannoi(n-1, temp, target, source, moves)

n = int(input("Enter the number of disks: "))
moves = []
hannoi(n, "A", "B", "C", moves)

# Save to file
with open("hannoi_moves.txt", "w") as f:
    for move in moves:
        f.write(move + "\n")

print(f"Process saved to hannoi_moves.txt")         