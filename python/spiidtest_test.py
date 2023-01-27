import speedtest   
  

st = speedtest.Speedtest() 
option = int(input('''
Выбери тип проверки:   

1 - Скорость скачивания   
2 - Скорость загрузки   
3 - Пинг

Твой выбор: ''')) 
  
  
if option == 1:   
    print(st.download())   
elif option == 2:  
    print(st.upload())   
elif option == 3:   
    servernames =[]   
    st.get_servers(servernames)   
    print(st.results.ping)     
else: 
    print("Пожалуйста, введите цифру от 1 до 3!")