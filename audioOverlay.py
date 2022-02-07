'''
    Written By : Prakriti Regmi
    Date : 07/02/2022
    Description : This program is used to overlay two audio files from two folders as primary and secondary

'''


#Necessary Libraries 
import itertools , os , random , re
from pydub import AudioSegment

#Global Variables 
src1=''
src2=''
outputFolder = None


#Function to create directory for storing output files
def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    else:
        print(dir_name+ "  has been created ")


#Function to overlay audio two audio files
def overlay_audio(src1,src2,mainAudioFolder,NoiseAudioFolder):

    count = 0 
    dirs = re.split("\/", mainAudioFolder)
    #Looping through the audio files in the primary and secondary audio folder
    for (a, b) in itertools.zip_longest(src1 , src2):
            #Storing the audio files from the primary folder as main audio
            mainAudio = AudioSegment.from_wav(mainAudioFolder + a)
            print("Main Audio : " + a )

            #Condition to submit secondary audio file incase the list runs out of files 
            if b is not None : 
                Noise = AudioSegment.from_wav(NoiseAudioFolder + b)
                print("Noise : " + b)
            else :
                b = random.choice(src2)   #Randomly selecting a file from the secondary folder
                Noise = AudioSegment.from_wav(NoiseAudioFolder + b)
                print("Noise : " + b)

            #Overlaying the audio files    
            combined = mainAudio.overlay(Noise)

            '''Count, cat and outputfiles are the attributes that are used to 
            create the output audio file name '''

            count += 1 #To keep count of the audiofiles providing them with unique names
            cat = dirs[len(dirs)-2]  #To extract the category of the audio file through the parent directory name
            outputFile=cat[:2]+str(count)  #Creating the output file name

            #Saving the output file in the output folder
            combined.export("Output/" +'/'.join((dirs)) + outputFile+".wav", format='wav')

    #End of the Overlaying of the audio files        
    print("Audio Overlay Completed and stored at path :" + "Output/" +'/'.join((dirs)))

#Main Function
def main():

    #Asking the user to enter the path of the primary audio folder
    mainAudioFolder = input("Enter folder path for the main audio: ")
    #Displaying for verification
    print("The directory path for main AudioFiles has been stored as : " + mainAudioFolder)

    #Checking if the directory exists or not
    try:
        src1 = list(os.listdir(mainAudioFolder))
        print("Directory Tracked...\n")
        print(src1)
    except FileNotFoundError:
        print ("The directory path {} is not correct".format(mainAudioFolder))
        print("Program Halted !..")
        return None

    #Asking the user to enter the path of the secondary audio folder
    NoiseAudioFolder = input("Enter folder path for the noise audio files: ")
    #Displaying for verification
    print("The directory path for secondary Audiofiles has been stored as : " + NoiseAudioFolder)

    #Checking if the directory exists or not
    try:
        src2 = list(os.listdir(NoiseAudioFolder))
        print("Directory Tracked...\n")
        print(src2)
    except FileNotFoundError:
        print ("The directory path {} is not correct".format(NoiseAudioFolder))
        print("Program Halted !..")
        return None

    #Creating the output directory    
    try :
        create_dir("Output/" +'/'.join((re.split("\/", mainAudioFolder))))
    except  FileExistsError:
        print("Directory path created")
    
    #Calling the overlay_audio function to overlay the audio files
    overlay_audio(src1,src2,mainAudioFolder,NoiseAudioFolder)

  

 

if __name__ == '__main__':
    main()