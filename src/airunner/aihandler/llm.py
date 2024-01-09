import torch
import traceback

from airunner.aihandler.transformer_runner import TransformerRunner
from airunner.aihandler.logger import Logger
from airunner.aihandler.enums import MessageCode
import os
from jinja2 import Environment, FileSystemLoader

from transformers.pipelines.conversational import Conversation


class LLM(TransformerRunner):
    def clear_conversation(self):
        if self.generator.name == "casuallm":
            self.chain.clear()
    
    def do_generate(self, data):
        Logger.info("Generating with LLM")
        self.process_data(data)
        self.handle_request()
        self.requested_generator_name = data["request_data"]["generator_name"]
        prompt = data["request_data"]["prompt"]
        model_path = data["request_data"]["model_path"]
        return self.generate(
            # app=self.app,
            # endpoint=data["request_data"]["generator_name"],
            # prompt=prompt, 
            # model=model_path,
            # stream=data["request_data"]["stream"],
            # images=[data["request_data"]["image"]],
        )
    
    history = []

    def generate(self):
        # Create a FileSystemLoader object with the directory of the template
        HERE = os.path.dirname(os.path.abspath(__file__))
        file_loader = FileSystemLoader(os.path.join(HERE, "chat_templates"))

        # Create an Environment object with the FileSystemLoader object
        env = Environment(loader=file_loader)

        # Load the template
        # Load the template
        chat_template = env.get_template('chat.j2')

        prompt = self.prompt
        if prompt is None or prompt == "":
            traceback.print_stack()
            return
        
        if self.generator.name == "casuallm":
            history = []
            for message in self.history:
                if message["role"] == "user":
                    history.append("[INST]" + self.username + ': "'+ message["content"] +'"[/INST]')
                else:
                    history.append(self.botname + ': "'+ message["content"] +'"')
            history = "\n".join(history)
            if history == "":
                history = None

            # Create a dictionary with the variables
            variables = {
                "username": self.username,
                "botname": self.botname,
                "history": history,
                "input": prompt,
                "bos_token": self.tokenizer.bos_token,
                "botmood": "angry. He hates " + self.username
            }

            self.history.append({
                "role": "user",
                "content": prompt
            })

            # Render the template with the variables
            rendered_template = chat_template.render(variables)
            #print(rendered_template)

            # Encode the rendered template
            encoded = self.tokenizer.encode(rendered_template, return_tensors="pt")

            model_inputs = encoded.to("cuda" if torch.cuda.is_available() else "cpu")

            # Generate the response
            generated_ids = self.model.generate(
                model_inputs,
                min_length=0,
                max_length=1000,
                num_beams=1,
                do_sample=True,
                top_k=20,
                eta_cutoff=10,
                top_p=1.0,
                num_return_sequences=self.sequences,
                eos_token_id=self.tokenizer.eos_token_id,
                early_stopping=True,
                repetition_penalty=1.15,
                temperature=0.7,
            )

            # Decode the new tokens
            decoded = self.tokenizer.batch_decode(generated_ids)[0]
            decoded = decoded.replace(self.tokenizer.batch_decode(model_inputs)[0], "")
            decoded = decoded.replace("</s>", "")

            # Extract the actual message content
            start_index = decoded.find('"') + 1
            end_index = decoded.rfind('"')
            decoded = decoded[start_index:end_index]

            self.history.append({
                "role": "assistant",
                "content": decoded
            })

            # print(self.history)

            # print("*"*80)
            # print(decoded)

            #return decoded
            self.engine.send_message(decoded, code=MessageCode.TEXT_GENERATED)
        elif self.generator.name == "visualqa":
            inputs = self.processor(
                self.image, 
                prompt, 
                return_tensors="pt"
            ).to("cuda")
            out = self.model.generate(
                **inputs
            )

            answers = []
            for res in out:
                answer = self.processor.decode(
                    res,
                    skip_special_tokens=True
                )
                answers.append(answer.strip().lower())
            return answers
        else:
            Logger.error(f"Failed to call generator for {self.generator.name}")
        # self.llm_api.request(**kwargs)
