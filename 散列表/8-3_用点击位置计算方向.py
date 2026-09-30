import math

dct = {0:'东',1:'东北',2:'北',3:'西北',4:'西',-1:'东南',-2:'南',-3:'西南',-4:'西'}

#传入角度，获取对应的方向
def getDirect(angle):
	angle = angle+22.5
	key = math.floor(angle/45)
	print(key)
	return dct[key]

angle = -135
diretion = getDirect(angle)
print(diretion)
