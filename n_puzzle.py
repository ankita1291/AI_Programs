import random
import numpy as np 



#np.where(init_config==0, 'b',z)
final_config = np.arange(9).reshape((3,3))
print(final_config)



def where_to_go(row, col):
	possible_moves = list()
	print("row col", row, col)
	if row > 0:
				possible_moves.append((row-1,col))
	if row < 2:
				possible_moves.append((row+1,col))
	if col > 0:
				possible_moves.append((row,col-1))
	if col < 2:
				possible_moves.append((row,col+1))
	return possible_moves

def get_best_move(init_config, possible_moves, row, col):
	temp_list = init_config
	h = []
	for i in possible_moves:
		print("----------" , possible_moves)
		temp_list = init_config
		temp_list[row, col], temp_list[i] = temp_list[i], temp_list[row, col]
		h.append(np.sum(temp_list != final_config))
		#h[i] = set(temp_list).intersection(final_config)
	best_move  = h.index(min(h))
	best_action = possible_moves[best_move]
	return best_action



def best_first_search():
	init_config = np.arange(9).reshape((3,3))
	np.random.shuffle(init_config)
	print("Initial Configuration", init_config)
	h1 = np.sum(init_config != final_config)
	print(h1)
	#get the index of 0
	i, j  = np.where(init_config==0)
	while((init_config != final_config).all()):
		#get moves
		possible_moves  = where_to_go(i, j)
		best_action = get_best_move(init_config, possible_moves, i, j)
		init_config[i, j], init_config[best_action] = init_config[best_action], init_config[i, j]
		print(init_config)
		i, j = best_action
		print(i,j)

best_first_search()





	