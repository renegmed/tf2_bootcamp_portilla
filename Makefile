create:
	virtualenv -p python3 ~/.virtualenvs/tf2_bootcamp_portilla/
.PHONY: create

source:
	$(source) ~/.virtualenvs/tf2_bootcamp_portilla/bin/activate
.PHONY: activate

install:
	pip install -r requirements.txt
	#pip install tensorflow-gpu==2.0.0 tensorflow-serving-api==2.0.0
	#pip install sagemaker smdebug smdebug-rulesconfig==0.1.2 awscli boto3 keras numpy pandas --upgrade
	#pip install jupyter --upgrade
.PHONY: install

exit:
	deactivate
.PHONY: exit

jupyter:
	jupyter notebook --allow-root
.PHONY: jupyter

