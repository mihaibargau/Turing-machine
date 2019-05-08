t_matrix = []
for i in range(10):
    row = []
    for j in range(10):
        row.append("0")
    t_matrix.append(row)

word = input("W= ")
word = 'B' + word + 'B'
f = open("input.txt", "r")

starting_state = f.readline()
current_state = int(starting_state[1])
final_state = f.readline()
final_state = final_state.split()
for line in f:

    s = line.split()
    i_transition = s[0]
    f_transition = s[2]
    t_matrix[int(i_transition[1])][int(f_transition[1])] = s[1] +  s[3] + s[4]

index = 1
max_stop = 0
stop = False
while word[index]!='B' and stop == False:
    max_stop = max_stop + 1
    if max_stop > 10:
        break
    for i in range(10):
        for j in range(10):
            if current_state == i and t_matrix[i][j][0] == word[index]:
                print("stare curenta " + str(current_state))
                word = list(word)
                word[index] = t_matrix[i][j][1]
                word = "".join(word)
                print("i=" + str(i) + " j=" + str(j))
                current_state = j
                if t_matrix[i][j][2] == 'R':
                    index = index + 1
                elif t_matrix[i][j][2] == 'L':
                    index = index - 1
                elif t_matrix[i][j][2] == 'S':
                    stop = True         
                print("stare curenta " + str(current_state))

if ("q" + str(current_state) in final_state):
    print("am ajuns in stare finala")
print(word)

