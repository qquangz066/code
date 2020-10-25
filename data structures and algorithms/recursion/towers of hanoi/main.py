def towers_of_hanoi(n: int, from_peg: str, to_peg: str, au_peg: str):
    if n == 1:
        print(f'Move disk 1 from peg {from_peg} to {to_peg}')
        return

    towers_of_hanoi(n - 1, from_peg=from_peg, to_peg=au_peg, au_peg=to_peg)

    print(f'Move disk {n} from peg {from_peg} to {to_peg}')

    towers_of_hanoi(n - 1, from_peg=au_peg, to_peg=to_peg, au_peg=from_peg)


if __name__ == '__main__':
    towers_of_hanoi(4, 'A', 'B', 'C')
