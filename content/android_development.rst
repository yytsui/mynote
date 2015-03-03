How to connect your Android phone to Ubuntu to do development, testing, installations or tethering
==================================================================================================

http://dimitar.me/how-to-connect-your-android-phone-to-ubuntu-to-do-developmenttestinginstallations-or-tethering/

If you do any Android development in Ubuntu it is much better to test your applications on a real device rather than just relying on the emulator.

If you just connect the phone to the computer through USB and run adb devices you will find out that your phone is not recognized:

$ adb devices
List of devices attached
???????????? no permissions
This is easily fixable in Ubuntu. You have to add a line to a file in the /etc/udev/rules.d directory.

What line in which file depends on the manufacturer and model of the device. You can find out the Vendor ID number and Product ID number of the device by running (after you connected it via USB of course):

$ lsusb
For example, if you had a Nexus One connected you would get:

Bus 002 Device 004: ID 18d1:4e12

In this case the Vendor Id is “18d1″ and the Product ID is “4e12″. Please keep in mind that the Vendor ID for HTC changed from “0bb4″ to “18d1″. The older HTC phones like the G1 have a Vendor ID of “0bb4″.

Here is how to set up some of the major Android phones:

Step 1. Depending on your phone follow these instructions:

G1
Create/edit a file in /etc/udev/rules.d called 51-android.rules:
$ sudo gedit /etc/udev/rules.d/51-android.rules
Add the following line to it and save it:

SUBSYSTEMS==”usb”, ATTRS{idVendor}==”0bb4″, ATTRS{idProduct}==”0c01″, MODE=”0666″

HTC Hero
Create/edit a file in /etc/udev/rules.d called 51-android.rules:
$ sudo gedit /etc/udev/rules.d/51-android.rules
Add the following line to it and save it:

SUBSYSTEMS==”usb”, ATTRS{idVendor}==”0bb4″, ATTRS{idProduct}==”0c02″, MODE=”0666″

Motorola Droid
Create/edit a file in /etc/udev/rules.d called 10-motorola-droid.rules:
$ sudo gedit /etc/udev/rules.d/10-motorola-droid.rules
Add the following line to it and save it:

SUBSYSTEMS==”usb”, ATTRS{idVendor}==”22b8″, ATTRS{idProduct} ==”41db”, MODE=”0600″

Nexus One
Create/edit a file in /etc/udev/rules.d called 99-android.rules:
$ sudo gedit /etc/udev/rules.d/99-android.rules
Add the following line to it and save it:

SUBSYSTEM==”usb”, ATTRS{idVendor}==”18d1″, SYMLINK+=”android_adb”, MODE=”0666″

Step 2. Restart udev:

$ sudo restart udev
Check if the device is recognized:

$ adb devices
You may need to stop and start the adb server:

$ adb kill-server
$ sudo  adb start-server
You should be good to go…

I had to start the server with sudo in order for it to recognize the permissions – using Ubuntu 10.04


Android: Getting source code from an APK file
===============================================
http://stackoverflow.com/questions/3593420/android-getting-source-code-from-an-apk-file?lq=1
http://comptech-blogger.blogspot.in/2012/09/how-to-get-source-code-from-apk-file.html

#all the tools alreday download to
Procedure to decoding .apk files ---step wise method-->

Step 1:

Make a new folder and put .apk file (which you want to decode) now rename this .apk file with extension .zip
(eg:rename from filename.apk to filename.apk.zip) and save it..now you get classes.dex 
files etc...at this stage you are able to see drawable but not xml and java file...so cont...

Step 2:

Now extract this zip apk file in the same folder(in this eg or case NEW FOLDER). now dowmload dex2jar from
this link http://code.google.com/p/dex2jar/ and extract it to the same folder (in this case NEW FOLDER).....
now open command prompt and reach to that folder (in this case NEW FOLDER)....after reaching write dex2jar
classes.dex and press enter.....now you get classes.dex.dex2jar file in the same folder......
now download java decompiler from http://java.decompiler.free.fr/?q=jdgui and now double click on 
jd-gui and click on open file then open classes.dex.dex2jar file from that folder...now you get class file...
save all these class file (click on file then click "save all sources" in jd-gui)..by src name....
at this stage you get source...but xml files are still unreadable...so cont...

