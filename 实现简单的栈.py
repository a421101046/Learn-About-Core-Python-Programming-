#!/usr/bin/env python

stack = []

def pushit():
    stack.append(raw_input('Enter new string: '))

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed [', stack.pop(), ']'

def viewstack():
    print str(stack)

def showmenu():
    prompt = """
	p(U)sh
	p(O)p
	(V)iew
	(Q)uit

	Enter choice: """

    done = 0
    while not done:

        chosen = 0
        while not chosen:
            try:
                choice = raw_input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'uovq':
                print 'invalid option, try again'
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'u': pushit()
        if choice == 'o': popit()
        if choice == 'v': viewstack()



if __name__ == '__main__':  
	showmenu()

# TODO  重写一遍


''' 
	1. 如果模块是被导入,__name__的值为模块名字  
	2. 如果模块是被直接执行,__name__的值为'__main__'
	
	3.可以在if __name__ == '__main__':   放一些调试的代码
'''