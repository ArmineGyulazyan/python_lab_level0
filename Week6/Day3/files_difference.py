def difference(path1,path2):
    with open(path1) as file1,open(path2) as file2, open('path3.txt','w') as output:
        lines1=file1.read().splitlines()
        lines2=file2.read().splitlines()
        min_len = min(len(lines1),len(lines2))
        for i in range(min_len):
            diff = set(lines1[i].split())^set(lines2[i].split())
            output.write(f"lines{i+1}:{''.join(diff)}")
            output.write('\n')


difference('path1','path2')
