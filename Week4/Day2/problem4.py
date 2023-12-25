def trap_area(sr,b_base,h_base_side):
    hight = (sr**2 - h_base_side**2)**0.5
    s_base = b_base - 2*h_base_side
    area = ((b_base+s_base)/2)*hight
    return area

print(trap_area(25,30,7))