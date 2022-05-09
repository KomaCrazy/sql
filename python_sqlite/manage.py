import sqlite3
from sqlite3 import Error
import datetime 
import pytesseract
import cv2
import numpy as np
import time
from threading import Thread
from PIL import Image
import os,os.path
import signal
import yaml
from yaml.loader import SafeLoader,FullLoader
import RPi.GPIO as GPIO

prox_pin = 3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(prox_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

img_frame = None
cmd_save = False
cur_img_no = 0

def get_filecount():
    DIR = 'prepare_img'
    return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])


def remove_entire_dir():# for remove file after job complete
    file_path = "prepare_img"
    for root, dirs, files in os.walk(file_path):
        for file in files:
            os.remove(os.path.join(root, file))
    print("Remove entire dir")


print("File count:",get_filecount())

def write_log(str_msg):
    f = open("logs.txt", "a")
    val_txt = str(get_clock()) + " => " + str_msg +  "\n"
    f.write(val_txt)
    f.close()
    print(val_txt)

#Car detection system ==================================================================================================>>>>>
def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    print(label)
    print(confidence)
    color = (0,0,255)
    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    cv2.imwrite("object-detection.jpg", img)
    """if (label == "truck" or label == "car" or label == "train") and confidence > 0.7:
        image = img
        image = image[y:y_plus_h, x:x_plus_w]
        result_txt = ""
        write_log(" Save image and data")
        with conn:
            _file = "backup_img/image"+str(get_date())+str(get_clock())+".jpg"
            task_1 = (str(get_date()), str(result_txt), str(get_date()),get_month(),get_year(), str(get_clock()), _file)

            try:
               cv2.imwrite(_file,image)
            except Exception as e:
               image = cv2.imread("object-detection.jpg")
               cv2.imwrite(_file,image)
               write_log(" Save with error")

            os.chmod(_file,0o777)
            create_task(conn, task_1)
            print("Success saved data")
            remove_entire_dir()
            state = True
            sec = 10
            for i in range(0,10):
                time.sleep(1)
                sec = sec - 1
                print("Finishing: ",sec)"""

