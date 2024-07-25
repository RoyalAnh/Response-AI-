# Speech analysis
import nltk
from nltk.tokenize import word_tokenize  # tách văn bản thành từ 
from nltk.tag import pos_tag  # gắn nhãn phân loại cú pháp (phân loại N, V, adj)
from nltk.corpus import wordnet  # từ đồng nghĩa 
# tải các tài nguyên ngôn ngữ để sử dụng 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def process_text(text):
    """
    Xử lý và phân tích cú pháp của văn bản đầu vào.
    
    Parameters:
    - text (str): Văn bản cần xử lý.
    
    Returns:
    - tokens (list): Danh sách các từ trong văn bản.
    - tagged_tokens (list): Danh sách các từ đã được gắn nhãn phân loại cú pháp.
    """
    tokens = word_tokenize(text)  # Tách văn bản thành các từ
    tagged_tokens = pos_tag(tokens)  # Gắn nhãn phân loại cú pháp cho các từ
    return tokens, tagged_tokens

def analyze_command(tagged_tokens, text):
    """
    Phân tích và hiểu lệnh từ người dùng dựa trên các từ đã gắn nhãn phân loại cú pháp.
    
    Parameters:
    - tagged_tokens (list): Danh sách các từ đã được gắn nhãn phân loại cú pháp.
    - text (str): Văn bản gốc để kiểm tra các biến thể.
    
    Returns:
    - action (str): Hành động cần thực hiện dựa trên lệnh của người dùng.
    """
    keywords = {
        "move": ["forward", "backward", "left", "right"],
        "turn": ["left", "right"],
        "stop": ["stop", "halt"],
        "go": ["ahead", "straight"],
        "run": ["fast", "quickly"],
        "walk": ["slow", "slowly"]
    }
    
    for token in tagged_tokens:
        word = token[0].lower()
        if word in keywords.keys():
            for action, variations in keywords.items():
                if word == action:
                    for variation in variations:
                        if variation in text.lower():
                            action = f"{action} {variation}"
                            return action
            return word
    else:
        return "unknown"

def get_synonyms(word):
    """
    Lấy các từ đồng nghĩa của một từ từ WordNet.
    
    Parameters:
    - word (str): Từ cần tìm đồng nghĩa.
    
    Returns:
    - synonyms (list): Danh sách các từ đồng nghĩa.
    """
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def expand_command(action):
    """
    Mở rộng hành động thành các biến thể để tăng khả năng nhận diện.
    
    Parameters:
    - action (str): Hành động cần mở rộng.
    
    Returns:
    - expanded_actions (list): Danh sách các hành động mở rộng.
    """
    expanded_actions = [action]
    words = action.split()
    for word in words:
        synonyms = get_synonyms(word)
        for synonym in synonyms:
            expanded_actions.append(action.replace(word, synonym))
    return expanded_actions

def module3():
    with open("recognized_text.txt", "r") as f:
        text = f.read()
    tokens, tagged_tokens = process_text(text)
    
    action = analyze_command(tagged_tokens, text)
    
    expanded_actions = expand_command(action)

    with open("processed_text.txt", "w") as f:
        f.write(f"Processed tokens: {tokens}\n")
        f.write(f"Tagged tokens: {tagged_tokens}\n")
        f.write(f"Action to perform: {action}\n")
        f.write(f"Expanded actions: {expanded_actions}\n")
    
    print(f"Processed tokens: {tokens}")
    print(f"Tagged tokens: {tagged_tokens}")
    print(f"Action to perform: {action}")
    print(f"Expanded actions: {expanded_actions}")

'''CC: Coordinating conjunction

CD: Cardinal number

DT: Determiner

EX: Existential there

FW: Foreign word

IN: Preposition or subordinating conjunction

JJ: Adjective

VP: Verb Phrase

JJR: Adjective, comparative

JJS: Adjective, superlative

LS: List item marker

MD: Modal

NN: Noun, singular or mass

NNS: Noun, plural

PP: Preposition Phrase

NNP: Proper noun, singular Phrase

NNPS: Proper noun, plural

PDT: Pre determiner

POS: Possessive ending

PRP: Personal pronoun Phrase

PRP: Possessive pronoun Phrase

RB: Adverb

RBR: Adverb, comparative

RBS: Adverb, superlative

RP: Particle

S: Simple declarative clause

SBAR: Clause introduced by a (possibly empty) subordinating conjunction

SBARQ: Direct question introduced by a wh-word or a wh-phrase.

SINV: Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal.

SQ: Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ.

SYM: Symbol

VBD: Verb, past tense

VBG: Verb, gerund or present participle

VBN: Verb, past participle

VBP: Verb, non-3rd person singular present

VBZ: Verb, 3rd person singular present

WDT: Wh-determiner

WP: Wh-pronoun

WP: Possessive wh-pronoun

WRB: Wh-adverb'''
