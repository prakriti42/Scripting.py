# Scripting.py

Scripting.py is a repository being maintained to keep log of the python scripts that I create for automating and executing some of my boring manual task. 

### Script I : Audio Overlayer 
This script was created as per my requirement to add some noise to the already refined audio dataset I had. Hence, with python and its near to omnipresent library, I wrote this basic code that takes in two folder paths from the user as the primary and secondary folder and iterates over the audio files in the respective folders parallely to mix them by overlaying the audio contents. After the successful audio overlaps, all the output files gets stored in a newly created directory with its path similar to that of the provided primary folder but all of it under the root directory called Output. 

#### Libraries Used 
1. [OS](https://docs.python.org/3/library/os.html)
2. [RegEx Module](https://docs.python.org/3/library/re.html)
3. [Random](https://docs.python.org/3/library/random.html)
4. [Itertools](https://docs.python.org/3/library/itertools.html)
5. [Pydub](https://pypi.org/project/pydub/) 

* [Redirect to the Script](https://github.com/prakriti42/Scripting.py/blob/main/audioOverlay.py)
<hr>


### Script II : Automated Email Sender 
This script was created to automate one of my monotonous weekly ritual that is to send an email to my workplace address indicating the succesful completeion of my weekly task.  With the script, I have a statically placed subject and body that will be sent to a list of pre-determined recievers with the smtp server. 

#### Libraries Used 
1. [Datetime](https://docs.python.org/3/library/datetime.html)
2. [SMTPLIB Module](https://docs.python.org/3/library/smtplib.html)

* [Redirect to the Script](https://github.com/prakriti42/Scripting.py/blob/main/automatedemail.py)
<hr>


