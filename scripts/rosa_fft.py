import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import librosa
import getopt,sys,os
from tqdm.auto import tqdm

def usage():
    print("Usage:")
    print("-h,--help        \tDisplay this message")
    print("-f,--flac_file   \t.flac file to read song information from")
    print("-o,--output_dir  \tDirectory to save output file (output by default)")
    print("-s,--sample_rate \tSample rate of .flac song (44100 by default)")

def animate(i,line,power,t):
    t.update()
    line.set_ydata(power[i])

#def init(line,power):
#    line.set_ydata(power[0])

def main():
    song_file=[]
    song_sr=44100 #default
    frame_no=1
    output_dir="output"
    start_time=0
    duration=1 # Default 1s window

    try:
        opts,args = getopt.getopt(sys.argv[1:],"hf:o:s:",["help","flac_file=","output_dir=","sample_rate="])
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

    os.makedirs(output_dir, exist_ok=True)
    fps=30
    dpi=150

    song_data,sr=librosa.load(song_file,sr=song_sr,offset=start_time)
    freq=librosa.fft_frequencies(sr=song_sr)
    S=np.abs(librosa.stft(song_data,hop_length=int(song_sr/fps) ) )
    power=np.abs(S).T

    nFrames,width=power.shape

    plt.style.use("ggplot")
    fig, ax = plt.subplots()


    ax.set_title(song_file)
    ax.set_ylim(0,160)
    ax.set_xlim(100,2.205*10**4)

    line, = ax.semilogx(freq,power[0])
    #w=len(power[0])//100
    #max_frame=len(power)
    #some_ones=np.ones(w)

    frames=np.arange(nFrames)
    t=tqdm(frames,unit='frames')
    ani_f = animation.FuncAnimation(
        fig,animate,frames=frames,fargs=(line,power,t))
    plt.close()

    extra_args=['-report']
    ffmpeg_writer=animation.FFMpegWriter(fps=fps,codec='png',extra_args=extra_args)
    ani_f.save(output_dir+"/silent.mp4",dpi=dpi,writer=ffmpeg_writer)


if __name__== "__main__":
    main()
