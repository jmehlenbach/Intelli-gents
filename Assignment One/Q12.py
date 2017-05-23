board = {
	1:'b', 2:'b', 3:'b',
	4:'o', 5:'o', 6:'o',
	7:'w', 8:'w', 9:'w'}

for bk, bv in board.iteritems():
	if bv == 'b':
		for ok1, ov1 in board.iteritems():
			if ov1 == 'o':
				board[bk], board[ok1] = board[ok1], board[bk]
				for wk, wv in board.iteritems():
					if wv == 'w':
						for ok2, ov2 in board.iteritems():
							if ov2 == 'o':
								board[wk], board[ok2] = board[ok2], board[wk]
								for i in range(1, 10):
									print board[i],
									if i%3 == 0:
										print "\n"
								print "\n"
								board[wk], board[ok2] = board[ok2], board[wk]

				board[bk], board[ok1] = board[ok1], board[bk]
