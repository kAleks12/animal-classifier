import logging
import os
import re

from ultralytics import YOLO

from src.server.model.image_classification import TagsDTO
from src.utils.config_parser import parser

__yolo_old_run_path = parser.get_attr('yolo', 'old_run_path')
__yolo_labels_path = parser.get_attr('yolo', 'labels_path')
__input_img_data_path = parser.get_attr('yolo', 'img_data_path')

logger = logging.getLogger('ImageClassificationService')

try:
    os.remove(__yolo_old_run_path)
except WindowsError as e:
    logger.error(e)
__model = YOLO(parser.get_attr('yolo', 'model_weights'))


def classify(image_file: any) -> TagsDTO:
    content = image_file.file.read()
    full_path = __input_img_data_path + image_file.filename
    with open(full_path, 'wb') as file:
        file.write(content)

    __model(full_path, save_txt=True, imgsz=640)
    os.remove(full_path)

    return TagsDTO(tags=_parse_labels(image_file.filename))


def _parse_labels(image_name: str) -> list[str]:
    image_name = re.sub(rf'\..*', '.txt', image_name)
    full_path = "".join(__yolo_labels_path + image_name)

    with open(full_path) as file:
        mapped_labels = {}
        for line in file.readlines():
            split_line = line.split()
            mapped_labels[split_line[1]] = float(split_line[0])

        results = [mapped_label[0] for mapped_label in mapped_labels.items() if mapped_label[1] > 0.0]

    return results
