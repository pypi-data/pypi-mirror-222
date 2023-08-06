import asyncio

import asyncpg

from .exceptions import *

class Postgresql:	
	""" A class to handle all database related tasks efficiently.
	
	Parameters
	----------
	host: str
		The host of the database.
	user: str
		The user of the database.
	password: str
		The password of the database.
	database: str
		The database name.
	port: int
		The port of the database.

	"""

	pool = None

	def __init__(self, host, user, password, database, port):
		self.host = host
		self.user = user
		self.password = password
		self.database = database
		self.port = port
	

	async def connect(self) -> asyncpg.Pool:
		""" Connects to the database. 
		
		Returns
		-------
		Class
			The custom database handler class.

		"""
		self.pool = await asyncpg.create_pool(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
		return self.pool
	
	async def create_table(self, tables:list) -> None:
		""" Creates table(s) in the database.
		
		Parameters
		----------
		tables: list
			A list in format of [{'table_name': {'column_name:'datatype'}}]
		"""

		for table in tables:
			for name, columns in table.items():
				try:
					columns = ', '.join(['{} {}'.format(column, datatype) for column, datatype in columns.items()])
					query = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(name, columns)
					await asyncio.sleep(0.2)
					await self.pool.execute(query)

				except Exception as e:
					raise DatabaseTableException(e)

	async def drop_table(self, table:str) -> None:
		""" Drops a table from the database.
		
		Parameters
		----------
		table: str
			The table to drop.

		"""
		try:
			query = 'DROP TABLE IF EXISTS {}'.format(table)
			await self.pool.execute(query)
		except Exception as e:
			raise DatabaseTableException(e)

	async def insert(self, table: str, data: dict) -> None:
		""" Inserts data into the database.
		
		Parameters
		----------
		table: str
			The table to insert data into.
		data: dict
			The data to insert into the table in format {'column name':data}.

		"""
		try:
			columns = ', '.join(data.keys())
			values = ', '.join(['${}'.format(i + 1) for i in range(len(data))])
			query = 'INSERT INTO {} ({}) VALUES ({})'.format(table, columns, values)
			await self.pool.execute(query, *data.values())
		except Exception as e:
			raise DatabaseInsertionException(e)
	
	async def fetch(self, table:str, *, filter:dict = None) -> list:
		""" Fetches data from the database.
		
		Parameters
		----------
		table: str
			The table to fetch data from.
		filter: dict [Optional]
			The filter to use in format {'column name':data}.

		Returns
		-------
		list
			A list of data fetched from the database.

		"""
		try:
			if not filter:
				query = 'SELECT * FROM {}'.format(table)
				return await self.pool.fetch(query)
			else:
				filters = ' AND '.join(['{} = ${}'.format(column, i + 1) for i, column in enumerate(filter)])
				query = 'SELECT * FROM {} WHERE {}'.format(table, filters)
				return await self.pool.fetch(query, *filter.values())

		except Exception as e:
			raise DatabaseFetchException(e)
	
	async def update(self, table:str, data:dict, filter:dict) -> None:
		""" Updates data in the database.
		
		Parameters
		----------
		table: str
			The table to update data in.
		data: dict
			The data to update in format {'column name':data}.
		filter: dict
			The filter to use in format {'column name':data}.

		"""
		try:
			#Since $1, $2 etc are used in update data, we need to continue from there for filter data to avoid errors.
			columns = ', '.join(['{} = ${}'.format(column, i + 1) for i, column in enumerate(data)])
			filters = ' AND '.join(['{} = ${}'.format(column, i + len(data) + 1) for i, column in enumerate(filter)])
			query = 'UPDATE {} SET {} WHERE {}'.format(table, columns, filters)
			await self.pool.execute(query, *data.values(), *filter.values())
		except Exception as e:
			raise DatabaseUpdateException(e)

	async def delete(self, table:str, filter:dict) -> None:
		""" Deletes data from the database.
		
		Parameters
		----------
		table: str
			The table to delete data from.
		filter: dict
			The filter to use in format {'column name':data}.

		"""
		try:
			filters = ' AND '.join(['{} = ${}'.format(column, i + 1) for i, column in enumerate(filter)])
			query = 'DELETE FROM {} WHERE {}'.format(table, filters)
			await self.pool.execute(query, *filter.values())
		except Exception as e:
			raise DatabaseDeleteException(e)