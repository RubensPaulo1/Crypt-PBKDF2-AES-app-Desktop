from flask import Flask, render_template, jsonify
import webview
import threading
from crypto_utilis import encrypt_file, decrypt_file

app = Flask(__name__)

class Api:
    def __init__(self):
        self.selected_file = None

    def select_file(self):
        file_path = webview.windows[0].create_file_dialog(webview.OPEN_DIALOG)
        if file_path:
            self.selected_file = file_path[0]
            return self.selected_file
        return None

    def encrypt(self, password):
        if not self.selected_file:
            return {"status": "error", "message": "Selecione um arquivo primeiro."}

        if len(password) < 6:
            return {"status": "error", "message": "Senha muito curta (mínimo 6 caracteres)."}

        try:
            new_file = encrypt_file(self.selected_file, password)
            return {"status": "success", "message": f"Arquivo salvo em: {new_file}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def decrypt(self, password):
        if not self.selected_file:
            return {"status": "error", "message": "Selecione um arquivo primeiro."}

        try:
            new_file = decrypt_file(self.selected_file, password)
            return {"status": "success", "message": f"Arquivo salvo em: {new_file}"}
        except Exception:
            return {"status": "error", "message": "Senha incorreta ou arquivo inválido."}

    def decrypt(self, password):
        file_path = webview.windows[0].create_file_dialog(webview.OPEN_DIALOG)
        if file_path:
            try:
                new_file = decrypt_file(file_path[0], password)
                return f"Arquivo descriptografado: {new_file}"
            except Exception:
                return "Senha incorreta ou arquivo inválido!"
        return "Nenhum arquivo selecionado"

@app.route("/")
def index():
    return render_template("index.html")

def start_flask():
    app.run()

if __name__ == "__main__":
    api = Api()

    t = threading.Thread(target=start_flask)
    t.daemon = True
    t.start()

    webview.create_window(
        "Crypto Desktop App",
        "http://127.0.0.1:5000",
        width=500,
        height=400,
        resizable=False,
        js_api=api
    )

    webview.start()