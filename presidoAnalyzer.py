from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()
def mask(text, score):
    sc = score
    #Patterns
    cnic_pattern = Pattern(
        name="cnic_pattern",
        regex=r"\b\d{5}-\d{7}-\d{1}\b",
        score=0.9
    )

    student_id_pattern = Pattern(
        name="student_id_pattern",
        regex=r"\bFA\d{2}-[A-Z]{3}-\d{3}\b",
        score=0.95
    )

    phone_pattern = Pattern(
        name="phone_pattern",
        regex=r"\b03\d{9}\b",
        score=0.9
    )

    #Recognizers
    cnic_recognizer = PatternRecognizer(
        supported_entity="CNIC",
        patterns=[cnic_pattern]
    )

    student_id_recognizer = PatternRecognizer(
        supported_entity="STUDENT_ID",
        patterns=[student_id_pattern]
    )

    phone_recognizer = PatternRecognizer(
        supported_entity="PHONE_NUMBER",
        patterns=[phone_pattern]
    )

    #Add to analyzer
    analyzer.registry.add_recognizer(cnic_recognizer)
    analyzer.registry.add_recognizer(student_id_recognizer)
    analyzer.registry.add_recognizer(phone_recognizer)

    #Analyze
    results = analyzer.analyze(text=text, language="en")

    #Mask
    masked_result = anonymizer.anonymize(
        text=text,
        analyzer_results=results,
        operators={"DEFAULT": OperatorConfig("replace", {"new_value": "[MASKED]"})}
    )

    masked_text = masked_result.text  

    # Scoring
    detected = len(results) > 0
    #increase score if personal information is detected (context-aware scoring)
    if detected:
        sc += 10   # PII score

    if len(results) > 1:
        sc += 10   # composite entity

    return masked_text, sc, detected, len(results) > 1