from flask import Flask, render_template, request, jsonify
import os
from .config import config
from .pipeline import ComparisonPipeline

app = Flask(__name__, 
            template_folder=os.path.join(os.getcwd(), 'templates'),
            static_folder=os.path.join(os.getcwd(), 'static'))

app.secret_key = config.FLASK_SECRET_KEY
pipeline = ComparisonPipeline()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json or {}
    problem = data.get('problem_description')
    
    if not problem:
        return jsonify({"error": "Missing problem description"}), 400
        
    result = pipeline.run(problem)
    
    if result.get('status') == 'error':
        return jsonify(result), 500
        
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT, debug=True)
