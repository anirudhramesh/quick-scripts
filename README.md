# quick-scripts
Short scripts written to do quick tasks. Totally random.

File rename - quickly rename all files in a directory using defined rules.

File splitter - uses pandas' built in functionality to split very large files and store them according to given rules. Uses the multiprocessing modules to significantly speed up the process by parallelising it.
file_reader = parallelises file reading so that subsequent reads which require skipping lines are all parallelised.
chunk_splitter = reads the segment of the file split by file_reader into manageable chunks and passes them to file_writer
file_writer = takes the chunk passed to it, splits it according to rules defined and writes the splits into separate files.

wordle - solve a game called wordle that was viral in early 2022.

excel writer modules - codify pandas' writing and editing to excel by wrapping extended functionality from xlsxwriter or openpyxl into single function calls.

csv to sqlite3 - use pandas' sql capabilities to dynamically write large csv's into sqlite databases. vastly increases functionality since you can query it.
