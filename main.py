from flask import Flask, request, jsonify # type: ignore
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY= os.getenv("GEMINI_API_KEY")

app = Flask(__name__)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_module_ajar(data):
    prompt = f"""
    Buatkan modul ajar Kurikulum Merdeka untuk Sekolah Dasar (SD).
    - Kelas: {data['kelas']}
    - Semester: {data['semester']}
    - Mata Pelajaran: {data['mata_pelajaran']}
    - Pertemuan: {data['pertemuan']}
    - Tema: {data['tema']}
    - Sub Tema: {data['sub_tema']}

    Format output dalam JSON:
    {{
      "kompetensi_dasar": "...",
      "tujuan_pembelajaran": "...",
      "materi_pembelajaran": "...",
      "strategi_pembelajaran": "...",
      "media_pembelajaran": "...",
      "asesmen": "..."
    }}
    """

    response = model.generate_content(prompt)
    print(response.text)
    return response.text

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        result = generate_module_ajar(data)
        return jsonify({"status": "success", "module": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)