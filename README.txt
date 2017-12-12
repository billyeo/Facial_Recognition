READ ME for running Python/Open CV demo

The version of python that runs with this demo is Python 3.6.3 with OpenCV 2.4. This is important
because if you run an earlier version of Python like the legacy model, some commands will not be translated.
Also make sure you have a camera on your laptop or linked to your pc.

In your cmd, make sure to install these libraries through these methods:

	pip install opencv
	pip install numpy
	pip install pillow
	pip install opencv-contrib-python

On my system when I am running each file, I am opening python files by 'Editing through IDLE', where
you can read/write the physical code.

In the zip file make sure these directories and files are present:
	dataSet (directory that contains all the gray-scaled data images)
	recognizer (directory that contains the yml file of the recognized dataset)
	haarcascade_frontalface_default.xml (xml file that contains the computed facial detection schemes)
	
	dataSetCreator(python file that collects data set by taking snaps of a user)
	trainer(python file that trains system to recognize entered dataset)
	detector(python file that detects users depending if the machine is trained to recognize them)

To run the complete demo:
	step 1: run dataSetCreator and enter the userID, this can be any numeric value 0,1,2.. 
	this will take about 20 snapshots of a user and save it in the dataSet folder.


	step 2: run the trainer, you will see a window pop up, scanning all the images in the dataset

	step 3: within the detector.py code, make sure that for the ID that you entered in step 1, 
	changes the value of the variable id to the label you want. for example, if i entered 1 for the 
	userID in step 1, I would change the if statement in the Detector.py to change the value of 
	id to "user1", so whenever it detects this user, it would output the name of the user on the detection
	window.

	step 4: (not a step) you can add additional datasets and further train your machine

	Have fun!! Thank You