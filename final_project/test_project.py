import project

def test_create_board():
    assert project.create_board() == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def test_check_win_with_winning_board():
    board = [
        ['X', 'X', 'X'],
        ['O', 'O', '-'],
        ['-', '-', '-']
    ]
    assert project.check_win(board, 'X') == True

def test_check_win_with_no_winning_board():
    board = [
        ['X', 'O', '-'],
        ['-', 'O', '-'],
        ['-', '-', 'X']
    ]
    assert project.check_win(board, 'X') == False

def test_check_win_vertical():
    board = [
        ['X', '-', '-'],
        ['X', 'O', 'O'],
        ['X', '-', '-']
    ]
    assert project.check_win(board, 'X') == True

def test_check_win_diagonal():
    board = [
        ['O', 'X', 'X'],
        ['X', 'O', '-'],
        ['-', '-', 'O']
    ]
    assert project.check_win(board, 'O') == True

def test_tie():
    board = [
        ['O', 'X', 'X'],
        ['X', 'O', 'O'],
        ['X', 'O', 'X']
    ]
    assert project.check_tie(board) == True