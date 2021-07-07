'''Реализуйте программу, которая будет эмулировать работу с пространствами имен.
Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе
   из пространства <namespace>, или None, если такого пространства не существует.
   

Sample Input:

9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

Sample Output:

global
None
bar
foo

'''

n=int(input())
l=[input().split() for i in range(n)]

scopes={} # scopes = {'global': {'parent': None, 'variables': set()}}
scopes['global']= {'parent': 'None', 'variables':set()}
 
def get_var (scope, var) :
    if var in scopes[scope]['variables']:
        print (scope)
    elif scopes[scope]['parent'] != 'None' :
        get_var(scopes[scope]['parent'] ,var)
    else :    
        print('None')    
    
for i in range(n):
    if l[i][0] == 'create':
        if l[i][1] not in scopes :
            scopes[l[i][1]]={'parent':l[i][2], 'variables':set()}
    if l[i][0] == 'add' :
        scopes[l[i][1]]['variables'].add(l[i][2])
    if l[i][0] == 'get' : 
         get_var(l[i][1], l[i][2])
       
for key, value in scopes.items():
    print(key, value, end='; ')
