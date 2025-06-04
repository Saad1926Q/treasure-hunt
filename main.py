from ultralytics import YOLO
import random
import cv2

model = YOLO("yolov8n.pt")
model.to("cuda")

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

all_objects=model.names

# The classes which we will be using for our game

game_item_mappings = {
    0: "person",
    1: "bicycle",
    2: "car",
    5: "bus",
    9: "traffic light",
    10: "fire hydrant",
    11: "stop sign",
    13: "bench",
    24: "backpack",
    25: "umbrella",
    26: "handbag",
    28: "suitcase",
    32: "sports ball",
    36: "skateboard",
    38: "tennis racket",
    39: "bottle",
    41: "cup",
    45: "bowl",
    46: "banana",
    47: "apple",
    48: "sandwich",
    49: "orange",
    50: "broccoli",
    51: "carrot",
    53: "pizza",
    54: "donut",
    55: "cake",
    56: "chair",
    57: "couch",
    58: "potted plant",
    60: "dining table",
    62: "tv",
    63: "laptop",
    65: "remote",
    67: "cell phone",
    73: "book",
    74: "clock",
    75: "vase",
    77: "teddy bear",
    79: "toothbrush"
}


game_items=list(game_item_mappings.values())

# results=model("testing.mp4",stream=True)


score=0
total=0
quit=False
selected=False
prev_targets=set()

count=1

while True:
    if total==5:
        break

    while selected==False:
        target=random.choice(game_items)
        while target in prev_targets:
            target=random.choice(game_items)
        prev_targets.add(target)
        selected=True


    cam.grab()
    ret, frame = cam.read()
    
    if not ret:
        continue

    result = model(frame, imgsz=320)
    annotated = result[0].plot()

    
    boxes=result[0].boxes
    for i,box in enumerate(boxes):
        class_id=int(box.cls.item())
        if all_objects[class_id]==target:
            print(f"Found {target}")
            cv2.putText(
                annotated,             
                f"Found {target}",                   
                (10, 30),                
                cv2.FONT_HERSHEY_SIMPLEX,
                1,                        
                (0, 255, 0),                
                2                           
            )
            selected=False
            score+=1
            total+=1
            break
    

    if total==5:
        cv2.putText(
            annotated,
            f"You got a score of {score}/{total}",
            (10, 470),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

    else:
        if selected==True:
            cv2.putText(
                annotated,
                f"Find: {target}",
                (10, 470),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )
    
    if count==1:
        cv2.putText(
            annotated,
            "Press 'g' to give up | Press 'q' to quit",
            (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, 
            (0, 255, 255),
            2
        )


    cv2.imshow("YOLO Inference", annotated)


    count+=1

    if selected==True and cv2.waitKey(10) & 0xFF==ord('g'): #Gave Up
        total+=1
        selected=False
        continue

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

print(f"Final Score: {score}/{total}")
cam.release()
cv2.destroyAllWindows()

'''

for result in results:
    boxes=result.boxes
    for i,box in enumerate(boxes):
        class_id=box.cls[i].item()
        print(f"predicted {class_id_mappings[class_id]}")
    break

'''
