from transformers import pipeline

class ModelManager:
    def __init__(self):
        self.models = {
            "bert-base": pipeline("text-classification", model="bert-base-uncased"),
            "roberta": pipeline("text-classification", model="roberta-base"),
            "distilbert": pipeline("text-classification", model="distilbert-base-uncased"),
            "albert": pipeline("text-classification", model="albert-base-v2"),
            "xlnet": pipeline("text-classification", model="xlnet-base-cased"),
            "t5-small": pipeline("summarization", model="t5-small"),
            "t5-base": pipeline("summarization", model="t5-base"),
        }

    def evaluate(self, text, task):
        results = {}
        for name, model in self.models.items():
            if task == "text-classification":
                results[name] = model(text)
            elif task == "ner":
                results[name] = model(text)
            elif task == "question-answering":
                results[name] = model(question=text)
            elif task == "summarization":
                results[name] = model(text)
        return results

    def benchmark(self, dataset):
        pass
