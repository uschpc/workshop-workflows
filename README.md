# Methods for Automating Job Submission

Workshop materials for *Methods for Automating Job Submission*.

Researchers commonly find themselves repetitively checking the job scheduler to find the status of jobs and deciding what jobs to submit next. Workflow management software (wms) allows users to automate this process by defining a sequence of tasks to be done. When a workflow is then run, the wms can automatically manage job dependencies, resubmit failed jobs, and delete unneeded intermediate files.

This presentation will use `makeflow` to demonstrate some of these ideas. Other tools such as `snakemake` and Pegasus will be discussed.

Slides available at: https://uschpc.github.io/workshop-workflows/

## Requirements

### Not available on discovery/endeavour
---
Python packages
```
# for processing audio data
pip3 install librosa --user

# progress bar library
pip3 install tqdm --user
```

### Available as modules on discovery/endeavour
---
libsndfile
```
module load libsndfile
```

ffmeg
```
module load ffmpeg
```

makeflow
```
module load cctools
```
