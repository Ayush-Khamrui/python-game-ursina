from ursina import *
global score
def update():
    global score
    score +=1 
    circle.y -= circle.dy
    circle2.y -= circle2.dy1
    circle3.y -= circle3.dy2
    circle4.y -= circle4.dy3
    circle5.y -= circle5.dy4
    circle6.y -= circle6.dy5
    if held_keys['a']:
        load_person.x -= 4*time.dt
    if held_keys['d']:
        load_person.x += 4*time.dt
    
    hit_info = circle.intersects()
    hit_info1 = circle2.intersects()
    hit_info2 = circle3.intersects()
    hit_info3 = circle4.intersects()
    hit_info4 = circle5.intersects()
    hit_info5 = load_person.intersects()
    hit_info6 = circle6.intersects()
    
    if hit_info5.hit:
        if hit_info5.entity==circle or hit_info5.entity==circle2 or hit_info5.entity==circle3 or hit_info5.entity==circle4 or hit_info5.entity==circle5 or hit_info5.entity==circle6:
            end("final Score is: "+str(score))
        if hit_info5.entity==block12:
            load_person.x += 4*time.dt
        if hit_info5.entity==block3:
            load_person.x -= 4*time.dt

    if hit_info.hit:
        circle.dy = -circle.dy
    if hit_info1.hit:
        circle2.dy1 = -circle2.dy1
    if hit_info2.hit:
        circle3.dy2 = -circle3.dy2
    if hit_info3.hit:
        circle4.dy3 = -circle4.dy3
    if hit_info4.hit:
        circle5.dy4 = -circle5.dy4
    if hit_info6.hit:
        circle6.dy5 = -circle6.dy5
    
def end(final_score):
    display = Text(text=final_score, scale =2,origin=(0,0),background=True,color=color.green)
    application.pause()


app = Ursina()
score = 0


window.title = 'Ayush Game'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = False
window.color = color.white


block2 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (7,-3),collider='box')
block3 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (7,-2),collider='box')
block4 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (7,-1),collider='box')
block5 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (7,0),collider='box')
block6 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (7,1),collider='box')
block7 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (7,2),collider='box')
block8 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (7,3),collider='box')
block9 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (7,4),collider='box')

block11 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,-3),collider='box')
block12 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,-2),collider='box')
block13 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,-1),collider='box')
block14 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,0),collider='box')
block15 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,1),collider='box')
block15 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,1),collider='box')
block15 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,1),collider='box')
block16 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,2),collider='box')
block17 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,3),collider='box')
block18 = Entity(model = 'quad',texture = 'brick',color = color.orange, scale=(1,1), position = (-7,4),collider='box')

floor = Entity(model = 'quad',color=color.green,scale=(16,2),position=(0,-4),collider = 'box')
ceil = Entity(model = 'quad',texture='brick',color=color.red,scale=(16,2),position=(0,4),collider='box')

person = load_texture('/Sans.png')
load_person = Entity(model = 'quad',texture = person,position = (0,-2.5,0),collider='box')

circle = Entity(model = "circle",color = color.red,position =(-5,2),dy = 0.08, collider = 'box')
circle2 = Entity(model = "circle",color = color.red,position =(-3,2),dy1 = 0.07, collider = 'box')
circle3 = Entity(model = "circle",color = color.red,position =(-1,2),dy2 = 0.06, collider = 'box')
circle4 = Entity(model = "circle",color = color.red,position =(1,2),dy3 = 0.05, collider = 'box')
circle5 = Entity(model = "circle",color = color.red,position =(3,2),dy4 = 0.04, collider = 'box')
circle6 = Entity(model = "circle",color = color.red,position =(5,2),dy5 = 0.04, collider = 'box')

app.run()