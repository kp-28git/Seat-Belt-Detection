import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt 

#Slope of line
def Slope(a,b,c,d):
    return (d - b)/(c - a)

#Centre of line
def Centre(a,b,c,d):
    return (a+b)/2,(c+d)/2

#path = 'D:\SEM 6 kp_090\Scientific Programming\Seat Belt Detection\with3.jpg'
path = 'D:\SEM 6 kp_090\Scientific Programming\Seat Belt Detection\without2.jpg'

# Reading Image
beltframe = cv2.imread(path)

# Resizing The Image
beltframe = imutils.resize(beltframe, height=800)
height, width = beltframe.shape[:2]

# Size of image
print("Size of Image : (",height,",",width,")")

#Generating copy of image for all lines
alllineimg = beltframe.copy()

#Converting To GrayScale
beltgray = cv2.cvtColor(beltframe, cv2.COLOR_BGR2GRAY)

# No Belt Detected Yet
belt = False

# Bluring The Image For Smoothness
blur = cv2.blur(beltgray, (1, 1))

# Converting Image To Edges
edges = cv2.Canny(beltgray, 50, 400)

# Previous Line Slope
ps = 0

# Previous Line Co-ordinates
px1, py1, px2, py2 = 0, 0, 0, 0

# Extracting Lines
lines = cv2.HoughLinesP(edges, 1, np.pi/270, 30, maxLineGap = 20, minLineLength = 170)

#Total Hough Lines Detected
tottalhough = 0
for line in lines:
    tottalhough += 1
print("Total Hough Lines Detected = ",tottalhough)    


# If "lines" Is Not Empty
if lines is not None:

    # Loop line by line
    for line in lines:

        # Co-ordinates Of Current Line
        x1, y1, x2, y2 = line[0]

        # Slope Of Current Line
        s = Slope(x1,y1,x2,y2)
        
        #Centre of Current line
        cx,cy = Centre(x1,y1,x2,y2)
        #Centre of Previous line
        pcx,pcy = Centre(px1,py1,px2,py2)

        # Drwaing all lines detected
        allx1, ally1, allx2, ally2 = line[0]
        cv2.line(alllineimg, (allx1, ally1), (allx2, ally2), (0, 0, 255), 2)
        
        #Distance between centres
        dist = ((cx - pcx)**2 + (cy - pcy)**2)**0.5;
        
        
        # If Current Line's Slope Is Greater Than 0.7 And Less Than 2
        if ((abs(s) > 0.7) and (abs (s) < 2)):

            # And Previous Line's Slope Is Within 0.7 To 2
            if((abs(ps) > 0.7) and (abs(ps) < 2)):

                # And Both The Lines Are Not Too Far From Each Other
                #if(((abs(x1 - px1) > 5) and (abs(x2 - px2) > 5)) or ((abs(y1 - py1) > 5) and (abs(y2 - py2) > 5))):
                if dist < 150:
                    # Plot The Lines On "beltframe"
                    cv2.line(beltframe, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.line(beltframe, (px1, py1), (px2, py2), (0, 0, 255), 3)

                    # Belt Is Detected
                    belt = True
                    print ("Belt Detected")
                    cv2.putText(beltframe,"Belt Detected", (30,50), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,0,0),2)

        # Otherwise Current Slope Becomes Previous Slope (ps) And Current Line Becomes Previous Line (px1, py1, px2, py2)            
        ps = s
        px1, py1, px2, py2 = line[0]
        
                   
if belt == False:
    print("No Seatbelt detected")
    cv2.putText(beltframe,"No Seatbelt detected", (30,50), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,0,0),2)


#cv2.imshow('image', beltframe)
#cv2.imshow('Hough lines', alllineimg)

# Horizontally concatenate the 2 images
img3 = cv2.hconcat([cv2.resize(alllineimg, (480, 640)),cv2.resize(beltframe, (480, 640))])
# Display the concatenated image
cv2.imshow('Hough Lines image                                                                                                           Final image',img3)

# waits for user to press any key 
# (this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(0)

# closing all open windows 
cv2.destroyAllWindows() 