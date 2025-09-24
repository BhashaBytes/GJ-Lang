import subprocess


mapping = {
      "બતાવો": "print", "batavo": "print",
      "લાવજો": "input", "lavjo": "input",
      "જો": "if", "jodi": "if",
      "નહિતોજો": "elif", "nahilejo": "elif",
      "નહિતો": "else", "nahile": "else",
      "માટે": "for", "mate": "for",
      "જ્યાંસુધી": "while", "jyasudhi": "while",
      "પરિભાષો": "def", "paribhasho": "def",
      "વર્ગ": "class", "varg": "class",
      "પછાાપો": "return", "pachhaapo": "return",
      "તોડો": "break", "toddo": "break",
      "ચલુરાખો": "continue", "chalurakho": "continue",
      "આયાતકરો": "import", "aayatkaro": "import",
      "થી": "from", "thi": "from",
      "તરિકે": "as", "tarike": "as",
      "સાથે": "with", "sathe": "with",
      "પ્રયત્નકરો": "try", "prayatnkaro": "try",
      "સિવાય": "except", "sivay": "except",
      "અંતેમાં": "finally", "antema": "finally",
      "સાચું": "True", "sachu": "True",
      "ખોટું": "False", "khotu": "False",
      "કૈનનથી": "None", "kainnathi": "None",
      "અથવા": "or", "athava": "or",
}
def translate(code: str) -> str:

    for gj_word, py_word in mapping.items():
        code = code.replace(gj_word, py_word)
    return code

with open("test.gj", "r", encoding="utf-8") as f:
    gj_code = f.read()


python_code = translate(gj_code)
with open("temp.py", "w", encoding="utf-8") as f:
    f.write(python_code)

subprocess.run(["python3", "temp.py"])
