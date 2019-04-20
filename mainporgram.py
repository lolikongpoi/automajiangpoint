#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#这是一个针对预制选手库进行日本麻将计分、排名的python小程序
#copyright lolikongpoi
#2019/4/16
import sys

#create class-----------------------
class Database:
	"数据库"
	list=[]
	def __init__(self,file):
		self.file=file
		Database.list.append(self)

	def lines(self):
		lines0=self.text.split("\n")
		lines1=[]
		for i in lines0:
			try:
				if i[0] != "!":
					lines1.append(i)
			except IndexError:
				pass
		setattr(self,"lines",lines1)
		#逐行化数据库

class Palyer:
	"选手"
	number=0
	def __init__(self,times,avgrank,avgpoint,avgjspoint,stp,ndp,rdp,thp,flyp,rankhistory):
		self.times=times
		self.avgrank=avgrank
		self.avgpoint=avgpoint
		self.avgjspoint=avgjspoint
		self.stp=stp;self.ndp=ndp;self.rdp=rdp;self.thp=thp;self.flyp=flyp
		self.rankhistory=rankhistory
		playernumber+=1
		 #创建选手对象


#comand lines function--------------
def help():#当程序作为脚本运行时的帮助
	print("做梦呢吧，怎么可能会有帮助。要退出的话输入exit()")
	print('#copyright lolikongpoi\n#2019/4/16')


#database check & generate----------
filelist=("newgameinfo.txt","playerinfo.txt","gameinfo.txt","ranking.txt")
#本程序使用的数据库文件
form="""这是本程序的数据库文件用途和格式说明。
newgameinfo.txt：新增加的对局信息
playerinfo.txt：选手各项信息（场次，平均顺位，平均得点，平均精算点，1/2/3/4位率，击飞率，历史名次百分比)
gameinfo.txt：历史对战得点信息
ranking.txt：当前各个选手名次，积分，积分升降
在每个文件中有范例格式"""
#数据库文件格式说明
fileform={"newgameinfo.txt":"!player1\tpoint1\tplayer2\tpoint2\tplayer3\tpoint3\tplayer4\tpoint4",
"playerinfo.txt":"!player1\tgametimes\tavgrank\tavgpoint\tavgjspoint\t1stp\t2ndp\t3rdp\t4thp\tflyp\trankhistory",
"gameinfo.txt":"!gameNo.\t1stplayer\tpoint\tjspoint\t2ndplayer\tpoint\tjspoint\t3rdplayer\tpoint\tjspoint\t4thplayer\tpoint\tjspoint",
"ranking.txt":"!player1\tjspoint\trank\tdelta"}
#数据库范例头文件
filestate="未进行文件操作"

try:
	newgameinfo=Database(open("newgameinfo.txt","r+"))
except FileNotFoundError:
	print("没有找到文件newgameinfo.txt。请问是否是第一次使用此程序，是输入y，否输入n。输入y将覆盖生成空白数据库及格式说明。")
	answer=input()
	if answer=="y":
		with open('form.txt', 'w') as f:
			filestate=''
			f.write(form)
			print('已生成格式说明文件form.txt')
		for filename in filelist:
			with open(filename, 'w') as f:
				f.write(fileform[filename])
				filestate+="已生成文件%s"%filename+"\n"
	if answer=="n":
		print("请检查数据库文件完整性，包含文件",filelist)
	print(filestate);exit()


#read database---------------------
playerinfo=Database(open("playerinfo.txt","r+"))
ranking=Database(open("ranking.txt","r+"))
gameinfo=Database(open("gameinfo.txt","r+"))
#创建数据库对象
setattr(gameinfo,"text",gameinfo.file.read())
setattr(newgameinfo,"text",newgameinfo.file.read())
setattr(playerinfo,"text",playerinfo.file.read())
setattr(ranking,"text",ranking.file.read())
#读入数据库文本

for i in Database.list:
	i.lines()
	#print(i.lines)
	#将输入逐行拆分


#read player info------------------


#read new game info----------------
if len(newgameinfo.lines)==0:
	print("未检测到任何信息，请检查是否已经向newgameinfo.txt添加有效的新对战信息")
	print(filestate);exit()
	#检测输入是否为空

legallines=0
illegalines=0
unknownplayer=[]
illegalinput=0
pointerror=0
#初始化输入统计

for i in newgameinfo.lines:
	i=i.split("\t")
	print(i)

	if len(i)!=8:
		illegalines+=1;illegalinput+=1
		continue

	try:
		sumpoint=int(i[1])+int(i[3])+int(i[5])+int(i[7])
	except:
		illegalines+=1;illegalinput+=1
		continue

	if sumpoint==100000:
		legallines+=1
	else:
		illegalines+=1;pointerror+=1
linesstate=[legallines,illegalines,illegalinput,len(unknownplayer),pointerror]
print(linesstate)
#输入统计

if legallines == 0:
	print()
if legallines > 0:
	if sum(linesstate[1:])==0:
		print('新对战信息读入完成，检测到%d场新对战，没有非法输入、点数错误与未知选手'%linesstate[0])
	elif sum(linesstate[3:])==0:
		print('新对战信息读入完成，检测到%d场新对战，%d行非法输入，没有点数错误与未知选手'
			%(linesstate[0],linesstate[1]))
		print("要忽略非法数据继续，输入y。任意其他输入将退出。")
		answer=input()
		if answer=="y":
			pass
		else:
			print(filestate);exit()
			


#print(ranking.text)

while 1:
	try:
		eval(sys.stdin.readline())
	except NameError:
		pass
	except SyntaxError:
		print("输入错误，请检查语法，输入help()获得帮助")
