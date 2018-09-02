# apppub.yong.comfunc
import time
import re

# getTimeStr  http://www.runoob.com/python/att-time-strftime.html

def getTimeStr(mode=0):
    if mode == 0:
        return time.strftime("%Y/%m/%d %I:%M:%S %p", time.localtime())
    if mode == 1:
        return time.strftime("%b %d,%Y %I:%M:%S %p", time.localtime())
    if mode == 2:
        return time.strftime("%Y/%m/%d",time.localtime())

def checkEmail(email):
    Len = len(email)
    if Len <= 0: return "Email can not be blank! "
    if Len <= 3: return "Email must be 3+ characters! "
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if re.match(EMAIL_REGEX, email): return ''
    return "Invalid email address! "

def setPostOnce(request):
    rs = request.session
    key = 'post_once'
    rs[key] = True

def addPostOnce(request):
    rs = request.session
    key = 'post_once'
    counter = 'post_counter'
    rs[key] = True
    rs[counter] += 1

def checkPostOnce(request, counter_init_val=0, counter_init=True, session_init=False):
    rs = request.session
    key = 'post_once'
    counter = 'post_counter'
    if counter not in rs:
        rs[counter] = counter_init_val
    if key in rs and rs[key]:
        rs[key] = False
        return True
    else:
        rs[key] = False
        if session_init:
            old = counter_init_val
            if counter in rs:
                old = rs[counter]
            rs.clear()
            rs[key] = False
            rs[counter] = old
        if counter_init:
            rs[counter] = counter_init_val
        return False

def initSession(request, keys=[]):
    for key in keys:
        request.session[key] = ''

def cpySession(request, keys):
    for key in keys:
        request.session[key] = ''
        if key in request.POST and request.method=='POST':
            request.session[key]=request.POST[key]

def clearSession(request):
    rs = request.session
    rs.clear()

def nullSessionDicts(request, dictskey='dicts'):
    rs = request.session
    rs[dictskey] = []

def addSessionDicts(request, keys=[],  posttime='', dictskey='dicts'):
    form = request.POST
    rs = request.session
    dicts = []
    if dictskey in rs:
        dicts = rs[dictskey]
    dict = {}
    for key in keys:
        val = ''
        if key in form:
            val = form[key]
        dict[key] = val
    if dict != {}:
        if posttime != '':
            dict['posttime'] = posttime
        dicts.append(dict)
        rs[dictskey] = dicts

def resetSessionDicts(request, key, val0, val1):
    dicts = request.session['dicts']
    for dict in dicts:
        if dict[key] == val0:
            dict[key] = val1

def showSessionDicts(request, dictskey = 'dicts'):
    print(request.session[dictskey])

def show(val):
    print('hi', val)

def show_post(request):
    for key in request.POST:
        print(key, request.POST[key])

def showQry(rcds, keys=[]):
    dicts = rcds.values()
    for dict in dicts:
        for key, val in dict.items():
            if keys == [] or key in keys:
                print(val, end=',  ')
        print('', end='|')
    print('')

def showCls(cls, keys=[]):
    print('\n--------- ' + cls.__name__ + ' ---------')
    showQry(cls.objects.all(), keys)

def qryStr(rcds, title=''):
    txt = ''
    if title != '': txt = title+'\n'
    arr = rcds.values()
    for dict in arr:
        for key, val in dict.items():
            txt += str(key) + ":" + str(val) + ',  '
        txt += ' |  '
    return txt

def clsStr(cls, title = ''):
    return qryStr(cls.objects.all(), title)


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class CustomNode(object):
    def __init__(self,val,*bonus):
        self.val = val
        self.next = None
        self.bonus = bonus

class LinkedList(object):
    def __init__(self):
      self.head = None
    def addNode(self, val, *extras):
        if not self.head:
            if extras:
                self.head = CustomNode(val, extras)
            else:
                self.head = ListNode(val)
            return self
        current = self.head
        while current.next:
            current = current.next
        if extras:
            current.next = CustomNode(val,extras)
        else:
            current.next = ListNode(val)
        return self

def test_LL():
    myList = LinkedList()
    myList.addNode(72, "hello world", "banana").addNode(45).addNode(21, "Yay")
    print(myList)
    print(myList.head.val)
    print(myList.head.next)
    print(myList.head.next.next.bonus)


