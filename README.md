# Sleepiness-Detector

This is a project under the Microsoft Engage program to alert drowsy drivers in order to prevent accidents from taking place.

# Requirements ✨

1. Python\
   Allowed versions: 3.7–3.10 (This restriction in version is because II have used a library called tensorflow which is compatible only with these versions of python) \
   I have used version 3.7.9\
   This version can be installed from https://www.python.org/downloads/release/python-379/ \
   I had installed the Windows x86-64 executable installer from above website for my local machine.

2. Git\
   Git for Windows can be installed from https://git-scm.com/download/win \
   I have used git version 2.30.0.windows.2

3. Any code editor of your choice\
   I have made use of Visual Studio Code which can be installed from https://code.visualstudio.com/download

# Execute the project 💻

First clone the repository to your local machine

```
git clone https://github.com/Anuka04/Sleepiness-Detection.git
```

Next you cd into the directory of the project

```
cd Sleepiness-Detection
```

Next (and this specific step is optional) I like to open the code in my code editor (VS Code) but you can choose to run the project from the terminal itself in which case skip this step and go ahead to the next one

```
code .
```

Now we install the Requirements

```
pip install -r requirements.txt
```

There is one more step to install dlib which is a toolkit for making real world machine learning and data analysis applications. \
This involves taking the file path of the dlib-19.19.0-cp37-cp37m-win_amd64.whl file that has gotten cloned into your folder along with everything else.

```
pip install "your_file_path\dlib-19.19.0-cp37-cp37m-win_amd64.whl”
```

Example: pip install "D:\Projects\Engage\dlib-19.19.0-cp37-cp37m-win_amd64.whl”

The final step is to run the main file

```
python main.py
```

# Output 🚘

On running the project you should have the application open at loacalhost port 5000
