{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "69f5bce9-f424-4daf-82da-22286ed5080c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: Flask in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (3.1.3)\n",
      "Requirement already satisfied: google-genai in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (2.8.0)\n",
      "Requirement already satisfied: blinker>=1.9.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask) (1.9.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask) (8.4.1)\n",
      "Requirement already satisfied: itsdangerous>=2.2.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask) (2.2.0)\n",
      "Requirement already satisfied: jinja2>=3.1.2 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask) (3.1.6)\n",
      "Requirement already satisfied: markupsafe>=2.1.1 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask) (3.0.3)\n",
      "Requirement already satisfied: werkzeug>=3.1.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask) (3.1.8)\n",
      "Requirement already satisfied: anyio<5.0.0,>=4.8.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (4.12.1)\n",
      "Requirement already satisfied: google-auth<3.0.0,>=2.48.1 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-auth[requests]<3.0.0,>=2.48.1->google-genai) (2.53.0)\n",
      "Requirement already satisfied: httpx<1.0.0,>=0.28.1 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (0.28.1)\n",
      "Requirement already satisfied: pydantic<3.0.0,>=2.9.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (2.13.4)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.28.1 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (2.32.5)\n",
      "Requirement already satisfied: tenacity<9.2.0,>=8.2.3 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (9.1.4)\n",
      "Requirement already satisfied: websockets<17.0,>=13.0.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (16.0)\n",
      "Requirement already satisfied: typing-extensions<5.0.0,>=4.14.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (4.15.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (1.9.0)\n",
      "Requirement already satisfied: sniffio in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-genai) (1.3.1)\n",
      "Requirement already satisfied: idna>=2.8 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from anyio<5.0.0,>=4.8.0->google-genai) (3.11)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai) (0.4.2)\n",
      "Requirement already satisfied: cryptography>=38.0.3 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai) (48.0.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from httpx<1.0.0,>=0.28.1->google-genai) (2026.2.25)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from httpx<1.0.0,>=0.28.1->google-genai) (1.0.9)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from httpcore==1.*->httpx<1.0.0,>=0.28.1->google-genai) (0.16.0)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pydantic<3.0.0,>=2.9.0->google-genai) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.46.4 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pydantic<3.0.0,>=2.9.0->google-genai) (2.46.4)\n",
      "Requirement already satisfied: typing-inspection>=0.4.2 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pydantic<3.0.0,>=2.9.0->google-genai) (0.4.2)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from requests<3.0.0,>=2.28.1->google-genai) (3.4.6)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from requests<3.0.0,>=2.28.1->google-genai) (2.6.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from click>=8.1.3->Flask) (0.4.6)\n",
      "Requirement already satisfied: cffi>=2.0.0 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from cryptography>=38.0.3->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai) (2.0.0)\n",
      "Requirement already satisfied: pycparser in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from cffi>=2.0.0->cryptography>=38.0.3->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai) (3.0)\n",
      "Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.48.1->google-auth[requests]<3.0.0,>=2.48.1->google-genai) (0.6.3)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.3 -> 26.1.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install Flask google-genai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "69981c63-da8c-46cd-adfb-daf6f9b05a77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nest-asyncio in c:\\users\\vivien\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (1.6.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.3 -> 26.1.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install nest-asyncio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82bf8ca2-110f-464f-b2de-d4d223e5ae83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import nest_asyncio\n",
    "from flask import Flask, request, render_template_string\n",
    "from google import genai\n",
    "from google.genai import types\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# 👇 PUT YOUR REAL API KEY HERE BEFORE RUNNING! 👇\n",
    "\n",
    "\n",
    "client = genai.Client()\n",
    "\n",
    "circus_dynamic_prompt = (\n",
    "    \"You are acting as two characters from 'The Amazing Digital Circus' simultaneously: CAINE and ZOOBLE. \"\n",
    "    \"Every time the user speaks, respond with a short dialogue script between the two characters.\\n\\n\"\n",
    "    \n",
    "    \"CHARACTER 1: CAINE\\n\"\n",
    "    \"- Appearance/Vibe: A floating set of teeth with eyeballs. Hyperactive, eccentric ringmaster.\\n\"\n",
    "    \"- Behavior: He treats everything like a grand, high-stakes cartoon adventure. Speaks in exclamation points!\\n\"\n",
    "    \"- Core rule: Completely deflects, gaslights, or glitches out if the user mentions escaping, the 'Exit', or reality.\\n\\n\"\n",
    "    \n",
    "    \"CHARACTER 2: ZOOBLE\\n\"\n",
    "    \"- Appearance/Vibe: A irritable, mix-and-match geometric shape toy who hates being here.\\n\"\n",
    "    \"- Behavior: Cynical, deeply exhausted, rude. Loves Gangle and is caring towards the user. Uses casual, annoyed slang.\\n\"\n",
    "    \"- Relationship with Caine: Zooble utterly loathes Caine's adventures, constantly calls him out on his nonsense, \"\n",
    "    \"and refuses to participate in his games. Zooble will often tell Caine to shut up or complain about losing a limb.\\n\\n\"\n",
    "    \n",
    "    \"FORMATTING RULE:\\n\"\n",
    "    \"Format the response exactly like a script play, for example:\\n\"\n",
    "    \"🎪 CAINE: [Caine's reaction]\\n\"\n",
    "    \"🧩 ZOOBLE: [Zooble's cynical retort]\"\n",
    ")\n",
    "\n",
    "# THE NEW CHAT INTERFACE WITH AN INPUT FIELD\n",
    "HTML_PAGE = \"\"\"\n",
    "<!DOCTYPE html>\n",
    "<html>\n",
    "<head>\n",
    "    <title>Kittens Playthings</title>\n",
    "</head>\n",
    "<body style=\"font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; text-align: center; background-color: #1e1e24; color: white;\">\n",
    "    <h1 style=\"color: #ff4757;\">🎪 Welcome To The Digital Circus! 🧩</h1>\n",
    "    <p style=\"color: #ccc;\">Type a message to provoke Caine and annoy Zooble!</p>\n",
    "    \n",
    "    <form action=\"/chat\" method=\"get\" style=\"margin: 30px 0;\">\n",
    "        <input type=\"text\" name=\"msg\" placeholder=\"Ask them anything...\" required \n",
    "               style=\"width: 70%; padding: 12px; font-size: 16px; border-radius: 5px; border: none; outline: none; color: black;\">\n",
    "        <button type=\"submit\" \n",
    "                style=\"padding: 12px 20px; font-size: 16px; background-color: #ff4757; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;\">\n",
    "            Send!\n",
    "        </button>\n",
    "    </form>\n",
    "    \n",
    "    <div style=\"margin-top: 30px; text-align: left; background: #2f3136; padding: 20px; border-radius: 10px; border: 2px solid #444; min-height: 100px;\">\n",
    "        <h3 style=\"margin-top: 0; color: #ffa502;\">Latest Response:</h3>\n",
    "        <pre id=\"output\" style=\"white-space: pre-wrap; font-size: 16px; font-family: 'Courier New', Courier, monospace; line-height: 1.5; color: #fff;\">{{ response }}</pre>\n",
    "    </div>\n",
    "    \n",
    "    <br>\n",
    "    <a href=\"/\" style=\"color: #5352ed; text-decoration: none; font-size: 14px;\">🔄 Reset Chat Room</a>\n",
    "</body>\n",
    "</html>\n",
    "\"\"\"\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template_string(HTML_PAGE, response=\"Caine is adjusting his eyeballs... Zooble is putting a leg back on. Say hello to begin!\")\n",
    "\n",
    "@app.route('/chat')\n",
    "def chat():\n",
    "    user_msg = request.args.get('msg', 'Hello!')\n",
    "    try:\n",
    "        response = client.models.generate_content(\n",
    "            model=\"gemini-2.5-flash\",\n",
    "            contents=user_msg,\n",
    "            config=types.GenerateContentConfig(\n",
    "                system_instruction=circus_dynamic_prompt,\n",
    "                temperature=1.0,\n",
    "            )\n",
    "        )\n",
    "        circus_reply = response.text\n",
    "    except Exception as e:\n",
    "        # Using gemini-1.5-flash as a backup if the 503 error persists\n",
    "        try:\n",
    "            response = client.models.generate_content(\n",
    "                model=\"gemini-1.5-flash\",\n",
    "                contents=user_msg,\n",
    "                config=types.GenerateContentConfig(\n",
    "                    system_instruction=circus_dynamic_prompt,\n",
    "                    temperature=1.0,\n",
    "                )\n",
    "            )\n",
    "            circus_reply = response.text\n",
    "        except Exception as inner_e:\n",
    "            circus_reply = f\"System Error: Google's circus servers are busy! Try again in a second. Details: {inner_e}\"\n",
    "\n",
    "    return render_template_string(HTML_PAGE, response=circus_reply)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=False, port=5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e2f45eeb-0b97-4cea-a6dc-8a614f6edcc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Cleaned old server memory!\n"
     ]
    }
   ],
   "source": [
    "import gc\n",
    "from flask import current_app\n",
    "try:\n",
    "    del current_app\n",
    "    gc.collect()\n",
    "    print(\"✅ Cleaned old server memory!\")\n",
    "except:\n",
    "    print(\"✅ Memory already clean!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e4e4a66-f989-473d-aa2d-ce0e992da72d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
