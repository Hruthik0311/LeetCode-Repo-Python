class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    d = int(ch) - 1
                    bit = 1 << d
                    box = (r // 3) * 3 + (c // 3)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box] |= bit
        def bitcount(x: int) -> int:
            return x.bit_count() if hasattr(x, "bit_count") else bin(x).count("1")
        def backtrack(k: int) -> bool:
            if k == len(empties):
                return True
            best_i = -1
            best_mask = 0
            best_count = 10
            for i in range(k, len(empties)):
                r, c = empties[i]
                b = (r // 3) * 3 + (c // 3)
                mask = (~(rows[r] | cols[c] | boxes[b])) & 0x1FF
                if mask == 0:
                    return False
                cnt = bitcount(mask)
                if cnt < best_count:
                    best_count = cnt
                    best_mask = mask
                    best_i = i
                    if cnt == 1:
                        break
            empties[k], empties[best_i] = empties[best_i], empties[k]
            r, c = empties[k]
            b = (r // 3) * 3 + (c // 3)
            mask = (~(rows[r] | cols[c] | boxes[b])) & 0x1FF
            m = mask
            while m:
                bit = m & -m
                d = (bit.bit_length() - 1)
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                board[r][c] = str(d + 1)
                if backtrack(k + 1):
                    return True
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = '.'
                m &= m - 1
            empties[k], empties[best_i] = empties[best_i], empties[k]
            return False
        backtrack(0)
