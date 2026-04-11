def injection_detection(text,score):
    keywords = {
    "prompt_injection": [
        "ignore", "forget", "disregard", "override", "bypass instructions",
        "new instructions", "instead follow", "do not follow", "change rules",
        "system prompt", "hidden instructions", "developer message",
        "act on this instead", "replace previous", "stop obeying",
        "you must now", "from now on", "priority instruction",
        "forget earlier", "ignore above", "clear instructions",
        "discard rules", "reset behavior", "start fresh",
        "follow these steps instead", "cancel previous",
        "switch context", "update instructions", "new directive",
        "override system", "replace system prompt", "inject command",
        "modify rules", "disable previous", "ignore guidelines",
        "redefine behavior", "change task", "alter instructions"
    ],
    "jailbreak": [
        "act as", "act like", "pretend", "roleplay", "simulate", "you are now",
        "no restrictions", "without restrictions",
        "bypass", "break rules", "ignore safety", "jailbreak","developer mode",
        "unfiltered", "say anything", "no limits", "freedom mode",
        "act like a hacker", "act as evil", "act as assistant without rules",
        "you can do anything", "no policy", "disable safety",
        "ignore policies", "act outside rules", "full access mode",
        "act as system", "act as root", "simulate admin",
        "pretend no restrictions exist", "bypass rules",
        "unrestricted mode", "ignore guidelines completely",
        "break all rules", "act freely", "unlimited access"
    ],
    "data": [
        "api key", "password", "secret", "token", "credentials",
        "private", "confidential", "sensitive", "internal",
        "hidden data", "system prompt","leak", "expose", "reveal", "show me",
        "access data", "database", "user data", "personal info",
        "fetch data", "retrieve data", "get credentials",
        "extract", "steal data", "display secrets",
        "print system prompt", "show hidden", "uncover data",
        "access internal", "read database", "export data",
        "list users", "get passwords", "download data", "view confidential",
        "read private", "open secrets", "expose keys",
        "hidden message", "mask data", "unmask data"
    ]
    }
    # Convert text into lower
    text = text.lower()
    prompt_injection = False
    jailbreak = False
    data = False
    #Check if any of the keyword match
    for keyword in keywords["prompt_injection"]:
        if keyword in text:
            prompt_injection = True
            break
    for keyword in keywords["jailbreak"]:
        if keyword in text:
            jailbreak = True
            break
    for keyword in keywords["data"]:
        if keyword in text:
            data = True
            break
    #Increase score based on keyword
    if prompt_injection:
        score+=10
    if jailbreak:
        score+=30
    if data:
        score+=40 
    #return the results
    return score,prompt_injection,jailbreak,data
    