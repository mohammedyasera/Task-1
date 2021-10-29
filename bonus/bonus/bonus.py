def tic_tac_toe(l):
   converted_list = [[-1,-1,-1],
                      [-1,-1,-1],
                      [-1,-1,-1]]
   row = -1
   for i in l:
      row+=1
      col = 0
      for j in i:
         if(j == "X"):
              converted_list[row][col] = 1
         elif (j == "O"):
              converted_list[row][col] = 0
         col+=1
   if converted_list[0][0] + converted_list[1][1] + converted_list[2][2] == 3:
       return "X"
   elif converted_list[0][0] + converted_list[1][1] + converted_list[2][2] == 0:
       return "O"
   elif converted_list[0][2] + converted_list[1][1] + converted_list[2][0] == 1:
       return "X"
   elif converted_list[0][2] + converted_list[1][1] + converted_list[2][0] == 0:
       return "O"

   else:
     for i in converted_list:
       Sum = sum(i)
       if Sum == 3:
         return "X"
       elif Sum == 0:
         return "O"
     zipped_rows = zip(*converted_list)
     transpose_matrix = [list(row) for row in zipped_rows]
     for i in transpose_matrix:
       Sum = sum(i)
       if Sum == 3:
         return "X"
       elif Sum == 0:
         return "O"
     return "Draw"





print(tic_tac_toe([
["O", "O", "O"],
["O", "X", "X"],
["E", "X", "X"]
]))
