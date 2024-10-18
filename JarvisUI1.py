<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1440</width>
    <height>900</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1440</width>
      <height>900</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>Jarvis/utils/images/live_wallpaper.gif</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>1180</x>
      <y>790</y>
      <width>101</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(0, 170, 255);
font: 75 18pt &quot;MS Shell Dlg 2&quot;;</string>
    </property>
    <property name="text">
     <string>Run</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>1310</x>
      <y>790</y>
      <width>101</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:rgb(255, 0, 0);
font: 75 18pt &quot;MS Shell Dlg 2&quot;;</string>
    </property>
    <property name="text">
     <string>Exit</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>401</width>
      <height>91</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>Jarvis/utils/images/initiating.gif</pixmap>
    </property>
   </widget>
   <widget class="QTextBrowser" name="textBrowser">
    <property name="geometry">
     <rect>
      <x>640</x>
      <y>30</y>
      <width>291</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 16pt &quot;MS Shell Dlg 2&quot;;
background-color:transparent;
border-radius:none;
</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="textBrowser_2">
    <property name="geometry">
     <rect>
      <x>930</x>
      <y>30</y>
      <width>291</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 16pt &quot;MS Shell Dlg 2&quot;;
background-color:transparent;
border-radius:none;</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="textBrowser_3">
    <property name="geometry">
     <rect>
      <x>1000</x>
      <y>500</y>
      <width>431</width>
      <height>281</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 11pt &quot;MS Shell Dlg 2&quot;;
background-color:transparent;</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1440</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>