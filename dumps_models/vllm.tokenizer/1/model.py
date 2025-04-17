import os
from typing import Dict, List

import numpy as np
import triton_python_backend_utils as pb_utils
from transformers import AutoTokenizer, PreTrainedTokenizer, TensorType

class TritonPythonModel:
    tokenizer: PreTrainedTokenizer

    def initialize(self, args: Dict[str, str]) -> None:
        """
        Initialize the tokenization process
        :param args: arguments from Triton config file
        """
        # more variables in https://github.com/triton-inference-server/python_backend/blob/main/src/python.cc
        path: str = os.path.join(args["model_repository"], args["model_version"])
        self.tokenizer = AutoTokenizer.from_pretrained(path)

    def execute(self, requests) -> "List[List[pb_utils.Tensor]]":
        """
        Parse and tokenize each request
        :param requests: 1 or more requests received by Triton server.
        :return: text as input tensors
        """
        responses = []
        # for loop for batch requests (disabled in our case)
        for request in requests:
            # binary data typed back to string
            texts = [
                t.decode("UTF-8")
                for t in pb_utils.get_input_tensor_by_name(request, "text_input")
                .as_numpy()
                .tolist()
            ]
            print(f"Received text: {texts}")
            text_templates = []
            for text in texts:
                chat_template = [{"role": "user", "content": text}]
                chat_template = self.tokenizer.apply_chat_template(chat_template, tokenize=False)
                text_templates.append(chat_template)
            print(f"Tokenized text: {text_templates}")
            # communicate the tokenization results to Triton server
            outputs = [
                pb_utils.Tensor("text_template", np.array(text_templates, dtype=object)),
            ]
            inference_response = pb_utils.InferenceResponse(output_tensors=outputs)
            responses.append(inference_response)

        return responses