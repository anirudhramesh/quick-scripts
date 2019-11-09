import pandas as pd
import os
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

column_names = []
output_file_path = 'some/file/path'

def file_writer(chunk):
    chunk.columns = column_names
    for ticker in chunk.SYM_ROOT.unique():
        if os.path.exists(os.path.join(output_file_path, ticker+'.csv')):
            header = False
        else:
            header = True
        with open(os.path.join(output_file_path, ticker+'.csv'), 'a') as f:
            chunk[chunk.SYM_ROOT == ticker].to_csv(f, index=False, header=header)
            f.close()


def chunk_splitter(main_file, chunksize, skiprows, per_process_chunk):
    print(skiprows)
    with ThreadPool(processes=10) as pool:
        pool.imap(file_writer, pd.read_csv(main_file, skiprows=skiprows, chunksize=chunksize,
                                           nrows=chunksize*per_process_chunk, header=None))
        pool.close()
        pool.join()


def main():
    main_file = 'main_file.csv'

    chunksize = 10 ** 6
    per_process_chunk = 10 * 5
    skiprows = 1
    total_rows = 284191154

    with Pool(processes=5, maxtasksperchild=1) as pool:
        pool.starmap(chunk_splitter, [(main_file, chunksize, s, per_process_chunk) for s in
                                      range(skiprows, total_rows, chunksize*per_process_chunk)])
        pool.close()
        pool.join()


if __name__ == '__main__':
    main()
