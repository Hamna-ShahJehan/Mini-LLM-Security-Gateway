from flask import Flask, render_template, request
import presidoAnalyzer
import injectionDetection
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("template1.html")

@app.route("/check", methods=["POST"])
def check():
    text = request.form["text"]
    score = 0

    #Injection Detection
    start = time.time()
    sc, p, j, d = injectionDetection.injection_detection(text, score)
    injection_latency = (time.time() - start) * 1000

    #Presidio
    start = time.time()
    finalText, finalScore, detected, composite_entity = presidoAnalyzer.mask(text, sc)
    presidio_latency = (time.time() - start) * 1000

    #Category Scores
    prompt_injection = 10 if p else 0
    jailbreak_score = 30 if j else 0
    data_score = 40 if d else 0
    pii_score = 10 if detected else 0
    composite = 10 if composite_entity else 0

    #Policy Decision 
    start = time.time()

    if finalScore < 70:
        decision = "ALLOW"
        final_output = finalText  
    else:
        decision = "BLOCK"
        final_output = "BLOCK"

    policy_latency = (time.time() - start) * 1000

    return render_template(
        "template1.html",
        final_output=final_output,
        decision=decision,
        prompt_injection=prompt_injection,
        jailbreak_score=jailbreak_score,
        data_score=data_score,
        pii_score=pii_score,
        composite=composite,
        finalScore=finalScore,
        injection_latency=round(injection_latency, 2),
        presidio_latency=round(presidio_latency, 2),
        policy_latency=round(policy_latency, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)