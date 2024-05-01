
"""
--------------------------------------------------------------------------
Autonomous Sixth Finger
--------------------------------------------------------------------------
License:   
Copyright 2021-2023 - Ben Leebron

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Requires Pins for Rotation and Curl servos. 

Currently has camera to use as first camera found on system (index = 0)

"""
import servo
import cv2
ROT_SERVO_PIN = "P2_1"

CURL_SERVO_PIN = "P1_36"
X_INIT = 280
X_WIDTH = 20

Y_INIT = 40
Y_HEIGHT = 20
vid = cv2.VideoCapture(0) 
if __name__ == '__main__':
	
	rot_servo = servo.Servo(ROT_SERVO_PIN)
	
	curl_servo = servo.Servo(CURL_SERVO_PIN)
	gripped = False
	# Main_ctrl loop
	while (True):
		
		print("taking a pic")
		# Check for finger in pos
		ret, frame = vid.read() 
		# cv2.imwrite('frame.jpg', frame)
		print("pic taken")
		if cv2.waitKey(1) & 0xFF == ord('q'): 
			break
		print("Checking for yellow, not like Stefan")
		if not gripped:
			for x in range(X_INIT, X_INIT+X_WIDTH):
				for y in range(Y_INIT, Y_INIT+Y_HEIGHT):
					p=frame[x,y]
					if p[0] > 150 and p[1] > 150 and p[2] < 150: # added p[2] < 150 for blue
						print("Found Yellow")
						x = 301
						y = 61
						rot_servo.turn(-100)
						gripped = True
						# rot_servo.turn(50)
		
