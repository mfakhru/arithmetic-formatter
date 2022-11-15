def arithmetic_arranger(problems, answers=False):
  
  line1, line2, line3, line4 = '', '', '', ''
  lst_n = []
  space = ' '
  dashes = '-'
  
  if len(problems) > 5:
      return "Error: Too many problems."
  
  for problem in problems:
      _problem = problem.split(' ')
      
      n_problem1 = len(_problem[0])
      n_problem2 = len(_problem[2])

      n = ''
      if n_problem1 > n_problem2:
          n = n_problem1+2
      else:
          n = n_problem2+2
      lst_n.append(n)

      if _problem[1] != '+' and _problem[1] != '-':
          return "Error: Operator must be '+' or '-'."

      for x in range(0, len(_problem), 2):
          try:
              prob = int(_problem[x])
          except:
              return "Error: Numbers must only contain digits."

          if len(_problem[x]) > 4:
              return "Error: Numbers cannot be more than four digits."

      if problem == problems[-1]:
          line1 += str(_problem[0].rjust(n))
          line2 += str(_problem[1] + _problem[2].rjust(n-1))
          line3 += str(dashes*n)
          continue

      line1 += str(_problem[0].rjust(n) + space*4)
      line2 += str(_problem[1] + _problem[2].rjust(n-1) + space*4)
      line3 += str(dashes*n + space*4)

  

  totals = list(map(lambda x: eval(x), problems))
  for i in range(len(totals)-1):
      line4 += str(str(totals[i]).rjust(lst_n[i]) + space*4)

  line4 += str(str(totals[-1]).rjust(lst_n[-1]))
  
  arranged_problems = "\n".join([line1, line2, line3])
  if answers:
      arranged_problems = "\n".join([line1, line2, line3, line4])
  
  return arranged_problems
