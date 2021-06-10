import getopt,sys,os
import librosa
import math

def usage():
    print("Usage:")
    print("-h,--help        \tDisplay this message")
    print("-d,--debug       \tEnable debug mode (process only 2 seconds of song")
    print("-f,--song_file   \tSong file to read song information from")



def main():
    output_dir="."
    song_sr=44100
    rosa_path="../../scripts/rosa_fft.py"
    debug=False


    try:
        opts,args = getopt.getopt(sys.argv[1:],"dhf:o:s:r:",["debug","help","flac_file=","output_dir=","sample_rate=","rosa_path="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
   
    for o,a in opts:
        if o in ("-d", "--debug"):
            debug=True
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-f", "--song_file"):
            song_file=a
        elif o in ("-o", "--output_dir"):
            output_dir=a
        elif o in ("-s", "--sample_rate"):
            song_sr=int(a)



    
    # Get filename and remove  extension

    song_name=song_file.split('/')[-1].split('.')[0]
    makeflow_dir=output_dir+'/makeflows'
    output_files_dir=output_dir+'/'+song_name
    
    
    movie_file=output_files_dir+"/"+song_name+'.mp4'
    dummy_file=output_files_dir+"/time_index_{file_id:04d}_complete"
    
    ffmpeg_command1='ffmpeg -threads 4 -framerate 60 -i '+output_files_dir+ '/images/frame%09d.png -i ' +song_file+ ' -pix_fmt yuv420p  ' +movie_file
    python_command='python3 {script_path} -f {flac_file}  -i {start_time} -o {outdir}'
    dummy_command='touch ' +dummy_file

    y,sr=librosa.load(song_file,sr=song_sr)

    if debug:
        duration=2
    else:
        duration=librosa.get_duration(y,sr=sr)

    max_time=math.ceil(duration)
    max_frame=duration*60

    print("Generating makeflow file for " + song_name)
    print("Should be %d s and %d frames long"%(max_time,max_frame))
    
    os.makedirs(makeflow_dir,exist_ok='True')


    with open(makeflow_dir+'/'+song_name+".makeflow", "w") as makefile:
        
        # Write portion of makeflow file that describes ffmpeg job
        # Format is:
        # outputfile(s) : inputfile(s)
        # (tab) command to generate outputfile(s)

        # Output file done for you
        makefile.write(movie_file+": ")
        # TODO: write list of input files
        makefile.write(dummy_file.format(file_id=0) + " ")
        for i in range(10):
            makefile.write(output_files_dir+"/inputfile_{file_id:04d} ".format(file_id=i) + " ")

        # ffmpeg command done for you
        makefile.write("\n\t" +  ffmpeg_command1 + "\n\n")
    

        time_index=0
        # Write itermediate step to reduce number of input files
        # required for ffmpeg job
        #
        # Format is:
        # outputfile(s) : inputfile(s)
        # (tab) command to generate outputfile(s)

        #Output file done for you
        makefile.write(dummy_file.format(file_id=time_index) + ": ")
        # TODO: write list of input files
        for i in range(10):
            makefile.write(output_files_dir+"/inputfile_{file_id:04d} ".format(file_id=i) + " ")
        makefile.write("\n\t"+dummy_command.format(file_id=time_index)+"\n\n") 
    
        #Write portion of makeflow file that describes rosa_fft.py job
        # Format is:
        # outputfile(s) : inputfile(s)
        # (tab) command to generate outputfile(s)
    
        # TODO: write list of outputfiles
        makefile.write(output_files_dir+"/outputfile_{file_id:04d}".format(file_id=time_index))
        # Input file done for you
        makefile.write(": " + song_file)
        
        # Command to generate input files done for you (mostly)
        makefile.write("\n\t" + python_command.format(script_path=rosa_path,flac_file=song_file,start_time=time_index,outdir=output_files_dir) )
        
if __name__== "__main__":
    main()
