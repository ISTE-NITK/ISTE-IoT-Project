import math
x0 =300 
y0 = 50
p= float(input("Enter diameter of first circle: "))
x1=600
y1=50
q= float(input("Enter diameter of second circle: "))
x2=450
y2=350
r =float(input("Enter diameter of third circle: "))
EPSILON = 0.000001
r0=p/2
r1=q/2
r2=r/2
'''
intersectionPoint1_x=0 
intersectionPoint2_x=0
intersectionPoint1_y=0
intersectionPoint2_y=0
intersectionPoint1_x1=0
intersectionPoint2_x1=0
intersectionPoint1_y1=0
intersectionPoint2_y1=0
intersectionPoint1_x2=0
intersectionPoint2_x2=0
intersectionPoint1_y2=0
intersectionPoint2_y2=0
'''	
def calculateThreeCircleIntersection(x0, y0, r0, x1, y1, r1, x2, y2, r2):
	'''a=0
	dx=0
	dy=0
	d=0
	h=0
	rx=0
	ry=0
	point2_x=0 
	point2_y=0
	d1=0
	d2=0
	
	 
	dx and dy are the vertical and horizontal 
	distances between the circle centers.
	'''
	dx = x1 - x0;
	dy = y1 - y0;
	#Determine the straight-line distance between the centers.
	d = (math.sqrt((dy*dy) + (dx*dx)));
	#Check for solvability. 
	if d > (r0 + r1):
		print ("No solution exists");
		#no solution. circles do not intersect.
		return False;
	
	if d < abs(r0 - r1):
		print("No solution exists  !!"); 
		#no solution. one circle is contained in the other 
		return False;

	#point 2 is the point where the line through the circle intersection points crosses the line between the circle centers.
	#Determine the distance from point 0 to point 2
	a = (((r0*r0) - (r1*r1) + (d*d)) / (2.0 * d));
	# Determine the coordinates of point 2
	point2_x = x0 + (dx * a/d);
	point2_y = y0 + (dy * a/d);
	#Determine the distance from point 2 to either of the intersection points
	h = (math.sqrt((r0*r0) - (a*a)));	
	#Now determine the offsets of the intersection points from point 2.
	rx = (-dy) * (h/d);
	ry = dx * (h/d);
	#Determine the absolute intersection points
	intersectionPoint1_x = point2_x + rx;
	intersectionPoint2_x = point2_x - rx;
	intersectionPoint1_y = point2_y + ry;
	intersectionPoint2_y = point2_y - ry;
	print ("INTERSECTION Circle1 AND Circle2:"+"(" + str(intersectionPoint1_x) + "," + str(intersectionPoint1_y) + ")" + " AND (" + 			str(intersectionPoint2_x) + "," + str(intersectionPoint2_y) + ")");
	# determine if circle 3 intersects at either of the above intersection points
	dx = intersectionPoint1_x - x2;
	dy = intersectionPoint1_y - y2;
	d1 = math.sqrt((dy*dy) + (dx*dx));
		
	dx = intersectionPoint2_x - x2;
	dy = intersectionPoint2_y - y2;
	d2 = math.sqrt((dy*dy) + (dx*dx));
	
	
	if abs(d1 - r2) < EPSILON: 
		print ("INTERSECTION Circle1 AND Circle2 AND Circle3:"+ "(" + str(intersectionPoint1_x) + "," + str(intersectionPoint1_y) + ")");
	elif abs(d2 - r2) < EPSILON:
		print ("INTERSECTION Circle1 AND Circle2 AND Circle3:"+"(" + str(intersectionPoint2_x) + "," + str(intersectionPoint2_y) + ")");		
		#here was an error
	else:
		print("INTERSECTION Circle1 AND Circle2 AND Circle3:"+ "NONE");
	'''
	a1=0 
	dx1=0 
	dy1=0 
	d11=0 
	h1=0
	rx1=0 
	ry1=0
	point2_x1=0 
	point2_y1=0
	dx and dy are the vertical and horizontal distances between the circle centers.
	'''	
	dx1 = x2 - x1
	dy1 = y2 - y1

	#Determine the straight-line distance between the centers
	d11 = math.sqrt((dy1*dy1) + (dx1*dx1))
	
	#Check for solvability. 
	if d11 > (r2 + r1):

		print ("No solution exists")
		#no solution. circles do not intersect.
		return False
		
	if d11 < abs(r1 - r2):
			
		print("No solution exists  !!"); 
		#no solution. one circle is contained in the other 
		return False;

	#point 2 is the point where the line through the circle intersection points crosses the line between the circle centers.

	#Determine the distance from point 0 to point 2
	a1 = (((r1*r1) - (r2*r2) + (d11*d11)) / (2.0 * d11))

	# Determine the coordinates of point 2
	point2_x1 = x1 + (dx1 * a1/d11)
	point2_y1 = y1 + (dy1 * a1/d11)
	
	#Determine the distance from point 2 to either of the intersection points
	h1 = math.sqrt((r1*r1) - (a1*a1))
	
	#Now determine the offsets of the intersection points from point 2.
	rx1 = -dy1 * (h1/d11)
	ry1 = dx1 * (h1/d11)

	#Determine the absolute intersection points
	intersectionPoint1_x1 = point2_x1 + rx1
	intersectionPoint2_x1 = point2_x1 - rx1	
	intersectionPoint1_y1 = point2_y1 + ry1
	intersectionPoint2_y1 = point2_y1 - ry1

	print ("INTERSECTION Circle2 AND Circle3:"+"(" + str(intersectionPoint1_x1) + "," + str(intersectionPoint1_y1) + ")" + " AND (" + 		str(intersectionPoint2_x1) + "," + str(intersectionPoint2_y1) + ")")
	
	# determine if circle 3 intersects at either of the above intersection points
	dx1 = intersectionPoint1_x1 - x0
	dy1 = intersectionPoint1_y1 - y0
	dou1 = math.sqrt((dy1*dy1) + (dx1*dx1))

	dx1 = intersectionPoint2_x1 - x0
	dy1 = intersectionPoint2_y1 - y0
	dou2 = math.sqrt((dy*dy) + (dx1*dx1))


	if abs(dou1 - r0) < EPSILON: 
		print ("INTERSECTION Circle1 AND Circle2 AND Circle3:"+ "(" + str(intersectionPoint1_x1) + "," + str(intersectionPoint1_y1) + ")")
		
	elif abs(dou2 - r0) < EPSILON:
		print ("INTERSECTION Circle1 AND Circle2 AND Circle3:"+"(" + str(intersectionPoint2_x1) + "," + str(intersectionPoint2_y1) + ")") 
				
		#here was an error
	else:
		print("INTERSECTION Circle1 AND Circle2 AND Circle3:"+ "NONE")
	'''
	a2=0 
	dx2=0 
	dy2=0 
	d22=0 
	h2=0 
	rx2=0 
	ry2=0
	point2_x2=0 
	point2_y2=0

	dx and dy are the vertical and horizontal distances between the circle centers.
	'''	
	dx2 = x0 - x2
	dy2 = y0 - y2
	

	#Determine the straight-line distance between the centers
	d22 = math.sqrt((dy2*dy2) + (dx2*dx2))

	#Check for solvability. 
	if d22 > (r0 + r2):
		
		print ("No solution exists")
		#no solution. circles do not intersect.
		return False
	
	if d22 < abs(r2 - r0):
		
		print("No solution exists  !!"); 
		#no solution. one circle is contained in the other 
		return False;

	#point 2 is the point where the line through the circle intersection points crosses the line between the circle centers.

	#Determine the distance from point 0 to point 2
	a2 = ((r2*r2) - (r0*r0) + (d22*d22)) / (2.0 * d22)

	# Determine the coordinates of point 2
	point2_x2 = x2 + (dx2 * a2/d22)
	point2_y2 = y2 + (dy2 * a2/d22)

	#Determine the distance from point 2 to either of the intersection points
	h2 = math.sqrt((r2*r2) - (a2*a2))

	#Now determine the offsets of the intersection points from point 2.
	rx2 = -dy2 * (h2/d22)
	ry2 = dx2 * (h2/d22)

	#Determine the absolute intersection points
	intersectionPoint1_x2 = point2_x2 + rx2
	intersectionPoint2_x2 = point2_x2 - rx2
	intersectionPoint1_y2 = point2_y2 + ry2
	intersectionPoint2_y2 = point2_y2 - ry2

	print ("INTERSECTION Circle3 AND Circle2:"+"(" + str(intersectionPoint1_x2) + "," + str(intersectionPoint1_y2) + ")" + " AND (" + 		str(intersectionPoint2_x2) + "," + str(intersectionPoint2_y2) + ")")
	
	# determine if circle 3 intersects at either of the above intersection points
	dx2 = intersectionPoint1_x2 - x1
	dy2 = intersectionPoint1_y2 - y1
	do1 = math.sqrt((dy2*dy2) + (dx2*dx2))
	
	dx2 = intersectionPoint2_x2 - x1
	dy2 = intersectionPoint2_y2 - y1
	do2 = math.sqrt((dy2*dy2) + (dx2*dx2))
	
	
	if abs(do1 - r1) < EPSILON: 
		print ("INTERSECTION Circle1 AND Circle2 AND Circle3:"+ "(" + str(intersectionPoint1_x2) + "," + str(intersectionPoint1_y2) + ")")
		
	elif abs(do2 - r1) < EPSILON:
		print ("INTERSECTION Circle1 AND Circle2 AND Circle3:"+"(" + str(intersectionPoint2_x2) + "," + str(intersectionPoint2_y2) + ")") 
				
		#here was an error
	else:
		print("INTERSECTION Circle1 AND Circle2 AND Circle3:"+ "NONE")
	centroidx=(intersectionPoint1_x1+intersectionPoint1_x+intersectionPoint1_x2)/3
	centroidy=(intersectionPoint1_y1+intersectionPoint1_y+intersectionPoint1_y2)/3
	
	print ("("+str(centroidx)+","+str(centroidy)+")")	
	return True

calculateThreeCircleIntersection(x0,y0,r1,x1,y1,r2,x2,y2,r2)


