class BHAgent:
    def __init__(self):
        # Layer 8, 9, 10: الذاكرة (Memory)
        self.short_term_memory = []
        self.long_term_memory = {} # قاعدة بيانات بسيطة

    def process_query(self, query: str) -> dict:
        # نبدأ بتمرير النص عبر الطبقات واحدة تلو الأخرى
        context = {
            "raw": query,
            "clean": "",
            "lang": "unknown",
            "tokens": [],
            "intent": "none",
            "entities": [],
            "context_type": "general",
            "response": ""
        }

        # --- تنفيذ الطبقات ---
        context = self._layer_1_input(context)
        context = self._layer_2_cleaning(context)
        context = self._layer_3_lang_detection(context)
        context = self._layer_4_tokenization(context)
        context = self._layer_5_intent_understanding(context)
        context = self._layer_6_entity_extraction(context)
        context = self._layer_7_context_analysis(context)
        
        # الطبقة 29: إعداد الرد (دمج الطبقات السابقة في رد)
        context["response"] = f"فهمت نيتك ({context['intent']}) في سياق ({context['context_type']})."
        
        # حفظ في الذاكرة (Layer 27)
        self.short_term_memory.append(context)
        
        return {"response": {"message": context["response"]}}

    # --- تنفيذ الطبقات ---
    def _layer_1_input(self, ctx): return ctx
    
    def _layer_2_cleaning(self, ctx):
        ctx["clean"] = "".join(c for c in ctx["raw"] if c.isalnum() or c.isspace()).lower()
        return ctx

    def _layer_3_lang_detection(self, ctx):
        ctx["lang"] = "Arabic" if any('\u0600' <= c <= '\u06FF' for c in ctx["clean"]) else "English"
        return ctx

    def _layer_4_tokenization(self, ctx):
        ctx["tokens"] = ctx["clean"].split()
        return ctx

    def _layer_5_intent_understanding(self, ctx):
        if "مرحبا" in ctx["clean"]: ctx["intent"] = "greeting"
        elif "وقت" in ctx["clean"]: ctx["intent"] = "query_time"
        return ctx

    def _layer_6_entity_extraction(self, ctx):
        # هنا تستخرج أسماء أو تواريخ
        return ctx

    def _layer_7_context_analysis(self, ctx):
        ctx["context_type"] = "conversation"
        return ctx

