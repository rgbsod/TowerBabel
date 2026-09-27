from lab2 		import Tower
from classes 	import Entry


def print_towers(S, A, E, space):
    # tallest tower for reference
    h = max(S.size, A.size, E.size)

    for i in range(h-1, -1, -1):
        # get entry or blank
        s_val = S.array[i].value if i < S.size and S.array[i] is not None else " " * space
        a_val = A.array[i].value if i < A.size and A.array[i] is not None else " " * space
        e_val = E.array[i].value if i < E.size and E.array[i] is not None else " " * space


        print(f"{s_val} | {a_val} | {e_val}")


def create_rings(num_rings):
    avail_rings = []
    for i in range(num_rings, 0, -1):
        curr_string = "=" * (i * 2)
        curr_string = curr_string.center(num_rings * 2, " ")
        avail_rings.append(Entry(i-1,curr_string))
        if curr_string == '':
            break
    return avail_rings

validTower = False

while (validTower == False):
    try:
        rings = int(input('Enter rings for Tower of Hanoi Puzzle: '))

        if (rings <= 0):
            raise Exception('Invalid number of rings!')
        else:
            validTower = True
    except Exception as err:
        print(f"ERROR. {err} Input again.\n")


#rings = int(input('Enter rings for Tower of Hanoi Puzzle: '))
    

spacing = rings * 2

avail_rings = create_rings(rings)
#avail_rings = [Entry(5, "=========="), Entry(4, " ======== "), Entry(3, "  ======  "), Entry(2, "   ====   "), Entry(1, "    ==    "),]

start = Tower()
aux = Tower()
end = Tower()

for i in range(rings-1, -1, -1):
    start.push(avail_rings[len(avail_rings)- 1 - i])

#Game is not complete until all rings are in End Tower

while (end.size != rings):
    try:
        print()
        print_towers(start, aux, end, spacing)
        print(f"{'S'.center(spacing)} | {'A'.center(spacing)} | {'E'.center(spacing)}")
        print()


        from_tower = str(input('Enter tower to move top ring: ')).upper().strip()
        
        match from_tower:
            case 'S':
                to_tower = str(input('Move to which tower?: ')).upper().strip()
                match to_tower:
                    case 'A':
                        start.move_to(aux)
                    case 'E':
                        start.move_to(end)
                    case _:
                        raise Exception('Invalid tower given in target tower!')

            case 'A':
                to_tower = str(input('Move to which tower?: ')).upper().strip()
                match to_tower:
                    case 'S':
                        aux.move_to(start)
                    case 'E':
                        aux.move_to(end)
                    case _:
                        raise Exception('Invalid tower given in target tower!')

            case 'E':
                to_tower = str(input('Move to which tower?: ')).upper().strip()
                match to_tower:
                    case 'S':
                        end.move_to(start)
                    case 'A':
                        end.move_to(aux)
                    case _:
                        raise Exception('Invalid tower given in target tower!')
            case _:
                raise Exception('Invalid tower given in source tower!')
    except Exception as err:
        print(f"ERROR. {err} Try again.\n")
        continue

print()
print_towers(start, aux, end, spacing)
print(f"{'S'.center(spacing)} | {'A'.center(spacing)} | {'E'.center(spacing)}")
print()
print("Tower of Hanoi Complete! Great job!")



