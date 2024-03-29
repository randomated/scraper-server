import json
from flask import Flask, Response
from database.saver import Saver
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, str):
      return obj.encode('utf-8').decode('unicode-escape')
    return super().default(obj)

@app.route('/api/v1/scraper/server')
def index():
  saver = Saver(current_directory)
  data = saver.fetch_datas()

  json_data = json.dumps(data, ensure_ascii=False, cls=CustomJSONEncoder)
  response = Response(json_data, content_type='application/json; charset=utf-8')
  
  saver.close_db()
  return response

if __name__ == '__main__':
  app.json_provider_class = CustomJSONEncoder
  app.run(host='0.0.0.0', port=4000)
