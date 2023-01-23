# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os
import sys
import traceback
import requests


GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable


# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"] #pylint: disable=undefined-variable,self-assigning-variable
invofox_directory_path = os.path.join(base_path, "modules", "Invofox")
invofox_libs_path = os.path.join(invofox_directory_path, "libs")

if invofox_libs_path not in sys.path:
    sys.path.append(invofox_libs_path)


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
            j = r.json()

            if j == "Hello world!":
                self.valid = True
            else:
                print(j)
                self.valid = False

        except Exception as exc:
            PrintException()
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
            
            # TODO - Verificar si es necesario enviar los urls como un string separado por comas, o si se puede enviar como un array
            # if urls:
            #     urls = urls.split(",")
            #     payload["urls"] = urls
            if id_company:
                payload["company"] = id_company
            if id_load_batch:
                payload["loadBatch"] = id_load_batch
            if close_batch:
                payload["closeBatch"] = close_batch
            if additional_data:
                payload["clientData"] = additional_data

            if files != []:
                r = requests.post(url, headers=headers, files=files, data=payload, timeout=60)
            else:
                r = requests.post(url, headers=headers, data=payload, timeout=60)

            j = r.json()

            return j

        except Exception as exc:
            PrintException()
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
            PrintException()
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
            PrintException()
            raise exc


global mod_invofox  #pylint: disable=invalid-name,global-at-module-level
global invofox  #pylint: disable=invalid-name,global-at-module-level
SESSION_DEFAULT = "default"
try:
    if not mod_invofox: #pylint: disable=used-before-assignment
        mod_invofox = {SESSION_DEFAULT: {}}
except NameError:
    mod_invofox = {SESSION_DEFAULT: {}}


module = GetParams("module")
session = GetParams("session")

if not session:
    session = SESSION_DEFAULT #pylint: disable=invalid-name


try:
    apikey_session = mod_invofox[session].get("apikey", None)
except KeyError:
    pass

try:
    if module == "config":
        api = GetParams("api_key")
        result = GetParams("result")


        try:
            mod_invofox[session] = {
                "apikey": api
            }
            invofox = invofox_auth(mod_invofox[session]["apikey"])
            SetVar(result, invofox.valid)
        except Exception as e:
            PrintException()
            SetVar(result, invofox.valid)
            raise e

    if module == "upload_documents":
        path_file = GetParams("path_file")
        path_folder = GetParams("path_folder")
        type_document = GetParams("type_document")
        id_company = GetParams("id_company")
        id_load_batch = GetParams("id_load_batch")
        close_batch = GetParams("close_batch")
        additional_data = GetParams("additional_data")
        result = GetParams("result")

        upload = invofox.upload_documents(
            path_file=path_file,
            path_folder=path_folder,
            type_document=type_document,
            id_company=id_company,
            id_load_batch=id_load_batch,
            close_batch=close_batch,
            additional_data=additional_data
        )
        SetVar(result, upload)

    if module == "get_documents":
        skip = GetParams("skip")
        limit = GetParams("limit")
        type_document = GetParams("type_document")
        public_state = GetParams("public_state")
        id_company = GetParams("id_company")
        result = GetParams("result")


        documents = invofox.get_documents(
            skip=skip,
            limit=limit,
            type_document=type_document,
            public_state=public_state,
            id_company=id_company
        )

        SetVar(result, documents)

    if module == "read_document":
        id_document = GetParams("id_document")
        values = GetParams("values")
        result = GetParams("result")

        values = values.replace(" ", "").split(",")

        document = invofox.read_document(
            id_document=id_document,
            values=values)

        SetVar(result, document)

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e
