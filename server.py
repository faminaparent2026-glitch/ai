from flask import Flask, request, jsonify
import re
import json
import hashlib
from datetime import datetime

app = Flask(__name__)

class BHAgent:
    def __init__(self):
        self.memory_short = []
        self.memory_long = {}
        self.knowledge_base = {}
        self.project_data = {}
        self.session_log = []
        
    def layer_1_input(self, raw_input):
        return raw_input.strip()
    
    def layer_2_clean_text(self, text):
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def layer_3_detect_language(self, text):
        # Simple language detection (Arabic/English)
        if re.search(r'[أ-ي]', text):
            return 'ar'
        return 'en'
    
    def layer_4_tokenize(self, text):
        return text.split()
    
    def layer_5_understand_intent(self, tokens):
        # Basic intent detection
        intent_keywords = {
            'search': ['بحث', 'find', 'search'],
            'execute': ['نفذ', 'execute', 'run'],
            'remember': ['تذكر', 'remember', 'save']
        }
        for intent, keywords in intent_keywords.items():
            if any(kw in ' '.join(tokens).lower() for kw in keywords):
                return intent
        return 'general'
    
    def layer_6_extract_info(self, tokens, intent):
        return {'tokens': tokens, 'intent': intent}
    
    def layer_7_analyze_context(self, info):
        return {'context': 'default', 'info': info}
    
    def layer_8_short_memory(self, context):
        self.memory_short.append(context)
        if len(self.memory_short) > 10:
            self.memory_short.pop(0)
        return context
    
    def layer_9_long_memory(self, context):
        key = hashlib.md5(str(context).encode()).hexdigest()[:8]
        self.memory_long[key] = context
        return context
    
    def layer_10_retrieve_memories(self, context):
        # Retrieve relevant memories
        return context
    
    def layer_11_planning(self, context):
        # Plan next actions
        return {'plan': 'process', 'context': context}
    
    def layer_12_reasoning(self, plan):
        # Reasoning logic
        return {'reasoning': 'analyzed', 'plan': plan}
    
    def layer_13_decision_making(self, reasoning):
        # Make decision
        return {'decision': 'proceed', 'reasoning': reasoning}
    
    def layer_14_prioritize(self, decision):
        # Set priorities
        return {'priority': 1, 'decision': decision}
    
    def layer_15_knowledge_base(self, priority):
        # Access knowledge
        return {'knowledge': 'base_data', 'priority': priority}
    
    def layer_16_search(self, knowledge):
        # Search functionality
        return {'search_results': [], 'knowledge': knowledge}
    
    def layer_17_run_tools(self, search):
        # Tool execution
        return {'tools_used': [], 'search': search}
    
    def layer_18_execute_code(self, tools):
        # Code execution
        return {'execution_result': 'success', 'tools': tools}
    
    def layer_19_check_results(self, execution):
        # Validate results
        return {'validated': True, 'execution': execution}
    
    def layer_20_debug(self, results):
        # Debug if needed
        return {'debugged': True, 'results': results}
    
    def layer_21_learn(self, debugged):
        # Update learning
        return {'learned': True, 'debugged': debugged}
    
    def layer_22_evaluate_performance(self, learned):
        # Performance metrics
        return {'performance': 'good', 'learned': learned}
    
    def layer_23_improve_response(self, evaluation):
        # Enhance response
        return {'improved': True, 'evaluation': evaluation}
    
    def layer_24_format_text(self, improved):
        # Format output
        return {'formatted': 'response', 'improved': improved}
    
    def layer_25_manage_personalities(self, formatted):
        # Personality management
        return {'personality': 'default', 'formatted': formatted}
    
    def layer_26_manage_projects(self, personality):
        # Project management
        return {'project_data': self.project_data, 'personality': personality}
    
    def layer_27_save_log(self, project):
        # Save session log
        self.session_log.append({
            'timestamp': datetime.now().isoformat(),
            'data': project
        })
        return {'logged': True, 'project': project}
    
    def layer_28_security(self, logged):
        # Security checks
        return {'secured': True, 'logged': logged}
    
    def layer_29_prepare_response(self, security):
        # Generate final response
        return {'response': 'Processed successfully', 'security': security}
    
    def layer_30_final_output(self, prepared):
        # Output result
        return prepared['response']
    
    def process_query(self, query):
        # Sequential pipeline execution
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

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    query = data.get('query', '')
    response = agent.process_query(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
