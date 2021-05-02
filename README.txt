PowerShell method

1. Try to run Python in Windows PowerShell
	a. Run PowerShell
	b. python
		Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
		Type "help", "copyright", "credits" or "license" for more information.
		>>>

2. If you get no output or something like "the term 'python' is not recognized as the name of a cmdlet", then you probably don't have Python for Windows installed

3. Download and Install Python 3 for Windows - https://www.python.org/
	a. When the installers runs, make sure you check the box that says "add to PATH." (this makes your life easier later)
	
4. Once you have Python installed and can run it from PowerShell, run the game. In PowerShell:
	a. change your working directory to the directory containing the game file
		ex: cd C:\Users\alan\Downloads
	b. python game.py
		ex: python Gothon25.py


WSL method

1. If you haven't already, install the Windows Subsystem for Linux - https://docs.microsoft.com/en-us/windows/wsl/install-win10

2. Open your WSL VM (I used the Ubuntu distribution)
	a. Search >> Ubuntu >> launch

3. Change working directory to the directory containing the game file (the WSL VM automatically mounts your PCs C drive under /mnt/c/, results may vary).
	ex: cd /mnt/c/Users/alan/Downloads/
	
4. Run the game
	a. python Gothon25.py


Linux machine method

1. change your working directory to the directory containing the game file
	ex: cd /home/alan/

2. python Gothon25.py
	a. if you get an error, try "python3 Gothon25.py"

3. If the above fails you might need to install Python 3 - https://docs.python-guide.org/starting/install3/linux/