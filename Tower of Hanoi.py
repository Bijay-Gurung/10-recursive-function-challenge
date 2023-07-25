def tower_of_hanoi(num,source,aux,destination):
    if num == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(num-1,source,destination,aux)
    print(f"Move disk {num} from {source} to {destination}")
    tower_of_hanoi(num-1,aux,source,destination)
result = tower_of_hanoi(3,'A','B','C')