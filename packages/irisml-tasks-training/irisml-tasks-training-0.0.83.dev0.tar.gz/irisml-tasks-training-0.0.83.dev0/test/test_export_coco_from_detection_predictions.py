import unittest
import json
import tempfile
import pathlib
import PIL.Image
import torch
from irisml.tasks.export_coco_from_detection_predictions import Task


class FakeDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]


class TestExportCOCOFromDetectionPredictions(unittest.TestCase):
    def test_simple(self):
        width = height = 10
        od_dataset = FakeDataset([(PIL.Image.new('RGB', (width, height)), [[i, 0, 0, 0.5, 0.5]]) for i in range(2)])
        detections = [torch.tensor([[0, 0.9, 0, 0, 0.5, 0.5]], dtype=float), torch.tensor([[1, 0.2, 0, 0, 0.3, 0.3], [2, 0.1, 0.3, 0.3, 0.6, 0.6]], dtype=float)]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = pathlib.Path(temp_dir)
            filepath = temp_dir / 'detections.json'
            Task(Task.Config(filepath)).execute(Task.Inputs(dataset=od_dataset, detections=detections))
            coco = json.loads(filepath.read_text())
            self.assertDictEqual(coco[0], {"image_id": 1, "category_id": 1, "score": 0.9, "bbox": [0., 0., 5., 5.]})
            self.assertDictEqual(coco[1], {"image_id": 2, "category_id": 2, "score": 0.2, "bbox": [0., 0., 3., 3.]})
            self.assertDictEqual(coco[2], {"image_id": 2, "category_id": 3, "score": 0.1, "bbox": [3., 3., 3., 3.]})