scale = 0.00392
classes = None
with open('yolov3.txt', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

#Car detection system ==================================================================================================>>>>>
position_left = 750
position_top = 250
width = 512
height = 512
brightness = 40

def check_ipcam():
    for i in range (30,200):
        try:
            cam_url  = 'rtsp://admin:HUOLOV@192.168.2.'+str(i)+':554/H.264'
            cam = cv2.VideoCapture(cam_url)
            ret,frame = cam.read()
            cv2.imwrite(str(i)+".jpg",frame)
            return str(i)
        except Exception as e:
            print(e)

def get_config(): 
    global position_left,position_top,width,height,brightness
    with open("system_conf/config.yaml") as f:
         sys_conf = yaml.load(f,Loader=SafeLoader)
         brightness = sys_conf["brightness"]
         position_top = sys_conf["position_top"]
         position_left = sys_conf["position_left"]
         width = sys_conf["width"]
         height = sys_conf["height"]
         write_log("Get configuration")
    f.close()

ip_no = "55"
def get_img():
    global position_left,position_top,width,height,ip_no
    try:
       cam = cv2.VideoCapture('rtsp://admin:HUOLOV@192.168.2.'+ip_no+':554/H.264')
       ret,frame = cam.read()
       crop_img = frame[position_top:position_top+height, position_left:position_left+width]
       img_frame = crop_img
       cv2.imwrite("image.jpg",crop_img)
       cv2.imwrite("fullframe.jpg",frame)
       return crop_img
    except Exception as e:
       ip_no = check_ipcam()
       return crop_img
    
sql_create_data_table = """CREATE TABLE IF NOT EXISTS car_name_plate (
                                    id integer PRIMARY KEY,
                                    project_id integer NOT NULL,
                                    label text NOT NULL,
                                    date text NOT NULL,
                                    month text NOT NULL,
                                    year text NOT NULL,
                                    time text NOT NULL,
                                    image text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
try:
   con = sqlite3.connect('db/data.db')
except Exception as e:
   print("Creating database")
   create_db(r"db/data.db")

database = r"db/data.db"
conn = create_connection(database)

if conn is not None:
    create_table(conn, sql_create_data_table)
else:
    print("Error! cannot create the database connection.")

def get_date():
    current_date = datetime.datetime.now() 
    output = str(current_date)
    output = output.split()
    return output[0]

def get_month():
    current_date = datetime.datetime.now() 
    output = str(current_date)
    output = output.split()
    output = output[0]
    output = output.split("-")
    return output[1]

def get_year():
    current_date = datetime.datetime.now() 
    output = str(current_date)
    output = output.split()
    output = output[0]
    output = output.split("-")
    return output[0]

def get_clock():
    current_time = datetime.datetime.now() 
    output = str(current_time)
    output =  output.split()
    output = output[1]
    output = output.split('.',2)
    return output[0]

print("month:",get_month()," year:",get_year())

def get_text_img():
    #pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'#Comment when user on ubuntu linux
    image_file = 'image.jpg'
    output = pytesseract.image_to_string(Image.open(image_file), lang='tha').replace('','')
    data = output.replace('\n\x0c', ' ')
    data = data.replace('\n\n', ' ')
    data = data.replace('\n', ' ')
    return data

def create_task(conn, task):
    """CREATE TABLE IF NOT EXISTS car_name_plate (
                                    id integer PRIMARY KEY,
                                    project_id integer NOT NULL,
                                    label text NOT NULL,
                                    date text NOT NULL,
                                    month text NOT NULL,
                                    year text NOT NULL,
                                    time text NOT NULL,
                                    image text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    sql = ''' INSERT INTO car_name_plate(project_id,label,date,month,year,time,image)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

"""with conn:
   _file = "backup_img/image"+str(get_date())+str(get_clock())+".jpg"
   task_1 = (str(get_date()), str(result_txt), str(get_date()),get_month(),get_year(), str(get_clock()), _file)
   time.sleep(0.5)
   image = cv2.imread("image.jpg")
   cv2.imwrite(_file,image)
   os.chmod(_file,0o777)
   create_task(conn, task_1)
   print("Success saved data")"""

"""def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE project_id=?", (priority,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

with conn:
    print("1. Query task by priority:")
    select_task_by_priority(conn, 1)

    print("2. Query all tasks")
    select_all_tasks(conn)

cam.release()"""
#get_img(brightness)
def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)
signal.signal(signal.SIGINT, handler)

captured = False
state = True
new_h = int(720 / 2)
new_w = int(1080 / 2)

COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
#net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
conf_threshold = 0.7
nms_threshold = 0.2

def get_filecount():
    DIR = 'prepare_img'
    return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

def get_work_time():
    current_time = datetime.datetime.now() 
    output = str(current_time)
    output =  output.split()
    output = output[1]
    output = output.split(':',2)
    return output[0]

last_mills = 0
detect_count = 0
def check_detection():
    global last_mills,detect_count
    cur_mills  =  round(time.time() * 1000)
    if cur_mills - last_mills > 14000:
        last_mills = cur_mills
        detect_count = 0
        

print("running system")
while True:
    try:
        run_hours = int(get_work_time())
        """count = get_filecount()
        files = os.listdir("prepare_img")
        val_list = []
        for _name in files:
           _str = _name.split(".jpg")
           _num = int(_str[0])
           val_list.append(_num)
        if run_hours > 19:
            write_log(" Stand by mode end of running")
            time.sleep(60)"""
        
        """if run_hours > 0 and run_hours < 8:
            write_log(" Stand by mode before start running")
            time.sleep(60)
            remove_entire_dir()"""
        #if  run_hours > 7 and run_hours < 19:
        #cur_img_no = min(val_list)

        if  run_hours > 7 and run_hours < 20:
            try:
                state = GPIO.input(prox_pin)
                time.sleep(1)
                check_detection()
                if state == False:
                    print("Detected")
                    detect_count = detect_count + 1
                    print("Detected count:",detect_count)

                else:
                    print("Not detect")
                """class_ids = []
                confidences = []
                boxes = []
                write_log("Start car detection")
                image = get_img()
                write_log("read"+img_path)
                Height = image.shape[0]
                Width = image.shape[1]
                blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)
                net.setInput(blob)
                outs = net.forward(get_output_layers(net))
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.7:
                            center_x = int(detection[0] * Width)
                            center_y = int(detection[1] * Height)
                            w = int(detection[2] * Width)
                            h = int(detection[3] * Height)
                            x = center_x - w / 2
                            y = center_y - h / 2
                            class_ids.append(class_id)
                            confidences.append(float(confidence))
                            boxes.append([x, y, w, h])

                indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
                for i in indices:
                    i = i[0]
                    box = boxes[i]
                    x = box[0]
                    y = box[1]
                    w = box[2]
                    h = box[3]
                    draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))
                cv2.imwrite("resize.jpg",image)"""
                if detect_count >= 13:
                        with conn:
                            image = get_img()
                            _file = "backup_img/image"+str(get_date())+str(get_clock())+".jpg"
                            task_1 = (str(get_date()), "..", str(get_date()),get_month(),get_year(), str(get_clock()), _file)
                            cv2.imwrite(_file,image)
                            os.chmod(_file,0o777)
                            create_task(conn, task_1)
                            print("Success saved data")
                            remove_entire_dir()
                            state = True
                            sec = 37
                            for i in range(0,37):
                                time.sleep(1)
                                sec = sec - 1
                                print("Finishing: ",sec)
                                check_detection()
            except Exception as e:
                print(e)
        else:
            print("Out of time or No file to read")
            time.sleep(2)
    except Exception as e:
        pass