Step 3:

Now open another new folder and put these files
put .apk file which you want to decode
download apktool v1.x AND apktool install window using google and put in the same folder
download framework-res.apk file using google and put in the same folder (Not all apk file need framework-res.apk file)
Open a command window
Navigate to the root directory of APKtool and type the following command: apktool if framework-res.apk
apktool d "fname".apk ("fname" denotes filename which you want to decode)
now you get a file folder in that folder and now you can easily read xml files also.

Step 4:

It's not any step just copy contents of both folder(in this case both new folder)to the single one
and now enjoy with source code...

Adding a library/JAR to an Eclipse Android project
===================================================
http://stackoverflow.com/questions/3642928/adding-a-library-jar-to-an-eclipse-android-project


down vote
accepted
Now for the missing class problem.

I'm an Eclipse JEE developer and have been in the habit for many years of adding third-party libraries via the "User Library" mechanism in Build Path. Of course, there are at least 3 ways to add a third-party library, the one I use is the most elegant, in my humble opinion.

This will not work, however, for Android, whose Dalvik "JVM" cannot handle an ordinary Java-compiled class, but must have it converted to a special format. This does not happen when you add a library in the way I'm wont to do it.

Instead, follow the (widely available) instructions for importing the third-party library, then adding it using Build Path (which makes it known to Eclipse for compilation purposes). Here is the step-by-step:

Download the library to your host development system.
Create a new folder, libs, in your Eclipse/Android project.
Right-click libs and choose Import -> General -> File System, then Next, Browse in the filesystem to find the library's parent directory (i.e.: where you downloaded it to).
Click OK, then click the directory name (not the checkbox) in the left pane, then check the relevant JAR in the right pane. This puts the library into your project (physically).
Right-click on your project, choose Build Path -> Configure Build Path, then click the Libraries tab, then Add JARs..., navigate to your new JAR in the libs directory and add it. (This, incidentally, is the moment at which your new JAR is converted for use on Android.)
What you've done here accomplishes two things:

Includes a Dalvik-converted JAR in your Android project.
Makes Java definitions available to Eclipse in order to find the third-party classes when developing (that is, compiling) your project's source code.


Reverse Engineering
====================

http://blog.apkudo.com/2012/10/16/reverse-engineering-android-disassembling-hello-world/
http://kkinder.com/2011/11/27/so-you-want-to-reverse-engineer-an-android-app-apk/
http://elinux.org/Android_aapt
http://developer.sonymobile.com/2012/04/13/powerful-tool-to-analyse-your-apks-now-released-open-source/
http://code.google.com/p/apkinspector/
http://code.google.com/p/droidbox/
http://code.google.com/p/androguard/

Debugger disconnect
====================


http://stackoverflow.com/questions/8056661/debugger-disconnects-when-calling-external-intent-camera
add these line in front of debug code:

if (!Debug.isDebuggerConnected()){
    	    Debug.waitForDebugger();
    	    Log.d("debug", "started"); // Insert a breakpoint at this line!!
    	}


Building Android programs on the command line
==============================================
http://geosoft.no/development/android.html

This guideline shows how to build Android programs (apps) using a command line environment only.

Even though the Eclipse IDE (among others) can be a powerful development environment for Android programmers, there are several reasons why you could benefit from utilizing simple command line utilities and build scripts instead. Actually understanding what's going on is one of them.


 
Using the stepwise approach outlined below might seem overwhelming, but there is a great educational value in performing these steps, and the information present is essential if you are setting up a build system based on make, SCons, Ant, or similar tools.

