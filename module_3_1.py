calls = 0


def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):    
  x = (len(string), string.upper(), string.lower())
  count_calls()
  return x

def is_contains(string, list_to_search): 
  count_calls()
  for i in range(len(list_to_search)):
      if list_to_search[i].lower() == string.lower():
          result = True
          break
      else:
          result = False
  return result      

print(string_info('Стекло'))
print(string_info('Пыль'))
print(is_contains('Камень', ['мень', 'Кам', 'КаМень']))
print(is_contains('Аргумент', ['Агрессия', 'Грум', 'Аргум', 'енТ'])) 

print(calls)


    
  