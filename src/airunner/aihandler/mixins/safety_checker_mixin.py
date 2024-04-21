import os
from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
from transformers import AutoFeatureExtractor
from airunner.enums import SignalCode, ModelStatus, ModelType
from airunner.settings import SD_FEATURE_EXTRACTOR_PATH
from airunner.utils.clear_memory import clear_memory


class SafetyCheckerMixin:
    def __init__(self, *args, **kwargs):
        self.safety_checker = None
        self.feature_extractor = None
        self.safety_checker_status = ModelStatus.UNLOADED
        self.feature_extractor_path = SD_FEATURE_EXTRACTOR_PATH

    @property
    def is_pipe_loaded(self) -> bool:
        if self.sd_request.is_txt2img:
            return self.txt2img is not None
        elif self.sd_request.is_img2img:
            return self.img2img is not None
        elif self.sd_request.is_pix2pix:
            return self.pix2pix is not None
        elif self.sd_request.is_outpaint:
            return self.outpaint is not None
        elif self.sd_request.is_depth2img:
            return self.depth2img is not None

    @property
    def pipe(self):
        try:
            if self.sd_request.is_txt2img:
                return self.txt2img
            elif self.sd_request.is_img2img:
                return self.img2img
            elif self.sd_request.is_outpaint:
                return self.outpaint
            elif self.sd_request.is_depth2img:
                return self.depth2img
            elif self.sd_request.is_pix2pix:
                return self.pix2pix
            else:
                self.logger.warning(f"Invalid action unable to get pipe")
                return None
        except Exception as e:
            self.logger.error(f"Error getting pipe {e}")
            return None

    @pipe.setter
    def pipe(self, value):
        if self.sd_request.is_txt2img:
            self.txt2img = value
        elif self.sd_request.is_img2img:
            self.img2img = value
        elif self.sd_request.is_outpaint:
            self.outpaint = value
        elif self.sd_request.is_depth2img:
            self.depth2img = value
        elif self.sd_request.is_pix2pix:
            self.pix2pix = value

    @property
    def model(self):
        path = self.settings["generator_settings"]["model"]
        if path == "":
            name = self.settings["generator_settings"]["model_name"]
            model = self.ai_model_by_name(name)
        else:
            model = self.ai_model_by_path(path)
        return model

    @property
    def model_path(self):
        if self.model is not None:
            return self.model["path"]

    @property
    def use_safety_checker(self):
        return self.settings["nsfw_filter"]

    @property
    def safety_checker_model(self):
        try:
            return self.models_by_pipeline_action("safety_checker")[0]
        except IndexError:
            return None

    @property
    def text_encoder_model(self):
        try:
            return self.models_by_pipeline_action("text_encoder")[0]
        except IndexError:
            return None

    def unload_safety_checker(self, data_: dict = None):
        self.safety_checker = None
        self.feature_extractor = None
        self.safety_checker_status = ModelStatus.UNLOADED
        self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
            "model": ModelType.SAFETY_CHECKER,
            "status": ModelStatus.UNLOADED,
            "path": "",
        })
        self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
            "model": ModelType.FEATURE_EXTRACTOR,
            "status": ModelStatus.UNLOADED,
            "path": "",
        })

    def load_safety_checker(self, data_: dict = None):
        if self.use_safety_checker and self.safety_checker is None and "path" in self.safety_checker_model:
            self.safety_checker = self.initialize_safety_checker()

        if self.use_safety_checker and self.feature_extractor is None and "path" in self.safety_checker_model:
            self.feature_extractor = self.load_feature_extractor()

    def unload_feature_extractor(self):
        self.feature_extractor = None
        clear_memory()
        self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
            "model": ModelType.FEATURE_EXTRACTOR,
            "status": ModelStatus.UNLOADED,
            "path": "",
        })

    def is_ckpt_file(self, model_path) -> bool:
        if not model_path:
            self.logger.error("ckpt path is empty")
            return False
        return model_path.endswith(".ckpt")

    def is_safetensor_file(self, model_path) -> bool:
        if not model_path:
            self.logger.error("safetensors path is empty")
            return False
        return model_path.endswith(".safetensors")


    def load_feature_extractor(self):
        feature_extractor = None
        self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
            "model": ModelType.FEATURE_EXTRACTOR,
            "status": ModelStatus.LOADING,
            "path": self.safety_checker_model["path"],
        })
        try:
            feature_extractor = AutoFeatureExtractor.from_pretrained(
                os.path.expanduser(
                    os.path.join(
                        self.settings["path_settings"]["feature_extractor_model_path"],
                        f"{self.feature_extractor_path}/preprocessor_config.json"
                    )
                ),
                local_files_only=True,
                torch_dtype=self.data_type,
                use_safetensors=True,
                device_map=self.device
            )
            self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.FEATURE_EXTRACTOR,
                "status": ModelStatus.LOADED,
                "path": self.safety_checker_model["path"],
            })
        except Exception as e:
            self.logger.error("Unable to load feature extractor")
            print(e)
            self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.FEATURE_EXTRACTOR,
                "status": ModelStatus.FAILED,
                "path": self.safety_checker_model["path"],
            })
        return feature_extractor

    def initialize_safety_checker(self):
        self.logger.debug(f"Initializing safety checker with {self.safety_checker_model}")
        safety_checker = None
        self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
            "model": ModelType.SAFETY_CHECKER,
            "status": ModelStatus.LOADING,
            "path": self.safety_checker_model["path"],
        })
        try:
            safety_checker = StableDiffusionSafetyChecker.from_pretrained(
                os.path.expanduser(
                    os.path.join(
                        self.settings["path_settings"]["safety_checker_model_path"],
                        "CompVis/stable-diffusion-safety-checker/"
                    )
                ),
                local_files_only=True,
                torch_dtype=self.data_type,
                use_safetensors=True,
                device_map=self.device
            )
            self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.SAFETY_CHECKER,
                "status": ModelStatus.LOADED,
                "path": self.safety_checker_model["path"],
            })
        except Exception as e:
            print(e)
            self.send_error("Unable to load safety checker")
            self.emit_signal(SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.SAFETY_CHECKER,
                "status": ModelStatus.FAILED,
                "path": "",
            })
        return safety_checker