The setup below depends on a few environment variables identifying directory paths on the local system. The exact procedure for setting and accessing environment variables differs between operating systems and command shells. In the present guideline the simplest possible notation is being used. In practice these variables needs to be accessed using special notation like %JAVA_HOME%, ${JAVA_HOME} or even "${JAVA_HOME}" if the path contains spaces. In addition, commands are listed over multiple lines to improve readability. In practice commands must be written on a single line or separated by proper line delimiters. Note also that the forward slash character ("/") is consistently used as directory delimiter even though the backslash ("\") is still used on some systems.

Color coding is used in the commands in order to easily indicate where local replacements needs to take place.

All commands are self-contained meaning that they can be executed from any directory.

1. Download Java

The Java Standard Edition (Java SE) is available from Oracle at http://www.oracle.com/technetwork/java/javase/downloads.

Default installation location will vary between Java versions and OS platforms, so create a pointer to its location:

JAVA_HOME = C:/Program Files/Java/jdk1.6.0_26
2. Download Android

The Android Software Development Kit (Android SDK) is available from Google at http://developer.android.com/sdk.

Default installation location will vary between Android versions and OS platforms, so create a pointer to its location:

ANDROID_HOME = C:/Program Files/Android/android-sdk
The download includes the core parts of Android. In addition you need SDK(s) for the specific Android platforms you will develop for and test on. Launch the SDK manager GUI, select Available packages and open the Android Repository:

ANDROID_HOME/tools/android
Select the required platform/tool packages (all is fine) and hit the Install Selected button. After installation, the platform/ and platform-tools/ directories of ANDROID_HOME should have been populated.

3. Choose project name

At some disk location create a project directory that will hold the code, libraries and other files that constitutes the Android project. Create a pointer to this location:

DEV_HOME = C:/Users/johnd/dev/AndroidTest
The project name in this context is simply a convenience in order to consistently name directories and files related to the application being created.

In the example AndroidTest is used as the project name. The term has been emphasized below so that it can be easily replaced.

4. Create development area

Beneath the project directory create sub directories as follows:

DEV_HOME/src/com/mycompany/package1/...
         res/drawable/
             layout/
             values/
         obj/
         lib/
         bin/
         docs/
The src/ directory will hold java code and other source files in a package structure common for java projects. Using the reverse domain name system (Reverse DNS) for package names is optional but recommended. 
The res/ directory will hold user provided resources like text strings, images, menues, layouts etc. The res/ sub directories have predefined names according to the Android resource documentation. 
The obj/ directory will contain .class files and other secondary files produced by the Java tools as explained below. 
The lib/ directory should hold 3rd-party .jar files the project depends on. 
The bin/ directory will hold intermediate and final executables produced by the Android tools. 
The docs/ directory will hold javadoc HTML documents for the project. If generated, the docs/index.html file will be the entry point.

5. Create manifest

The Android manifest file is used to specify application settings like name and version, as well as what permissions the application requires to run and what components it is comprised of. The file contains a single application tag inside the root manifest tag.

Put the manifest file in the project root directory: DEV_HOME/AndroidManifest.xml. Note that the file must be called AndroidManifest.xml and nothing else.

A typical manifest file is shown below:

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
      package="com.mycompany.package1"
      android:versionCode="1"
      android:versionName="1.0">

    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>

    <uses-sdk android:minSdkVersion="2"/>

    <application android:icon="@drawable/mylogo"
                 android:label="@string/myApplicationName">
        <activity android:name="com.mycompany.package1.HelloAndroid"
                  android:label="@string/myApplicationName">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
The package attribute identifies the application and is also the destination location of the generated R.java file (see below). versionCode is a numeric version value for managing application updates. versionName is the application version in a human readable form.

The application tag contains the activities of the program, one of which should contain the main launcher activity as shown.

6. Select target platform

The different Android OS versions are known through target names like android-3, android-4, android-5 etc. All available platforms can be listed by the following command:

ANDROID_HOME/tools/android list target
For the examples below we use android-7 (Android OS 2.1) consistently. Replace this with a different target as required.

7. Define virtual device

An Android Virtual Device (AVD) defines the main characteristics of the target Android device. AVDs are used only when testing an Android program in the Android emulator. The typical approach is to define several AVDs in order to verify that a program behave correct across hardware platforms and OS versions.

Use the android tool to create AVDs:

ANDROID_HOME/tools/android
                     --verbose
                     create avd
                     --name MySonyEricsson
                     --target android-7
                     --sdcard 1024M
This will create an AVD with the specified name and with a 1 GB memory card disk image. When the command is executed you are asked if you want to specify a custom hardware profile. By this the AVD can be tailored to a specific hardware device by identifying properties for features like screen, camera, memory, battery, audio, accelerometer, wi-fi, bluetooth, GPS, keyboard and so on.

If no longer needed, an AVD can be deleted as follows:

ANDROID_HOME/tools/android
                     --verbose
                     delete avd
                     --name MySonyEricsson
The actual AVD profiles are stored within the HOME/.android/avd/ directory.

8. Create keystore

A keystore is a database of private keys and their associated X.509 certificate chains authenticating the corresponding public keys. An Android program must be signed in order to execute on a device, and the program is signed by using a key from a keystore.

Use the keytool program to create a keystore:

JAVA_HOME/bin/keytool
                -genkeypair
                -validity 10000
                -dname "CN=company name,
                        OU=organisational unit,
                        O=organisation,
                        L=location,
                        S=state,
                        C=country code"
                -keystore DEV_HOME/AndroidTest.keystore
                -storepass password
                -keypass password
                -alias AndroidTestKey
                -keyalg RSA
                -v
Replace the distinguished name (dname) information with your own. Make sure to specify passwords as indicated. The key is accessed through the specified alias which can be any string.

The output of the command will be the DEV_HOME/AndroidTest.keystore file which contains one key identified by the supplied alias.

9. Write code

Define a suitable package structure and put the Java code within the src/ tree of the project area.

The following minimal class can serve as an example. It should be located in DEV_HOME/src/com/mycompany/package1/HelloAndroid.java:

package com.mycompany.package1;

import android.app.Activity;
import android.content.res.Resources;
import android.os.Bundle;
import android.widget.TextView;

public class HelloAndroid extends Activity {

  @Override
  public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    TextView textView = new TextView(this);

    String text = getResources().getString(R.string.helloText);
    textView.setText(text);

    setContentView(textView);
  }
}
The Android API documentation contains a complete reference to the Android packages and classes, including the ones provided by the Java SE.

