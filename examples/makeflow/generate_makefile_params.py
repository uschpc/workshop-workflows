import getopt,sys,os
import librosa
import math

def usage():
    print("Usage:")
    print("-h,--help        \tDisplay this message")
    print("-f,--flac_file   \t.flac file to read song information from")
    print("-o,--output_dir  \tDirectory to save output files (output/song_name by default)")
    print("-r,--rosa_path   \tPath to rosa_fft.py")



def main():
    output_dir="."
    song_sr=44100
    rosa_path="/project/hpcroot/csul/workflows/scripts/rosa_fft.py"


    try:
        opts,args = getopt.getopt(sys.argv[1:],"hf:o:s:r:",["help","flac_file=","output_dir=","sample_rate=","rosa_path="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
   
    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-f", "--flac_file"):
            song_file=a
        elif o in ("-o", "--output_dir"):
            output_dir=a
        elif o in ("-s", "--sample_rate"):
            song_sr=int(a)
        elif o in ("-r","--rosa_path"):
            rosa_path=a



    
    # Get filename and remove  extension

    song_name=song_file.split('/')[-1].split('.')[0]
    makeflow_dir=output_dir+'/makeflows'
    output_files_dir=output_dir+'/'+song_name
    
    
    movie_file=output_files_dir+"/"+song_name+'.mp4'
    
    ffmpeg_command1='ffmpeg -threads 4 -framerate 60 -i '+output_files_dir+ '/images/frame%09d.png -i ' +song_file+ ' -pix_fmt yuv420p  ' +movie_file
    python_command1='python3 {script_path} -f {flac_file}  -i {start_time} -o {outdir}'
    frameName=output_files_dir+'/images/frame{task_id:09d}.png'
    
    y,sr=librosa.load(song_file,sr=song_sr)
    #duration=librosa.get_duration(y,sr=sr)
    duration=2
    max_time=math.ceil(duration)
    max_frame=duration*60

    print("Generating makeflow file for " + song_name)
    print("Should be %d s and %d frames long"%(max_time,max_frame))
    
    os.makedirs(makeflow_dir,exist_ok='True')
    with open(makeflow_dir+'/'+song_name+".makeflow", "w") as makefile:

        # Merge images and song into .mp4
        makefile.write(movie_file+": ")
        for task_no in range(max_time):
            for counter in range(0,60):
                if (task_no*60+counter) >= max_frame :
                    break
                makefile.write(frameName.format(task_id=(task_no*60+counter) ) + " " )
        makefile.write("\n\t" +  ffmpeg_command1 + "\n")
    
    
    
        # Generate images
        for task_no in range(max_time):
            for counter in range(0,60):
                if (task_no*60+counter) >= max_frame :
                    break
                makefile.write(frameName.format(task_id=task_no*60+counter) + " ")
            makefile.write(": "+ song_file +  "\n")
            makefile.write("\t"+python_command1.format(script_path=rosa_path,flac_file=song_file,start_time=task_no,outdir=output_files_dir) + "\n")


if __name__== "__main__":
    main()
