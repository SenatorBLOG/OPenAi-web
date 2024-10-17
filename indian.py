from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    ingredients = data.get("ingredients")
    if not isinstance(ingredients, list):
        return jsonify({"error": "Ingredients must be a list."}), 400

    description = data.get("description")
    
    prompt = f"""
    На основе следующих ингредиентов: {', '.join(ingredients)}, предложи рецепт блюда. Описание блюда: {description}.
    """
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты шеф-повар, который помогает людям готовить блюда на основе доступных ингредиентов."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.2,
        presence_penalty=0.5
    )
    
    recipe = response.choices[0].message.content
    return jsonify({"recipe": recipe})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
