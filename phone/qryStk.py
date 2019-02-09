import webbrowser
import stklib
import sys
if sys.platform == 'ios':
        import ui        
        class MyView(ui.View):
                def will_close(self):
                        webbrowser.open("shortcuts:")
        def view(text):
                v=MyView()
                wv = ui.WebView()
                v.add_subview(wv)
                wv.load_html(text)
                v.frame = (0,0,400,568)
                wv.frame = (0,0,400,568)
                v.present()
else:
        import webview
        import threading
		
#print(sys.argv)
  
h1='''
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">
</script>
<script>
function stkQry(){
    $(".salTy").each(function(){
        if ($(this).text()=='賣'){
	    $(this).css("background-color","orange");
	    $(this).siblings().css("background-color","orange");
	}else{
	    $(this).css("background-color","white");
	    $(this).siblings().css("background-color","white");
	}
    });
}
</script>
</head>
<body onload="stkQry()">
<p><span id="mainContent">
'''

e1='''
</span></p>
</body>
'''

if sys.platform == 'ios':
        content=h1+stklib.qry(sys.argv[1],sys.argv[2],sys.argv[3])+e1
        view(content)
else:
        content=h1+stklib.qry('stk','2548','stk,dtdat')+e1
        def load_html():
                webview.load_html(content)
        t = threading.Thread(target=load_html)
        t.start()
        webview.create_window('Load HTML Example')
#print('邵世昌')
#webbrowser.open("shortcuts://?name=eric")
#f=open("helloworld.html","w",encoding="UTF-8")
#s=webdict.stk.qry('2548')
#f.write(s)
#f.close()
#webbrowser.open("safari-helloworld.html")
#view(h1+stk.qry('2548')+e1)

