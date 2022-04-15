import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')
import librosa, librosa.display
import getopt,sys,os
from tqdm import tqdm

def usage():
    print("Usage:")
    print("-h,--help        \tDisplay this message")
    print("-f,--flac_file   \t.flac file to read song information from")
    print("-o,--output_dir  \tDirectory to save output files (output by default)")
    print("-i,--start_time  \tBeginning of window of interest")
    print("-t,--duration    \tLength of window of interest in sec (1 by default)")
    print("-s,--sample_rate \tSample rate of .flac song (44100 by default)")


def main():
    song_file=[]
    song_sr=44100 #default
    frame_no=1
    output_dir="output"
    start_time=0
    duration=1 # Default 1s window
    
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hf:o:i:t:s:",["help","flac_file=","output_dir=","start_time=","duration=","sample_rate="])
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
            os.makedirs(output_dir+"/images", exist_ok=True)

        elif o in ("-i", "--start_time"):
            start_time=int(a)
        elif o in ("-t", "--duration"):
            duration=int(a)
        elif o in ("-s", "--sample_rate"):
            song_sr=int(a)
    
    song_name=song_file.split('/')[-1].split('.')[0]
    song_data,sr=librosa.load(song_file,sr=song_sr,offset=start_time,duration=duration)
    freq=librosa.fft_frequencies(sr=song_sr)
    S=librosa.stft(song_data,hop_length=int(song_sr/60))
    power=np.abs(S).T

    fig, ax = plt.subplots()


    ax.set_title(song_name)

    w=len(power[0])//100
    max_frame=len(power)
    some_ones=np.ones(w)

    moving_average=np.convolve(power[0],np.ones(w),mode='same')
    
    changeable_plot,=ax.semilogx(freq,moving_average,'.')
    ax.set_ylim(0,160)
    ax.set_xlim(500,2.205*10**4)
    fig.savefig(output_dir+"/images/frame%d.png"%(start_time*60),dpi=400,bbox_inches='tight')

    for counter in tqdm(range(1,max_frame)):

        moving_average=np.convolve(power[counter],some_ones,mode='same')

        minp=np.min(moving_average)
        maxp=np.max(moving_average)
        changeable_plot.set_data(freq,moving_average)
        fig.savefig(output_dir+"/images/frame%d.png"%(counter+start_time*60),dpi=300,bbox_inches='tight')

if __name__== "__main__":
    main() 
