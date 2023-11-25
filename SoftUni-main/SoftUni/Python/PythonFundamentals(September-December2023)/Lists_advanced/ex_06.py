electrons = int(input())
shells = []
shell = 1
while electrons>0:
    els_in_shell = 2*(shell**2)
    if electrons >= els_in_shell:
        electrons -= els_in_shell
        shells.append(els_in_shell)
    else:
        shells.append(electrons)
        electrons = 0
    shell += 1
print(shells)