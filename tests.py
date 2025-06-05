import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None, seed=0)
        # Because we used "__cells" as a private attribute, access it via name‐mangling:
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        m = Maze(0, 0, 3, 3, 10, 10, win=None, seed=0)
        # Before breaking, both flags should be True
        self.assertTrue(m._Maze__cells[0][0].has_top_wall)
        self.assertTrue(m._Maze__cells[2][2].has_bottom_wall)

        # Call the private method
        m._Maze__break_entrance_and_exit()

        # Now those two should be False
        self.assertFalse(m._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m._Maze__cells[2][2].has_bottom_wall)

    def test_reset_cells_visited(self):
        # Build a small maze so that __break_walls_r visits every cell
        m = Maze(0, 0, 2, 3, 10, 10, win=None, seed=0)
        # After carving, all cells should have visited == True
        for col in range(m._Maze__cells.__len__()):
            for row in range(m._Maze__cells[0].__len__()):
                self.assertTrue(
                    m._Maze__cells[col][row].visited,
                    f"Cell[{col}][{row}] should be visited after carve."
                )

        # Now reset them
        m._Maze__reset_cells_visited()
        for col in range(m._Maze__cells.__len__()):
            for row in range(m._Maze__cells[0].__len__()):
                self.assertFalse(
                    m._Maze__cells[col][row].visited,
                    f"Cell[{col}][{row}] should be reset to False."
                )

if __name__ == "__main__":
    unittest.main()
