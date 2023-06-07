import ultralytics
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor


def detect(source):

    ultralytics.checks()

    model = YOLO('best.pt') 
    # source = "upload an  image path"
    results = model.predict(source="captured_image.jpg", show=True, conf=0.55,save=True,project = "runs",name = "detect",save_txt=True )

    return results


if __name__ == '__main__':
    print(detect("captured_image.jpg"))
