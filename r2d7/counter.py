import json
import logging
import re
import requests
from r2d7.core import DroidCore

logger = logging.getLogger(__name__)

class Counter(DroidCore):
    """
    This class counts occurences of in-jokes
    """
    solved_handler = re.compile('(.*?solved the format.*)', re.I)
    curse_handler = re.compile('(!curse.*)', re.I)
    dad_handler = re.compile('(!dad.*)', re.I)

    _json_store_url = 'https://www.jsonstore.io/a12bdb4a180a6213b45968ed5ea5626afef1d792f0a683d870c7b5b709189b43'

    # Values are accurate at time of writing
    _counter_data = {
        'curse_count': 1010,
        'solved_format_count': 3,
        'dad_joke_count': 0
    }

    def __init__(self):
        super().__init__()
        self.register_handler(Counter.solved_handler, self.solved_format)
        self.register_handler(Counter.curse_handler, self.curse_mark)
        self.register_handler(Counter.dad_handler, self.dad_joke)

        self._load_json()
        self._store_json() # re-uploading ensures cloud json is valid

    def _load_json(self):
        try:
            stored_data = requests.get(Counter._json_store_url).json().get('result')
            if stored_data is not None:
                stored_dict = json.loads(stored_data)
                for key, local in self._counter_data.items():
                    stored = stored_dict.get(key) or 0
                    self._counter_data[key] = max(stored, local)
        except Exception as err:
            logger.debug(f'Error downloading stored json: {str(err)}')
            print(f'Error downloading stored json: {str(err)}')

    def _store_json(self):
        try:
            payload = json.dumps(self._counter_data)
            requests.put(Counter._json_store_url, json=payload)
        except Exception as err:
            logger.debug(f'Error uploading json for storage: {str(err)}')
            print(f'Error uploading json for storage: {str(err)}')

    def solved_format(self, message):
        self._load_json()
        count = (self._counter_data.get('solved_format_count') or 3) + 1
        self._counter_data['solved_format_count'] = count
        self._store_json()
        return [[f'Solved format count: {count}']]

    def curse_mark(self, message):
        self._load_json()
        count = (self._counter_data.get('curse_count') or 1010) + 1
        self._counter_data['curse_count'] = count
        self._store_json()
        return [[f'Mark\'s dice have now been cursed {count} times!']]

    def dad_joke(self, message):
        self._load_json()
        count = (self._counter_data.get('dad_joke_count') or 0) + 1
        self._counter_data['dad_joke_count'] = count
        self._store_json()
        return [[f'Dad joke count: {count}']]

