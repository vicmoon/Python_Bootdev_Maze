import unittest 
# assuming your `Maze` class is in a file called `maze.py`
from maze import Maze 


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )


    def test_break_entrance_and_exit():
        # build a small maze without a window (win=None is fine for memory-only tests)
        m = Maze(x1=0, y1=0, num_rows=3, num_cols=3, cell_size_x=10, cell_size_y=10, win=None)
        # before breaking, every cell has all walls=True
        assert m.cells[0][0].has_top_wall is True
        assert m.cells[2][2].has_bottom_wall is True

        # now run the method that “breaks” entrance+exit
        m._Maze__break_entrance_and_exit()

        # verify the flags flipped
        assert m.cells[0][0].has_top_wall is False
        assert m.cells[2][2].has_bottom_wall is False


if __name__ == "__main__":
    unittest.main()