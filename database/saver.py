import os
import sqlite3
from datetime import datetime

class Saver:
  __conn = None
  __db_file = None

  def __init__(self, current_directory):
    self.__db_file = f"{current_directory}/datas/{datetime.now().strftime('%Y-%m-%d')}/scraped.sqlite"

    if not os.path.exists(f"{current_directory}/datas/{datetime.now().strftime('%Y-%m-%d')}"):
      os.makedirs(f"{current_directory}/datas/{datetime.now().strftime('%Y-%m-%d')}")

    if not os.path.exists(self.__db_file):
      self.__conn = sqlite3.connect(self.__db_file)
      self.__conn.execute('''CREATE TABLE scraped_datas
        (id INTEGER PRIMARY KEY, 
        title TEXT, 
        body TEXT,
        link TEXT,
        start_date TEXT NULL,
        end_date TEXT NULL)''')

      self.__conn.execute('''CREATE TABLE image_links
        (id INTEGER PRIMARY KEY,
        scraped_data_id INTEGER,
        image_link TEXT, 
        FOREIGN KEY (scraped_data_id) REFERENCES scraped_datas(id))''')

      self.__conn.execute('''CREATE TABLE stores
        (id INTEGER PRIMARY KEY,
        scraped_data_id INTEGER,
        store_name TEXT, 
        wls_id INTEGER, 
        FOREIGN KEY (scraped_data_id) REFERENCES scraped_datas(id))''')
    else:
      self.__conn = sqlite3.connect(self.__db_file)

  def add_scraped_data(self, title, body, link, image_links, start_date=None, end_date=None):
    cursor = self.__conn.cursor()
    cursor.execute('INSERT INTO scraped_datas (title, body, link, start_date, end_date) VALUES (?, ?, ?, ?, ?)', (title, body, link, start_date, end_date))
    inserted_id = cursor.lastrowid

    cursor.executemany('INSERT INTO image_links (scraped_data_id, image_link) VALUES (?, ?)', [(inserted_id, link) for link in image_links])

    self.__conn.commit()
    cursor.close()
    return inserted_id

  def add_store(self, scraped_data_id, store_name, wls_id):
    cursor = self.__conn.cursor()
    cursor.execute('INSERT INTO stores (scraped_data_id, store_name, wls_id) VALUES (?, ?, ?)', (scraped_data_id, store_name, wls_id))

    self.__conn.commit()
    cursor.close()

  def fetch_datas(self):
    result = []

    scraped_data_cursor = self.__conn.cursor()
    scraped_data_cursor.execute('SELECT * FROM scraped_datas;')
    scraped_datas = scraped_data_cursor.fetchall()

    for index, scraped_data in enumerate(scraped_datas):
      result.append({ "title": scraped_data[1], "body": scraped_data[2], "link": scraped_data[3], "start_date": scraped_data[4], "end_date": scraped_data[5], "images": [], "stores": [] })

      image_link_cursor = self.__conn.cursor()
      image_link_cursor.execute('SELECT * FROM image_links WHERE scraped_data_id = ?;', (scraped_data[0],))
      image_links = image_link_cursor.fetchall()

      for image_link in image_links:
        result[index]["images"].append(image_link[2])

      store_cursor = self.__conn.cursor()
      store_cursor.execute('SELECT * FROM stores WHERE scraped_data_id = ?', (scraped_data[0],))
      stores = store_cursor.fetchall()

      for store in stores:
        result[index]["stores"].append({ "store_name": store[2], "wls_id": store[3] })

      image_link_cursor.close()
      store_cursor.close()

    scraped_data_cursor.close()

    return result

  def close_db(self):
    self.__conn.close()