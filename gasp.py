from gasp import *

begin_graphics()

def draw_face(x,y):
    Line((200, 100), (100, 300))
    Circle((x-15, y+10), 5)
    Line((x, y+10), (x-10, y-10))


draw_face(200,200)
update_when('key_pressed')
end_graphics()