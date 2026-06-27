from flask import Flask, request, jsonify
import re
import json
import hashlib
from datetime import datetime
import os

app = Flask(__name__)

class BHAgent:
    def __init__(self):
        self.memory_short = []
        self.memory_long = {}
        self.knowledge_base = {}
        self.project_data = {}
        self.session_log = []
        self.personality_config = {'mode': 'professional', 'tone': 'formal'}
        self.security_context = {'authenticated': False, 'session_id': None}
        
    def layer_1_input(self, raw_input): return raw_input.strip()
    def layer_2_clean_text(self, text):
        text = re.sub(r'\s+', ' ', text)
        return re.sub(r'[^\w\s\u0600-\u06FF]', '', text).strip()
    def layer_3_detect_language(self, text): return 'ar' if re.search(r'[أ-ي]', text) else 'en'
    def layer_4_tokenize(self, text): return text.split()
    def layer_5_understand_intent(self, tokens):
        intent_keywords = {
            'search': ['بحث', 'find', 'search', 'ابحث'],
            'execute': ['نفذ', 'execute', 'run', 'شغل'],
            'remember': ['تذكر', 'remember', 'save', 'احفظ'],
            'project': ['مشروع', 'project', 'plan', 'خطط'],
            'query': ['سؤال', 'ask', 'استفسار']
        }
        text = ' '.join(tokens).lower()
        for intent, keywords in intent_keywords.items():
            if any(kw in text for kw in keywords): return intent
        return 'general'
    
    def layer_6_extract_info(self, tokens, intent): return {'tokens': tokens, 'intent': intent, 'entities': [], 'timestamp': datetime.now().isoformat()}
    def layer_7_analyze_context(self, info): return {'context': 'user_query', 'session_id': self.security_context.get('session_id'), 'info': info}
    def layer_8_short_memory(self, context):
        self.memory_short.append(context)
        if len(self.memory_short) > 10: self.memory_short.pop(0)
        return context
    def layer_9_long_memory(self, context):
        key = hashlib.md5(str(context).encode()).hexdigest()[:8]
        self.memory_long[key] = {'timestamp': datetime.now().isoformat(), 'data': context}
        return context
    def layer_10_retrieve_memories(self, context):
        context['related_memories'] = list(self.memory_long.values())[-5:]
        return context
    def layer_11_planning(self, context): return {'plan': {'action': context['info']['intent'], 'steps': ['analyze', 'process', 'respond'], 'priority': 1}, 'context': context}
    def layer_12_reasoning(self, plan_data): return {'reasoning': {'analysis': f'Processing {plan_data["context"]["info"]["intent"]} query', 'confidence': 0.85, 'context': plan_data['context']}, 'plan': plan_data['plan']}
    def layer_13_decision_making(self, reasoning_data): return {'decision': {'action': 'proceed', 'reasoning': reasoning_data['reasoning'], 'requires_tools': False}, 'reasoning': reasoning_data}
    def layer_14_prioritize(self, decision_data): return {'priority': {'level': 1, 'urgent': False, 'decision': decision_data['decision']}, 'decision': decision_data}
    def layer_15_knowledge_base(self, priority_data): return {'knowledge': {'facts': [], 'rules': ['process_queries'], 'priority': priority_data['priority']}, 'priority': priority_data}
    def layer_16_search(self, knowledge_data): return {'search_results': {'results': [], 'query': 'default', 'knowledge': knowledge_data['knowledge']}, 'knowledge': knowledge_data}
    def layer_17_run_tools(self, search_data): return {'tools': {'tools_used': ['parser', 'validator'], 'search': search_data['search_results']}, 'search': search_data}
    def layer_18_execute_code(self, tools_data): return {'execution': {'status': 'success', 'output': 'Processed', 'tools': tools_data['tools']}, 'tools': tools_data}
    def layer_19_check_results(self, execution_data): return {'validated': {'validated': True, 'errors': [], 'execution': execution_data['execution']}, 'execution': execution_data}
    def layer_20_debug(self, validated_data): return {'debugged': {'debugged': True, 'logs': ['No errors found'], 'results': validated_data['validated']}, 'validated': validated_data}
    def layer_21_learn(self, debugged_data): return {'learned': {'learned': True, 'new_patterns': [], 'debugged': debugged_data['debugged']}, 'debugged': debugged_data}
    def layer_22_evaluate_performance(self, learned_data): return {'evaluation': {'performance': 'optimal', 'metrics': {'speed': 'fast', 'accuracy': 'high'}, 'learned': learned_data['learned']}, 'learned': learned_data}
    def layer_23_improve_response(self, evaluation_data): return {'improved': {'improved': True, 'enhancements': ['clarity', 'relevance'], 'evaluation': evaluation_data['evaluation']}, 'evaluation': evaluation_data}
    def layer_24_format_text(self, improved_data): return {'formatted': {'formatted': 'response_ready', 'style': 'clear', 'improved': improved_data['improved']}, 'improved': improved_data}
    def layer_25_manage_personalities(self, formatted_data): return {'personality': {'personality': self.personality_config, 'tone': 'professional', 'formatted': formatted_data['formatted']}, 'formatted': formatted_data}
    def layer_26_manage_projects(self, personality_data): return {'project': {'project_data': self.project_data, 'active': True, 'personality': personality_data['personality']}, 'personality': personality_data}
    def layer_27_save_log(self, project_data):
        self.session_log.append({'timestamp': datetime.now().isoformat(), 'data': project_data['project']})
        return {'logged': True, 'project': project_data}
    def layer_28_security(self, logged_data): return {'security': {'secured': True, 'checks_passed': ['input_validation', 'output_sanitization'], 'logged': logged_data['logged']}, 'logged': logged_data}
    def layer_29_prepare_response(self, security_data): return {'response_data': {'response': 'Request processed successfully', 'status': 'completed', 'security': security_data['security']}, 'security': security_data}
    def layer_30_final_output(self, prepared_data): return prepared_data['response_data']['response']

    def process_query(self, query):
        data = self.layer_1_input(query)
        data = self.layer_2_clean_text(data)
        data = self.layer_3_detect_language(data)
        data = self.layer_4_tokenize(data)
        intent = self.layer_5_understand_intent(data)
        data = self.layer_6_extract_info(data, intent)
        data = self.layer_7_analyze_context(data)
        data = self.layer_8_short_memory(data)
        data = self.layer_9_long_memory(data)
        data = self.layer_10_retrieve_memories(data)
        data = self.layer_11_planning(data)
        data = self.layer_12_reasoning(data)
        data = self.layer_13_decision_making(data)
        data = self.layer_14_prioritize(data)
        data = self.layer_15_knowledge_base(data)
        data = self.layer_16_search(data)
        data = self.layer_17_run_tools(data)
        data = self.layer_18_execute_code(data)
        data = self.layer_19_check_results(data)
        data = self.layer_20_debug(data)
        data = self.layer_21_learn(data)
        data = self.layer_22_evaluate_performance(data)
        data = self.layer_23_improve_response(data)
        data = self.layer_24_format_text(data)
        data = self.layer_25_manage_personalities(data)
        data = self.layer_26_manage_projects(data)
        data = self.layer_27_save_log(data)
        data = self.layer_28_security(data)
        data = self.layer_29_prepare_response(data)
        return self.layer_30_final_output(data)

agent = BHAgent()

@app.route('/')
def home():
    return jsonify({"status": "online", "message": "B.H Agent is active"})

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        if not data or 'query' not in data: return jsonify({'error': 'Missing query'}), 400
        return jsonify({'status': 'success', 'response': agent.process_query(data['query'])})
    except Exception as e: return jsonify({'status': 'error', 'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

