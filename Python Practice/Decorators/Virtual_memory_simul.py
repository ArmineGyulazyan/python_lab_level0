def page_aloc(page_n,frames,page_table):
    if 0 in frames:
        empty_fr = frames.index(0)
        frames[empty_fr] = page_n
        page_table[page_n] = empty_fr
    else:
        page_table.pop(page_n)
    print(page_table)

def page_access(page_n,page_table):
    if page_n in page_table:
        print(page_n,'->',page_table[page_n])
    else:
        print('no such page')

def memory_status(frames):
    for frame_n,page_n in enumerate(frames):
        if page_n != 0:
            print(frame_n,page_n)
        else:
            print(frame_n,'empty')


page_size = 4096
num_frames = 5
frames = [0]*num_frames
page_table = {}
while True:
    print("\nMenu for Virtual memory stimul\n1.Page allocation\n2.Page access\n3.Memory status\n4.Exit\n")
    inp = int(input('Choose an option: '))
    if inp == 1:
        inp = int(input('Enter page num to memory: '))
        page_aloc(inp,frames,page_table)
    elif inp == 2:
        inp1 = int(input('Enter page num to access in memory: '))
        page_access(inp1,page_table)
    elif inp == 3:
        memory_status(frames)
    elif inp == 4:
        break
    else:
        print('Invalid input,Choose again')