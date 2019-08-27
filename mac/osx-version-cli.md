# OSX version from command line

```
xxx-macbookpro:~ name$ system_profiler
```
Response:-
```
system_profiler SPSoftwareDataType
Software:

    System Software Overview:

      System Version: macOS 10.14.6 (18G87)
      Kernel Version: Darwin 18.7.0
      Boot Volume: Macintosh HD
      Boot Mode: Normal
      Computer Name: xxx’s MacBook Pro (2)
      User Name: XX XX (XXXX)
      Secure Virtual Memory: Enabled
      System Integrity Protection: Enabled
      Time since boot: X days X:XX
```

---
```
xxx-macbookpro:~ name$ sw_vers
ProductName:	Mac OS X
ProductVersion:	10.14.6
BuildVersion:	18G87
```
---
```
xxx-macbookpro:~ name$ defaults read loginwindow SystemVersionStampAsString
10.14.6
```

## Links
[Apple docs](https://support.apple.com/en-us/HT203001)
