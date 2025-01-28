from flask import Flask, request, render_template, make_response
from azure.keyvault.secrets import SecretClient
from azure.identity import ManagedIdentityCredential

credential = ManagedIdentityCredential(client_id="fb9b4fc1-7856-4b09-ac12-713345ecd510")

#Todo, replace with environment variable after testing
secretClient = SecretClient(vault_url="https://key-vault-in-mi-group.vault.azure.net/", credential=credential)
secret = secretClient.get_secret("test-secret")
print(secret.value)
print(secret.name)
print(secret.id)

app = Flask(__name__)

@app.route('/')
def index():
    print("Request received.")
    if request.headers.get('Authorization') == 'Bearer testSecretValue':
        response = make_response(render_template('index.html'))
        return response, 200
    return "Unauthorized", 401

if __name__ == '__main__':
    app.run()