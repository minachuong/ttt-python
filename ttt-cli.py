# print(u'\u2550')
# print(u'\u2551')
# print(u'\u2554')
# print(u'\u2557')
# print(u'\u255A')
# print(u'\u255D')
# print(u'\u2560')
# print(u'\u2563')
# print(u'\u2566')
# print(u'\u2569')
# print(u'\u256C')

horizontal_line = u'\u2550'
vertical_line = u'\u2551'
top_left_corner = u'\u2554' 
top_right_corner = u'\u2557' 
bottom_left_corner = u'\u255A'
bottom_right_corner = u'\u255D' 
left_intersect = u'\u2560' 
right_intersect = u'\u2563'
top_intersect = u'\u2566'
bottom_intersect = u'\u2569'
middle_intersect =  u'\u256C'
p1 = "1"
p2 = "2"
p3 = "3"
p4 = "4"
p5 = "5"
p6 = "6"
p7 = "7"
p8 = "8"
p9 = "9"

# Board
print(top_left_corner + horizontal_line + top_intersect + horizontal_line + top_intersect + horizontal_line + top_right_corner)
print(vertical_line + p1 + vertical_line + p2 + vertical_line + p3 + vertical_line)
print(left_intersect + horizontal_line + middle_intersect + horizontal_line + middle_intersect + horizontal_line + right_intersect)
print(vertical_line + p4 + vertical_line + p5 + vertical_line + p6 + vertical_line)
print(left_intersect + horizontal_line + middle_intersect + horizontal_line + middle_intersect + horizontal_line + right_intersect)
print(vertical_line + p7 + vertical_line + p8 + vertical_line + p9 + vertical_line)
print(bottom_left_corner + horizontal_line + bottom_intersect + horizontal_line + bottom_intersect + horizontal_line + bottom_right_corner)

