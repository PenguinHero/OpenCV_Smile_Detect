# OpenCV_Smile_Detect
A Python3 program that uses a Raspberry Pi (v3 B+) and OpenCV to detect faces, eyes, and smiles.
I expect the code will work on any machine with a camera that OpenCV can use, and Python 3.

OpenCV set up for a Pi 3 B+
https://pysource.com/2018/10/31/raspberry-pi-3-and-opencv-3-installation-tutorial/

It worked for me when I followed all the dependency steps. I think I must have missed one the first time I tried it as step 4 went for hours until I turned the Pi off.

The original code and data files came from: https://www.electromaker.io/project/view/open-cv--face-eyes--smile-detection-with-raspberry-pi

I have tweaked the code slightly to get Smile detection to work (old parameters present and commented out), as previously it only (for me) detected Face and Eyes.
I'll keep playing with it to see if I can improve smile detection as it doesn't work as well as face and eyes, but at least it works. :)

FaceEyesSmile.py is the default version.
FaceEyesSmile2.py is a version that inlcudes use of a Pi SenseHat to display status of the detection. I had planned to run the program on a Pi without a monitor, and have it echo its detection status via the LEDs on the hat.