10. Provide resources

Android programmers are advised to keep all non-logic data (text strings, images, animations, colors, layouts etc.) within the designated res/ directory of the project area. The res/ directory consists of a predefined set of sub directories with a naming structure that will simplify application localization and adoption to different hardware types.

The following minimal text resource can serve as an example. It should be located in DEV_HOME/res/values/strings.xml:

<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="myApplicationName">Android Test Program</string>
    <string name="helloText">Hello, world!</string>
</resources>
The manifest file refers to the myApplicationName entry, while the java class above refers to the helloText entry. The example manifest file above also refers to the drawable resource mylogo which is the icon image for the program. Put an image file in the res/ directory to serve this purpose: DEV_HOME/res/drawable/mylogo.png.

11. Create R.java

In order for the application source code to be able to access the resources within the res/ directory, a class called R.java (for Resources) is created.

Use the Android Asset Packaging Tool (aapt) to create the R.java file:

ANDROID_HOME/platform-tools/aapt
                        package
                        -v
                        -f
                        -m
                        -S DEV_HOME/res
                        -J DEV_HOME/src
                        -M DEV_HOME/AndroidManifest.xml
                        -I ANDROID_HOME/platforms/android-7/android.jar
The destination location of R.java within the src/ tree is determined by the package attribute of the manifest file.

12. Compile code

Use the javac tool to compile java source code in a package:

