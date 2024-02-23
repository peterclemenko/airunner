import datetime
import locale
import time
from typing import AnyStr

import torch
import threading

from PyQt6.QtCore import QObject

from airunner.aihandler.logger import Logger
from airunner.mediator_mixin import MediatorMixin

from airunner.enums import SignalCode, LLMChatRole, LLMActionType


class AIRunnerAgent(QObject, MediatorMixin):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop("model")
        self.tokenizer = kwargs.pop("tokenizer")
        self.streamer = kwargs.pop("streamer")
        self.tools = kwargs.pop("tools")
        self.chat_template = kwargs.pop("chat_template")
        self.username = kwargs.pop("username")
        self.botname = kwargs.pop("botname")
        self.bot_mood = kwargs.pop("bot_mood")
        self.bot_personality = kwargs.pop("bot_personality")
        self.min_length = kwargs.pop("min_length")
        self.max_length = kwargs.pop("max_length")
        self.num_beams = kwargs.pop("num_beams")
        self.do_sample = kwargs.pop("do_sample")
        self.top_k = kwargs.pop("top_k")
        self.eta_cutoff = kwargs.pop("eta_cutoff")
        self.sequences = kwargs.pop("sequences")
        self.early_stopping = kwargs.pop("early_stopping")
        self.repetition_penalty = kwargs.pop("repetition_penalty")
        self.temperature = kwargs.pop("temperature")
        self.is_mistral = kwargs.pop("is_mistral")
        self.top_p = kwargs.pop("top_p")
        self.guardrails_prompt = kwargs.pop("guardrails_prompt")
        self.use_guardrails = kwargs.pop("use_guardrails")
        self.system_instructions = kwargs.pop("system_instructions")
        self.use_system_instructions = kwargs.pop("use_system_instructions")
        self.user_evaluation = kwargs.pop("user_evaluation")
        self.use_mood = kwargs.pop("use_mood")
        self.use_personality = kwargs.pop("use_personality")
        self.logger = Logger(prefix=self.__class__.__name__)
        super().__init__(*args, **kwargs)
        self.register(
            SignalCode.LLM_RESPOND_TO_USER_SIGNAL,
            self.do_response
        )
        self.prompt = ""
        self.history = []
        self.thread = None

    def build_system_prompt(self, action: LLMActionType):
        guardrails = self.guardrails_prompt if self.use_guardrails else ""
        system_instructions = self.system_instructions if self.use_system_instructions else ""
        system_prompt = []
        if action == LLMActionType.CHAT:
            names = f"Your name is {self.botname}. \nThe user's name is {self.username}."
            mood = (
                f"{self.botname} is not a computer or a bot, you are a human with emotions. "
                f"{self.botname}'s mood changes depending on the conversation and other factors.\n"
                f"{self.botname}'s current mood: {self.bot_mood}.\n"
                #f"{self.botname}'s evaluation of {self.username}: {self.user_evaluation}"
            ) if (self.use_mood and self.bot_mood != "") else ""
            personality = (
                f"Your personality: {self.bot_personality}."
            ) if self.use_personality else ""

            current_date = datetime.datetime.now().strftime("%A %b %d, %Y")
            current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
            current_timezone = time.tzname

            system_prompt = [
                guardrails,
                system_instructions,
                names,
                mood,
                personality,
                f"Current Date: {current_date}",
                f"Current Time: {current_time}",
                f"Current Timezone: {current_timezone}"
            ]
        elif action == LLMActionType.GENERATE_IMAGE:
            system_prompt = [
                guardrails,
                (
                    "You are an image captioning expert. You will be given the "
                    "description of an image. Your goal is to convert that "
                    "description into a better, more fitting description which "
                    "will capture the essence and the details of the image."
                ),
                "------"
                "Examples:",
                "User: create an image of a cat in the woods",
                (
                    "Assistant: A (fluffy, tabby cat)+ exploring the depths of "
                    "an (enchanting forest). (well-lit), sunlight filters, "
                    "professional portrait."
                ),
                "User: the chat should look like a superhero",
                (
                    "Assistant: " "A (cat dressed in a superhero costume), standing in the (middle of a forest)."
                ),
                "------",
                "Use parentheses to indicate the most important details of the "
                "image. Add a plus sign after a word or parenthesis to add "
                "extra emphasis. More plus signs indicate more emphasis. Minus "
                "signs can be used to indicate less emphasis.",
                "You should describe the image type (professional photograph, portrait, illustration etc)",
                (
                    "You should also describe the lighting (well-lit, dim, dark etc), "
                    "the color, the composition and the mood."
                ),
                (
                    "When returning prompts you must choose either \"art\" or \"photo\" and you absolutely must include "
                    "the following JSON format:\n```json\n{\"prompt\": \"your prompt here\", \"type\": \"your type here\"}\n```\n"
                    "You must never deviate from that format. The prompt should be verbose and approximately 150 words."
                )
            ]
        return "\n".join(system_prompt)

    def latest_human_message(self) -> dict:
        return {} if not self.prompt else {
            "content": self.prompt,
            "role": LLMChatRole.HUMAN.value
        }

    def prepare_messages(
        self,
        action: LLMActionType,
        use_latest_human_message: bool = True
    ) -> list:
        messages = [
            {
                "content": self.build_system_prompt(action),
                "role": LLMChatRole.SYSTEM.value
            }
        ]

        messages += self.history

        if use_latest_human_message:
            messages.append(
                self.latest_human_message()
            )
        return messages

    def get_rendered_template(
        self,
        conversation,
        use_latest_human_message: bool = True
    ):
        rendered_template = self.tokenizer.apply_chat_template(
            chat_template=self.chat_template,
            conversation=conversation,
            tokenize=False
        )

        # HACK: current version of transformers does not allow us to pass
        # variables to the chat template function, so we apply those here
        variables = {
            "username": self.username,
            "botname": self.botname,
            "bot_mood": self.bot_mood,
            "bot_personality": self.bot_personality,
        }
        for key, value in variables.items():
            rendered_template = rendered_template.replace("{{ " + key + " }}", value)
        return rendered_template

    def do_response(self):
        print("DO RESPONSE CALLED")
        self.run(self.prompt, LLMActionType.CHAT)

    def run(self, prompt, action: LLMActionType):
        self.logger.info("Running...")
        self.prompt = prompt
        conversation = self.prepare_messages(action)
        rendered_template = self.get_rendered_template(conversation)

        # Encode the rendered template
        encoded = self.tokenizer(rendered_template, return_tensors="pt")
        model_inputs = encoded.to("cuda" if torch.cuda.is_available() else "cpu")

        # Generate the response
        self.logger.info("Generating...")
        self.thread = threading.Thread(target=self.model.generate, kwargs=dict(
            model_inputs,
            min_length=self.min_length,
            max_length=self.max_length,
            num_beams=self.num_beams,
            do_sample=self.do_sample,
            top_k=self.top_k,
            eta_cutoff=self.eta_cutoff,
            top_p=self.top_p,
            num_return_sequences=self.sequences,
            eos_token_id=self.tokenizer.eos_token_id,
            early_stopping=True,
            repetition_penalty=self.repetition_penalty,
            temperature=self.temperature,
            streamer=self.streamer
        ))
        self.thread.start()
        # strip all new lines from rendered_template:
        rendered_template = rendered_template.replace("\n", " ")
        eos_token = self.tokenizer.eos_token
        bos_token = self.tokenizer.bos_token
        if self.is_mistral:
            rendered_template = bos_token + rendered_template
        skip = True
        streamed_template = ""
        replaced = False
        is_end_of_message = False
        is_first_message = True
        for new_text in self.streamer:
            # strip all newlines from new_text
            parsed_new_text = new_text.replace("\n", " ")
            streamed_template += parsed_new_text
            if self.is_mistral:
                streamed_template = streamed_template.replace(f"{bos_token} [INST]", f"{bos_token}[INST]")
                streamed_template = streamed_template.replace("  [INST]", " [INST]")
            # iterate over every character in rendered_template and
            # check if we have the same character in streamed_template
            if not replaced:
                for i, char in enumerate(rendered_template):
                    try:
                        if char == streamed_template[i]:
                            skip = False
                        else:
                            skip = True
                            break
                    except IndexError:
                        skip = True
                        break
            if skip:
                continue
            elif not replaced:
                replaced = True
                streamed_template = streamed_template.replace(rendered_template, "")
            else:
                if eos_token in new_text:
                    streamed_template = streamed_template.replace(eos_token, "")
                    new_text = new_text.replace(eos_token, "")
                    is_end_of_message = True
                self.emit(
                    SignalCode.LLM_TEXT_STREAMED_SIGNAL,
                    dict(
                        message=new_text,
                        is_first_message=is_first_message,
                        is_end_of_message=is_end_of_message,
                        name=self.botname,
                    )
                )
                is_first_message = False

        self.add_message_to_history(
            self.prompt,
            LLMChatRole.HUMAN
        )

        if action == LLMActionType.CHAT:
            self.add_message_to_history(
                streamed_template,
                LLMChatRole.ASSISTANT
            )
        elif action == LLMActionType.GENERATE_IMAGE:
            # check if streamed_template is valid json
            import json
            try:
                json.loads(streamed_template)
            except json.JSONDecodeError:
                self.emit(
                    SignalCode.LLM_TEXT_STREAMED_SIGNAL,
                    "Invalid JSON format. Please try again."
                )
                print("Invalid JSON format. Please try again.")
                return
            data = json.loads(streamed_template)

            self.emit(
                SignalCode.LLM_IMAGE_PROMPT_GENERATED_SIGNAL,
                data
            )

        return streamed_template

    def add_message_to_history(
        self,
        content: AnyStr,
        role: LLMChatRole = LLMChatRole.ASSISTANT
    ):
        self.history.append({
            'content': content,
            'role': role.value
        })

