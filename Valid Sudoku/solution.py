class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        }
        columns = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        }
        box = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        }

        boardbox = [[ 0,0,0,1,1,1,2,2,2],[3,3,3,4,4,4,5,5,5],[6,6,6,7,7,7,8,8,8]]

        boxlevel = 0
        row = 0
        col = 0

        while True:
            num = board[row][col]
            if "." not in num:
                if num in rows[row]:
                    return False
                if num in columns[col]:
                    return False
                if num in box[boardbox[boxlevel][col]]:
                    return False

                rows[row] += num
                columns[col] += num
                box[boardbox[boxlevel][col]] += num

            if (col == 8) and (row == 8):
                break
            elif col == 8:
                row += 1
                col = 0

                if row%3 == 0:
                    boxlevel += 1
            else:
                col += 1



        return True