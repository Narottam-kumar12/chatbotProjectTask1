from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

class ModelLoader:
    def __init__(self, model_name="google/flan-t5-base"):
        self.model_name = model_name

    def load(self):
        # Load tokenizer and model from Hugging Face
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        # Create text2text-generation pipeline (instruction-based)
        generator = pipeline(
            "text2text-generation",
            model=model,
            tokenizer=tokenizer,
            device_map="auto"  # Use Apple M2's Metal Performance Shaders (MPS) if available
        )
        return generator