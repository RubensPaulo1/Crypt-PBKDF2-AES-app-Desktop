# Crypt-PBKDF2-AES-app-Desktop
Aplicativo desktop para criptografia de arquivos usando AES e derivação de chave via PBKDF2, desenvolvido com Flask e PyWebView.


SecureVault Desktop é um aplicativo desktop leve para criptografia e descriptografia segura de arquivos, utilizando padrões modernos de criptografia.

Desenvolvido com Flask e PyWebView, o sistema funciona como um aplicativo nativo, sem barra de navegador.

---

##Funcionalidades

- Criptografia AES (via Fernet)
- Derivação de chave baseada em senha (PBKDF2)
- 200.000 iterações para reforço de segurança
- Salt único por arquivo
- Restauração segura do arquivo original
- Interface moderna em modo escuro
- Seletor de arquivos nativo
- Compatível com Windows

---

- Python 3.13
- Flask
- PyWebView
- Cryptography (AES + PBKDF2)

---

## Modelo de Segurança

Ao criptografar um arquivo:

1. Um salt aleatório é gerado.
2. A senha do usuário é processada usando PBKDF2 (200.000 iterações).
3. Uma chave segura é derivada.
4. O arquivo é criptografado com AES.
5. O salt é incorporado ao arquivo criptografado.

Isso garante:

- Ausência de chave fixa
- Proteção contra ataques de força bruta
- Isolamento por arquivo
- Integridade e autenticação via Fernet

ATENÇÃO: Sem a senha correta, o arquivo não pode ser recuperado.

Ficarei muito feliz se você modificar o projeto, por favor caompartilhe comigo.
