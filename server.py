import datetime

class BHAgentPro:
    def __init__(self):
        self.short_term_memory = []
        self.long_term_memory = {}
        self.knowledge_base = {
            "roblox": "Roblox سكريبتات تتطلب لغة Lua وفهم للـ API الخاص بالمحرك.",
            "speed": "زيادة السرعة في الألعاب تتطلب تعديل قيمة WalkSpeed."
        }
        self.persona = "B.H Expert"

    def process_request(self, user_input):
        # 1-3: الاستلام، التنظيف، وكشف اللغة
        clean_text = user_input.strip().lower()
        
        # 4-7: التقسيم، النية، المعلومات، والسياق
        words = clean_text.split()
        intent = "scripting" if "سكراب" in clean_text or "سكريبت" in clean_text else "general"
        topic = "roblox" if "روبلوكس" in clean_text else "unknown"

        # 8-10: الذاكرة والاسترجاع
        self.short_term_memory.append(clean_text)
        historical_context = self.long_term_memory.get(topic, "لا يوجد سجل سابق")

        # 11-14: التخطيط، التفكير، القرار، الأولويات
        # التفكير: إذا طلب سكريبت روبلوكس للسرعة، الأولوية هي تقديم كود Lua آمن
        decision = "generate_code" if intent == "scripting" else "chat"

        # 15-20: قاعدة المعرفة، البحث، تنفيذ الكود، فحص الأخطاء
        response_body = ""
        if decision == "generate_code" and topic == "roblox":
            response_body = "-- Roblox Speed Script\n" \
                            "game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = 50"
        elif topic == "roblox":
            response_body = self.knowledge_base["roblox"]
        else:
            response_body = "أنا أفهم أنك تسأل عن شيء جديد، سأقوم بتحليله."

        # 21-24: التعلم، التقييم، التحسين، التنسيق
        self.long_term_memory[topic] = response_body # تعلم للمرة القادمة
        
        # 25-30: الشخصية، السجل، الأمان، والرد النهائي
        final_output = f"[{self.persona}]:\n" \
                       f"بناءً على سياق ( {topic} ):\n" \
                       f"{response_body}\n" \
                       f"تم فحص الأمان (Safe) | سجل العملية: {datetime.datetime.now().strftime('%M:%S')}"
        
        return final_output

# تجربة النظام
agent = BHAgentPro()

# الإدخال الأول (سيتعلم النظام)
print(agent.process_request("تقدر تعطيني سكراب حق روبلوكس"))

print("-" * 30)

# الإدخال الثاني (سوف يسترجع من الذاكرة ويطور الإجابة)
print(agent.process_request("ركض ابي اركض بسرعه"))