JAVA_HOME/bin/javac
                -verbose
                -d DEV_HOME/obj
                -classpath ANDROID_HOME/platforms/android-7/android.jar;DEV_HOME/obj
                -sourcepath DEV_HOME/src
                DEV_HOME/src/com/mycompany/package1/*.java
The command must be applied for each existing package. 3rd-party .jar files from the lib/ directory must be listed in the -classpath entry. Note that on UNIX-like operating systems the classpath entry delimiter should be a colon (":").

The output of the command is .class files in the obj/ tree.

Non-java files within the src/ tree must be copied to the associated location in the obj/ tree.

13. Create DEX file

DEX ("Dalvik Executable") is the specific bytecode format understood by the Dalvik virtual machine (VM) present in all Android devices.

Use the dx tool to bundle the content of the obj/ directory as well as 3rd-party .jar files from the lib/ directory into a single .dex file:

ANDROID_HOME/platform-tools/dx
                --dex
                --verbose
                --output=DEV_HOME/bin/classes.dex
                DEV_HOME/obj
                DEV_HOME/lib
This will create the classes.dex file in the bin/ directory. The content of a .dex file can be inspected using the ANDROID_HOME/platform-tools/dexdump tool.

14. Create APK file

The Android package format (APK) is the .jar equivalent for Android. The package contains the manifest file, the resources and the classes.dex file.

Use the aapt tool to create the .apk file:

ANDROID_HOME/platform-tools/aapt
                         package
                         -v
                         -f
                         -M DEV_HOME/AndroidManifest.xml
                         -S DEV_HOME/res
                         -I ANDROID_HOME/platforms/android-7/android.jar
                         -F DEV_HOME/bin/AndroidTest.unsigned.apk
                         DEV_HOME/bin
This will create the AndroidTest.unsigned.apk file in the bin/ directory. Note that APK is an ordinary archive format that can be inspected by tools like WinZip or unzip -l.

15. Sign APK file

In order to execute on an Android device, the Android package needs to be signed.

Use the jarsigner tool and the key from the keystore created above to create a signed version of the package:
JAVA_HOME/bin/jarsigner
                -verbose
                -keystore DEV_HOME/AndroidTest.keystore
                -storepass password
 	        -keypass password
	        -signedjar DEV_HOME/bin/AndroidTest.signed.apk
                DEV_HOME/bin/AndroidTest.unsigned.apk
	        AndroidTestKey
The signing process adds the META-INF/ directory to the APK archive including the signature (.SF) file and the associated PKSC file (.RSA).

The signed APK is stored as AndroidTest.signed.apk file in the bin/ directory.

16. Zip-align APK file

zipalign is an archive alignment tool that provides important optimization to Android packages. This step is optional, but recommended:

ANDROID_HOME/tools/zipalign
                -v
                -f
                4
                DEV_HOME/bin/AndroidTest.signed.apk
                DEV_HOME/bin/AndroidTest.apk
This will create the AndroidTest.apk which is the final product delivered in one self-contained unit.

17. Start emulator

In order to test the application, start the Android emulator and specify the virtual device (AVD) to use:

ANDROID_HOME/tools/emulator
                -wipe-data
                -avd MySonyEricsson
This will launch the emulator GUI. The wipe-data option ensures the emulator starts up clean. The initialization process may take some time, so don't proceed until the emulator is ready.

18. Install in emulator

When the emulator is ready, use the Android Debug Bridge (adb) tool to install the Android package in the running emulator:

ANDROID_HOME/platform-tools/adb
                -e
                install DEV_HOME/bin/AndroidTest.apk
The program should eventually show up in the emulator and can be executed by selecting it.

The application can be uninstalled as follows:

ANDROID_HOME/platform-tools/adb
                shell
                rm /data/app/com.mycompany.package1.apk
Note that inside the emulator or device the APK is stored using its main package name (from the package attribute of the manifest file) with an .apk extension.

19. Install on device

Attach the Android device to the computer and install the program using the adb command:

ANDROID_HOME/platform-tools/adb
                -d
                install DEV_HOME/bin/AndroidTest.apk
The program should be ready for execution on the target device.

20. Create documentation

7Every well managed project should have up-to-date documentation available at any time. This step is of course optional, but strongly recommended.

Use the javadoc tool to create HTML documentation as follows:

JAVA_HOME/bin/javadoc
                -verbose
                -d DEV_HOME/docs
                -sourcepath DEV_HOME/src
                -classpath ANDROID_HOME/platforms/android-7/android.jar;DEV_HOME/obj
                -author
                -package
                -use
                -splitIndex
                -version
                -windowtitle 'AndroidTest'
                -doctitle 'AndroidTest'
                DEV_HOME/src/com/mycompany/package1/*.java
Source from additional packages should be added to the last argument using ":" or ";" as delimiter (depending on platform).

The documentation entry point will be DEV_HOME/docs/index.html.


another related article
http://asantoso.wordpress.com/2009/09/15/how-to-build-android-application-package-apk-from-the-command-line-using-the-sdk-tools-continuously-integrated-using-cruisecontrol/

Java Collections: How to divide a sorted list into sub lists
============================================================
http://stackoverflow.com/questions/4073592/java-collections-how-to-divide-a-sorted-list-into-sub-lists

