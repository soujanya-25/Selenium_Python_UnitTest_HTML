import os
from datetime import datetime
import time
import random
import inspect
import platform
import getpass
import socket
from Main.Utility import xmlReader as Env
from pathlib import Path

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



class HTMlLogger(metaclass=Singleton):

    filepath = str(Path(__file__).parent.parent.parent) +"/Reports/LatestTree/report_" + str(time.strftime("%Y%m%d-%H%M%S")) + ".html"
    f = open(filepath, "a")
    parentid=""
    rowid=""
    childid=""

    def __init__(self):
        #self.filepath = "../../Reports/LatestTree/report" + str(time.strftime("%Y%m%d-%H%M%S")) + ".html"
        #self.f = open(self.filepath, "a")
        strStartFile = """<html>
        	<head>
        	    <meta charset="utf-8">
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
              <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
              <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.6/umd/popper.min.js"></script>
              <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js"></script>
        		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/jquery-ui.min.js"></script>
        		<script type="text/javascript" src="./js/jquery.tbltree.js"></script>
        		<link type="text/css" href="css/jquery.tbltree.css" rel="stylesheet">
        		<script type="text/javascript" src="./js/jquery.cookie.js"></script>
				<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
              
        		<script type="text/javascript">
        		  $(function() {
        			 // initialize with default options
        			$( "#table1" ).tbltree();
        		  });
				  google.charts.load("current", {packages:["corechart"]});
				  google.charts.setOnLoadCallback(drawChart);
				  function openTab(evt, cityName) {
					  var i, tabcontent, tablinks;
					  tabcontent = document.getElementsByClassName("maincontent");
					  for (i = 0; i < tabcontent.length; i++) {
						tabcontent[i].style.display = "none";
					  }
					  tablinks = document.getElementsByClassName("tablinks");
					  for (i = 0; i < tablinks.length; i++) {
						tablinks[i].className = tablinks[i].className.replace(" active", "");
					  }
					  document.getElementById(cityName).style.display = "";
					  evt.currentTarget.className += " active";
				}
				function load(){
				document.getElementById("defaultOpen").click();
				}
				function calcFail()
				{
					
					var elements = document.getElementsByClassName("fail");
					var names = '';
					for(var i=0; i<elements.length; i++) {
						names = elements[i].getAttribute('parentid');
						document.getElementById(names).innerHTML="<img src='img/fail_4.png'/>&nbsp FAIL";
						document.getElementById(names).setAttribute("class", "testFAIL"); 
					}
					
				}
				function drawChart() {
				    var pass  = document.getElementsByClassName("testPASS").length
					var fail  = document.getElementsByClassName("testFAIL").length
					var norun = 1
					var data = google.visualization.arrayToDataTable([
					  ['Task', 'Hours per Day'],
					  ['PASS',     pass],
					  ['FAIL',      fail],
					  ['No Run',   norun],
					 
					]);

					var options = {
					  title: 'Execution Result',
					  pieHole: 0.4,
					  
					  colors: ['green', '#FF0000', '#3498db']
					};

					var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
					chart.draw(data, options);
				  }
        		</script>
        		<style>
					#sidebar {
						width: 15%;
						height: 100%;
						position: fixed;
						background: #2f323a;
						
					}
					
					.nav-collapse.collapse {
						display: inline;
					}

					ul.sidebar-menu , ul.sidebar-menu li ul.sub{
						margin: -2px 0 0;
						padding: 0;
					}

					ul.sidebar-menu {
						margin-top: 75px;
					}

					#sidebar > ul > li > ul.sub {
						display: none;
					}

					#sidebar > ul > li.active > ul.sub, #sidebar > ul > li > ul.sub > li > a {
						display: block;
					}

					ul.sidebar-menu li ul.sub li{
						background: white;
						margin-bottom: 0;
						margin-left: 0;
						margin-right: 0;
					}

					ul.sidebar-menu li ul.sub li:last-child{
						border-radius: 0 0 4px 4px;
						-webkit-border-radius: 0 0 4px 4px;
					}

					ul.sidebar-menu li ul.sub li a {
						font-size: 12px;
						padding: 6px 0;
						line-height: 35px;
						height: 35px;
						-webkit-transition: all 0.3s ease;
						-moz-transition: all 0.3s ease;
						-o-transition: all 0.3s ease;
						-ms-transition: all 0.3s ease;
						transition: all 0.3s ease;
						color: #fcfffa;
					}

					ul.sidebar-menu li ul.sub li a:hover {
						color: white;
						background: transparent;
					}

					ul.sidebar-menu li ul.sub li.active a {
						color: white;
						-webkit-transition: all 0.3s ease;
						-moz-transition: all 0.3s ease;
						-o-transition: all 0.3s ease;
						-ms-transition: all 0.3s ease;
						transition: all 0.3s ease;
						display: block;
					}

					ul.sidebar-menu li{
						/*line-height: 20px !important;*/
						margin-bottom: 5px;
						margin-left:10px;
						margin-right:10px;
					}

					ul.sidebar-menu li.sub-menu{
						line-height: 15px;
					}

					ul.sidebar-menu li a span{
						display: inline-block;
						color: white;
					}

					ul.sidebar-menu li a{
						color: #fcfffa;
						text-decoration: none;
						display: block;
						padding: 15px 0 15px 10px;
						font-size: 12px;
						font-color:white
						outline: none;
						-webkit-transition: all 0.3s ease;
						-moz-transition: all 0.3s ease;
						-o-transition: all 0.3s ease;
						-ms-transition: all 0.3s ease;
						transition: all 0.3s ease;
					}

					ul.sidebar-menu li a.active, ul.sidebar-menu li a:hover, ul.sidebar-menu li a:focus {
						background: #4ECDC4;
						color: #fff;
						display: block;

						-webkit-transition: all 0.3s ease;
						-moz-transition: all 0.3s ease;
						-o-transition: all 0.3s ease;
						-ms-transition: all 0.3s ease;
						transition: all 0.3s ease;
					}


					ul.sidebar-menu li a i {
						font-size: 15px;
						padding-right: 6px;
					}

					ul.sidebar-menu li a:hover i, ul.sidebar-menu li a:focus i {
						color: #fff;
					}

					ul.sidebar-menu li a.active i {
						color: #fff;
					}
					.mail-info, .mail-info:hover {
						margin: -3px 6px 0 0;
						font-size: 11px;
					}
					 #rcorners2 {
                      border-radius: 25px;
                      border: 4px solid #73AD21;
                      box-shadow: 5px
                      padding: 0px; 
                      width: 80%;  
                    }
                    #table1 {
                      
                      box-shadow: 5px
                      padding: 0px; 
                      width:70%;
					  isplay: inline-block;
					
                    }
                     #fail{
					  align:center
					}
					.img-circle {
					   
						border-radius: 50%;
							border-top-left-radius: 50%;
							border-top-right-radius: 50%;
							border-bottom-right-radius: 50%;
							border-bottom-left-radius: 50%;
					}
					
					.header{
					    
						background: #22242a;
						border-bottom: 1px solid #393d46;
						height: 10%;
						position: fixed;
						left: 0;
						right: 0;
						z-index: 1002;
					}
					.logo{
					   background: #4ECDC4;
					   size:12px;
					}
					.logo1{
					   background: White;
					   size:13px;
					}
					.container{
					   background: white;
					}
					.maincontent{
					  display: inline-block;
					  margin-top: 5%;
					  
					  /* padding-left: 1px;*/
					  padding-right: 15px;
					  padding-bottom: 15px;
					  padding-top: 0px;
					  width: 100%;
					}
					#detailedreport{
					  padding-left: 2px;
					}
                    #dashboard{
					  padding-left: 32px;
					}					
        		</style>
        	</head>

        <body onload="load();calcFail()">
         
    <!-- **********************************************************************************************************************************************************
        TOP BAR CONTENT & NOTIFICATIONS
        *********************************************************************************************************************************************************** -->
    <!--header start-->
    <header class="header">
      <div class="sidebar-toggle-box">
        <div class="fa fa-bars tooltips" data-placement="right" data-original-title="Toggle Navigation"></div>
      </div>
      <!--logo start-->
     <div align=Center><b><font size=34 color="White" >TEST</font><font size=34 color="#4ECDC4" >AUTO</font></b></div>
      
    </header>
		  <div id="sidebar" class="nav-collapse ">
				<!-- sidebar menu start-->
				<ul class="sidebar-menu" id="nav-accordion">
				  <p class="centered" align="Center"><a href="profile.html"><img src="img/ui-sam.png" class="img-circle" width="80px" align="Center"></a></p>
				  <p align="Center"><b><font size=6 color="White" >TEST</font><font size=6 color="#4ECDC4" >AUTO</font></b></p>
				  <li class="mt">
					<a class="tablinks" onclick="openTab(event, 'dashboard')" id="defaultOpen">
					  <i class="fa fa-dashboard"></i>
					  <span >Dashboard</span>
					  </a>
				  </li>
				  <li class="sub-menu">
					<a onclick="openTab(event, 'detailedreport')" class="tablinks">
					  <i class="fa fa-desktop"></i>
					  <span>Detailed Report</span>
					  </a>
					<ul class="sub">
					  <li><a href="general.html">General</a></li>
					  <li><a href="buttons.html">Buttons</a></li>
					  <li><a href="panels.html">Panels</a></li>
					  <li><a href="font_awesome.html">Font Awesome</a></li>
					</ul>
				  </li>
				  <li class="sub-menu">
					<a onclick="openTab(event, 'envdetails')" class="tablinks">
					  <i class="fa fa-cogs"></i>
					  <span>Environment Details</span>
					  </a>
					<ul class="sub">
					  <li><a href="grids.html">Grids</a></li>
					  <li><a href="calendar.html">Calendar</a></li>
					  <li><a href="gallery.html">Gallery</a></li>
					  <li><a href="todo_list.html">Todo List</a></li>
					  <li><a href="dropzone.html">Dropzone File Upload</a></li>
					  <li><a href="inline_editor.html">Inline Editor</a></li>
					  <li><a href="file_upload.html">Multiple File Upload</a></li>
					</ul>
				  </li>
				  <li class="sub-menu">
					<a href="javascript:;">
					  <i class="fa fa-book"></i>
					  <span>Extra Pages</span>
					  </a>
					<ul class="sub">
					  <li><a href="blank.html">Blank Page</a></li>
					  <li><a href="login.html">Login</a></li>
					  <li><a href="lock_screen.html">Lock Screen</a></li>
					  <li><a href="profile.html">Profile</a></li>
					  <li><a href="invoice.html">Invoice</a></li>
					  <li><a href="pricing_table.html">Pricing Table</a></li>
					  <li><a href="faq.html">FAQ</a></li>
					  <li><a href="404.html">404 Error</a></li>
					  <li><a href="500.html">500 Error</a></li>
					</ul>
				  </li>
				 
				</ul>
				<!-- sidebar menu end-->
      </div>
       <div id="envdetails" class="maincontent" style="width: 900px; height: 500px; padding-left: 15%;" >
	      <p ><h1><b>Environment Details</b></h1></p>
		  <p><b> OS Name : </b>"""+platform.system()+"""</p>
		  <p><b> OS Release : </b>"""+platform.release()+""" </p>
		  <p><b> Machine Name :</b> """+socket.gethostname()+""" </p>
		  <p><b> User Name : </b>"""+getpass.getuser()+""" </p>
	  </div>
	  <div id="dashboard" class="maincontent" >
	      <p ><h1><b>Dashboard</b></h1></p>
		  <div id="donutchart" style="width: 900px; height: 500px; padding-left: 15%;"></div>
	  </div>
      <div class="maincontent" id="detailedreport">
          <table id="table1" border=1 align=Center class="container">
          <tr>
          <th>Test Case Name</th><th>Status</th><th>Time taken</th>
  </tr>"""
        self.f.writelines(strStartFile)
        self.f.close()
        # print(inspect.stack()[1][0].f_code.co_name)

    def assert_testcase_log(self, log):

        self.f = open(self.filepath, "a")
        self.parentid = random.randrange(0, 6000, 1)
        tlog = """
              <tr row-id='"""+str(self.parentid)+"""'>
                <td><b>"""+log+"""</b></td><td class="testPASS" id = '"""+str(self.parentid)+"""'><img src="img/pass_4.png"/>PASS</td><td class="data">"""+str(time.strftime("%H:%M:%S"))+"""</td>
              </tr>
            """
        self.f.writelines(tlog)
        self.f.close()
        # print(self.__doc__)

    def assert_step_log(self, status,log):
        self.f = open(self.filepath, "a")
        self.rowid = random.randrange(6000, 200000, 1)


        tlog = """
                      <tr row-id='""" + str(self.rowid) + """' parent-id='""" + str(self.parentid) + """'>
                        <td>"""+log+"""</td><td class="data"><img src="img/pass_4.png"/>&nbsp """+status+"""</td><td class="data">"""+str(time.strftime("%H:%M:%S"))+"""</td>
                      </tr>
                    """
        self.f.writelines(tlog)
        self.f.close()

    def assert_step_fail_log(self, driver, log):
        self.f = open(self.filepath, "a")
        self.childid = random.randrange(20000, 60000, 1)

        snappath = self.filepath.replace("html", "png")
        snappath = snappath.replace("LatestTree/report_", "FailureImg/snap_")
        strP = snappath.split("/")[len(snappath.split("/"))-1]
                   #snappath.replace("LatestTree/report_", "FailureImg/report_"+str(random.randint(1,101)))
        driver.get_screenshot_as_file(snappath)
        tlog = """
                      <tr row-id='""" + str(self.childid) + """' parent-id='""" + str(self.parentid) + """'>
                        <td>""" + log + """</td><td class="fail" id="fail" parentid='""" + str(self.parentid) + """'><img src="img/fail.png"/>&nbsp FAIL</td><td class="data">""" + str(time.strftime("%H:%M:%S")) + """</td>
                      </tr>
                      <tr row-id='""" + str(self.childid+1) + """' parent-id='""" + str(self.childid) + """'>
                        <td colspan="3"><img src='../FailureImg/"""+strP+"""' width="25%" height="25%"/></td>
                      </tr>
                    """
        self.f.writelines(tlog)
        self.f.close()

    def close_report(self):
        self.f = open(self.filepath, "r+")
        data = self.f.read()
        data = data.replace("</table></div></body></html>",'')
        self.f.seek(0)
        self.f.truncate()
        self.f.writelines(data + "</table></div></body></html>")
        self.f.close()


