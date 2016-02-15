def main():
	a=raw_input('enter:')
	try:
		assert int(a)==1,'Assert error'
	except AssertionError,e:
		print e
	except ValueError,e:
		print e,' : ',e.__class__
	else:
		print 'Else : no problem.'
	finally:
		print 'Done!'
if __name__ == '__main__':
    main()
