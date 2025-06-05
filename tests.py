import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None, seed=0)

        # Now since __break_entrance_and_exit and __break_walls_r have NOT
        # yet been called, the grid should simply exist with all walls up:
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        m = Maze(0, 0, 3, 3, 10, 10, win=None, seed=0)
        
        # Before calling break_entrance_and_exit, walls are still intact:
        self.assertTrue(m._Maze__cells[0][0].has_top_wall)
        self.assertTrue(m._Maze__cells[2][2].has_bottom_wall)

        # Now explicitly call the private method under test:
        m._Maze__break_entrance_and_exit()
        self.assertFalse(m._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m._Maze__cells[2][2].has_bottom_wall)

    def test_reset_cells_visited(self):
        m = Maze(0, 0, 2, 3, 10, 10, win=None, seed=0)

        # Carve the maze so that every cell becomes visited:
        m._Maze__break_walls_r(0, 0)

        # Now all cells should have visited==True
        for col in range(len(m._Maze__cells)):
            for row in range(len(m._Maze__cells[0])):
                self.assertTrue(
                    m._Maze__cells[col][row].visited,
                    f"Cell[{col}][{row}] should be visited after carving."
                )

        # Now reset everything
        m._Maze__reset_cells_visited()
        for col in range(len(m._Maze__cells)):
            for row in range(len(m._Maze__cells[0])):
                self.assertFalse(
                    m._Maze__cells[col][row].visited,
                    f"Cell[{col}][{row}] should be False after reset."
                )

if __name__ == "__main__":
    unittest.main()
