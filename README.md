# Methods for Automating Job Submission

Workshop materials for *Methods for Automating Job Submission*.

Researchers commonly find themselves repetitively checking the job scheduler to find the status of jobs and deciding what jobs to submit next. Workflow management software (wms) allows users to automate this process by defining a sequence of tasks to be done. When a workflow is then run, the wms can automatically manage job dependencies, resubmit failed jobs, and delete unneeded intermediate files.

This presentation will use `makeflow` to demonstrate some of these ideas. Other tools such as `snakemake` and Pegasus will be discussed

Slides: https://uschpc.github.io/workshop-hpc-python/

Example job scripts:

- [serial.job](examples/job-scripts/serial.job)
- [multicore.job](examples/job-scripts/multicore.job)
- [mpi.job](examples/job-scripts/mpi.job)

Example python scripts:

- [examples](examples)

### Additional resources

[Using Python on CARC Systems](https://carc.usc.edu/user-information/user-guides/software-and-programming/python)  

[multiprocessig](https://cran.r-project.org/manuals.html)

[mpi4py](https://cran.r-b.org/web/views/HighPerformanceComputing.html)  

[h5py](https://pbdr.org/)

[hdf5](https://pbdr.org/)

[cProfile](https://docs.python.org/3/library/profile.html)

[snakeviz](https://jiffyclub.github.io/snakeviz/)

[viztracer](https://viztracer.readthedocs.io/en/latest/basic_usage.html)
