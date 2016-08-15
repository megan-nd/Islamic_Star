import turtle
t=turtle.Pen()

def oneline():  			    # geometric design
	t.speed(0)
	for x in range(1,12):
		t.forward(202)
		t.left(77)
		t.forward(185)
		t.right(80.4)
		t.forward(185)
		t.left(77)
		t.forward(202)
		startip()
		t.right(110)

def startip():
    t.right(110)
    t.forward(115)
    t.left(145)
    t.forward(80)
    t.right(60)
    t.forward(75)
    t.left(140)
    t.forward(75)
    t.right(60)
    t.forward(80)
    t.left(145)
    t.forward(115)

def bottomleft():
    t.up()
    t.back(250)
    t.right(90)
    t.forward(240)
    t.left(90)
    t.down()

def onelineoutline():
    t.pensize(20)
    oneline()
    t.pensize(10)
    t.color("white")
    oneline()

bottomleft()
onelineoutline()
