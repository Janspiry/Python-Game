import sys,pygame,random
from pygame.locals import *

pygame.init()
#图片参数设置
bk_image='bk.png'
bg_image='bg.png'
begin_image='begin.png'
barrier_image='barrier.png'
car_image='car.png'
cover_image='cover.png'

# 辅助功能图片
switch_image_off='switch_image_off.png'
switch_image_on='switch_image_on.png'
left_on_image='left_on.png'
left_off_image='left_off.png'
right_off_image='right_off.png'
right_on_image='right_on.png'
cover_car_left_image='cover_car_left.png'
cover_car_right_image='cover_car_right.png'

# 窗口图片参数设置
screen =pygame.display.set_mode((300,500))
screen_width,screen_height=300,500
pygame.display.set_caption('Road')
font1= pygame.font.SysFont("黑体",30)
font2= pygame.font.Font(None,24)
bk=pygame.image.load(bk_image).convert_alpha()
bg=pygame.image.load(bg_image).convert_alpha()
begin=pygame.image.load(begin_image).convert_alpha()
barrier=pygame.image.load(barrier_image).convert_alpha()
car=pygame.image.load(car_image).convert_alpha()
cover=pygame.image.load(cover_image).convert_alpha()

switch_off=pygame.image.load(switch_image_off).convert_alpha()
switch_on=pygame.image.load(switch_image_on).convert_alpha()
left_on=pygame.image.load(left_on_image).convert_alpha()
left_off=pygame.image.load(left_off_image).convert_alpha()
right_on=pygame.image.load(right_on_image).convert_alpha()
right_off=pygame.image.load(right_off_image).convert_alpha()
cover_car_left=pygame.image.load(cover_car_left_image).convert_alpha()
cover_car_right=pygame.image.load(cover_car_right_image).convert_alpha()

#事件处理
#设置按esc键退出游戏
def keyboardCheck():
	keys=pygame.key.get_pressed()
	if(keys[K_ESCAPE]):
		quitGame()
#设置速度
def velSet(num):
	if(num<100):
		return 2+num/100
	elif(num<400):
		return 2.5+num/200
	else:
		return 5+num/500
#输出文字函数
def print_text(font,x,y,text,color=(0,0,0)):
	imgText=font.render(text,True,color)
	screen.blit(imgText,(x,y))
#退出游戏设置
def quitGame():
	pygame.quit()
	sys.exit()
#游戏界面设置
def beginGame():
	screen.fill((255,255,255))
	screen.blit(bk,(0,0))
	global random_car,top_x,car_road,game_over,vel_level,mile
	print_text(font2,240,485,'vel:'+str(vel_level))
	print_text(font2,0,485,'mile:'+str(mile))
	for i in top_x[0]:
		screen.blit(barrier,(6,i))	#显示车道车辆现在位置
	for i in top_x[1]:
		screen.blit(barrier,(90,i))
	for i in top_x[2]:
		screen.blit(barrier,(170,i))
	for i in top_x[3]:
 		screen.blit(barrier,(254,i))
	keys=pygame.key.get_pressed()
	if(keys[K_ESCAPE]):
		quitGame()
	if(keys[K_RIGHT]):	#设置左右按键功能
		screen.blit(car,(254,380))
		screen.blit(right_on,(175,470))
		car_road[3]=1
		car_road[2]=0
	else:
		screen.blit(car,(170,380))
		screen.blit(right_off,(175,470))
		car_road[3]=0
		car_road[2]=1
	if(keys[K_LEFT]):
		screen.blit(car,(6,380))
		screen.blit(left_on,(90,470))
		car_road[0]=1
		car_road[1]=0
	else:
		screen.blit(car,(90,380))
		screen.blit(left_off,(90,470))
		car_road[0]=0
		car_road[1]=1
	for i in range(4):		#碰撞检测
		for j in top_x[i]:
			if(car_road[i]==1 and j>-80 and j>300 and j<460):
				game_over=1

