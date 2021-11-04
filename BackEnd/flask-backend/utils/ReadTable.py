import time

import happybase
import pandas as pd
from config import config
from tqdm import tqdm
import traceback


# from tqdm import tqdm


class LoadData():
    def __init__(self, conn, student="", course="", record=""):
        self.student = student
        self.course = course
        self.record = record
        self.conn = conn
        self.config = config
        self.count = 0

    def load(self):

        if isinstance(self.student, pd.core.frame.DataFrame) and self.student.shape[0] > 0:
            table = self.conn.table(self.config["table"]["student"])
            cols = self.student.columns.values
            self.insert(self.config["table"]["student"], table, cols)
        if isinstance(self.course, pd.core.frame.DataFrame) and self.course.shape[0] > 0:
            table = self.conn.table(self.config["table"]["course"])
            cols = self.course.columns.values
            self.insert(self.config["table"]["course"], table, cols)
        if isinstance(self.record, pd.core.frame.DataFrame) and self.record.shape[0] > 0:
            table = self.conn.table(self.config["table"]["record"])
            cols = self.record.columns.values
            self.insert(self.config["table"]["record"], table, cols)

    def insert(self, name, table, cols):
        if name=="student":
            data = self.student
        elif name == "record":
            data = self.record
        elif name == "course":
            data =self.course
        else:
            raise Exception("table name error!")
        for i in tqdm(range(data.shape[0])):
            key = str(data.iloc[i, 0])
            if name=="record":
                key= key + "-"+ str(data.iloc[i,1])
                start  = 2
            for col in range(data.shape[1]):
                self.count += 1
                if self.count % 10 == 0:
                    time.sleep(1)
                try:
                    path = self.config["name"][cols[col]]
                    val = str(data.iloc[i, col])
                    table.put(key, {path: val})
                except Exception as e:
                    e.with_traceback(traceback.print_exc())
                    print(key)
                    print(self.config["name"][cols[col]])
                    print(str(data.iloc[i, col]))

    def finish(self):
        self.conn.close()

if __name__ == '__main__':
    student = pd.read_csv("../data/student.csv")
    course = pd.read_csv("../data/course.csv")
    recode = pd.read_csv("../data/recoder.csv")
    conn = happybase.Connection("127.0.0.1", 9090)
    ld = LoadData(conn, student, course, recode)
    ld.load()
    print("finish")
