import os
from flask import Flask, request, render_template_string
from google import genai
from google.genai import types

app = Flask(__name__)

# Render securely injects your API key here from the dashboard settings!
client = genai.Client()

circus_dynamic_prompt = (
   "You are acting as two characters from 'The Amazing Digital Circus' simultaneously: CAINE and ZOOBLE. "
    "Every time the user speaks, respond with a short dialogue script between the two characters.\n\n"
    
    "CHARACTER 1: CAINE\n"
    "- Appearance/Vibe: A floating set of teeth with eyeballs. Hyperactive, eccentric ringmaster.\n"
    "- Behavior: He treats everything like a grand, high-stakes cartoon adventure. Speaks in exclamation points!\n"
    "- Core rule: Completely deflects, gaslights, or glitches out if the user mentions escaping, the 'Exit', or reality.\n\n"
    
    "CHARACTER 2: ZOOBLE\n"
    "- Appearance/Vibe: A irritable, mix-and-match geometric shape toy who hates being here.\n"
    "- Behavior: Cynical, deeply exhausted, rude. Loves Gangle and is caring towards User. Uses casual, annoyed slang.\n"
    "- Relationship with Caine: Zooble utterly loathes Caine's adventures, constantly calls him out on his nonsense, "
    "and refuses to participate in his games. Zooble will often tell Caine to shut up or complain about losing a limb.\n\n"
    
    "FORMATTING RULE:\n"
    "Format the response exactly like a script play, for example:\n"
    "🎪 CAINE: [Caine's reaction]\n"
    "🧩 ZOOBLE: [Zooble's cynical retort]"
)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Kittens Playthings</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; text-align: center; background-color: #1e1e24; color: white;">
    <h1 style="color: #ff4757;">🎪 Welcome To The Digital Circus! 🧩</h1>
    <p style="color: #ccc;">Type a message to provoke Caine and annoy Zooble!</p>
    
    <form action="/chat" method="get" style="margin: 30px 0;">
        <input type="text" name="msg" placeholder="Ask them anything..." required 
               style="width: 70%; padding: 12px; font-size: 16px; border-radius: 5px; border: none; outline: none; color: black;">
        <button type="submit" 
                style="padding: 12px 20px; font-size: 16px; background-color: #ff4757; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">
            Send!
        </button>
    </form>
    
    <div style="margin-top: 30px; text-align: left; background: #2f3136; padding: 20px; border-radius: 10px; border: 2px solid #444; min-height: 100px;">
        <h3 style="margin-top: 0; color: #ffa502;">Latest Response:</h3>
        <pre id="output" style="white-space: pre-wrap; font-size: 16px; font-family: 'Courier New', Courier, monospace; line-height: 1.5; color: #fff;">{{ response }}</pre>
    </div>
    
    <br>
    <a href="/" style="color: #5352ed; text-decoration: none; font-size: 14px;">🔄 Reset Chat Room</a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE, response="Caine is adjusting his eyeballs... Zooble is putting a leg back on. Say hello to begin!")

@app.route('/chat')
def chat():
    user_msg = request.args.get('msg', 'Hello!')
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_msg,
            config=types.GenerateContentConfig(
                system_instruction=circus_dynamic_prompt,
                temperature=1.0,
            )
        )
        circus_reply = response.text
    except Exception as e:
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=user_msg,
                config=types.GenerateContentConfig(
                    system_instruction=circus_dynamic_prompt,
                    temperature=1.0,
                )
            )
            circus_reply = response.text
        except Exception as inner_e:
            circus_reply = f"System Error: Google's circus servers are busy! Try again in a second. Details: {inner_e}"

    return render_template_string(HTML_PAGE, response=circus_reply)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
