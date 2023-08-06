class ClassOne:
    """
    ClassOne คือตัวทดสอบสำหรับ การเรียนรู้
    โดยใน class ให้ทดสอบโดย เขียน code
    เพื่อแนะนำตัวเอง
    """

    def __init__(self):
        self.name = 'บาส'
        self.page = 'https://folygon3d.com/'

    def ShowName(self):
        print('สวัสดีฉันชื่อ {}'.format(self.name))

    def ShowPage(self):
        print(self.page)

    def About(self):
        text = """
        ----------------------------------------
        สวัสดีจ้า ผมชื่อบาส ทำอาชีพ 3D จ้า
        สามารถติดตามผลงานของ page ผมได้เลยนะครับ
        ตอนนี้ผมพึ่งฝึกเรียนโปรแกรม Python อยู่ครับ
        ----------------------------------------"""
        print(text)
 

if __name__ == '__main__' :
    My = ClassOne()
    My.ShowName()
    My.ShowPage()
    My.About()

