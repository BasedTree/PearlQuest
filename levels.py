#floors are lists

#w = Wall
#z = Zombie (ghost)
#p = Player 
#b = BOSS
#e = exit portal
#1 = left turret
#2 = right turret
#3 = up turret
#4 = down turret
#x = hurt tile
#h = health tile

#M = MEGA GHOST (ghost boss)
# B = blocked walls, breaks when you kill all ghosts
#F =  FINAL BOSS 



#template should be 15x10

'''

[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
]


'''


#F0
Floor1ID = ([
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
]
,
    
  #F1  
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','z',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ','w'],
['w','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
], 

#F2
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w',' ',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ','w'],
['w','2',' ',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ',' '],
['w',' ',' ',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ',' '],
['w','p',' ',' ','w',' ',' ',' ','w',' ',' ',' ',' ',' ',' '],
['w',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ',' ',' ',' '],
['w',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ','1',' ','w'],
['w','w',' ',' ','w',' ',' ',' ','w',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F3
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','x','x','x','x','x','x','x','x','x','x','x','x','w'],
['w','x','x',' ',' ',' ',' ','x',' ',' ','x',' ',' ','x','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ','h',' ',' '],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' '],
['w',' ',' ',' ',' ','x',' ',' ',' ',' ','x',' ',' ',' ',' '],
['w',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w','x','x',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ','w'],
['w','w','x','x','x','x','x','x','x','x','x','x','x','x','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],

#F4
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','p',' ','h',' ',' ',' ',' ','e',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
])




#F0
Floor2ID = ([
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ','x',' ',' ','w',' ',' ','x',' ',' ',' ','w'],
['w',' ',' ',' ','x',' ',' ',' ',' ',' ','x',' ',' ',' ','w'],
['w',' ',' ',' ','x',' ',' ','z',' ',' ','x',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ','x',' ',' ','z',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ','w',' ',' ','x',' ',' ','w',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
], 
#F1
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ','3',' ','3',' ','3',' ','3',' ','3',' ','h','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F2
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ','w',' ',' ',' ','w',' ','z',' ','w','4','w'],
['w',' ',' ',' ',' ',' ',' ',' ','w',' ',' ',' ','w',' ','w'],
['w',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ','w',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w','p',' ',' ',' ',' ',' ',' ','z',' ',' ',' ','h',' ','B'],
['w',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ','w',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ','w',' ',' ',' ','w',' ','w'],
['w',' ',' ',' ','w',' ',' ',' ','w',' ','z',' ','w','3','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F3
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ','h',' ',' ',' ','4',' ',' ',' ',' ',' ','1','w'],
['w',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ','w','w','w',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ','z',' ',' ',' ',' ','B'],
['w','p',' ',' ',' ',' ',' ',' ',' ','z',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ','w','w','w',' ',' ',' ',' ',' ','B'],
['w',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ','3',' ',' ',' ',' ',' ','1','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F4
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','p',' ',' ',' ',' ',' ',' ','e',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
])

#F0
Floor3ID = (
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ','x','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ','w','w','w','w','w','w','w','x','w',' ','w','w'],
['w',' ',' ',' ',' ',' ','w','x','w','x',' ',' ',' ',' ','w'], 
['w',' ',' ',' ','x',' ',' ',' ','w',' ',' ',' ',' ',' ',' '],
['w','p',' ',' ','w',' ',' ',' ','w',' ',' ','x',' ',' ',' '],
['w',' ',' ','x','w','x','w',' ',' ',' ',' ','w','x',' ',' '],
['w',' ',' ','w','w','x','w','w','w','x','w','w','x',' ','w'],
['w',' ',' ','w','w','x','w','w','w','x','w','w','x','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F1

[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ','w','w','w','w','4',' ',' ','w','w',' ',' ','w'],
['w',' ',' ','w','w','w','w',' ',' ',' ','w','w',' ','1','w'],
['w','2',' ',' ','w','w',' ',' ',' ',' ',' ','w',' ',' ','w'],
['w',' ',' ',' ','w','w',' ',' ',' ',' ',' ','w','1',' ',' '],
['w','p',' ',' ',' ','w',' ',' ','w',' ',' ',' ',' ',' ',' '],
['w',' ',' ',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' ','w'],
['w',' ',' ','w','w',' ',' ',' ','w','w',' ',' ',' ','1','w'],
['w',' ','w','w','w',' ',' ',' ','w','w',' ',' ','1',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#f2
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w'],
['w','x',' ',' ',' ',' ',' ',' ',' ','z',' ',' ',' ','x','w'],
['w',' ',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ','w','w','w',' ',' ',' ',' ',' ','B'],
['w','p',' ','h',' ','z','w','w','w',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' ',' ','B'],
['w','x',' ',' ',' ',' ',' ',' ',' ','z',' ',' ',' ','x','w'],
['w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#f3
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','x','h',' ',' ','h',' ','h',' ',' ','h','x','w','w'],
['w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w','p',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w'],
['w','w','x','h',' ',' ',' ',' ','h',' ',' ','h','x','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F4
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','p',' ','h',' ',' ',' ',' ','e',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
]
)




#F0
Floor4ID =(
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ','w','4','w','4','w','4','w','4','w','4','w',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' '],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','w'],
['w',' ','w',' ','w',' ','w',' ','w',' ','w',' ','w',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F1
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ','4',' ','4',' ',' ',' ','4',' ',' ',' ','w'],
['w',' ',' ','4',' ',' ',' ','4',' ',' ',' ','4',' ',' ','w'],
['w',' ','4',' ',' ',' ',' ',' ','4',' ',' ',' ','4',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F2
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ','w',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' '],
['w','2',' ','w',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' '],
['w',' ',' ','w',' ',' ','w',' ',' ','w',' ',' ',' ','1',' '],
['w',' ',' ','w',' ',' ','w',' ',' ','w',' ',' ','w',' ','w'],
['w',' ','2','w',' ',' ','w',' ',' ','w',' ',' ','w',' ','w'],
['w',' ',' ','w',' ',' ','w',' ',' ','w',' ',' ','w',' ','w'],
['w','p',' ',' ',' ',' ','w',' ',' ',' ',' ',' ','w','1','w'],
['w',' ',' ',' ','h','2','w',' ',' ',' ',' ',' ','w',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F3
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ','w','x','x','x','w',' ',' ',' ',' ','w','4','w'],
['w',' ',' ','w',' ',' ',' ','w',' ',' ','z',' ','w','w','w'],
['w',' ',' ',' ',' ',' ',' ','z',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','B'],
['w',' ',' ',' ',' ',' ',' ','z',' ',' ',' ',' ',' ',' ','B'],
['w','p',' ','w',' ',' ',' ','w',' ',' ','z',' ','w','w','w'],
['w',' ',' ','w','x','x','x','w',' ',' ',' ',' ','w','3','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F4
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ','w',' ','w',' ','w',' ','w',' ','w',' ','w',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','p',' ',' ',' ',' ',' ',' ','e',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
])


#F0
Floor5ID = (
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w',' ',' ',' ',' ',' ',' ','4',' ',' ','w'],
['w',' ','w','w',' ','4',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','h',' ','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ','z',' ',' ',' ',' ',' ',' ','B'],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ','z',' ',' ',' ','B'],
['w',' ',' ','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ','w','w','3',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','w','w','w','w',' ',' ',' ',' ','3',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F1
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' '],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F2
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w',' ','4',' ',' ',' ','4',' ',' ','w',' ',' ',' ','w'],
['w',' ','w',' ',' ',' ',' ',' ',' ',' ',' ','w',' ',' ','w'],
['w',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ','w','1','w'],
['w',' ',' ','2','w',' ',' ',' ','w',' ',' ',' ',' ','w','w'],
['w','p',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ',' '],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w','1',' ',' '],
['w',' ',' ','h',' ','3',' ',' ',' ',' ',' ',' ','w',' ',' '],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F3
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w',' ',' ',' ','w',' ',' ',' ',' ','w',' ',' ',' ',' ','B'],
['w',' ','z',' ',' ',' ',' ','z',' ','w',' ',' ','z',' ','B'],
['w',' ',' ',' ',' ',' ',' ',' ',' ','w',' ',' ',' ',' ','B'],
['w',' ',' ',' ','w',' ',' ',' ','w','w','w',' ',' ',' ','B'],
['w',' ',' ','w','w','w',' ',' ',' ','w',' ',' ',' ','w','w'],
['w',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','p',' ',' ','w',' ',' ','z',' ',' ',' ',' ','z',' ','w'],
['w',' ',' ',' ','w',' ',' ',' ',' ','w',' ',' ',' ',' ','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
],
#F4
[
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','2',' ',' ',' ',' ',' ','h',' ',' ',' ',' ','4','1','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ','F',' ',' ',' ',' ','w'],
['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
['w','2',' ',' ',' ',' ',' ','h',' ',' ',' ',' ','3','1','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
])

