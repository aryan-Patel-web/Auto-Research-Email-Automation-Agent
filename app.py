from flask import Flask, request, render_template
import dill
import pandas as pd

with open("automation_agent.pkl", "rb") as f:
    agent = dill.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run', methods=['POST'])
def run_agent():
    try:
        user_query = request.form.get('query', '').strip()
        df = pd.read_csv("emails.csv")
        email_list = df["email"].dropna().tolist()

        if not user_query:
            return render_template("result.html",
                summary="❌ No query entered.", email_list=[])
        if not email_list:
            return render_template("result.html",
                summary="❌ No valid emails in emails.csv", email_list=[])

        raw = agent.invoke({"input": user_query, "email_list": email_list})
        if not isinstance(raw, dict):
            result = {"summary": str(raw)}
        else:
            result = raw

        summary = result.get("summary", "⚠️ No summary generated.")
        return render_template("result.html", summary=summary, email_list=email_list)

    except Exception as e:
        return render_template("result.html",
            summary=f"❌ Error occurred: {str(e)}", email_list=[])

if __name__ == "__main__":
    app.run(debug=True)
