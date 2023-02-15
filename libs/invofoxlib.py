'''
    Invofox API Requests
'''

import os
import requests

class invofox_auth: #pylint: disable=invalid-name
    '''
        Clase Invofox
    '''
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://prod.kinequo.com/backends/midas/"
        self.valid = None
        self.getValid()

    def getValid(self):
        '''
            Metodo para validar la API Key
        '''
        try:
            url = self.url
            headers = {
                "x-api-key": self.api_key
            }
            r = requests.get(url, headers=headers, timeout=30)

            if r.status_code == 200:
                self.valid = True
            else:
                self.valid = False

        except Exception as exc:
            raise exc



    def upload_documents(self,
                         path_file=None,
                         path_folder=None,
                         type_document=None,
                         id_company=None,
                         id_load_batch=None,
                         close_batch=None,
                         additional_data=None):
        '''
            Metodo para subir documentos
        '''
        try:
            url = self.url + "documents/bulk"

            if path_folder:
                file_paths = [file_name for file_name in os.listdir(path_folder) if os.path.isfile(os.path.join(path_folder, file_name))]
            elif path_file:
                file_paths = [path_file]
            else:
                file_paths = None
            ext_to_mime = {
                'jpeg': 'image/jpeg',
                'jpg': 'image/jpg',
                'png': 'image/png',
                'tiff': 'image/tiff',
                'gif': 'image/gif',
                'pdf': 'application/pdf',
                'zip': 'application/x-zip-compressed'
            }

            mimes = []

            if file_paths is not None:
                for file_path in file_paths:
                    _, file_extension = os.path.splitext(file_path)
                    mime = ext_to_mime.get(file_extension[1:], None)
                    if mime is None:
                        print(f"No se ha podido determinar el tipo mime del archivo {file_path}. Por favor verifique la extensión del archivo.")
                    else:
                        mimes.append(mime)

                if path_folder:
                    files = [('files', (file_path, open(os.path.join(path_folder, file_path), 'rb'), mime)) for file_path, mime in zip(file_paths, mimes)]
                elif path_file:
                    files = [('files', (file_path, open(file_path, 'rb'), mime)) for file_path, mime in zip(file_paths, mimes)]
            else:
                files = []

            headers = {
                "accept": "application/json",
                "x-api-key": self.api_key,
            }

            payload = {
                "type": type_document
            }

            if id_company:
                payload["company"] = id_company
            if id_load_batch:
                payload["loadBatch"] = id_load_batch
            if close_batch:
                payload["closeBatch"] = 'true'
            if additional_data:
                payload["clientData"] = additional_data

            if files != []:
                r = requests.post(url, headers=headers, files=files, data=payload, timeout=60)
            else:
                r = requests.post(url, headers=headers, data=payload, timeout=60)

            j = r.json()

            return j

        except Exception as exc:
            raise exc

    def get_documents(self,
                      skip=None,
                      limit=None,
                      type_document=None,
                      public_state=None,
                      id_company=None
                      ):
        '''
            Metodo para obtener documentos
        '''
        try:
            url = self.url + "documents"

            headers = {
                "accept": "application/json",
                "x-api-key": self.api_key,
            }

            payload = {}

            if skip:
                payload["skip"] = skip
            if limit:
                payload["limit"] = limit
            if type_document:
                payload["type"] = type_document
            if public_state:
                if public_state != 'all':
                    payload["publicState"] = public_state
            if id_company:
                payload["company"] = id_company

            if payload:
                r = requests.get(url, headers=headers, params=payload, timeout=60)
            else:
                r = requests.get(url, headers=headers, timeout=60)


            j = r.json()
            print(j)

            j = [{"id": i["_id"], "name": i["name"]} for i in j['result']]



            return j

        except Exception as exc:
            raise exc

    def read_document(self,
                      id_document,
                      values=None
                      ):
        '''
            Metodo para leer un documento
        '''
        try:
            url = self.url + "documents/" + id_document

            headers = {
                "accept": "application/json",
                "x-api-key": self.api_key,
            }

            r = requests.get(url, headers=headers, timeout=60)

            j = r.json()

            res = {}

            if values:
                for i in values:
                    res[i] = j['result'][i] if i in j['result'] else None
            else:
                res = j['result']

            return res

        except Exception as exc:
            raise exc

    def create_company(self,
                       country_code=None,
                       tax_id=None,
                       name=None):
        '''
            Metodo para crear una empresa
        '''
        try:
            url = self.url + "companies"

            headers = {
                "accept": "application/json",
                "x-api-key": self.api_key,
            }

            data = {
                "countryCode": country_code,
                "taxId": tax_id,
                "name": name
            }

            r = requests.post(url, headers=headers, data=data, timeout=60)

            j = r.json()

            return j

        except Exception as exc:
            raise exc

    def get_companies(self,
                      skip=0,
                      limit=50
    ):
        '''
            Metodo para obtener empresas
        '''
        try:
            url = self.url + "companies"

            headers = {
                "accept": "application/json",
                "x-api-key": self.api_key,
            }

            payload = {
                "skip": skip,
                "limit": limit
            }

            r = requests.get(url, headers=headers, params=payload, timeout=60)

            j = r.json()['result']

            return j

        except Exception as exc:
            raise exc
