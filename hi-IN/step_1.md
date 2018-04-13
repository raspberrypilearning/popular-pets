## भूमिका

इस प्रोजेक्ट में आप अपने कोड क्लब के सदस्यों से एकत्रित डेटा द्वारा पाई चार्ट और बार ग्राफ बनाना सीखेंगे।  

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/70d24d92b8?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/pets-finished.png">
</div>


### क्लब लीडर्स के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं, तो कृपया [प्रिंटर के लिए अनुकूल संस्करण](https://projects.raspberrypi.org/en/projects/popular-pets/print) का उपयोग करें।


--- collapse ---
---
title: क्लब लीडर के नोट्स
---


## भूमिका:
यह प्रोजेक्ट डेटा प्रदर्शित करने के लिए Pygal ग्राफिंग और चार्टिंग मॉड्यूल का उपयोग करता है। बच्चे पाई चार्ट और बार ग्राफ द्वारा डेटा एकत्रित करते हैं और इसे प्रदर्शित करने के लिए Pygal का उपयोग करते हैं।  

## ऑनलाइन संसाधन

__यह प्रोजेक्ट Python 3 का उपयोग करता है।__ हम Python ऑनलाइन लिखने के लिए [trinket](https://trinket.io/) का उपयोग करने की अनुशंसा करते हैं। इस प्रोजेक्ट में निम्नलिखित Trinkets शामिल होते हैं:

+ ['लोकप्रिय पालतू जानवर' आरंभ बिंदु -- jumpto.cc/python-new](http://jumpto.cc/python-new)

ऐसा ट्रिंकेट भी होता है, जिसमें चुनौतियों के लिए हल का नमूना शामिल होता है:

+ [‘लोकप्रिय पालतू जानवर’ पूर्ण -- trinket.io/python/9339862606](https://trinket.io/python/9339862606)

## ऑफ़लाइन संसाधन
इस प्रोजेक्ट को [ऑफ़लाइन पूरा किया जा सकता है](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) यदि वरीय हो। आप इस प्रोजेक्ट के लिए 'प्रोजेक्ट सामग्री' लिंक पर क्लिक करके प्रोजेक्ट के संसाधनों तक पहुँच कर सकते हैं। इस लिंक में 'प्रोजेक्ट संसाधन' भाग शामिल है, जिसमें ऐसे स्रोत शामिल हैं जिनकी आवश्यकता बच्चों को अपने प्रोजेक्ट ऑफ़लाइन पूरा करने के लिए हो सकती है। सुनिश्चित करें कि प्रत्येक बच्चे की इन संसाधनों तक पहुँच है। इस भाग में निम्नलिखित फाइलें शामिल हैं:

+ popular-pets/popular-pets.py

आप इस प्रोजेक्ट की चुनौतियों का पूर्ण संस्करण 'स्वैच्छिक संसाधन' भाग में भी देख सकते हैं, जिसमें ये शामिल हैं:

+ popular-pets-finished/popular-pets.py
+ popular-pets-finished/pets.txt
+ popular-pets-finished/butterflies.txt
+ popular-pets-finished/piratesinjas.txt

(ऊपर्युक्त सभी संसाधन, प्रोजेक्ट और स्वैच्छिक `.zip` फाइलों के रूप में डाउनलोड योग्य भी होते हैं।)

## अधिगम उद्देश्य
+ डेटा - Pygal चार्ट और ग्राफ
+ फाइलों से पढ़ना

इस प्रोजेक्ट में [Raspberry Pi डिजिटल निर्माण पाठ्यचर्या](http://rpf.io/curriculum) के निम्नलिखित चीज़ों के तत्व शामिल होते हैं:

+ [समस्या का हल करने के लिए प्रोग्रामिंग निर्माण का संयोजन करें।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ
+ अपना स्वयं का बार चार्ट बनाएँ;
+ फाइल से बार चार्ट बनाएँ;
+ और चार्ट और ग्राफ!

## अक्सर पूछे जाने वाले प्रश्न
+ चरण 1 स्वयंसेवक को समूह को पसंदीदा पालतू जानवरों के बारे में डेटा एकत्र करने के लिए सर्वेक्षण आयोजित करने में सहायता करने के लिए पूछता है। यदि आपके पास प्रोजेक्ट पर काम करने वाले बच्चों की संख्या कम है, तो आप इसमें शामिल नमूना डेटा का उपयोग कर सकते हैं या इसे तैयार कर सकते हैं।
+ चुनौतियों के लिए आप समूह के रूप में सर्वेक्षण करना चुन सकते हैं और क्लब के सभी सदस्यों द्वारा उपयोग करने के लिए व्हाइटबोर्ड पर परिणाम दर्ज कर सकते हैं या आप बच्चों को उनके स्वयं के सर्वेक्षण करने और स्वयं का डेटा दर्ज करने के लिए अनुमति दे सकते हैं।


--- /collapse ---


--- collapse ---
---
title: प्रोजेक्ट सामग्री
---
## प्रोजेक्ट संसाधन
* [प्रोजेक्ट के सभी संसाधनों सहित .zip फाइल](resources/popular-pets-project-resources.zip)
* [ऑनलाइन खाली Python Trinket](http://jumpto.cc/python-new)
* [ऑफ़लाइन खाली Python फ़ाइल](resources/new-new.py)

## क्लब लीडर के संसाधन
* [प्रोजेक्ट के सभी पूर्ण संसाधनों सहित .zip फाइल](resources/popular-pets-volunteer-resources.zip)
* [ऑनलाइन पूर्ण ट्रिंकेट प्रोजेक्ट](https://trinket.io/python/70d24d92b8)
* [popular-pets-finished/popular-pets.py](resources/popular-pets-finished-popular-pets.py)
* [popular-pets-finished/pets.txt](resources/popular-pets-finished-pets.txt)
* [popular-pets-finished/butterflies.txt](resources/popular-pets-finished-butterflies.txt)
* [popular-pets-finished/piratesninjas.txt](resources/popular-pets-finished-piratesninjas.txt)

--- /collapse ---
