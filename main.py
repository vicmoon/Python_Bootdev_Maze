from theCanvas import MyWindow
from shapes import Cell, Point, Line
from maze import Maze 

def main():
    window = MyWindow()

    # # some standalone lines
    # window.draw_line(Line(Point(50, 50), Point(150, 150)), fill_color="blue", width=2)
    # window.draw_line(Line(Point(200, 50), Point(300, 150)), fill_color="green", width=2)

    # # two cells with different wall configurations
    # c1 = Cell(window)
    # c2 = Cell(window)

    # c1.draw(50, 50, 100, 100)
    # c2.draw(110, 50, 160, 100)

    # #  step forward 
    # c1.draw_move(c2)
    # c2.draw_move(c1, undo=True)


    # create a maze
    maze = Maze(
        x1=20, y1=20,
        num_rows=11, num_cols=17,
        cell_size_x=50, cell_size_y=50,
        win=window
    )


    

    # now hand control over to the window loop,
    # which will call redraw() every frame
    window.wait_for_close()












if __name__ == "__main__":
    main()
