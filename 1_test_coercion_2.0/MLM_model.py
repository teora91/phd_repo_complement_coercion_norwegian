from transformers import AutoModelForCausalLM, AutoModelForMaskedLM, AutoTokenizer

class MLMHeadModel:

    def __init__(self, model_name):
        # Initialize the model and the tokenizer.
        self.model = AutoModelForMaskedLM.from_pretrained(model_name, trust_remote_code=True).to("cuda")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # self.model.eval()  # Set the model to evaluation mode

        self.model_name = model_name


