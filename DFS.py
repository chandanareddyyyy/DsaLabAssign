def dfs_permutations(elements):
    result = [] 
    
   
    def dfs(path, used):
       
        if len(path) == len(elements):
            result.append(path[:])  
            return
        
       
        for i, element in enumerate(elements):
            if not used[i]:
                used[i] = True  
                path.append(element) 
                
                dfs(path, used)
                
                
                path.pop() 
                used[i] = False 
    
    dfs([], [False] * len(elements)) 
    return result



elements = [1, 2, 3]
permutations = dfs_permutations(elements)
print("All Permutations:", permutations)
