import ultralytics
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor


def detect(source):

    ultralytics.checks()

    model = YOLO('best.pt')
    results = model.predict(source=source, conf=0.55)

    return results


if __name__ == '__main__':
    print(detect("captured_image.jpg"))
