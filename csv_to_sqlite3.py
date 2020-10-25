import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def date_parser(dt_str):
    return datetime.strptime(dt_str, '%Y%m%d').date()

def main():
	file_loc = r'path\to\file'
	db_loc = r'path\to\db'

	db_engine = create_engine('sqlite:///' + db_loc)
	chunksize = 10**6  # number of lines to read per chunk
	for chunk in pd.read_csv(file_loc, chunksize=chunksize, parse_dates=['date'], date_parser=date_parser):
	    chunk.to_sql('table_name', db_engine, if_exists='append', index=False)


if __name__ == '__main__':
	main()
