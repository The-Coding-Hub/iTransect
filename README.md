## **NLP Boot Camp (Jan) Synopsis**

### **Full Name:**

Prameya Mohanty

### **Name of your School:**

Delhi Public School, Rourkela

### **Class:**

VIII

### **Title of the Project:**

iTransect – A Language Detector cum Translator

### **Project Domain:**

Domain

### **Summary:**

This application is an AI and NLP enabled language detector cum translator. It can first detect the language used in the text entered by the user. Then it can also convert the text in your desired language. This app has a capability to recognize and translate text to over 15 languages.

### **Context:**

We frequently face problems while reading google articles or while going through websites which are not in English language or our mother tongue. Many rural people also don't understand any language except their Mother Tongue. So, they can also translate the text and go through it.

My idea for this problem is that we can create a translator to translate the text into a language which we can understand. But another problem which occurs is that we need to first recognize that the original text is written in which language and mostly we fail to do so. For this reason, my application would just take the text as input, recognize the language of the text and then it would also translate the text into our desired language.

I transformed my idea into a solution by performing some Natural Language Processing on the text given by the user to first recognize the language used in the text and then translate into the desired language of the user.

### **How does it work:**

I have used the MultinomialNB Model of the Scikit-Learn Library. The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification). The multinomial distribution normally requires integer feature counts. However, in practice, fractional counts such as tf-idf may also work. 

My application contains a Huge Dataset which contains over 15 languages and some texts on those languages. This dataset in trained on the MultinomialNB Model of the Scikit-Learn Library. This helps it to predict the language of the desired text which we provide to it. Then I have used the GoogleTrans API to Translate our Text into the desired language of the user.

My application takes some text as input from the user. Then it detects the language used in the text by a MultinomialNB Model of the Scikit-Learn Library. After that it uses the GoogleTrans API to translate the text into the desired language of the user.

The future scope of my model is that we can increase the dataset by adding more languages so that the predictions would be more accurate. This would also help our application to cover a broader audience.

### **Instructions for Usage:**

1. **Prerequisite:** To use this application, you should have Python installed in your system. Installation of Git is recommended but not compulsory.
2. **Clone Repo:** If you have git installed in your system then you can use the command given here or else you can just click on the Code button and then click on the Download ZIP Button.
```git clone https://github.com/The-Coding-Hub/iTransect.git```

3. **Install Requirements:** Now you need to install the requirements of this application using pip and the requirements.txt file. Command to be executed in the console is given below.
```pip install -r ./requirements.txt```

4. **Start App:** Now you are all set the use this application. You just need to execute the command given below to start the development server of Python Flask in your Localhost.
5. **Enjoy App:** Just open the link given in your console and then you can enjoy our application!

### **Video Link:**

https://youtu.be/QsJQ1lxI2Lw

### **Code Folder Link:**

https://github.com/The-Coding-Hub/iTransect
