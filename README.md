# TerraTest
Planet Survivability Testing

- Abhay Bhat, Jonathan Chiu, Alan Di, and Cadin Le
- https://github.com/EpicGamer007/emp-space-hackathon/tree/main

## About the project
As humanity continues to use Earth without restrain, it is inevitable that humanity needs to explore new planets. As such, it is important to consider the planets available to us as livable or not. Without any existing tool that is able to calculate all these values, we decided that we needed a solution to this issue.

TerraTest is designed to determine the survivability of inputted planets, which is outputted in the form of a habitability index. This index combines important factors to live, such as presence of water and an atmosphere, and then weights them for the final score. TerraTest also determines a survival guide for the user's target planet generated through AI, taking in the factors of the planet statistics to do so. As a whole, TerraTest will be extremely useful for finding potential planets to explore, being able to quickly evaluate the potential for life and colonization of the planet and whether or not it is worth it to travel.

One aspect of TerraTest that we are proud of is the Habilitability Index formula. This formula was specially designed through careful research with sources like NASA and the Kennedy Space Center, determining the individual importance of each of our 7 main factors. This formula takes into account all variables at play when making this decision of survivability and is the core of our program. We are also very proud of our code linking. In this project, we successfully linked our python/nodejs backend that utilized OpenAI API with JS, CSS, and HTML for our frontend UI. This process turned out to be much more challenging and difficult than expected, but through our perseverance we got the job done.

The python backend interfaced with openai's api in order to get a survival "guide". Mathematical operations were used for calculating the score. The frontend uses expressjs for the web server and servers regular html/css/js. HTML is in the form of ejs so we can easily pass data from the backend to frontend.

Throughout the course of development, we faced several key difficulties. First, given the lack of reliable data regarding what makes a planet habitable (we have one sample) and the multitude of factors that goes into the topic, our formula, Habitation Index, was difficult to create. In the end, we chose to narrow our factors into the seven most impactful, assigning relative weights such that certain characteristics like water availability and atmosphere were more important than others like geological activity. In addition, we also had to account for cases where one of the seven factors was missing. Our formula had to be able to handle these cases. Finally, we struggled with connecting our python backend and javascript frontend but were able to figure out an easy way to use it

## Building and Running

Running from powershell:
```pwsh
cd backend-python
py -m venv env
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
./env/Scripts/activate.ps1

./env/Scripts/pip3.exe install openai
./env/Scripts/pip3.exe install python-dotenv

cd ..

cd web
npm i
npm run start
```

Running from POSIX-Compliant shell
```bash
cd backend-python
python -m venv env
chmod +x ./env/bin/activate ./env/bin/pip
./env/bin/activate

./env/bin/pip install openai python-dotenv

cd ..

cd web
npm i
npm run start
```