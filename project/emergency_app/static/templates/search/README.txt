Instruction: --------
Group 1
HMP669

*** Note, this only work on MAC****

Step1 (if you don't have virtualenv on your computer). 
	cd (to root directory)
	sudo easy_install pip
	sudo pip install virtualenv
	virtualenv hmp669 

Now you have virtual environment.

Step2. Activate virtual environment. Open virtualenv BY: 

	source hmp669/bin/activate

step3.  cd to the project folder, install package.

	pip install -r requirements.txt


** Now all pre-requirements setting are done.

Step4. -To open the application, go the emergency_app folder

	cd emergency_app

	python manage.py runserver


Final Step. 
	- Open browser and use URL — 127.0.0.1:8000

