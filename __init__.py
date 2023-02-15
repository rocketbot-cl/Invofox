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


GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable


# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"] #pylint: disable=undefined-variable,self-assigning-variable
invofox_directory_path = os.path.join(base_path, "modules", "Invofox")
invofox_libs_path = os.path.join(invofox_directory_path, "libs")

if invofox_libs_path not in sys.path:
    sys.path.append(invofox_libs_path)

from invofoxlib import invofox_auth #pylint: disable=import-error, wrong-import-position, no-name-in-module


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
            if not invofox.valid:
                raise Exception("Invalid API Key")

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

        if values:
            values = values.replace(" ", "").split(",")

        document = invofox.read_document(
            id_document=id_document,
            values=values
        )

        SetVar(result, document)

    if module == "create_company":
        country_code = GetParams("country_code")
        tax_id = GetParams("tax_id")
        name = GetParams("name")
        result = GetParams("result")

        company = invofox.create_company(
            country_code=country_code,
            tax_id=tax_id,
            name=name
        )

        SetVar(result, company)

    if module == "get_companies":
        skip = GetParams("skip")
        limit = GetParams("limit")
        result = GetParams("result")

        companies = invofox.get_companies(
            skip=skip,
            limit=limit
        )

        SetVar(result, companies)

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e