#登录界面设置
def welcome():
	global cover_time,direction,switch
	screen.blit(bg,(0,0))	#设置背景
	print_text(font2,70,465,'music:')	#设置文字
	print_text(font2,210,45,'vel:'+str(vel_level))
	print_text(font2,40,45,'mile:'+str(mile))
	if(switch==0):
		screen.blit(switch_off,(200,460))	#切换背景音乐开关图片
	else:
		screen.blit(switch_on,(200,460))
	x_centered=screen_width/2-begin.get_width()/2
	y_centered = screen_height/2 -begin.get_height()/2
	screen.blit(begin,(x_centered,y_centered-200))
	screen.blit(cover,(10,380))
	if(direction==0):	#设置左右图片
		screen.blit(cover_car_right,(10+cover_time//10,380))
	else:	
		screen.blit(cover_car_left,(-10-cover_time//10,380))
	if(cover_time//10>=210):#检测封面车辆变向
		cover_time=0
		direction^=1
# 初始参数设置
# 背景音乐设置
def playBgm(switch):
	if(switch==1):
		pygame.mixer.music.unpause()
	else:
		pygame.mixer.music.pause()

# 参数列表
mile=0	#路程
vel_level=1;	#速度
game_over=0		#游戏结束标志
game_begin=0	#游戏开始标志
clock = pygame.time.Clock()#控制帧率用
top_x=[list() for i in range(4)]	#四条车道设置
random_car=[0]*4	#随机生成四条车道
car_road=[0]*4		#判断车道是否重合
cover_time=0		#登录界面车辆运行时间
direction=0			#方向
switch=0			#背景音乐开关
time=0				#游戏时间
s=95				#初始坐标

#初始参数载入
pygame.mixer.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(1)
pygame.mixer.music.pause()
# 主循环
while True:
	for event in pygame.event.get():
		if(event.type==QUIT):
			quitGame()
		elif(event.type==MOUSEBUTTONDOWN):
			mouse_x,mouse_y=event.pos
			if((mouse_x<=screen_width/2+begin.get_width()/2) \
				and (mouse_x>=screen_width/2-begin.get_width()/2) \
				and (mouse_y>=screen_height/2-begin.get_height()/2-200 )\
				and (mouse_y<=screen_height/2+begin.get_height()/2-200)):#点击开始按钮响应
				game_begin=1#设置各种参数
				game_over=0
				top_x=[list() for i in range(4)]
				random_car=[0]*4
				car_road=[0]*4
				cover_time=0
				direction=0
				time=0
			elif(mouse_x<=240+40 and mouse_x>=240-40\
				and mouse_y>=450-24 and mouse_y<=450+24):#播放背景音乐响应
				switch^=1
				playBgm(switch)
	keyboardCheck()
	cover_time+=1
	if(game_begin==0 or game_over==1):#事件判断
		welcome()
	else:
		beginGame()
		time+=1;	#时间累加
		mile=time//1000		#路程计数
		vel_level=velSet(mile)
		s+=(vel_level/10)
		if(s>=100+random.randint(0,10)):	#超过一段距离可以设置新的车，随机产生车
			s=-80
			random_car=[random.randint(0,1) for i in range(4)]
			if(random_car[0]==random_car[1]):
				random_car[random.randint(0,1)]=random_car[1]^1		#避免两条车道同时出现车
			if(random_car[2]==random_car[3]):
				random_car[2+random.randint(0,1)]=random_car[3]^1
		for i in range(4):	#将新产生的车辆加入车道
			if(random_car[i]==1):
				top_x[i].append(-80)
				random_car[i]=0
			for j in range(len(top_x[i])):
				if(top_x[i][-j-1]>=500):
					del top_x[i][-j-1]
			for j in range(len(top_x[i])):
				top_x[i][j]+=(vel_level+random.randint(0,1))/10
	pygame.display.update()##刷新界面