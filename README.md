# quick-scripts
Short scripts written to do quick tasks. Totally random.

File rename - quickly rename all files in a directory using defined rules.

File splitter - uses pandas' built in functionality to split very large files and store them according to given rules. Uses the multiprocessing modules to significantly speed up the process by parallelising it.
file_reader = parallelises file reading so that subsequent reads which require skipping lines are all parallelised.
chunk_splitter = reads the segment of the file split by file_reader into manageable chunks and passes them to file_writer
file_writer = takes the chunk passed to it, splits it according to rules defined and writes the splits into separate files.

wordle - solve a game called wordle that was viral in early 2022.