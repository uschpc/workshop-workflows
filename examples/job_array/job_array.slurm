#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu-1GB
#SBATCH --time=00:10:00
#SBATCH --array=0-9
module load python
python3 rosa_fft.py -f 09Teachers.flac -i ${SLURM_ARRAY_TASK_ID} -o 09Teachers
