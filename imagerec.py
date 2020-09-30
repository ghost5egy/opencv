import cv2 as cv
import numpy as np
import sys 


#himg = cv.imread(sys.argv[1], cv.IMREAD_UNCHANGED)
himg = cv.imread(sys.argv[1], cv.IMREAD_REDUCED_COLOR_2)
#nimg = cv.imread(sys.argv[2], cv.IMREAD_UNCHANGED)
nimg = cv.imread(sys.argv[2], cv.IMREAD_REDUCED_COLOR_2)
res = cv.matchTemplate( himg , nimg , cv.TM_CCOEFF_NORMED )

minval, maxval , minloc , maxloc = cv.minMaxLoc(res)

print(maxloc)
print(maxval)

thsd = .8
if maxval >= thsd:
	print('Found')
	nimgw = nimg.shape[1]
	nimgh = nimg.shape[0]
	tpleft = maxloc  
	bright = ( maxloc[0] + nimgw , maxloc[1] + nimgh ) 
	cv.rectangle(himg, tpleft, bright , color=(0,255,0) , thickness=2 , lineType=cv.LINE_4)
	cv.imwrite('res.jpg', himg)
	cv.imshow('res', himg)
	cv.waitKey()
	
else:
	print('Not Found')
#cv.imshow('res', res)
#cv.waitKey()
