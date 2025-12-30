# server.py
import contextlib
import io
import traceback

from flask import Flask, jsonify, request

app = Flask(__name__)

# 全域變數字典，讓變數在不同請求間存活 (Stateful)
GLOBAL_CONTEXT = {}


@app.route("/execute", methods=["POST"])
def execute_code():
    data = request.json
    code = data.get("code", "")

    # 捕捉標準輸出 (stdout)
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    result = ""
    error = ""

    with (
        contextlib.redirect_stdout(stdout_capture),
        contextlib.redirect_stderr(stderr_capture),
    ):
        try:
            # 在 GLOBAL_CONTEXT 中執行代碼，這樣變數就會被記住
            exec(code, GLOBAL_CONTEXT)
            result = stdout_capture.getvalue()
        except Exception:
            # 捕捉錯誤並回傳
            error = traceback.format_exc()

    return jsonify({"output": result, "error": error})


if __name__ == "__main__":
    # 監聽所有 IP，Port 8000
    app.run(host="0.0.0.0", port=8000)
