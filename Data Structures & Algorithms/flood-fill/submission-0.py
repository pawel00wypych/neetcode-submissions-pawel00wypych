class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_pixel_color = image[sr][sc]
        if starting_pixel_color == color:
            return image

        def dfs(sr: int, sc: int) -> None:
            if min(sr, sc) < 0 or sr == len(image) or sc == len(image[0]) or image[sr][sc] == color or image[sr][sc] != starting_pixel_color:
                return
            elif image[sr][sc] == starting_pixel_color:
                image[sr][sc] = color 

            dfs(sr, sc-1) #left
            dfs(sr, sc+1) #right
            dfs(sr-1, sc) #up
            dfs(sr+1, sc) #down
            return

        dfs(sr, sc)
        return image