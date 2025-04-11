import requests
import time
import random

# ANSI color codes for red and yellow
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Banner function
def print_banner():
    print(RED + "███████╗ █████╗ ██████╗ ███╗   ██╗" + RESET)
    print(YELLOW + "██╔════╝██╔══██╗██╔══██╗████╗  ██║" + RESET)
    print(RED + "███████╗███████║██████╔╝██╔██╗ ██║" + RESET)
    print(YELLOW + "╚════██║██╔══██║██╔═══╝ ██║╚██╗██║" + RESET)
    print(RED + "███████║██║  ██║██║     ██║ ╚████║" + RESET)
    print(YELLOW + "╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═══╝" + RESET)
    print(f"{RED}      💰 EARN{RESET} & {YELLOW}POINTS 💎{RESET}\n")

# API Configuration
URL = "https://api.hyperbolic.xyz/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY_HERE"
}

# List of 100 unique questions
questions = [
"What’s the fastest way to learn a new skill?",  
"How do neural networks mimic the human brain?",  
"What are some quick and healthy lunch ideas?",  
"Can you explain how NFTs function?",  
"What’s the climate like on Venus?",  
"How can I take better smartphone photos?",  
"What are the mental health benefits of exercise?",  
"How do self-learning algorithms improve over time?",  
"What’s the history of social media?",  
"Can you recommend underrated movies or TV shows?",  
"Is there a scientific explanation for consciousness?",  
"How do I brew the perfect cup of tea?",  
"What are the newest breakthroughs in medicine?",  
"How can I build a consistent workout routine?",  
"What’s the future of hydrogen-powered vehicles?",  
"How do I create a successful online store?",  
"What are some unique date night ideas?",  
"Can you explain Schrödinger’s cat in simple terms?",  
"What’s the most effective way to memorize vocabulary?",  
"How do economic recessions happen?",  
"What’s the smartest way to invest in real estate?",  
"How do I backpack through Asia on a budget?",  
"What are the long-term impacts of deforestation?",  
"How do Bluetooth connections work?",  
"What’s the evolution of animation in cinema?",  
"How can I overcome stage fright?",  
"What’s the physics behind lightning?",  
"How do I keep succulents alive indoors?",  
"What happens if you don’t drink enough water?",  
"How do crypto wallets secure digital currency?",  
"What’s the cultural significance of tea worldwide?",  
"How can I manage anxiety naturally?",  
"What are the best sleep positions for back pain?",  
"How do wind turbines generate power?",  
"What’s the secret to making fluffy pancakes?",  
"How does the brain form habits?",  
"What are the most underrated travel destinations?",  
"How do I analyze a company’s stock before investing?",  
"Why do antibiotics not work on viruses?",  
"What are some zero-waste lifestyle changes?",  
"How did ancient civilizations influence modern sports?",  
"What’s the best way to house-train a puppy?",  
"How does Pilates benefit the body?",  
"Can you print human organs with 3D printers?",  
"What’s the fastest way to learn piano?",  
"How do helicopters stay airborne?",  
"What are some ways to overcome writer’s block?",  
"How does the body fight off a cold?",  
"Will humans ever colonize Mars?",  
"How can I stop procrastinating?"  
"How does facial recognition technology work?"
"What are the ethical concerns around AI?"
"How do self-healing materials function?"
"What’s the difference between 5G and 6G?"
"How do holograms work?"
"Can AI ever achieve human-like emotions?"
"What are the risks of genetic engineering?"
"How do lab-grown meats get produced?"
"What’s the science behind time travel?"
"How do drones navigate autonomously?"
"What's the best way to learn programming?",
"How does quantum computing work?",
"What are some healthy breakfast ideas?",
"Can you explain blockchain technology?",
"What's the weather like on Mars?",
"How do I improve my photography skills?",
"What are the benefits of meditation?",
"How does artificial intelligence work?",
"What's the history of the internet?",
"Can you suggest some good books to read?",
"What's the meaning of life?",
"How do I make a perfect cup of coffee?",
"What are the latest space discoveries?",
"How can I stay motivated to exercise?",
"What's the future of electric cars?",
"How do I start a small business?",
"What are some fun weekend activities?",
"Can you explain the theory of relativity?",
"What's the best way to learn a language?",
"How does the stock market work?",
"What's the best way to save money?",
"How do I plan a trip abroad?",
"What are the effects of climate change?",
"How does Wi-Fi actually work?",
"What's the history of video games?",
"How can I improve my public speaking?",
"What's the science behind rainbows?",
"How do I grow indoor plants successfully?",
"What are the benefits of drinking water?",
"How does cryptocurrency mining work?",
"What's the history of chocolate?",
"How can I reduce stress in my life?",
"What are some tips for better sleep?",
"How do solar panels generate electricity?",
"What's the best way to cook steak?",
"How does the human brain process memory?",
"What are some must-visit places in Europe?",
"How do I start investing in stocks?",
"What's the difference between viruses and bacteria?",
"How can I make my home more eco-friendly?",
"What's the history of the Olympic Games?",
"How do I train a dog effectively?",
"What are the benefits of yoga?",
"How does 3D printing work?",
"What's the best way to learn guitar?",
"How do airplanes stay in the air?",
"What are some creative writing tips?",
"How does the immune system fight diseases?",
"What's the future of space travel?",
"How can I improve my time management?",
"What's the history of pizza?",
"How do I create a budget?",
"What are the benefits of recycling?",
"How does virtual reality work?",
"What's the best way to study for exams?",
"How do I make homemade bread?",
"What are the causes of global warming?",
"How does GPS technology work?",
"What's the history of photography?",
"How can I boost my creativity?",
"What are some tips for healthy eating?",
"How do self-driving cars function?",
"What's the best way to learn cooking?",
"How does the moon affect tides?",
"What are some fun science experiments?",
"How do I start a podcast?",
"What's the history of democracy?",
"How can I improve my drawing skills?",
"What are the benefits of journaling?",
"How does nuclear energy work?",
"What's the best way to plan a party?",
"How do I maintain a car properly?",
"What are some tips for traveling cheap?",
"How does the internet of things work?",
"What's the history of coffee?",
"How can I learn to code faster?",
"What are the benefits of team sports?",
"How do black holes form?",
"What's the best way to declutter my home?",
"How does machine learning differ from AI?",
"What are some tips for gardening?",
"How do I make a good first impression?",
"What's the history of the English language?",
"How can I stay productive working from home?",
"What are the benefits of learning history?",
"How does the human eye see color?",
"What's the best way to train for a marathon?",
"How do I start a blog?",
"What are some unusual animal facts?",
"How does sound travel through the air?",
"What's the history of fashion?",
"How can I improve my negotiation skills?",
"What are the benefits of mindfulness?",
"How do I build a simple website?",
"What's the best way to learn math?",
"How does evolution work?",
"What are some tips for reducing waste?",
"How do I choose a good wine?",
"What's the future of renewable energy?",
"What's the fastest way to learn a new skill?",
"How do neural networks mimic the human brain?",
"What are some quick and healthy lunch ideas?",
"Can you explain how NFTs function?",
"What's the climate like on Venus?",
"How can I take better smartphone photos?",
"What are the mental health benefits of exercise?",
"How do self-learning algorithms improve over time?",
"What's the history of social media?",
"Can you recommend underrated movies or TV shows?",
"Is there a scientific explanation for consciousness?",
"How do I brew the perfect cup of tea?",
"What are the newest breakthroughs in medicine?",
"How can I build a consistent workout routine?",
"What's the future of hydrogen-powered vehicles?",
"How do I create a successful online store?",
"What are some unique date night ideas?",
"Can you explain Schrödinger's cat in simple terms?",
"What's the most effective way to memorize vocabulary?",
"How do economic recessions happen?",
"What's the smartest way to invest in real estate?",
"How do I backpack through Asia on a budget?",
"What are the long-term impacts of deforestation?",
"How do Bluetooth connections work?",
"What's the evolution of animation in cinema?",
"How can I overcome stage fright?",
"What's the physics behind lightning?",
"How do I keep succulents alive indoors?",
"What happens if you don't drink enough water?",
"How do crypto wallets secure digital currency?",
"What's the cultural significance of tea worldwide?",
"How can I manage anxiety naturally?",
"What are the best sleep positions for back pain?",
"How do wind turbines generate power?",
"What's the secret to making fluffy pancakes?",
"How does the brain form habits?",
"What are the most underrated travel destinations?",
"How do I analyze a company's stock before investing?",
"Why do antibiotics not work on viruses?",
"What are some zero-waste lifestyle changes?",
"How did ancient civilizations influence modern sports?",
"What's the best way to house-train a puppy?",
"How does Pilates benefit the body?",
"Can you print human organs with 3D printers?",
"What's the fastest way to learn piano?",
"How do helicopters stay airborne?",
"What are some ways to overcome writer's block?",
"How does the body fight off a cold?",
"Will humans ever colonize Mars?",
"How can I stop procrastinating?",
"How does facial recognition technology work?",
"What are the ethical concerns around AI?",
"How do self-healing materials function?",
"What's the difference between 5G and 6G?",
"How do holograms work?",
"Can AI ever achieve human-like emotions?",
"What are the risks of genetic engineering?",
"How do lab-grown meats get produced?",
"What's the science behind time travel?",
"How do drones navigate autonomously?",
"What are the benefits of intermittent fasting?",
"How does the placebo effect work?",
"What's the best diet for longevity?",
"How do vaccines train the immune system?",
"What are the signs of burnout?",
"How does caffeine affect the brain?",
"What are the health risks of vaping?",
"Can meditation rewire the brain?",
"What's the link between gut health and mental health?",
"How does sleep deprivation impact the body?",
"What's the best passive income strategy?",
"How do credit scores work?",
"What are the risks of day trading?",
"How do startups get venture capital funding?",
"What's the future of remote work?",
"How do economic sanctions impact countries?",
"What's the psychology behind consumer spending?",
"How do inflation and deflation affect savings?",
"What are the best side hustles in 2024?",
"How do companies manipulate stock prices?",
"What's the safest way to travel solo?",
"How do I find cheap flight deals?",
"What are the most overrated tourist destinations?",
"How can I travel sustainably?",
"What's the best way to learn a language while traveling?",
"How do digital nomads manage visas?",
"What are the hidden gems in South America?",
"How do I pack efficiently for long-term travel?",
"What's the best travel insurance?",
"How do I avoid tourist scams abroad?",
"What's the secret to restaurant-quality sushi?",
"How do I make the perfect sourdough starter?",
"What are the healthiest cooking oils?",
"How does fermentation preserve food?",
"What's the science behind umami flavor?",
"How do I pair wine with food correctly?",
"What's the best way to grill vegetables?",
"How do I make dairy-free cheese?",
"What's the history of spices in global trade?",
"How do Michelin-star restaurants maintain quality?",
"What caused the fall of the Roman Empire?",
"How did ancient Egyptians build pyramids?",
"What was life like during the Black Plague?",
"How did the Silk Road shape civilizations?",
"What's the real story behind Cleopatra?",
"How did propaganda influence World War II?",
"What were the biggest misconceptions about Vikings?",
"How did the Renaissance change Europe?",
"What's the origin of Halloween traditions?",
"How did hip-hop culture evolve globally?",
"How do I build unshakable confidence?",
"What's the best morning routine for success?",
"How do I stop overthinking everything?",
"What's the science of habit formation?",
"How can I become more charismatic?",
"What's the best way to set and achieve goals?",
"How do I develop a growth mindset?",
"What's the Pomodoro Technique, and does it work?",
"How can I improve my emotional intelligence?",
"What's the key to mastering any skill quickly?",
"How do coral reefs support marine life?",
"What's being done to save endangered species?",
"How do wildfires start and spread?",
"What's the impact of plastic in the ocean?",
"How do bees contribute to the ecosystem?",
"What causes the Northern Lights?",
"How do tsunamis form?",
"What's the role of fungi in nature?",
"How do animals adapt to urban environments?",
"What's the future of sustainable farming?",
"What's the psychology behind viral TikTok trends?",
"How do movie special effects work?",
"What's the history of comic book superheroes?",
"How do streaming algorithms recommend shows?",
"What's the secret behind K-pop's global success?",
"How did memes become a cultural phenomenon?",
"What's the future of virtual influencers?",
"How do video game developers create immersive worlds?",
"What's the science behind ASMR?",
"How do celebrities manage their public image?",
"Is free will an illusion?",
"What defines human consciousness?",
"Can machines ever develop morality?",
"Does the universe have a purpose?",
"What's the nature of reality?",
"Is happiness a choice or a circumstance?",
"How do different cultures define success?",
"What's the meaning of art in society?",
"Can true altruism exist?",
"What happens after death, scientifically and spiritually?"
]

# Function to send API request
def send_chat_request(question):
    data = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

# Main bot loop
def run_chat_bot():
    print_banner()
    print("Starting automated chat bot...")
    available_questions = questions.copy()
    
    for i in range(100):
        if not available_questions:
            print("Ran out of questions unexpectedly!")
            break
        
        question = random.choice(available_questions)
        available_questions.remove(question)
        
        print(f"\nQuestion {i + 1}: {question}")
        answer = send_chat_request(question)
        print(f"Answer: {answer}")
        
        delay = random.uniform(60, 120)
        print(f"Waiting {delay:.1f} seconds before next question...")
        time.sleep(delay)
    
    print("\nCompleted 100 questions!")

# Run the bot
if __name__ == "__main__":
    run_chat_bot()
