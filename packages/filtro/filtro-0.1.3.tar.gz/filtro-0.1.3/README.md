# filtro-python

The official Python API package for [filtro.ai](https://www.filtro.ai/). Empowering your applications with AI, while safeguarding sensitive data across all third-party models, in just a few lines of Python code. 

## ⚙️ Install

```bash
pip install filtro
```

## 🗣️ Usage

```py
from filtro import mask, clear

masked, mapping = mask(
    "Hi my name is Giovanni, I work at Google. What's up?"
) # Hi my name is Maria, I work at Marvel. What's up?

from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)
response = llm(masked) # Hi Maria! Im fine. Yourself?

cleared = clear(response, mapping) # Hi Giovanni! Im fine. Yourself?
```

## 🥽 Examples
The standard discussion
```diff
Hi my name is Gianmarco Rengucci! I am a software engineer at Apple, here in Milan. Whats up?
+[filtro.ai] Hi my name is Terri Clark! I am a manager at Google, here in Singapore. Whats up?
-[chat.openai.com] Hey there Terri! Doing great. Curious to learn more about Google. Tell me more!
+[filtro.ai]  Hey there Gianmarco! Doing great. Curious to learn more about Apple. Tell me more!
```

The email and credit cards credentials
```diff
Card number is 1234 5678 9012 3456. You can reach out to richard@gmail.com for questions 🤗 
+[filtro.ai] Card number is 6546410405081471.. You can reach out to teresabrooks@example.org for questions 🍖
```
