from flask import Flask, render_template 

zjw=Flask(__name__)

@zjw.route('/moban', methods=['GET','POST'])
def moban():
    data = {
        'name': '张家玮',
        'age':21,
        'mylist' : [1,2,3,4,5,6,7]
    }
    print(data)
    return render_template('moban.html',data=data)

def list_step(li):
    '''自定义过滤器'''
    return li[::2]

#注册过滤器 第一个值写自定义函数的名字 第二个值写你要用时候哦的名字
zjw.add_template_filter(list_step,'woc')


if __name__ == '__main__':
    zjw.run()