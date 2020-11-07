import box

class Board:
    # Attributes
    #   score
    #   dimensions
    #   available moves
    #   completed moves
    #   list of possible boxes
    
    # Initializer (takesnumber of rows and columns)
    def __init__(self, rows, cols):
        self.row = int(rows)
        self.col = int(cols)
        
        self.score = [0,0] # Format: [p1,p2]
        self.dimensions = [self.row, self.col]
        
        # TO DO self.available_moves = self.generateMoves()
        
        self.completed_moves = []
        self.possible_boxes = self.generateBoxes(self.row,self.col)

    # Create a queue of all available moves/lines that can be played on this board, given a particular number of rows and columns
    def generateMoves(self, r, c):
        # Should store each line on the board as a set (tuple) of coordinates in a queue
        # NOTE from Jared: I coded the text representation to use ((x,y),(x,y)), so a tuple of tuples
        # TODO: Ian
        return 

    # Creates a list of Box objects (from box.py)
    def generateBoxes(self, rows, cols):
        box_list = []
        for i in range(0,rows):
            for j in range(0,cols):
                self.box = box.Box(i, j)
                box_list.append(box)
        return box_list

    # Prints a text representation of the current board state for the command line
    def displayBoard(self):
        for i in range(0,self.dimensions[0]-1):
            horiz_row = ""
            for j in range(0,self.dimensions[1]):
                cell_width = "."
                if ((j,i),(j+1,i)) in self.completed_moves:
                    cell_width += "_____"
                else:
                    cell_width += "     "
                horiz_row += cell_width
            print(horiz_row)
            vert_row = ""
            for j in range(0,self.dimensions[1]):
                cell_width = ""
                if ((j,i),(j,i+1)) in self.completed_moves:
                    cell_width += "|"
                else:
                    cell_width += " "
                cell_width += "     "
                vert_row += cell_width
            print(vert_row)
            box_marker_row = ""
            for j in range(0,self.dimensions[1]):
                cell_width = ""
                if ((j,i),(j,i+1)) in self.completed_moves:
                    cell_width += "|"
                else:
                    cell_width += " "
                cell_width += "  "
                if j != self.dimensions[1]-1:
                    box_found = False
                    for box in self.possible_boxes:
                        if self.box.top_left[0] == j and self.box.top_left[1] == i and box.complete:
                            cell_width += str(box.filled_by)
                            box_found = True
                    if box_found == False:
                        cell_width += " "
                else:
                    cell_width += " "
                cell_width += "  "
                box_marker_row += cell_width
            print(box_marker_row)
            print(vert_row)
        horiz_row = ""
        for j in range(0,self.dimensions[1]):
            cell_width = "."
            if ((self.dimensions[0],j),(self.dimensions[0]+1,j)) in self.completed_moves:
                cell_width += "_____"
            else:
                cell_width += "     "
            horiz_row += cell_width
        print(horiz_row)


    # Check self.available_moves for the coordinates given in the parameters
    # If the coordinates are in self.available_moves then:
    #   - Remove the coordinates from self.available_moves
    #   - Add the coordinates to self.completed_moves
    #   - Check our list of boxes (call checkBoxes()) to determine if we have an completed boxes with this new line
    def connectDots(self, coordinates, player):
        # TODO: Ian
        return 

    # Checks the list of boxes to see if the coordinates for the newly-added line completes a box
    # Increment score for player who completed the box
    # Change self.owner in Box object (from box.py) to player's identity
    def checkBoxes(self, coordinates, player):
        # TODO: Victor
   
        
        
        
        return 
