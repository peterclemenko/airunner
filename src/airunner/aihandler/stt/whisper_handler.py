import os
import torch
from transformers import WhisperForConditionalGeneration
from transformers import WhisperProcessor
from transformers import WhisperFeatureExtractor
from airunner.aihandler.stt.stt_handler import STTHandler
from airunner.enums import SignalCode, ModelType, ModelStatus
from airunner.settings import DEFAULT_STT_HF_PATH


class WhisperHandler(STTHandler):
    """
    Handler for the Whisper model from OpenAI.
    """
    def stop_capture(self, data: dict):
        self.model = None
        self.processor = None
        self.feature_extractor = None
        super().stop_capture(data)
        self.emit_signal(
            SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.STT,
                "status": ModelStatus.UNLOADED,
                "path": ""
            }
        )
        self.emit_signal(
            SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.STT_PROCESSOR,
                "status": ModelStatus.UNLOADED,
                "path": ""
            }
        )
        self.emit_signal(
            SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.STT_FEATURE_EXTRACTOR,
                "status": ModelStatus.UNLOADED,
                "path": ""
            }
        )

    def load_model(self):
        self.logger.debug(f"Loading model")

        file_path = os.path.join(self.settings["path_settings"][f"stt_model_path"], DEFAULT_STT_HF_PATH)
        file_path = os.path.expanduser(file_path)
        file_path = os.path.abspath(file_path)
        self.emit_signal(
            SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.STT,
                "status": ModelStatus.LOADING,
                "path": file_path
            }
        )
        try:
            val = WhisperForConditionalGeneration.from_pretrained(
                file_path,
                local_files_only=True,
                torch_dtype=torch.bfloat16,
                device_map=self.device
            )
            self.emit_signal(
                SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                    "model": ModelType.STT,
                    "status": ModelStatus.LOADED,
                    "path": file_path
                }
            )
            return val
        except Exception as e:
            self.logger.error(f"Failed to load model")
            self.logger.error(e)
            self.emit_signal(
                SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                    "model": ModelType.STT,
                    "status": ModelStatus.FAILED,
                    "path": file_path
                }
            )
            return None

    def load_processor(self):
        self.logger.debug(f"Loading processor")
        file_path = os.path.join(self.settings["path_settings"][f"stt_model_path"], DEFAULT_STT_HF_PATH)
        file_path = os.path.expanduser(file_path)
        file_path = os.path.abspath(file_path)
        self.emit_signal(
            SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.STT_PROCESSOR,
                "status": ModelStatus.LOADING,
                "path": file_path
            }
        )
        try:
            val = WhisperProcessor.from_pretrained(
                file_path,
                local_files_only=True,
                torch_dtype=torch.bfloat16,
                device_map=self.device
            )
            self.emit_signal(
                SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                    "model": ModelType.STT_PROCESSOR,
                    "status": ModelStatus.LOADED,
                    "path": file_path
                }
            )
            return val
        except Exception as e:
            self.logger.error(f"Failed to load processor")
            self.logger.error(e)
            self.emit_signal(
                SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                    "model": ModelType.STT_PROCESSOR,
                    "status": ModelStatus.FAILED,
                    "path": file_path
                }
            )
            return None

    def load_feature_extractor(self):
        self.logger.debug(f"Loading feature extractor")
        file_path = os.path.join(self.settings["path_settings"][f"stt_model_path"], DEFAULT_STT_HF_PATH)
        file_path = os.path.expanduser(file_path)
        file_path = os.path.abspath(file_path)
        self.emit_signal(
            SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.STT_FEATURE_EXTRACTOR,
                "status": ModelStatus.LOADING,
                "path": file_path
            }
        )
        try:
            val = WhisperFeatureExtractor.from_pretrained(
                file_path,
                local_files_only=True,
                torch_dtype=torch.bfloat16,
                device_map=self.device
            )
            self.emit_signal(
                SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                    "model": ModelType.STT_FEATURE_EXTRACTOR,
                    "status": ModelStatus.LOADED,
                    "path": file_path
                }
            )
            return val
        except Exception as e:
            self.logger.error(f"Failed to load feature extractor")
            self.logger.error(e)
            self.emit_signal(
                SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                    "model": ModelType.STT_FEATURE_EXTRACTOR,
                    "status": ModelStatus.FAILED,
                    "path": file_path
                }
            )
            return None
