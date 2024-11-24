import random, os
dc = {'q': '', 'w': '', 'e': '', 'a': '', 's': '', 'd': '', 'z': '', 'x': '', 'c': ''}; 
def l(): os.system('cls' if os.name == 'nt' else 'clear')
def m(txt): print(" "); txt = "  " + txt + "  "; lr = len(txt) + 2; print(f"╔{'═' * (lr - 2)}╗"); print(f"║{txt}║"); print(f"╚{'═' * (lr - 2)}╝")
def i(): print("\n".join(" ".join(f"{p}[{'█' if dc[p] == 'X' else '▒' if dc[p] == 'O' else ' ' }]" for p in f) for f in [['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c']]))
def v(): return next((dc[c[0]] for c in [['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c'], ['q', 'a', 'z'], ['w', 's', 'x'], ['e', 'd', 'c'], ['q', 's', 'c'], ['e', 's', 'z']] if dc[c[0]] == dc[c[1]] == dc[c[2]] and dc[c[0]]), 'emp' if all(dc[pos] for pos in dc) else None)
def mvma(): return next((cmb[[dc[pos] for pos in cmb].index('')] for sym, riv in [('O', 'X'), ('X', 'O')] for cmb in [['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c'], ['q', 'a', 'z'], ['w', 's', 'x'], ['e', 'd', 'c'], ['q', 's', 'c'], ['e', 's', 'z']] if [dc[pos] for pos in cmb].count(sym) == 2 and [dc[pos] for pos in cmb].count('') == 1), random.choice([pos for pos in dc if dc[pos] == '']))
def trnj():
    while (jgda := input("\n▬▬▬ Elige casilla ►►► ").lower()) not in dc or dc[jgda] != '': pass
    dc[jgda] = 'X'
def jgar():
    ja = random.choice(['jug', 'maq']); fn="Fin del juego"
    if ja == 'maq': dc['s'] = 'O'; ja = 'jug'
    while True:
        l(); m(f"Turno de {'JUGADOR' if ja == 'jug' else 'MAQUINA'}"); i()
        if ja == 'jug':
            trnj(); est = v()
            if est == 'X': l(); m(fn); i(); m("¡El jugador gana!"); break
            if est == 'emp': l(); m(fn); i(); m("¡Empate!"); break
            ja = 'maq'
        elif ja == 'maq':
            dc[mvma()] = 'O'; est = v()
            if est == 'O': l(); m(fn); i(); m("¡La máquina gana!"); break
            if est == 'emp': l(); m(fn); i(); m("¡Empate!"); break
            ja = 'jug'
if __name__ == "__main__": jgar()