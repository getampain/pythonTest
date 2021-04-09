import win32com.client

#com이라는 윈도우 전용 기능을 사용한 파트이다

#com을 통해서 다른언어로 구성된 프로그램을 연결하고 활성화한다.
explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True