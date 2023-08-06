# infodata' u2python module to work with ..GRAPH... intools 
import sys 
import traceback 
import json 
import msal 

def helloWorld():
     print("hellp from inpython")

def getGraphTokenFromCertificate(path): 
# fonctions pour générer un token Graph avec un certificat
# retourne un objet string json 
# {
#      "token_type": "Bearer",
#      "expires_in": 3599,
#      "ext_expires_in": 3599,
#      "access_token": "eyJ0eXAiOiJKV1QiLCJub25jZS..."
# }
# ----------------------
# {
#      "error": "invalid_client",
#      "error_description": "AADSTS700027: The certificate with identifier used to sign the client assertion is not registered on application. [Reason - The key was not found., Thumbprint of key used by client: 'D02953830A67536051EFCB073FB05537287D3800', Please visit the Azure Portal, Graph Explorer or directly use MS Graph to see configured keys for app Id '15855fc2-ac31-4020-b32d-5dd531bd6b43'. Review the documentation at https://docs.microsoft.com/en-us/graph/deployments to determine the corresponding service endpoint and https://docs.microsoft.com/en-us/graph/api/application-get?view=graph-rest-1.0&tabs=http to build a query request URL, such as 'https://graph.microsoft.com/beta/applications/15855fc2-ac31-4020-b32d-5dd531bd6b43'].\r\nTrace ID: c239abbb-de7c-4092-8f1a-6a13382c5500\r\nCorrelation ID: 48f14b85-0366-451d-b576-e78bb526ade9\r\nTimestamp: 2023-07-17 10:33:11Z",
#      "error_codes": [
#           700027
#      ],
#      "timestamp": "2023-07-17 10:33:11Z",
#      "trace_id": "c239abbb-de7c-4092-8f1a-6a13382c5500",
#      "correlation_id": "48f14b85-0366-451d-b576-e78bb526ade9",
#      "error_uri": "https://login.microsoftonline.com/error?code=700027"
# }
# -----------------------------------------------------------------------------------------------------------
# c.f. 
# https://github.com/Azure-Samples/ms-identity-python-daemon/tree/master/2-Call-MsGraph-WithCertificate

     # load config file .json
     # {
     #   "authority": "https://login.microsoftonline.com/infodata.lu",
     #   "tenant_id": "e2a26e34-3...",
     #   "client_id": "15855fc2-...",
     #   "scope": [ "https://graph.microsoft.com/.default" ],
     #   "thumbprint": "9615472D8...",
     #   "private_key_file": "...//9615472D8...//9615472D8....privatekey"
     # }
     
     try:
          f = open(path)
          config = json.load(f)
     except: # catch *all* exceptions
          result = {"errorCode" : "1",
                    "errorFrom" : "json.load({0})".format(path), 
                    "error"     : "{0}".format(traceback.format_exc())
                    }
          f.close()
          return json.dumps(result)
     
     # try to connect
     try:
          app = msal.ConfidentialClientApplication(               
                    config["client_id"],                
                    authority=config["authority"],              
                    client_credential={"thumbprint": config["thumbprint"],                              
                                       "private_key": open(config['private_key_file']).read()},               )
     except:
          result = {"errorCode" : "2",
                    "errorFrom" : "msal.ConfidentialClientApplication(authority={authority}, client_credentials=thumbprint={thumbprint}, privatekey={privatekey})".format(authority=config["authority"], thumbprint=config["thumbprint"], privatekey=config['private_key_file']), 
                    "error" : "{0}".format(traceback.format_exc())
                    }
          f.close()
          return json.dumps(result)

     # try to get a token
     result = None
     try:
          result = app.acquire_token_for_client(scopes=config["scope"])
     except:
          result = {"errorCode" : "3",
                    "errorFrom" : "app.acquire_token_for_client {scopes}=".format(scopes=config["scope"]) , 
                    "error" : "{0}".format(traceback.format_exc())
                    }
          f.close()
          return json.dumps(result)

     return json.dumps(result)



def getGraphTokenFromCertificate2(path): 
# fonctions pour générer un token Graph avec un certificat
# retourne un objet string json 
# {
#      "token_type": "Bearer",
#      "expires_in": 3599,
#      "ext_expires_in": 3599,
#      "access_token": "eyJ0eXAiOiJKV1QiLCJub25jZS..."
# }
# ----------------------
# {
#      "error": "invalid_client",
#      "error_description": "AADSTS700027: The certificate with identifier used to sign the client assertion is not registered on application. [Reason - The key was not found., Thumbprint of key used by client: 'D02953830A67536051EFCB073FB05537287D3800', Please visit the Azure Portal, Graph Explorer or directly use MS Graph to see configured keys for app Id '15855fc2-ac31-4020-b32d-5dd531bd6b43'. Review the documentation at https://docs.microsoft.com/en-us/graph/deployments to determine the corresponding service endpoint and https://docs.microsoft.com/en-us/graph/api/application-get?view=graph-rest-1.0&tabs=http to build a query request URL, such as 'https://graph.microsoft.com/beta/applications/15855fc2-ac31-4020-b32d-5dd531bd6b43'].\r\nTrace ID: c239abbb-de7c-4092-8f1a-6a13382c5500\r\nCorrelation ID: 48f14b85-0366-451d-b576-e78bb526ade9\r\nTimestamp: 2023-07-17 10:33:11Z",
#      "error_codes": [
#           700027
#      ],
#      "timestamp": "2023-07-17 10:33:11Z",
#      "trace_id": "c239abbb-de7c-4092-8f1a-6a13382c5500",
#      "correlation_id": "48f14b85-0366-451d-b576-e78bb526ade9",
#      "error_uri": "https://login.microsoftonline.com/error?code=700027"
# }
# -----------------------------------------------------------------------------------------------------------
# c.f. 
# https://github.com/Azure-Samples/ms-identity-python-daemon/tree/master/2-Call-MsGraph-WithCertificate

     # load config file .json
     # {
     #   "authority": "https://login.microsoftonline.com/infodata.lu",
     #   "tenant_id": "e2a26e34-3...",
     #   "client_id": "15855fc2-...",
     #   "scope": [ "https://graph.microsoft.com/.default" ],
     #   "thumbprint": "9615472D8...",
     #   "private_key_file": "...//9615472D8...//9615472D8....privatekey"
     # }
    
     f = open(path)
     config = json.load(f)
     app = msal.ConfidentialClientApplication(               
               config["client_id"],                
               authority=config["authority"],              
               client_credential={"thumbprint": config["thumbprint"],                              
                                   "private_key": open(config['private_key_file']).read()},               )
     result = app.acquire_token_for_client(scopes=config["scope"])
