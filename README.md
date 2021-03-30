 # zerodha

Install all dependency package os(linux)

  >> sudo apt-get install python3-pip,redis-server
  
  >> sudo pip3 install virtualenv
 
Pull the code from the repo.

  >> cd /usr/local/src/

  >> sudo git clone https://github.com/pasamdinesh/zerodha.git
  
  >> cd zerodha
  
  >> source zerodhaenv/bin/activate
  
  >> python zerodha_project/manage.py migrate
  
Open one more tab and please be there in same path
 
  >> cd /usr/local/src/zerodha
  
  >> source zerodhaenv/bin/activate
  
  >>  python zerodha_project/manage.py runserver
  
  ## for time beign it is runing as a manual service, we can make it has system level deamon.
  
  >> python zerodha_project/manage.py download  
  
 now we can use below mentoned url for seeing results at front end.
  
  >> http://127.0.0.1:8000/
  
 
  
