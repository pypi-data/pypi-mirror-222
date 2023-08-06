import dataclasses
import typing
import pathlib
import json
import torch
import torch.utils.data
import irisml.core


class Task(irisml.core.TaskBase):
    """Export OD detections to COCO file.

    The OD detections is a list of tensor, with each tensor row being [category_id, score, x, y, x, y] normalized.
    The JSON file is a list of dictionaries, each dictionary has key "image_id", "bbox" xywh normalized, "category_id", and "score". All indices are supposed to start from 1.
    """

    VERSION = '0.1.0'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset
        detections: typing.List[torch.Tensor]

    @dataclasses.dataclass
    class Config:
        filepath: pathlib.Path = 'detections.json'

    def execute(self, inputs):
        def _convert_bbox(bbox: list, w: int, h: int):
            return [bbox[0] * w, bbox[1] * h, (bbox[2] - bbox[0]) * w, (bbox[3] - bbox[1]) * h]

        dataset = inputs.dataset
        coco = []
        detections = [torch.tensor(d) for d in inputs.detections]

        for idx, dts_img in enumerate(detections):
            image = dataset[idx][0]
            w, h = (image.shape[1], image.shape[0]) if isinstance(image, torch.Tensor) else image.size
            for dt in dts_img:
                coco.append({
                    "category_id": int(dt[0].item()) + 1,
                    "image_id": idx + 1,
                    "bbox": _convert_bbox(dt[2:].tolist(), w, h),
                    "score": dt[1].item()
                })

        pathlib.Path(self.config.filepath).write_text(json.dumps(coco, indent=2))
        return self.Outputs()
