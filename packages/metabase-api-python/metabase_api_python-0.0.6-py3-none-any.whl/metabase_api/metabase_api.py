import json
import requests
from urllib.parse import urlencode
from .exceptions import *

class MetabaseAPI():
	def __init__(self, base_url=None,user_name=None,password=None):
		self.base_url = base_url
		self.user_name = user_name
		self.password = password
		self.access_token = self._get_access_token()

	def _get_access_token(self):
		url = self.base_url+'/api/session'
		credential_json = {
			'username': self.user_name,
			'password': self.password
		}
		response = requests.post(
			url,
			json=credential_json
		)
		if response.status_code in (200,202):
			return response.json()['id']
		else:
			self._error_handle(response.status_code)

	def _error_handle(self, status_code):
		if status_code == 401:
			raise UnAutorizationException("Invalid Credentials, Please check your user_name and password")
		elif status_code == 400:
			raise BadReuestException(
				"Invalid base_url, Please check your base_url. If base_url contains '/' at the place of end then remove it"
			)
	
	def get_data_from_saved_metabase_question(self, card_id=None, params=None):
		if not card_id:
			raise InvalidRequest("Invalid Request, card_id is empty. please pass valid card_id")

		url = self.base_url + '/api/card/{card_id}/query/json'.format(card_id=card_id)
		headers = {
			'X-Metabase-Session': self.access_token
		}
		payload_json_string = urlencode({
			'parameters': json.dumps(params)
		})
		response = requests.post(
			url,
			headers=headers,
			params=payload_json_string
		)
		if response.status_code in (200,202):
			return json.dumps(response.json(), indent=4)
		else:
			self._error_handle(response.status_code)

	def archive_card(self,card_id=None):
		if not card_id:
			raise InvalidRequest("Invalid Request, card_id is empty. please pass valid card_id")

		url = self.base_url + '/api/card/{card_id}'.format(card_id=card_id)
		headers = {
			'X-Metabase-Session': self.access_token
		}

		response = requests.put(
			url,
			headers=headers,
			json={'archived': True}
		)
		if response.status_code in (200,202):
			return None
		else:
			print(response.content)
			self._error_handle(response.status_code)

	def delete_card(self,card_id=None):
		if not card_id:
			raise InvalidRequest("Invalid Request, card_id is empty. please pass valid card_id")

		url = self.base_url + '/api/card/{card_id}'.format(card_id=card_id)
		headers = {
			'X-Metabase-Session': self.access_token
		}
		response = requests.delete(
			url,
			headers=headers
		)
		if response.status_code in (200,202):
			return None
		else:
			self._error_handle(response.status_code)

	def create_saved_question(self):
		pass

